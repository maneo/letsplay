# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 4
# Video link: https://www.youtube.com/watch?v=mOckdKp3V38
# Adding graphics
from math import sqrt

# uncomment this to play headless
# import os
# os.environ['SDL_VIDEODRIVER'] = 'dummy'

import numpy as np
import pygame
import random
from os import path
import sys
import time
import rlagent as reinf
import game_utils as game

img_dir = path.join(path.dirname(__file__), '../img')

WIDTH = 480
HEIGHT = 600
FPS = 240
MOBS_SIZE = 8

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    state_vector_size = 2

    def dump_state_vector(self):
        return [self.speedx, self.rect.centerx]

    def update_with_action(self, action):
        self.speedx = 0
        if action == 0 or action == 4:
            self.speedx = -8
        if action == 1 or action == 5:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    state_vector_size = 7

    def dump_state(self, player) -> dict:
        state = dict()
        player_x = player.rect.centerx
        player_y = player.rect.centery
        mob_x = self.rect.centerx
        mob_y = self.rect.centery

        state["speedx"] = self.speedx
        state["speedy"] = self.speedy
        state["distance"] = round(sqrt((player_x - mob_x) * (player_x - mob_x)
                              + (player_y - mob_y) * (player_y - mob_y)))
        state["dist_x"] = player_x - mob_x
        state["dist_y"] = player_y - mob_y

        state['mob_x'] = mob_x
        state['mob_y'] = mob_y

        return state

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    state_vector_size = 3

    def dump_state_vector(self):
        return [self.rect.centerx, self.rect.centery, self.speedy]

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


games_played = 0

state_vector_size = game.GameState.vector_size
ai = reinf.RLAgent(state_vector_size)

while games_played < 400:

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()

    # Load all game graphics
    background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
    meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
    bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(MOBS_SIZE):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    game_start_time = time.time()
    game_state = game.GameState()
    score = 0

    # Game loop
    running = True
    while running:

        # level of randomness depending on number of games played
        ai.epsilon = 200 - games_played

        # keep loop running at the right speed
        clock.tick(FPS)
        was_shooting = False
        old_score = score

        # get state before action
        state_old = game_state.dump_state()

        # predict action
        final_move = reinf.RLAgent.to_categorical(random.randint(0, 5))
        if random.randint(0, 200) > ai.epsilon:
            # predict action based on the old state
            prediction = ai.model.predict(state_old.reshape((1, state_vector_size)))
            final_move = reinf.RLAgent.to_categorical(np.argmax(prediction[0]))

        # save action
        # game_state.save_action(action)

        action = reinf.RLAgent.from_categorical(final_move)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if action == 2 or action == 4 or action == 5:
            player.shoot()
            was_shooting = True
        else:
            player.update_with_action(action)

        # Update
        all_sprites.update()

        # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            score += 1

        # check to see if a mob hit the player
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            running = False

        # get reward
        reward = ai.set_reward(score - old_score, running)

        game_state.update_game_state(mobs, player, bullets)
        state_new = game_state.dump_state()

        # train short memory base on the new action and state
        ai.train_short_memory(state_old, final_move, reward, state_new, running)

        # store the new data into a long term memory
        ai.remember(state_old, final_move, reward, state_new, running)

        # Draw / render
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    end = time.time()
    print("games_played: {}, time: {} sec, score: {}".format(games_played, round(end - game_start_time), score))
    pygame.quit()
    games_played = games_played + 1
    ai.replay_new(ai.memory)
    # end large loop

ai.model.save_weights('weights.hdf5')
# save weights
#end training
# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 4
# Video link: https://www.youtube.com/watch?v=mOckdKp3V38
# Adding graphics
from math import sqrt

import pygame
import random
from os import path
import time
import sys
import score_utils as sc

img_dir = path.join(path.dirname(__file__), 'img')
generation = sys.argv[2]

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

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


# 3,0,113,532,1,5,361,2,4,269,2,5,520,2,2,224,1,6,491,0,3,433,-2,2,516,2,5
class GameState:
    def __init__(self):
        self.states = list()

    def __save_state(self, last_game_state):
        if len(self.states) >= 4:
            self.states.pop(0)
        self.states.append(last_game_state)
        # print(str(self.states))

    def dump_state(self):
        game_state_vector = list()
        if len(self.states) < 4:
            # for first frames append with zeros
            missing_states = 4 - len(self.states)
            game_state_length = len(self.states[0])
            for i in range(0, missing_states * game_state_length):
                game_state_vector.append(0)

        for state in self.states:
            game_state_vector.extend(state)

        return game_state_vector

    def update_game(self, mobs, player, bullets, action, score):
        state = list()
        state.extend(player.dump_state_vector())

        for mob in mobs.sprites():
            state.extend(mob.dump_state_vector(player))

        # pad with empty mobs to have vector of the same size
        mob_length = len(mobs.sprites())
        for j in range(MOBS_SIZE - mob_length):
            state.extend([0, 0, 0, 0])

        state.append(action)
        self.__save_state(state)



class MovesSequence:
    # default_move = 2   # if doubt shoot!
    default_move = 3

    def __init__(self, generation, path_to_evolution):
        self.path_to_evolution = path_to_evolution
        file_with_seq = self.path_to_evolution + "gen_" + str(generation) + ".seq"
        with open(file_with_seq, 'r') as seq_file:
            self.moves = seq_file.readlines()
        self.current_move_idx = 0
        self.generation = generation
        self.seq_is_over = False
        self.done_moves = []

    def next(self):
        if self.current_move_idx < (len(self.moves) - 1):
            current_action = int(self.moves[self.current_move_idx])
            self.done_moves.append(current_action)
            self.current_move_idx = self.current_move_idx + 1
            return current_action
        else:
            # give some time to bullets to reach target
            how_far_beyond = self.current_move_idx - len(self.moves)
            if how_far_beyond > 100:
                self.seq_is_over = True

            current_action = MovesSequence.default_move
            self.done_moves.append(current_action)
            self.current_move_idx = self.current_move_idx + 1
            return current_action

    def save_done_moves(self, score, time):
        file_with_seq = self.path_to_evolution + "gen_" \
                        + str(generation) + "_dead_s_" + str(int(score)) \
                        + "_t_" + str(int(time)) + ".seq"
        with open(file_with_seq, 'w') as seq_file:
            for move in self.done_moves:
                seq_file.write(str(move) + "\n")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

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

    def dump_state_vector(self, player):
        player_x = player.rect.centerx
        player_y = player.rect.bottom
        distance = round(sqrt((player_x - self.rect.x) * (player_x - self.rect.x)
                              + (player_y - self.rect.y) * (player_y - self.rect.y)))
        return [distance, self.speedx, self.speedy]

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

    def dump_state_vector(self):
        return [self.rect.centerx, self.speedy]

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


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
score = 0

ai_model = MovesSequence(generation, sc.path_to_evolution())
game_state = GameState()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    wasShooting = False

    action = ai_model.next()

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    if action == 2 or action == 4 or action == 5:
        player.shoot()
        wasShooting = True
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

    game_state.update_game(mobs, player, bullets, action, score)
    print(','.join(map(str, game_state.dump_state())))

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    if ai_model.seq_is_over:
        # when end of seq is reached terminate game
        break


end = time.time()

print("time: {} sec, score: {}".format(round(end - game_start_time), score))
ai_model.save_done_moves(score, round(end - game_start_time))
pygame.quit()
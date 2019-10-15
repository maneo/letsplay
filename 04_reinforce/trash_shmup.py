# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 4
# Video link: https://www.youtube.com/watch?v=mOckdKp3V38
# Adding graphics
import pickle
from math import sqrt
import pandas as pd

# uncomment this to play headless
# import os
# os.environ['SDL_VIDEODRIVER'] = 'dummy'

import numpy as np
import pygame
import random
from os import path
import sys
import time
import game_utils as game
impoty rlagent as ai
from sklearn.neural_network import MLPClassifier

model_name = sys.argv[1]
# ai_model_pkl = pickle.load(open("ai_model_" + model_name + ".pkl", "rb"))

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


# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


def load_historical_train():
    df = pd.read_csv('train.csv', sep = ';', encoding='utf-8')
    return df


def save_trainig_data(all_training_data):
    all_training_data.to_csv("train.csv", sep=';', encoding='utf-8', index=False)


def get_best_action(game_state, classifier):
    actions = [0, 1, 2, 3, 4, 5]
    results = dict()
    for action in actions:
        game_state_1f = game_state
        game_state_1f['action'] = action
        result = classifier.predict(game_state_1f.values.reshape(1, -1))
        results[action] = result[0]

    max_value = -1
    max_action = 0
    for key in results.keys():
        if results[key] > max_value:
            max_value = results[key]
            max_action = key
    return max_action


def initialize_classifier(all_training_data):
    X_train = all_training_data.drop(columns="reward")
    y_train = all_training_data["reward"]

    mlp = MLPClassifier(solver='adam', alpha=1e-4,
                        hidden_layer_sizes=(24, 24, 24, 24),
                        random_state=1, verbose=True)

    return mlp.fit(X_train, y_train)


def retrain_model(all_training_data, game_state, action, reward):
    final_training_vector = game_state
    final_training_vector['action'] = action
    final_training_vector['reward'] = reward

    all_training_data.append(final_training_vector)
    return initialize_classifier(all_training_data), all_training_data


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


class AI:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    # 0 - left, 1 - right, 2 - shoot, 3 - nothing,
    # 4 - left + shoot, 5 - right + shoot
    def next_move(self, game_state_vector):
        # print(game_state_vector)
        prediction = self.ai_model.predict(np.array(game_state_vector).reshape(1, -1))
        # print(prediction)
        # if prediction[0] == 0:
        #     return 4
        #
        # if prediction[0] == 1:
        #     return 5
        #
        # if prediction[0] == 3:
        #     return 2
        #
        return prediction[0]
        # return random.randint(0, 5)


# ai_agent = AI(ai_model_pkl)
all_training_data = load_historical_train()
classifier = initialize_classifier(all_training_data)

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
frame_count = 0

game_state = game.GameState(Player.state_vector_size, Mob.state_vector_size, MOBS_SIZE)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    was_shooting = False

    game_state.update_game_state(mobs, player, bullets, frame_count)

    action = ai_agent.next_move(game_state.dump_state())

    game_state.save_action(action)

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

    # game_state.update_game(mobs, player, bullets, action, score)
    # print(','.join(map(str, game_state.dump_state())))

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    frame_count = frame_count + 1


end = time.time()

print("time: {} sec, score: {}".format(round(end - game_start_time), score))
pygame.quit()
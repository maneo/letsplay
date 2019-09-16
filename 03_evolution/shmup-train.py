# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 4
# Video link: https://www.youtube.com/watch?v=mOckdKp3V38
# Adding graphics
from math import sqrt

import pygame
import time
import random
from os import path
import game_state as gstate


img_dir = path.join(path.dirname(__file__), '../img')

WIDTH = 480
HEIGHT = 600
FPS = 60
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

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
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

    state_vector_size = 3

    def dump_state_vector(self, player):
        player_x = player.rect.centerx
        player_y = player.rect.bottom
        distance = round(sqrt((player_x - self.rect.x) * (player_x - self.rect.x) + (player_y-self.rect.y) * (player_y-self.rect.y)))
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


def detect_and_save_action(pygame, was_shooting, game_state):
    action = 0
    keystate = pygame.key.get_pressed()

    # 0 - left, 1 - right, 2 - shoot, 3 - nothing,
    # 4 - left + shoot, 5 - right + shoot
    if was_shooting:
        if keystate[pygame.K_LEFT]:
            action = 4
        elif keystate[pygame.K_RIGHT]:
            action = 5
        else:
            action = 2
    elif keystate[pygame.K_LEFT]:  # print("key_pressed: K_LEFT")
        action = 0
    elif keystate[pygame.K_RIGHT]:  # print("key_pressed: K_RIGHT")
        action = 1
    elif keystate[pygame.K_SPACE]:  # print("key_pressed: K_SPACE")
        action = 2
    else:  # print("key_pressed: NONE")
        action = 3

    game_state.save_action(action)


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

# Game loop
score = 0
game_start_time = time.time()
game_state = gstate.GameState(Player.state_vector_size, Mob.state_vector_size, MOBS_SIZE)

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    wasShooting = False

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                wasShooting = True

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

    game_state.update_game_state(mobs, player, bullets)
    detect_and_save_action(pygame, wasShooting, game_state)

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    game_state.print_state()

end = time. time()
# print("time: {} sec, score: {}".format(round(end - game_start_time), score))

pygame.quit()

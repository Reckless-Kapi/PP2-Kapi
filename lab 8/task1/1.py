# Imports
import pygame, sys
from pygame.locals import *
import os, random, time

# Initialize pygame and sound
pygame.init()
pygame.mixer.init()

# Resource paths
BASE_PATH = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 8\task1"
IMAGES_PATH = os.path.join(BASE_PATH, "images")
MUSIC_PATH = os.path.join(BASE_PATH, "sounds")

# Screen setup
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer with Coins")

# Clock and FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Speeds and scores
SPEED = 5
SCORE = 0
COINS = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load resources
background = pygame.image.load(os.path.join(IMAGES_PATH, "AnimatedStreet.png"))
crash_sound = pygame.mixer.Sound(os.path.join(MUSIC_PATH, "crash.wav"))

# Play background music
pygame.mixer.music.load(os.path.join(MUSIC_PATH, "background.wav"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGES_PATH, "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGES_PATH, "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGES_PATH, "Coin.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.top = -50
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

# Sprites
P1 = Player()
E1 = Enemy()
coin1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(E1)
coins.add(coin1)
all_sprites.add(P1, E1, coin1)

# Timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Draw scores
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.mixer.music.stop()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision with coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        for coin in coins:
            coin.reset_position()

    pygame.display.update()
    FramePerSec.tick(FPS)

import pygame
import sys
import random
import time
import os

pygame.init()

# Настройки экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer with Coins")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Начальная настройка
SPEED = 5
SCORE = 0
COINS = 0
N_COINS_FOR_SPEED = 5  
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка ресурсов
BASE_PATH = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 8\task1"
IMAGES_PATH = os.path.join(BASE_PATH, "images")
background = pygame.image.load(os.path.join(IMAGES_PATH, "AnimatedStreet.png"))

# Звук
crash_sound = pygame.mixer.Sound(os.path.join(BASE_PATH, "sounds", "crash.wav"))
pygame.mixer.music.load(os.path.join(BASE_PATH, "sounds", "background.wav"))
pygame.mixer.music.play(-1)  # Воспроизведение фоновой музыки на повторе
pygame.mixer.music.set_volume(0.3)  # Уменьшение громкости музыки

# Классы
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

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGES_PATH, "Coin.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
        self.weight = random.randint(1, 5)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.top = -50
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGES_PATH, "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0) 
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0) 

# Создание объектов
P1 = Player()
E1 = Enemy()
coin1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(E1)
coins.add(coin1)
all_sprites.add(P1, E1, coin1)

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Двигаем и рисуем спрайты
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка на столкновение с врагом
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

    # Проверка на сбор монеты
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        for coin in coins:
            coin.reset_position()

    # Увеличение скорости врага после сбора N монет
    if COINS >= N_COINS_FOR_SPEED:
        SPEED *= 1.5  # Увеличиваем скорость в 1.5 раза
        COINS = 0  # Монеты больше не сбрасываются, но оставляем условие сброса

    pygame.display.update()
    pygame.time.Clock().tick(60)

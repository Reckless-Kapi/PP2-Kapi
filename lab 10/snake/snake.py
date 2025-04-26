import pygame, sys, random, time
import psycopg2
from config import load_config
from insert import insert_player_result
from update import update_person
from get_player import get_player_data

pygame.init()

# Размеры окна и блоков
BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.SysFont("Montserrat", 20)
game_over_font = pygame.font.SysFont("Montserrat", 50)

#ввод имени
clock = pygame.time.Clock()
def get_player_name():
    name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        screen.fill(WHITE)
        prompt = font.render("Enter your name:", True, BLACK)
        name_surface = font.render(name, True, BLACK)
        screen.blit(prompt, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
        screen.blit(name_surface, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(10)
    return name

player = get_player_name()

# Проверка игрока в базе
if get_player_data(player) is None:
    insert_player_result(player, 1, 0, 10)
else:
    print(f"Добро пожаловать обратно, {player}!")

# Змейка
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
score = 0
level = 1
speed = 10
paused = False

# Генерация еды
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            weight = random.randint(1, 5)
            return (x, y, weight)

def food_timer(food_spawn_time, expiration_time=5):
    return time.time() - food_spawn_time > expiration_time

food = generate_food()
food_spawn_time = time.time()

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    if get_player_data(player):
                        update_person(player, level, score, speed)
                        print("Игра поставлена на паузу и сохранена. Нажмите P, чтобы продолжить.")

    if paused:
        pause_text = game_over_font.render("PAUSE", True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        pygame.display.flip()
        clock.tick(5)
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_s] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_a] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_d] and direction != 'LEFT':
        direction = 'RIGHT'

    head_x, head_y = snake[0]
    if direction == 'UP': head_y -= BLOCK_SIZE
    elif direction == 'DOWN': head_y += BLOCK_SIZE
    elif direction == 'LEFT': head_x -= BLOCK_SIZE
    elif direction == 'RIGHT': head_x += BLOCK_SIZE
    new_head = (head_x, head_y)

    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake):
        game_over_text = game_over_font.render("Game Over", True, RED)
        final_score_text = game_over_font.render(f"Score: {score}", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
        screen.blit(final_score_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(2)
        if get_player_data(player):
            update_person(player, level, score, speed)
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)
    if new_head == food[:2]:
        score += food[2]
        food = generate_food()
        food_spawn_time = time.time()
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    if food_timer(food_spawn_time):
        food = generate_food()
        food_spawn_time = time.time()

    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    score_text = font.render(f"Score: {score}   Level: {level}   [P] Pause", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
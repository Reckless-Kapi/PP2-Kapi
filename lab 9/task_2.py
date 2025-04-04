import pygame, sys, random, time

pygame.init()

# Размеры окна и блоков
BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Montserrat", 20)

# Змейка: начальное положение
snake = [(100, 100), (80, 100), (60, 100)]  # Список блоков
direction = 'RIGHT'

score = 0
level = 1
speed = 10

# Функция генерации еды
def generate_food():
    is_super_food = random.random() < 0.1  # 10% шанс на супер еду
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            if is_super_food:
                return (x, y, 5, True)  # Супер еда даёт 5 очков
            else:
                return (x, y, 1, False)  # Обычная еда даёт 1 очко

# Функция для удаления еды по времени
def remove_food(food_time, food_lifetime=5):
    if time.time() - food_time > food_lifetime:
        return True
    return False

# Генерация начальной еды
food = generate_food()
food_time = time.time()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    # Проверяем нажатие клавиш и меняем направление только если оно не противоположное текущему
    if keys[pygame.K_w] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_s] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_a] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_d] and direction != 'LEFT':
        direction = 'RIGHT'
    
    # Обновление позиции головы змеи
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= BLOCK_SIZE
    elif direction == 'DOWN':
        head_y += BLOCK_SIZE
    elif direction == 'LEFT':
        head_x -= BLOCK_SIZE
    elif direction == 'RIGHT':
        head_x += BLOCK_SIZE
    new_head = (head_x, head_y)

    # Проверка выхода за границы — game over
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake):
        print("Game Over! Final score:", score)
        pygame.quit()
        sys.exit()
    snake.insert(0, new_head)

    # Проверка, съела ли змея еду
    if new_head == (food[0], food[1]):
        score += food[2]  # Добавляем очки в зависимости от еды
        if food[3]:  # Проверяем, была ли съедена супер еда
            print("Super food eaten!")
        food = generate_food()  # Генерация новой еды
        food_time = time.time()  # Обновляем время еды

        # Повышение уровня каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Удалить последний элемент, если еда не съедена

    # Удаление еды по таймеру, если она не была съедена
    if remove_food(food_time):
        food = generate_food()
        food_time = time.time()

    # Отрисовка еды и змеи
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Отображение очков и уровня
    score_text = font.render(f"Score: {score}   Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

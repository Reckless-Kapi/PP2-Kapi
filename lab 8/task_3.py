import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = (0, 0, 255)
mode = 'brush'
radius = 5
last_pos = None
start_pos = None

screen.fill(WHITE)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = 'brush'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_n:
                color = (0, 0, 255)
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_q:
                mode = 'rect'

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            last_pos = event.pos  # Запоминаем позицию
            if mode == 'brush':
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == 'eraser':
                pygame.draw.circle(screen, WHITE, event.pos, radius)

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Если зажата ЛКМ
                if last_pos:  # Проверяем, что last_pos не None
                    if mode == 'brush':
                        pygame.draw.line(screen, color, last_pos, event.pos, radius * 2)
                    elif mode == 'eraser':
                        pygame.draw.line(screen, WHITE, last_pos, event.pos, radius * 2)
                last_pos = event.pos  # Обновляем позицию

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if start_pos:
                if mode == 'circle':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    rect.normalize()
                    pygame.draw.ellipse(screen, color, rect, 2)
                elif mode == 'rect':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    rect.normalize()
                    pygame.draw.rect(screen, color, rect, 2)
            last_pos = None
            start_pos = None

    pygame.display.flip()
    clock.tick(60)

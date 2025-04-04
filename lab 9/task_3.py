import pygame
import sys
import math

pygame.init()

# Initialize screen and clock
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
color = (0, 0, 255)

# Drawing settings
mode = 'brush'
radius = 5
start_pos = None

# Initial screen setup
screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = 'brush'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_q:
                mode = 'rect'
            elif event.key == pygame.K_s:
                mode = 'square'  # Draw square
            elif event.key == pygame.K_t:
                mode = 'triangle'  # Draw right triangle
            elif event.key == pygame.K_h:
                mode = 'rhombus'  # Draw rhombus
            elif event.key == pygame.K_y:
                mode = 'equilateral_triangle'  # Draw equilateral triangle

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            if mode == 'brush':
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == 'eraser':
                pygame.draw.circle(screen, WHITE, event.pos, radius)

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # left button held
                if mode == 'brush':
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == 'eraser':
                    pygame.draw.circle(screen, WHITE, event.pos, radius)

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
                elif mode == 'square':
                    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
                    pygame.draw.rect(screen, color, rect, 2)
                elif mode == 'triangle':
                    # Draw right triangle
                    pygame.draw.polygon(screen, color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
                elif mode == 'equilateral_triangle':
                    # Calculate the equilateral triangle's points
                    side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    height = side_length * math.sqrt(3) / 2
                    points = [
                        start_pos, 
                        (start_pos[0] + side_length, start_pos[1]), 
                        ((start_pos[0] + (start_pos[0] + side_length)) // 2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(screen, color, points, 2)
                elif mode == 'rhombus':
                    # Draw rhombus (diamond shape)
                    half_diag1 = abs(end_pos[0] - start_pos[0]) // 2
                    half_diag2 = abs(end_pos[1] - start_pos[1]) // 2
                    rhombus_points = [
                        (start_pos[0] + half_diag1, start_pos[1]), 
                        (start_pos[0], start_pos[1] + half_diag2),
                        (start_pos[0] - half_diag1, start_pos[1]),
                        (start_pos[0], start_pos[1] - half_diag2)
                    ]
                    pygame.draw.polygon(screen, color, rhombus_points, 2)

                start_pos = None

    pygame.display.flip()
    clock.tick(60)

import pygame
pygame.init()

display = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
red = (255, 0, 0)
clock = pygame.time.Clock()
FPS = 60
pos = [30, 30]
speed = 20
radius = 25
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and pos[0] + radius + speed <= 800:
        pos[0] += speed
    if keys[pygame.K_LEFT] and pos[0] - radius - speed >= 0:
        pos[0] -= speed
    if keys[pygame.K_DOWN] and pos[1] + radius + speed <= 600:
        pos[1] += speed
    if keys[pygame.K_UP] and pos[1] - radius - speed >= 0:
        pos[1] -= speed

    display.fill(white)
    pygame.draw.circle(display, red, pos, radius)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

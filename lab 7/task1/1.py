import pygame
import time
import os

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Крыса Микки")
clock = pygame.time.Clock()

base_path = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 7\task1"
image_miki = pygame.image.load(os.path.join(base_path, "clock.png"))
image_min = pygame.image.load(os.path.join(base_path, "min_hand.png"))
image_sec = pygame.image.load(os.path.join(base_path, "sec_hand.png"))

sec = image_sec.get_rect(center=(400, 300))
minute = image_min.get_rect(center=(400, 300))
angle1 = 60
angle2 = -49.5
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rat_sec = pygame.transform.rotate(image_sec, angle1)
    sec_rect = image_sec.get_rect(center=(400, 300))
    rot_rect = rat_sec.get_rect(center=sec_rect.center)
    
    rat_min = pygame.transform.rotate(image_min, angle2)
    rotan_min = rat_min.get_rect(center=minute.center)

    display.fill((0, 0, 0))
    display.blit(image_miki, (0, 0))
    display.blit(rat_sec, rot_rect.topleft)
    display.blit(rat_min, rotan_min.topleft)

    pygame.display.flip()
    angle2 -= 0.5
    angle1 -= 6
    time.sleep(1)

pygame.quit()

import pygame
import os

pygame.init()
pygame.mixer.init()

BASE_PATH = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 7\task2"
MUSIC_PATH = os.path.join(BASE_PATH, "music")
BUTTONS_PATH = os.path.join(BASE_PATH, "buttons")

tracks = [
    os.path.join(MUSIC_PATH, "here_we_go_again.mp3"),
    os.path.join(MUSIC_PATH, "Theme_song.mp3"),
    os.path.join(MUSIC_PATH, "Intro.mp3")
]


current = 0

if os.path.exists(tracks[current]):
    pygame.mixer.music.load(tracks[current])
    pygame.mixer.music.play()

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("GTA Songs")

def load_image(filename):
    path = os.path.join(BUTTONS_PATH, filename)
    return pygame.image.load(path) if os.path.exists(path) else pygame.Surface((50, 50), pygame.SRCALPHA)

background_path = os.path.join(BASE_PATH, "gtasa.png")
if os.path.exists(background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (1280, 720))
else:
    background = pygame.Surface((1280, 720))

image_back = load_image("back 1.png")
image_next = load_image("back 2.png")
image_pause = load_image("pause 1.png")
image_play = load_image("play 1.png")

center_x, center_y = 640, 360
spacing = 120

back = image_back.get_rect(center=(center_x - spacing * 1.5, center_y + 150))
pause = image_pause.get_rect(center=(center_x - spacing / 2, center_y + 150))
play = image_play.get_rect(center=(center_x + spacing / 2, center_y + 150))
next = image_next.get_rect(center=(center_x + spacing * 1.5, center_y + 150))

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(event.pos):
                pygame.mixer.music.unpause()
            elif pause.collidepoint(event.pos):
                pygame.mixer.music.pause()
            elif next.collidepoint(event.pos):
                current = (current + 1) % len(tracks)
                if os.path.exists(tracks[current]):
                    pygame.mixer.music.load(tracks[current])
                    pygame.mixer.music.play()
            elif back.collidepoint(event.pos):
                current = (current - 1) % len(tracks)
                if os.path.exists(tracks[current]):
                    pygame.mixer.music.load(tracks[current])
                    pygame.mixer.music.play()

    display.blit(background, (0, 0))
    display.blit(image_back, back)
    display.blit(image_pause, pause)
    display.blit(image_play, play)
    display.blit(image_next, next)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Main Menu')
pygame.mixer.music.load("audio/music/main_menu.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load("sprites/backgrounds/main_menu_background/main.gif")

# DONE = False
# alphaSurface = pygame.Surface((1280, 720))  # The custom-surface of the size of the screen.
# alphaSurface.fill((255, 255, 255))  # Fill it with whole white before the main-loop.
# alphaSurface.set_alpha(0)  # Set alpha to 0 before the main-loop.
# alph = 0  # The increment-variable.
# while not DONE:
#     screen.fill((0, 0, 0))  # At each main-loop fill the whole screen with black.
#     alph += 0.1  # Increment alpha by a really small value (To make it slower, try 0.01)
#     alphaSurface.set_alpha(alph)  # Set the incremented alpha-value to the custom surface.
#     screen.blit(alphaSurface, (0, 0))  # Blit it to the screen-surface (Make them separate)

font_main = pygame.font.SysFont("Baskerville Old Face", 70)
font_start = pygame.font.SysFont("Baskerville Old Face", 50)
font_start_mouse = pygame.font.SysFont("Baskerville Old Face", 50, italic=True)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill((0, 0, 0))
        button_1 = pygame.Rect(510, 350, 225, 45)
        pygame.draw.rect(screen, (0, 0, 0, 0), button_1)
        screen.blit(background, (1, 0))
        draw_text('Wanted Ranger', font_main, (255, 255, 255), screen, 400, 200)
        mx, my = pygame.mouse.get_pos()
        if not button_1.collidepoint((mx, my)):
            draw_text('Start Game', font_start, (255, 255, 255), screen, 510, 350)
        if button_1.collidepoint((mx, my)):
            draw_text('Start Game', font_start_mouse, (255, 255, 255), screen, 510, 350)
            if click:
                game()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font_main, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()

import pygame
import time
import random
import os

WIDTH, HEIGHT = 750, 600
BG = pygame.transform.scale(pygame.image.load(os.path.join("png", "BG.png")), (WIDTH, HEIGHT))
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wanted Ranger")
CHARACTER_IMAGE = pygame.image.load(os.path.join("png", "Character.png"))

class character:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.bullet_img = None
        self.bullets = []
        self.cooldown_counter = 0

    def draw(self, WINDOW):
        WINDOW.blit(self.character_img, (self.x, self.y))

class Character(character):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.character_img = CHARACTER_IMAGE


def main():
    runnable = True
    FPS = 60
    clock = pygame.time.Clock()
    character = Character(300, 300)
    VELOCITY = 5

    def redraw_window():
        WINDOW.blit(BG, (0, 0))
        character.draw(WINDOW)
        pygame.display.update()

    while runnable:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnable = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and character.x - VELOCITY > 0: #left
            character.x -= VELOCITY
        if keys[pygame.K_d] and character.x + VELOCITY < WIDTH - 50: #right
            character.x += VELOCITY
        if keys[pygame.K_w] and character.y - VELOCITY > 0: #up
            character.y -= VELOCITY
        if keys[pygame.K_s] and character.y + VELOCITY < HEIGHT - 50: #down
            character.y += VELOCITY

main()

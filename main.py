import pygame
import time
import random
import os

WIDTH, HEIGHT = 1024, 768
TILE_SIZE = 24
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE
CHAR_WIDTH, CHAR_HEIGHT = 80, 160
LIGHTGREY = (169, 169, 169)
BG = pygame.transform.scale(pygame.image.load(os.path.join("png", "BG.png")), (WIDTH, HEIGHT))
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wanted Ranger")
CHARACTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("png", "Character.png")), (CHAR_WIDTH, CHAR_HEIGHT))

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
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health


def main():
    runnable = True
    FPS = 60
    clock = pygame.time.Clock()
    character = Character(240, 200)
    VELOCITY = TILE_SIZE

    def draw_grid():
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(WINDOW, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(WINDOW, LIGHTGREY, (0, y), (WIDTH, y))

    def redraw_window():
        WINDOW.blit(BG, (0, 0))
        character.draw(WINDOW)
        draw_grid()
        pygame.display.update()

    def player_movement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and character.x - VELOCITY > 0: #left
            character.x -= VELOCITY
        if keys[pygame.K_d] and character.x + VELOCITY < WIDTH - CHARACTER_IMAGE.get_width(): #right
            character.x += VELOCITY
        if keys[pygame.K_w] and character.y - VELOCITY > 0: #up
            character.y -= VELOCITY
        if keys[pygame.K_s] and character.y + VELOCITY < HEIGHT - CHARACTER_IMAGE.get_height(): #down
            character.y += VELOCITY

    while runnable:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnable = False

        player_movement()

main()

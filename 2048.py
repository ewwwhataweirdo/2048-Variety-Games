import pygame
import math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

win = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("2048")
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

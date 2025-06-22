import pygame , button, tiles
from button import Button
from tiles import tile
import random
from pygame.locals import *
import math
pygame.init()

SCREEN_WIDTH = 800
#pygame.display.Info().current_w
SCREEN_HEIGHT = 600
#pygame.display.Info().current_h

win = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Variety 2048")

Font = pygame.font.SysFont("arialblack", 50)
Text_col = (255, 255, 255)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))


run = True
while run:
    win.fill((255, 228, 196))

    draw_text("Welcome to Variety 2048", Font, Text_col, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 25)
    regular_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50, "Regular Mode")
    regular_button.draw(win)
    # Event handler
    for event in pygame.event.get():

        #Quit the game
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            print(event.button)
            # Checks for left mouse click
            if int(event.button) == 1:
                pygame.display.update()
                win.fill((0, 0, 0))

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            # Handle escape key quitting
            if event.key == pygame.K_ESCAPE:
                run = False
            # Handle arrow keys
            if event.key == pygame.K_RIGHT:
                # Move all avaiable tiles to the right
                print("Right key pressed")
            if event.key == pygame.K_LEFT:
                # Move all avaiable tiles to the left
                print("Left key pressed")
            if event.key == pygame.K_UP:
                # Move all avaiable tiles up
                print("Up key pressed")
            if event.key == pygame.K_DOWN:
                # Move all avaiable tiles down
                print("Down key pressed")
    pygame.display.update()

pygame.quit()

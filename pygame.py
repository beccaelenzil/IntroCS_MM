import random
import time
import pygame
from gameOfLifeFunctions import *

width = 90
height = 90
cell_size = 5
spacing = 1

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = height*(cell_size+spacing)
screen_height = width*(cell_size+spacing)

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game Of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def drawBoard(A,width,height,cell_size,spacing):
    #A = createBoard(width,height)
    for row in range(height):
        x_pos = row*(cell_size+spacing)
        for col in range(width):
            y_pos = col*(cell_size+spacing)
            if A[row][col] == 1:
                pygame.draw.rect(screen, WHITE, [x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == 0:
                pygame.draw.rect(screen, BLACK,[x_pos,y_pos,cell_size,cell_size])

A = randomCells(width,height)
drawBoard(A,width,height,cell_size,spacing)
pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    A = next_life_generation(A)
    drawBoard(A,width,height,cell_size,spacing)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    #clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

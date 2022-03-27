import random
import time

import numpy as np
import pygame

# Surface size (preferably a square)
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Cell size (preferably a square)
CELL_WIDTH = 20
CELL_HEIGHT = 20
 
# Margin between 2 cells (px)
MARGIN = 5

# Number of cells on each row
# Proportional to surface width
cells_in_row = WIN_WIDTH // (CELL_WIDTH + MARGIN)
print("-- Dimensions --")
print("{}x{} px".format(WIN_WIDTH, WIN_HEIGHT))
print("{}x{} ({}) cells\n".format(cells_in_row, cells_in_row, cells_in_row**2))

run = True # Main loop flag
random_anim = False # Cells color randomization flag
fps = 60 # Frame Per Second
anim_speed = 0.05 # Speed animation (second)

# Set colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# CREATING A 2 DIMENTIONNAL ARRAY
# An cells_in_row X cells_in_row dimension array where each value 
# represents the state of a cell. These values can be 0 for a white
# cell or 1 for a black cell. Initially all values are 
# initialized to zero

# METHOD WITHOUT NUMPY
# Crating a list of lists 
# Each list represents a row and each value in a list 
# represents the column
""" grid = []
for row in range(cells_in_row):
    grid.append([])
    for column in range(cells_in_row):
        grid[row].append(0) """

# METHOD WITH NUMPY
# Numpy has a quick and easy method to initialize all 
# values of an array of a desired dimension to zero
grid = np.zeros([cells_in_row, cells_in_row], dtype = int)
 
pygame.init()
 
# Set surface dimension
WINDOW_SIZE = [WIN_WIDTH, WIN_HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Grille Pygame")

clock = pygame.time.Clock()
 
# -------- MAIN LOOP -----------
while run:
    for event in pygame.event.get():  # All user events
        if event.type == pygame.QUIT:  # Closing window
            run = False # Exit from main loop
            break

        if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click
            if pygame.mouse.get_pressed()[0]: # Left click
                pos = pygame.mouse.get_pos() # Get cursor coordinates

                # Conversion of x,y coordinates to grid coordinates
                column = pos[0] // (CELL_WIDTH + MARGIN) # Column localisation (x axis)
                row = pos[1] // (CELL_HEIGHT + MARGIN) # Row localisation (y axis)
                print("[Column : {} - Row : {}]".format(column, row))
                """ print("column = {} // ({} + {}) = {}".format(pos[0], CELL_WIDTH, MARGIN, column))
                print("row = {} // ({} + {}) = {}\n".format(pos[1], CELL_WIDTH, MARGIN, row)) """
                
                # Cell state change
                # These values will define the color with which 
                # each cell should be drawn
                if grid[row][column] == 0:
                    grid[row][column] = 1 # Black cell
                else:
                    grid[row][column] = 0 # White cell
            
            if pygame.mouse.get_pressed()[2]: # Roght click
                if random_anim == False:
                    random_anim = True
                    print("\nRANDOMIZOR ON\n")
                else:
                    random_anim = False
                    print("\nRANDOMIZOR OFF\n")
 
    # Background color (margin color)
    screen.fill("darkblue") 
 
    # GRID DRAWING
    for row in range(cells_in_row):
        for column in range(cells_in_row):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            else :
                color = WHITE
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + CELL_WIDTH) * column + MARGIN,
                            (MARGIN + CELL_HEIGHT) * row + MARGIN,
                            CELL_WIDTH,
                            CELL_HEIGHT])

    if random_anim:
        x = random.randint(0, cells_in_row-1)
        y = random.randint(0, cells_in_row-1)

        if grid[x][y] == 1:
            grid[x][y] = 0
        else:
            grid[x][y] = 1

        time.sleep(anim_speed)

    # Limite de 60 FPS
    clock.tick(fps)
 
    # Mise à jour de l'affichage
    pygame.display.flip()
 
pygame.quit()
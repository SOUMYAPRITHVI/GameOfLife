# import pygame
import random


def create_initial_grid(GRID_WIDTH=60,GRID_HEIGHT=60):
    grid = []
    for _ in range(GRID_WIDTH):
        row = [random.randint(0, 0) for _ in range(GRID_HEIGHT)]
        grid.append(row)
    return grid
print(create_initial_grid(5,5))
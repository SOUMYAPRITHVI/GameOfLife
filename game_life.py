# import pygame
import random


def create_initial_grid(GRID_WIDTH=60,GRID_HEIGHT=60):
    grid = []
    for _ in range(GRID_WIDTH):
        row = [random.randint(0, 0) for _ in range(GRID_HEIGHT)]
        grid.append(row)
    return grid

def update_grid(grid,x,y):
    new_grid = create_initial_grid(x,y)
    for i in range(x):
        for j in range(y):
            live_neighbors=0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx==0 and dy==0:
                        continue
                    new_x,new_y=i+dx,j+dy
                    if 0<=new_x<y and 0<=new_y<x:
                        live_neighbors+=grid[new_x][new_y]   
            if grid[i][j] == 1:
                print(live_neighbors)
                if live_neighbors<2 or live_neighbors > 3:
                    new_grid[i][ j] = 0
                else:
                    new_grid[i][j] = 1
            elif live_neighbors == 3:
                new_grid[i][ j] = 1    
            else:
                new_grid[i][ j] = 0  
    return new_grid


import pygame
import random

WIDTH,HEIGHT=100,100
CELL_SIZE=20
GRID_WIDTH,GRID_HEIGHT=WIDTH//CELL_SIZE,HEIGHT//CELL_SIZE
GREEN=(0,225,110)
BLACK=(0,0,0)

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

running=True
while True:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit()
            # running=False
    
    [pygame.draw.line(screen,pygame.Color(BLACK),(x,0),(x,HEIGHT)) for x in range(0,WIDTH,CELL_SIZE)]
    [pygame.draw.line(screen,pygame.Color(BLACK),(0,y),(WIDTH,y)) for y in range(0,HEIGHT,CELL_SIZE)]
    pygame.display.flip()
    pygame.time.delay(200)
# clock.tick(10)
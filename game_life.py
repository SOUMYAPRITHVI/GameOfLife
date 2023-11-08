import pygame

WIDTH, HEIGHT = 1000, 1000
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
GREEN = (0, 255, 110)
BLACK = (0, 0, 0)


def create_initial_grid(GRID_WIDTH,GRID_HEIGHT):
    grid = []
    for _ in range(GRID_HEIGHT):
        row = [0] * GRID_WIDTH
        grid.append(row)
    return grid

def update_grid(grid,GRID_WIDTH,GRID_HEIGHT):
    new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    # new_grid = create_initial_grid()
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            live_neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    new_x, new_y = i + dx, j + dy
                    print(new_x,new_y,GRID_HEIGHT,GRID_WIDTH)
                    if 0 <= new_x < GRID_HEIGHT and 0 <= new_y < GRID_WIDTH:
                        live_neighbors += grid[new_x][new_y]
            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            elif live_neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

def draw_grid(screen, grid):
    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

running = True
grid = create_initial_grid(GRID_WIDTH,GRID_HEIGHT)
drawing = False  # Flag to indicate if the user is currently drawing
simulation = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle simulation when the spacebar is pressed
                simulation = not simulation

        if not simulation:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x //= CELL_SIZE
                y //= CELL_SIZE
                grid[x][y] = 1
    if simulation:
        grid = update_grid(grid,GRID_WIDTH,GRID_HEIGHT)

    screen.fill(GREEN)
    draw_grid(screen, grid)

    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()

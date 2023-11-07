import game_life
def test_empty_grid_initialzation():
    grid=game_life.create_initial_grid(5,5)
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_simulate_draw():
    grid=game_life.create_initial_grid(5,5)
    grid[2][3]=1
    grid[1][4]=1
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_simulate_erase():
    grid=game_life.create_initial_grid(5,5)
    grid[2][3]=1
    grid[1][4]=1
    grid[2][3]=0
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
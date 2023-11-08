from game_life import create_initial_grid,update_grid

def test_empty_grid_initialzation():
    grid=create_initial_grid(5,5)
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_simulate_draw():
    grid=create_initial_grid(5,5)
    grid[2][3]=1
    grid[1][4]=1
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_simulate_erase():
    grid=create_initial_grid(5,5)
    grid[2][3]=1
    grid[1][4]=1
    grid[2][3]=0
    assert grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_update_no_live_neighbor():
    grid=[[0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    new_grid=update_grid(grid,5,5)
    assert new_grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
def test_update_three_or_less_live_neighbors():
    grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    new_grid=update_grid(grid,5,5)
    assert new_grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

def test_update_more_than_three_live_neighbors():
    grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    new_grid=update_grid(grid,5,5)
    assert new_grid==[[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0]]

def test_update_stable_state():
    grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    new_grid=update_grid(grid,5,5)
    assert new_grid==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    
  
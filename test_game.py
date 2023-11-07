import game_life
def test_empty_grid_initialzation():
    grid=game_life.create_initial_grid(5,5)
    assert grid=="""[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]"""
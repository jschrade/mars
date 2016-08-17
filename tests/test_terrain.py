import numpy as np
import pytest

from mars_rover import Terrain


@pytest.mark.unit
def test_init():
    terrian = Terrain(2,2)

    assert np.array_equal(
        terrian.terrain,
        np.zeros(
            shape=(2,2),
            dtype=np.int
        )
    )


@pytest.mark.unit
def test_max_x(basic_terrain):
    assert basic_terrain.max_x == 1


@pytest.mark.unit
def test_max_x(basic_terrain):
    assert basic_terrain.max_y == 1


@pytest.mark.unit
def test_add_obstacle(basic_terrain):
    basic_terrain.add_obstacle((1,1))

    assert np.array_equal(
        basic_terrain.terrain,
        np.array(
            [[0,0], [0,1]],
            dtype=np.int
        )
    )


@pytest.mark.unit
def test_is_clear(terrain_with_obstacle):
    assert terrain_with_obstacle.is_clear((0,0)) == True
    assert terrain_with_obstacle.is_clear((0,1)) == True
    assert terrain_with_obstacle.is_clear((1,0)) == True
    assert terrain_with_obstacle.is_clear((1,1)) == False

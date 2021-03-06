import os

import pytest

from mars_rover import Rover, Terrain


@pytest.fixture()
def basic_terrain():
    return Terrain(2, 2)


@pytest.fixture()
def terrain_with_obstacle():
    terrain = Terrain(2, 2)
    terrain.add_obstacle((1, 1))
    return terrain


@pytest.fixture()
def basic_rover(basic_terrain):
    return Rover(
        basic_terrain, (0, 0), Rover.NORTH
    )


@pytest.fixture()
def obstacle_rover(terrain_with_obstacle):
    return Rover(
        terrain_with_obstacle, (0, 1), Rover.NORTH
    )

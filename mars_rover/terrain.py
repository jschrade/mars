import numpy as np


class Terrain():
    def __init__(self, width, height):
        self.terrain = np.zeros(
            shape=(width, height),
            dtype=np.int
        )

    @property
    def max_x(self):
        return self.terrain.shape[0] - 1

    @property
    def max_y(self):
        return self.terrain.shape[1] - 1

    def add_obstacle(self, coord):
        self.terrain[coord[0]][coord[1]] = 1

    def is_clear(self, coord):
        return not bool(self.terrain[coord[0]][coord[1]])


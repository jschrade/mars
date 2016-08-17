from exceptions import ObstacleBlocking


FORWARD = 'f'
BACKWARD = 'b'
LEFT = 'l'
RIGHT = 'r'
ALL_COMMANDS = [
    FORWARD,
    BACKWARD,
    LEFT,
    RIGHT
]


class Rover(object):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    def __init__(self, terrain, location, direction):
        """
        Init a rover object.

        :type terrain: mars_rover.Terrian
        :param location: current location as coordinate
        :type location: tuple
        :param direction: direction rover is facing
        :type direction: constant string
        :return:
        """
        self.terrain = terrain
        self.x, self.y = location
        self.direction = direction

    def _parse_commands(self, string_buffer):
        return [
            command
            for command
            in string_buffer.split(',')
            if command in ALL_COMMANDS
        ]

    def _get_command_function(self, command):
        return getattr(self, '_cmd_{}'.format(command))

    def _check_clear(self, location):
        if not self.terrain.is_clear(location):
                raise ObstacleBlocking()

    def _move_rover(self, x, y):
        if x < 0:
            x = self.terrain.max_x
        if x > self.terrain.max_x:
            x = 0

        if y < 0:
            y = self.terrain.max_y
        if y > self.terrain.max_y:
            y = 0

        location = (x, y)
        self._check_clear(location)
        self.x, self.y = location

    def _cmd_f(self):
        x = self.x
        y = self.y

        if self.direction == self.NORTH:
            x -= 1
        if self.direction == self.SOUTH:
            x += 1
        if self.direction == self.WEST:
            y -= 1
        if self.direction == self.EAST:
            y += 1

        self._move_rover(x, y)

    def _cmd_b(self):
        x = self.x
        y = self.y

        if self.direction == self.NORTH:
            x += 1
        if self.direction == self.SOUTH:
            x -= 1
        if self.direction == self.WEST:
            y += 1
        if self.direction == self.EAST:
            y -= 1

        self._move_rover(x, y)

    def _cmd_l(self):
        if self.direction == self.NORTH:
            self.direction = self.WEST
            return
        if self.direction == self.SOUTH:
            self.direction = self.EAST
            return
        if self.direction == self.EAST:
            self.direction = self.NORTH
            return
        if self.direction == self.WEST:
            self.direction = self.SOUTH

    def _cmd_r(self):
        if self.direction == self.NORTH:
            self.direction = self.EAST
            return
        if self.direction == self.SOUTH:
            self.direction = self.WEST
            return
        if self.direction == self.EAST:
            self.direction = self.SOUTH
            return
        if self.direction == self.WEST:
            self.direction = self.NORTH

    @property
    def location(self):
        """
        Returns the rovers current location.
        :rtype: tuple
        """
        return (self.x, self.y)

    def run_commands(self, string_buffer):
        commands = self._parse_commands(string_buffer)
        for command in commands:
            self._get_command_function(command)()

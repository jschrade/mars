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
        self.terrain = terrain
        self.location = location
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

    def _cmd_f(self):
        pass

    def _cmd_b(self):
        pass

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

    def run_commands(self, string_buffer):
        commands = self._parse_commands(string_buffer)
        for command in commands:
            self._get_command_function(command)()

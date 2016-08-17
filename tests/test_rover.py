import mock
import numpy as np
import pytest

from mars_rover import Rover, ObstacleBlocking
from mars_rover.rover import FORWARD, BACKWARD, LEFT, RIGHT


@pytest.mark.unit
def test_init(basic_terrain):
    rover = Rover(basic_terrain, (0, 0), Rover.NORTH)

    assert rover.terrain == basic_terrain
    assert rover.location == (0, 0)
    assert rover.direction == Rover.NORTH


@pytest.mark.unit
@mock.patch('mars_rover.rover.Rover._parse_commands')
@mock.patch('mars_rover.rover.Rover._get_command_function')
def test_run_commands(
        mock_get_command_function, mock_parse_commands, basic_rover
):
    mock_parse_commands.return_value = ['f', 'b']
    mock_forward = mock.Mock()
    mock_backward = mock.Mock()
    mock_get_command_function.side_effect = [
        mock_forward, mock_backward
    ]

    basic_rover.run_commands('foo commands')
    mock_parse_commands.assert_called_once_with('foo commands')
    assert mock_get_command_function.mock_calls == [
        mock.call('f'),
        mock.call('b')
    ]
    mock_forward.assert_called_once_with()
    mock_backward.assert_called_once_with()


@pytest.mark.unit
def test__parse_commands(basic_rover):
    assert basic_rover._parse_commands('f,b,l,r') == [
        FORWARD,
        BACKWARD,
        LEFT,
        RIGHT
    ]

    assert basic_rover._parse_commands('f,fi, tb,r,   qw, ! $') == [
        FORWARD,
        RIGHT
    ]

    assert basic_rover._parse_commands('') == []


@pytest.mark.unit
def test__get_command_function(basic_rover):
    assert basic_rover._get_command_function('f') == basic_rover._cmd_f
    assert basic_rover._get_command_function('b') == basic_rover._cmd_b
    assert basic_rover._get_command_function('l') == basic_rover._cmd_l
    assert basic_rover._get_command_function('r') == basic_rover._cmd_r


@pytest.mark.unit
def test__cmd_l(basic_rover):
    basic_rover._cmd_l()
    assert basic_rover.direction == Rover.WEST

    basic_rover._cmd_l()
    assert basic_rover.direction == Rover.SOUTH

    basic_rover._cmd_l()
    assert basic_rover.direction == Rover.EAST

    basic_rover._cmd_l()
    assert basic_rover.direction == Rover.NORTH


@pytest.mark.unit
def test__cmd_r(basic_rover):
    basic_rover._cmd_r()
    assert basic_rover.direction == Rover.EAST

    basic_rover._cmd_r()
    assert basic_rover.direction == Rover.SOUTH

    basic_rover._cmd_r()
    assert basic_rover.direction == Rover.WEST

    basic_rover._cmd_r()
    assert basic_rover.direction == Rover.NORTH


@pytest.mark.unit
def test__cmd_f(basic_rover):
    basic_rover._cmd_f()
    assert basic_rover.location == (1, 0)

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.SOUTH

    basic_rover._cmd_f()
    assert basic_rover.location == (1, 0)

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.WEST

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 1)

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.EAST

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 1)

    basic_rover._cmd_f()
    assert basic_rover.location == (0, 0)


@pytest.mark.unit
def test__cmd_f_obstacle(obstacle_rover):
    with pytest.raises(ObstacleBlocking):
        obstacle_rover._cmd_f()


@pytest.mark.unit
def test__cmd_b(basic_rover):
    basic_rover._cmd_b()
    assert basic_rover.location == (1, 0)

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.SOUTH

    basic_rover._cmd_b()
    assert basic_rover.location == (1, 0)

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.WEST

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 1)

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 0)

    basic_rover.direction = Rover.EAST

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 1)

    basic_rover._cmd_b()
    assert basic_rover.location == (0, 0)


@pytest.mark.unit
def test__cmd_b_obstacle(obstacle_rover):
    with pytest.raises(ObstacleBlocking):
        obstacle_rover._cmd_b()


@pytest.mark.integration
def test_multi_move(basic_rover):
    basic_rover.run_commands('r,f,r,f')

    assert basic_rover.direction == Rover.SOUTH
    assert basic_rover.location == (1, 1)

    basic_rover.run_commands('r,r,f')

    assert basic_rover.direction == Rover.NORTH
    assert basic_rover.location == (0, 1)

    basic_rover.run_commands('f,l,f')

    assert basic_rover.direction == Rover.WEST
    assert basic_rover.location == (1, 0)

    basic_rover.run_commands('b,l,b')

    assert basic_rover.direction == Rover.SOUTH
    assert basic_rover.location == (0, 1)


@pytest.mark.integration
def test_multi_move_obstacle(obstacle_rover):
    with pytest.raises(ObstacleBlocking):
        obstacle_rover.run_commands('l,f,l,f,l,f')

    assert obstacle_rover.direction == Rover.EAST
    assert obstacle_rover.location == (1, 0)

# Mars Rover: Challenge

Develop an api that moves a rover around on a grid.
*You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
*The rover receives a character array of commands.
*Implement commands that move the rover forward/backward (f,b).
*Implement commands that turn the rover left/right (l,r).
*Implement wrapping from one edge of the grid to another. (planets are spheres after all)
*Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point and reports the obstacle.

## Install
```
pip install -r requirements.txt
```

## Usage
```python
terrain = Terrain((2,2))
rover = Rover(terrain, (0,0), Rover.NORTH)
rover.run_commands('r,f,r,f')
```

## Testing
```
pip intall -r requirements_dev.txt
py.test
```

## Docs
Only a few examples of in code doc strings were added to save time.

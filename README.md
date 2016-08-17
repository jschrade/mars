# Mars Rover: Challenge

## Install
```
pip install -r requirements.txt
```

## Usage
```
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

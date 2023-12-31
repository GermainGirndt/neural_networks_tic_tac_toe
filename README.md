### Python PATH

Add the project root directory to the python path

```
export PYTHONPATH="$( pwd )"
```

### Versions

```
python3 --version
Python 3.11.5
```

```
pip --version
pip 23.2.1 from ..../neural_networks_tic_tac_toe/venv/lib/python3.11/site-packages/pip (python 3.11)
```

### Execute tests

```
pytest src/**/*Test.py
```

### Create venv

```
python3 -m venv venv
```

### Activate venv

```
source venv/bin/activate
```

### Architecture Draft

- A tic tac toe game has:

- Checkers
  Can be X (0) or Y (1)

- Position
  X and Y: 0, 1 or 2

- BoardPosition
  X and Y: 0, 1 or 2

- Tile
  Receive a checker
  Can be empty or filled
  Must have a position

- Board
  Has the tiles in a 3x3 space
  All tiles are empty at start
  Displays all tiles

- Move
  Has the Checker which should be placed and it's position

- Players (2)
  Either X or O
  Should make a move

- GameManager
  Checks which player should play now
  Checks if the game has ended
  Check if any player won

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
pytest
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

- Matches
  Can be X (0) or Y (1)

- Position
  X and Y: 0, 1 or 2

- Tile
  Receive a match
  Can be empty or filled
  Must have a position

- Board
  Has the tiles in a 3x3 space
  All tiles are empty at start
  Displays all tiles

- Judge
  Checks who should play now
  Receive orders from players
  Checks if the move is valid
  Checks if the game has ended
  Check if any player won

- Players (2)
  Either X or O
  Place a match into a board's tile

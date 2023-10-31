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

- Tile
  Can be empty or filled

- Board
  Has the tiles in a 3x3 space
  Displays which tiles are empty

- Players
  Place a match into a board's tile

- Judge
  Checks if the game has ended
  Check if any player won

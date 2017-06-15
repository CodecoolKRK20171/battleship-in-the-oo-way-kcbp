Contains all ships and game board and handles output.

### Class Ocean


__Instance attributes__

- `ships`
    - data: list of *Ship* objects
    - description: holds all ships to append them to the board
- `board`
    - data: list of lists
    - description: current board state

__Instance methods__

- `__init__(self)`
    Creates object with empty lists as the attributes.
- `__str__(self)`
    Used for printing current board.
- `check_if_position_is_valid(self, new_ship_data)`
    Checks if given by user position of new ship is correct. If it's correct, creates new *Ship* object and adds it to the attribute *ships* list. Returns bool.
- `insert_shot(self, cords)`
    Inserts shot mark ('X' or 'O') on given coordinates into current board.
- `insert_ship(self, ship)`
    Inserts *Ship* object on the board.
- `check_if_sunk(self, cords)`
    Checks if all parts of the *Ship* have been hit. Returns bool.

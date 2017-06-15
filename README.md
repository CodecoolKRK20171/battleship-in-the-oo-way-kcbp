# Battleship in the OOP way

## The story
  *Battleship (also Battleships or Sea Battle) is a guessing game
for two players. It is played on ruled grids (paper or board) on
which the players' fleets of ships (including battleships) are marked.
The locations of the fleet are concealed from the other player.
Players alternate turns calling "shots" at the other player's ships,
and the objective of the game is to destroy the opposing player's fleet.*

# Specification


### `main.py`

This is the file which initializes program execution and contains all game logic.

__Functions__

- `set_player(nr)`
    Creates and returns *Player* object with player name given from user. Calls other function to insert player's *Ship* objects into his attribute *player_ocean*.

- `add_ships_by(player)`
    Handles getting from user correct positions for *Ship* objects.

- `shot_handle(player)`
    Handles single user guess. Returns *True* if user hit the *Ship* object, *False* otherwise.

- `is_win(current_player)`
    Returns True if the winning condition is fulfilled. It means if there is no more *Ship* objects in attribute *ships* of attribute *enemy_ocean* of *Player* object.

- `main()`
    Initialize game execution, starts the main loop of the program.


### `square.py`

Holds data for each square.

### Class Square

__Instance attributes__

- `row`
    - data: int
    - description: indicates on which row square lies
- `columnn`
    - data: int
    - description: indicates on which column square lies
- `is_marked`
    - data: bool
    - description: indicates if square is marked or not

__Instance methods__
- `__init__(self, row, column)`
    Creates unmarked Square object with given position.


### `ship.py`

Holds data needed for proper ship description and methods for management.

### Class Ship

__Class atrributes__

- `ships_types`
    - data: dict
    - description: keys with ships names and values with corresponding lengths

__Instance attributes__

- `name`
    - data: str
    - description: one of 5 possible ship names
- `positions`
    - data: list of tuples of ints
    - description: carries all positions of ship squares
- `squares`
    - data: list of *Square* objects
    - description: carries all ship's parts
- `is_vertical`
    - data: bool
    - description: indicates ship direction. True if vertical, False if horizontal

__Instance methods__

- `__init__(self, name, positions, is_vertical=False)`
    Creates Ship object with name, list of *Square* objects and list of all squares positions.
- `is_sunk(self)`
    Checks if ship is sunk or not. Returns bool.


### `ocean.py`

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
    Inserts shot mark ('X' or 'O') on given coordinates into.
- `insert_ship(self, ship)`
    Inserts Ship object on the board.
- `check_if_sunk(self, cords)`
    Checks if all parts of the *Ship* have been hit. Returns bool.



### `player.py`

Holds player's attributes and takes all the inputs from user.

### Class Player

__Instance attributes__

- `name`
    - data: str
    - description: players name
- `player_ocean`
    - data: *Ocean* class object
    - description: board with players ships
- `enemy_ocean`
    - data: *Ocean* class object
    - description: enemy board with hits and misses

__Instance methods__

- `__init__(self, name)`
    Creates *Player* object with given name and two *Ocean* objects.
- `choose_initial_ship_position(self, ship_name)`
    Takes ship position from the user. Returns: list with ship name, tuple of given_positions and vertical/horizontal orientation as bool.
- `is_vertical(self, ship_name, new_ship_data)`
    Indicates ship direction and add it to the list. True if vertical, False if horizontal. Returns list with ship name, tuple of given positions and bool.
- `choose_shot_cords(self)`
    Takes coordinates for attack from user and returns them in a tuple.

__Static methods__

- `take_coordinates(input_message, ship_name="")`
    Get coordinates from the user and converts letters to numbers(0,10).
    Returns tuple with two integers as cords.

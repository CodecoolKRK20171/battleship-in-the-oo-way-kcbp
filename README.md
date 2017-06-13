# Battleship in the OOP way

## The story
  *Battleship (also Battleships or Sea Battle) is a guessing game
for two players. It is played on ruled grids (paper or board) on
which the players' fleets of ships (including battleships) are marked.
The locations of the fleet are concealed from the other player.
Players alternate turns calling "shots" at the other player's ships,
and the objective of the game is to destroy the opposing player's fleet.*

# Specification


## __main.py__


## __square.py__
#### class description
    Holds data for each square.

#### instance attributes
- `is_marked`
    - data: bool
    - description: indicates if square is marked or not
- `row`
    - data: int
    - description: indicates on which row square lies
- `columnn`
    - data: int
    - description: indicates on which column square lies


## __ship.py__
#### class description
    Holds data needed for proper ship description and methods for management.

#### class atrributes
- `ships_types`
    - data: dict
    - description: keys with ships names and values with corresponding lenghts.
    Used for length instance attribute creation.

#### instance attributes
- `name`
    - data: str
    - description: one of 5 possible ship names.
- `positions`
    - data: tuple of Square objects
    - description: carries all squares occupied by ship.
- `is_vertical`
    - data: bool
    - description: indicates ship direction. True if vertical, False if horizontal.

#### instance methods
- `__init__(self, name, positions)`
    - Creates Ship object with name and position.
- `is_sunk(self)`
    - Checks if ship is sunk or not.
    - returns: bool


## __ocean.py__
#### class description
    contains all ships and game board and handles output

#### attributes
- `ships`
    - data: list of Ship objects
    - description: holds all ships to append them to the board.
- `board`
    - data: list of lists
    - description: current board state.

#### instance methods
- `__init__(self)`
    - Creates object with empty list as an atrribute.
- `__str__(self)`
    - Used for printing current board.
- `add_ship(self, ship)`
    - Inserts Ship object on the board.
- `insert_shoot(self, cords)`
    - Interts shoot mark ('X', 'O') on given coordinates.


## __player.md__
#### class description
    Holds players attributes

#### instance attributes
- `name`
    - data: str
    - description: players name.
- `player_ocean`
    - data: Ocean class object
    - description: board with players ships.
- `enemy_ocean`
    - data: Ocean class object
    - description: enemy board with hits and misses.

#### instance methods
- `choose_initial_ships_position(self)`
    - Takes ships positions from user.
    - returns: dictionary with ships names as keys and tupples of given_positions as values
- `is_vertical`
    - data: bool
    - description: indicates ship direction. True if vertical, False if horizontal.
- `check_if_position_are_valid(self, given_position)`
    - Checks if ships don't overlay each other and don't hang off the edge.
    - returns: bool
- `choose_shoot_cords(self)`
    - Takes coordinates for atack from user.
    - returns: tuple with two integers
- `is_win(self)`
    - Checks if there is any part of ship left
    - returns: bool

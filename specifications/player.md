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

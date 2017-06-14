# class description
    Holds players attributes


# instance attributes
- `name`
    - data: str
    - description: players name.
- `player_ocean`
    - data: Ocean class object
    - description: board with players ships.
- `enemy_ocean`
    - data: Ocean class object
    - description: enemy board with hits and misses.


# instance methods
- `__init__(self, name)`
    - description: Creates Player object with given name and two Ocean objects.
    - returns: None
- `choose_initial_ships_position(self)`
    - parameters: ship names
    - description: Takes ships positions from user.
    - returns: list with ships names as keys and tupples of given_positions as values and situation as bool
- `is_vertical`
    - data: bool
    - description: indicates ship direction. True if vertical, False if horizontal.
    - returns: list with ships names as keys and tupple of given positions as values and bool
- `choose_shoot_cords(self)`
    - description: Takes coordinates for atack from user.
    - returns: tuple with two integers
- `win_or_lose(self)`
    - description: Checks if there is any part of ship left
    - returns: bool
- `take_coordinates(input_message, ship_name="")`
    - parameters: takes input message, and ship name if exist.
    - description: method converts letters to numbers(0,10)
    - returns: tuple with two integers as cords

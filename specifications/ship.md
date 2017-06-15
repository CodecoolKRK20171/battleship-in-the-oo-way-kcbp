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
    Creates Ship object with name, list of *Square* objects and list of all squares' positions.
- `is_sunk(self)`
    Checks if ship is sunk or not. Returns bool.

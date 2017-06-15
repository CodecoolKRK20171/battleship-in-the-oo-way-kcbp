from square import Square


class Ship:
    """Class has methods to create and manage single Ship object.

    Attributes:
        ships_types : dict
            Keys with ships names and values with corresponding lengths.
        name : str
            One of 5 possible ship names.
        positions : list of tuples of ints
            Carries all positions of ship squares.
        squares : list of Square objects
            Carries all ship's parts.
        is_vertical : bool
            Indicates ship direction. True if vertical, False if horizontal.
    """
    ship_types = {'Carrier': 5,
                  'Battleship': 4,
                  'Cruiser': 3,
                  'Submarine': 3,
                  'Destroyer': 2}

    def __init__(self, name, position, is_vertical=False):
        """Creates Ship object with name, list of Square objects and list of all squares' positions."""
        self.name = name
        self.positions = []
        self.squares = []
        self.positions.append(position)
        column = position[0]
        row = position[1]
        self.squares.append(Square(column, row))
        for i in range(Ship.ship_types[name] - 1):

            if is_vertical:
                row += 1
            else:
                column += 1
            self.squares.append(Square(column, row))
            self.positions.append((column, row))

    def is_sunk(self):
        """Checks if ship is sunk or not. Returns bool.

        Returns:
        ---------
            sunk : bool
                True if ship is sunk, False otherwise.
        """
        sunk = True
        for square in self.squares:
            if not square.is_marked:
                sunk = False
        return sunk

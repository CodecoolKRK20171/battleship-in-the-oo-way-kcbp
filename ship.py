class Ship:
    ship_types = {'Carrier': 5,
                  'Battleship': 4,
                  'Cruiser': 3,
                  'Submarine': 3,
                  'Destroyer': 2}

    def __init__(self, name, position, is_vertical=False):
        self.name = name
        self.positions = []
        # self.squares = []
        self.positions.append(position)
        column = position[0]
        row = position[1]
        for i in range(Ship.ship_types[name] - 1):
            # self.squares.append(Square(column, row))
            if is_vertical:
                row += 1
            else:
                column += 1
            self.positions.append((column, row))
        # print(self.positions)

    def is_sunk(self):
        sunk = True
        for square in self.squares:
            if not square.is_marked():
                sunk = False
        return sunk

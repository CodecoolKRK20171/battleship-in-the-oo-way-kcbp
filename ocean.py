from ship import Ship
from square import Square


class Ocean:
    """Class has methods to create and manage single Ocean object.

    Attributes:
        ships : list of Ship obj
            Holds all ships to append them to the board.
        board : list of lists
            Current board state.
    """
    def __init__(self):
        """Creates object with empty lists as the attributes."""
        size_of_board = 10
        self.ships = []
        self.board = []
        for i in range(size_of_board):
            self.board.append(['~'] * size_of_board)

    def __str__(self):
        """Prints current board state."""
        output = ''
        for row in self.board:
            output += ''.join(row) + '\n'
        return output

    def check_if_position_is_valid(self, new_ship_data):
        """Checks if given by user position of new ship is correct.
        If it's correct, creates new Ship object and adds it to the ships list.

        Parameters:
        -----------
            new_ship_data : list
                List with ships name, tuples of given positions and orientation as bool.

        Returns:
        ---------
            bool
        """
        ship_name = new_ship_data[0]
        ship_length = Ship.ship_types[new_ship_data[0]]
        col = new_ship_data[1][0] - 1
        row = new_ship_data[1][1] - 1
        is_vertical = new_ship_data[2]

        if is_vertical:
            if row not in range(0, 11 - ship_length):
                print('Ship out of the ocean')
                return False
        else:
            if col not in range(0, 11 - ship_length):
                print('Ship out of the ocean')
                return False

        for ship_part in range(ship_length):
            last_index = 9
            try:
                if row != last_index and col != last_index:
                    if(self.board[row][col] != '~' or
                            self.board[row + 1][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col + 1] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
                elif row == last_index and col == last_index:
                    if(self.board[row][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
                elif row == last_index:
                    if(self.board[row][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col + 1] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
                elif col == last_index:
                    if(self.board[row][col] != '~' or
                            self.board[row + 1][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
            except IndexError:
                print('Coordinates out of the ocean.')
                return False
            if is_vertical:
                row += 1
            else:
                col += 1
        ship = Ship(*new_ship_data)
        self.ships.append(ship)
        self.insert_ship(ship)
        return True

    def insert_shot(self, cords):
        """Inserts shot mark ('X' or 'O') on given coordinates into current board.

        Parameters:
        -----------
            cords : tuple of ints
                User shot.

        Returns:
        ---------
            bool
        """
        x = 0
        y = 1
        column = cords[x]
        row = cords[y]

        for ship in self.ships:

            for position in ship.positions:

                if (column, row) == position:
                    self.board[row - 1][column - 1] = 'X'
                    return True
        if self.board[row - 1][column - 1] == '~':
            self.board[row - 1][column - 1] = 'O'

        return False

    def insert_ship(self, ship):
        """Inserts Ship object on the board.

        Parameters:
        -----------
            ship : Ship obj
        """
        for position in ship.positions:
            column, row = position
            self.board[row-1][column-1] = 'X'

    def check_if_sunk(self, cords):
        """Checks if all parts of the *Ship* have been hit.

        Parameters:
        -----------
            cords : tuple of ints
                User shot.

        Returns:
        ---------
            bool
        """
        x = 0
        y = 1
        column = cords[x]
        row = cords[y]
        for ship in self.ships:
            for square in ship.squares:
                if square.column == column and square.row == row:
                    square.is_marked = True
            if ship.is_sunk():
                self.ships.remove(ship)
                return True
            else:
                return False

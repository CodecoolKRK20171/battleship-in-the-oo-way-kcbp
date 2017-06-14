from ship import Ship


class Ocean:

    def __init__(self):
        size_of_board = 10
        self.ships = []
        self.board = []
        for i in range(size_of_board):
            self.board.append(['~'] * size_of_board)

    def __str__(self):
        output = ''
        for row in self.board:
            output += ''.join(row) + '\n'
        return output

    def check_if_position_is_valid(self, new_ship_data):

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
            try:
                if row != 9 and col != 9:
                    if(self.board[row][col] != '~' or
                            self.board[row + 1][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col + 1] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
                elif row == 9:
                    if(self.board[row][col] != '~' or
                            self.board[row - 1][col] != '~' or
                            self.board[row][col + 1] != '~' or
                            self.board[row][col - 1] != '~'):
                        print('Ship is overlap another ship')
                        return False
                elif col == 9:
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
        x = 0
        y = 1
        column = cords[x]
        row = cords[y]
        for ship in self.ships:
            for position in ship.positions:
                if (column, row) == position:
                    self.board[row - 1][column - 1] = 'X'
                    return True
        self.board[row - 1][column - 1] = 'O'
        return False

    def insert_ship(self, ship):
        for position in ship.positions:
            column, row = position
            self.board[row-1][column-1] = 'X'

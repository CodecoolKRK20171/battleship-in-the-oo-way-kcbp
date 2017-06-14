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
        col = new_ship_data[1][0]
        row = new_ship_data[1][1]
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
                if(self.board[row][col] != '~' and
                        self.board[row + 1][col] != '~' and
                        self.board[row - 1][col] != '~' and
                        self.board[row][col + 1] != '~' and
                        self.board[row][col - 1] != '~'):
                    print('Ship overlay another ship.')
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

    def insert_shoot(self, cords):
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

def main():
    # ship1 = Ship('Cruiser', (1,2), True)
    # ship2 = Ship('Battleship', (5,5))
    ocean = Ocean()
    new_ship_data = ['Cruiser', (1, 1), True]
    new_ship_data1 = ['Battleship', (4, 4), False]
    new_ship_data2 = ['Battleship', (4, 4), True]
    ocean.check_if_position_is_valid(new_ship_data)
    ocean.check_if_position_is_valid(new_ship_data1)
    ocean.check_if_position_is_valid(new_ship_data2)
    # ocean.insert_ship()

    # player_ocean = Ocean()
    # enemy_ocean = Ocean()
    # player_ocean.ships.append(ship1)
    # player_ocean.ships.append(ship2)
    # enemy_ocean.ships.append(ship1)
    # enemy_ocean.ships.append(ship2)
    # enemy_ocean.insert_shoot((2,2))
    # enemy_ocean.insert_shoot((1,2))
    # enemy_ocean.insert_shoot((1,3))
    # # enemy_ocean = player_ocean.copy.deepcopy()
    # player_ocean.insert_ships()
    print(ocean)
    # print()
    # print(enemy_ocean)


if __name__ == '__main__':
    main()

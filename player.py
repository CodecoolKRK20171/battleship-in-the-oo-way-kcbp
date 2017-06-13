import re


class Player:
    pass

    def __init__(self, name, player_ocean, enemy_ocean):
        self.name = name
        self.player_ocean = player_ocean
        self.enemy_ocean = enemy_ocean

    def choose_initial_ships_position(self):
        """
        Takes ships positions from user.
        returns
        ---------
        dictionary with ships names as keys and tupples of given_position
        as values
        """

        given_position = {}
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # numbers = list(range(1,11))
        numbers_str = [str(i) for i in list(range(1,11))]
        ships_names = ['Carrier (occupies 5 spaces)', 'Battleship (4)', 'Cruiser (3)', 'Submarine (3)', 'Destroyer (2)']

        for element in ships_names:
            ship_cords = input('Enter ship starting coordinates for ' + element + ': (f.e. a6/A6)').upper()
            if not re.match("^[a-jA-J][1-9]$|^[a-jA-J][1][0]$", ship_cords):
              raise ValueError('Wrong Input!')

            else:
              ship_cords_list = [ship_cords[0], ship_cords[1]]
              for i in range(len(letters)):
                if ship_cords_list[0] == letters[i]:
                  ship_cords_list[0] = numbers_str[i]
              given_position[element] = (int(ship_cords_list[0]), int(ship_cords[1]))

        return given_position

    # def is_vertical(self):

    def check_if_position_are_valid(self, given_position):
        pass

    def choose_shoot_cords(self):
        pass

    def is_win(self):
        pass

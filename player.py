from ocean import Ocean
import re


class Player:
    pass

    def __init__(self, name):
        self.name = name
        self.player_ocean = Ocean()
        self.enemy_ocean = Ocean()

    def choose_initial_ships_position(self, ship_name):
        """
        Takes ships positions from user.
        returns
        ---------
        dictionary with ships names as keys and tupples of given_position
        as values
        """
        new_ship_data = []
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        numbers_str = [str(i) for i in list(range(1, 11))]

        ship_cords = input('Enter ship starting coordinates for ' + ship_name + ': (f.e. a6/A6)').upper()
        if not re.match("^[a-jA-J][1-9]$|^[a-jA-J][1][0]$", ship_cords):
            raise ValueError('Wrong Input!')

        else:
            ship_cords_list = [ship_cords[0], ship_cords[1]]
            for i in range(len(letters)):
                if ship_cords_list[0] == letters[i]:
                    ship_cords_list[0] = numbers_str[i]
            new_ship_data = [ship_name, (int(ship_cords_list[0]), int(ship_cords[1]))]

        self.is_vertical(ship_name)

        return new_ship_data

    def is_vertical(self, ship_name, new_ship_data):
        """indicates ship direction. True if vertical, False if horizontal"""

        is_vertical = input('If situation of ' + ship_name + 'suppouse to be vertical, input 1, otherwise 0: ')
        if is_vertical == "1":
            new_ship_data.append(True)
        elif is_vertical == "0":
            new_ship_data.append(False)

        return new_ship_data

    def choose_shot_cords(self):
        """
        Takes coordinates for atack from user.

        returns
        -------
        tuple with two integers
        """

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        numbers_str = [str(i) for i in list(range(1, 11))]

        shot_cords = input('Enter shoot coordinates: (f.e. a6/A6)').upper()

        if not re.match("^[a-jA-J][1-9]$|^[a-jA-J][1][0]$", shot_cords):
            raise ValueError('Wrong Input!')

        else:
            shot_cords_list = [shot_cords[0], shot_cords[1]]
            for i in range(len(letters)):
                if shot_cords_list[0] == letters[i]:
                    shot_cords_list[0] = numbers_str[i]
            shot_cords_tuple = (int(shot_cords_list[0]), int(shot_cords[1]))

        return shot_cords_tuple

    def is_win(self):
        pass

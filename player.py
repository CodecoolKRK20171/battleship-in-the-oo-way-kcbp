from ocean import Ocean
import re


class Player:

    def __init__(self, name):
        self.name = name
        self.player_ocean = Ocean()
        self.enemy_ocean = Ocean()

    def choose_initial_ship_position(self, ship_name):
        """
        parameters:
        -----------
        ship names

        Takes ships positions from user.

        returns:
        ---------
        list with ships names as keys and tupples of given_positions as values and situation as bool
        """
        ship_position_cords = Player.take_coordinates('Enter ship starting coordinates for', ship_name)
        new_ship_data = [ship_name, ship_position_cords]

        self.is_vertical(ship_name, new_ship_data)

        return new_ship_data

    def is_vertical(self, ship_name, new_ship_data):
        """indicates ship direction. True if vertical, False if horizontal"""

        is_vertical = input('If situation of ' + ship_name + ' suppouse to be vertical, input 1, otherwise 0: ')
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
        shot_cords = Player.take_coordinates('Enter shot coordinates')

        return shot_cords

    def is_win(self):
        pass
        # for ship in self.enemy_ocean.ships:
        #     for square in ship.squares:
        #         if not square.is_marked():
        #             return False
        # return True

    @staticmethod
    def take_coordinates(input_message, ship_name=""):
        """
        parameters:
        -----------
        takes input message, and ship name if exist

        method converts letters to numbers(0,10)

        returns:
        --------
        tuple with two integers as cords
        """
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        numbers = [str(i) for i in list(range(1, 11))]

        ship_or_shot_cords = input('{} {} (f.e. a6/A6):'.format(input_message, ship_name)).upper()

        if re.match("^[a-jA-J][1-9]$|^[a-jA-J][1][0]$", ship_or_shot_cords):
            coordinates = [ship_or_shot_cords[0], ship_or_shot_cords[1:]]
            for i in range(len(letters)):
                if coordinates[0] == letters[i]:
                    coordinates[0] = numbers[i]
            cords_xy = (int(coordinates[0]), int(ship_or_shot_cords[1:]))
        else:
            raise ValueError('Wrong Input!')

        return cords_xy

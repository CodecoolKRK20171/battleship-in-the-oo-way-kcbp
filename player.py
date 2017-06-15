from ocean import Ocean
import re


class Player:
    """Class has methods to create and manage Player object.

    Attributes:
        name : str
        player_ocean :  Ocean obj
        enemy_ocean : Ocean obj
    """
    def __init__(self, name):
        """Creates Player object."""
        self.name = name
        self.player_ocean = Ocean()
        self.enemy_ocean = Ocean()

    def choose_initial_ship_position(self, ship_name):
        """Takes ships positions from the user.

        Parameters:
        -----------
            ship_name : str

        Returns:
        ---------
            new_ship_data : list
                List with ships name, tuples of given positions and orientation as bool.
        """
        ship_position_cords = Player.take_coordinates('Enter ship starting coordinates for', ship_name)
        new_ship_data = [ship_name, ship_position_cords]

        self.is_vertical(ship_name, new_ship_data)

        return new_ship_data

    def is_vertical(self, ship_name, new_ship_data):
        """Indicates ship direction (True if vertical, False if horizontal) and add it to the list.

        Parameters:
        -----------
            ship_name : str
            new_ship_data : list
                List with ships name, tuples of given positions and orientation as bool.

        Returns:
        ---------
            new_ship_data : list
                List with ships name, tuples of given positions and orientation as bool.
         """

        is_vertical = input('If situation of ' + ship_name + ' suppouse to be vertical, input 1, otherwise 0: ')
        if is_vertical == "1":
            new_ship_data.append(True)
        elif is_vertical == "0":
            new_ship_data.append(False)
        else:
            raise ValueError('Wrong Input!')

        return new_ship_data

    def choose_shot_cords(self):
        """Takes coordinates for attack from user.

        Returns
        -------
            shot_cords : tuple of ints
                Shot coordinates.
        """
        shot_cords = Player.take_coordinates('Enter shot coordinates')

        return shot_cords

    @staticmethod
    def take_coordinates(input_message, ship_name=""):
        """Converts letters to numbers(0,10) in shot coordinates.

        Parameters:
        -----------
            input_message : str
            ship_name : str

        Returns:
        --------
            cords_xy : tuple of ints
                Coordinates.
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

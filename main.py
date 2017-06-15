import os
from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def set_player(nr):
    """Creates Player object with name given from user.
    Calls other function to insert player's Ship objects into his board.

    Parameters:
    -----------
        nr : str
            String with player's number.

    Returns:
    ---------
        player : Player obj
    """
    name = input('{} player please give your name: '.format(nr))
    player = Player(name)
    add_ships_by(player)
    return player


def add_ships_by(player):
    """Handles getting correct positions for Ship objects from user.

    Parameters:
    -----------
        player: Player obj
    """
    for ship_name in Ship.ship_types:
        is_valid = False
        while not is_valid:
            try:
                ship_data = player.choose_initial_ship_position(ship_name)
            except ValueError as err:
                print(err)
            else:
                is_valid = player.player_ocean.check_if_position_is_valid(ship_data)
                if not is_valid:
                    print('Wrong coordinates. Try again.')

        print(player.player_ocean)


def shot_handle(player):
    """Handles single user guess.

    Parameters:
    -----------
        player: Player obj

    Returns:
    ---------
        is_hit : bool
            Indicates if user hit the ship.
    """
    print('Turn: {}'.format(player.name))
    print(player.enemy_ocean, '\n')

    correct_cords = False
    while not correct_cords:
        try:
            cords = player.choose_shot_cords()
        except ValueError as err:
            print(err)
        else:
            correct_cords = True
            is_hit = player.enemy_ocean.insert_shot(cords)
            if is_hit:
                os.system('clear')
                if player.enemy_ocean.check_if_sunk(cords):
                    print('You hit and sunk!')
                else:
                    print('You hit!')
            else:
                os.system('clear')
                input('You miss!')

    return is_hit


def is_win(current_player):
    """Checks if the winning condition is fulfilled.

    Parameters:
    -----------
        current_player: Player obj

    Returns:
    ---------
        bool
            Indicates if user won or not.
    """
    os.system('clear')

    while shot_handle(current_player):

        if not current_player.enemy_ocean.ships:
            print('{} win!'.format(current_player.name))
            return True


def main():

    player_one = set_player('First')
    os.system('clear')
    player_two = set_player('Second')
    os.system('clear')
    input('Press return to start the battle.')

    player_one.enemy_ocean.ships = player_two.player_ocean.ships
    player_two.enemy_ocean.ships = player_one.player_ocean.ships

    is_win = False
    current_player = player_one

    while not is_win(current_player):

        if current_player == player_one:
            current_player = player_two
        else:
            current_player = player_one


if __name__ == '__main__':
    main()

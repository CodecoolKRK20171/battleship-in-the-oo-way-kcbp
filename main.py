from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def set_player(nr):
    name = input('{} player please give your name: '.format(nr))
    player = Player(name)
    add_ships_by(player)
    return player


def add_ships_by(player):
    for ship_name in Ship.ship_types:
        is_valid = False
        while not is_valid:
            try:
                ship_data = player.choose_initial_ship_position(ship_name)
            except ValueError as err:
                print(err)
            else:
                print(ship_data)
                is_valid = player.player_ocean.check_if_position_is_valid(ship_data)
                if not is_valid:
                    print('Wrong coordinates. Try again.')

        print(player.player_ocean)


def main():

    player_one = set_player('First')
    player_two = set_player('Second')

    print(player_one.player_ocean)



if __name__ == '__main__':
    main()

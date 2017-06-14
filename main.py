import os
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


def turn_handle(player):


    print(player.player_ocean)
    print()
    print(player.enemy_ocean)
    print()

    cords = player.choose_shot_cords()
    is_hit = player.enemy_ocean.insert_shot(cords)

    print(player.enemy_ocean)

    return is_hit



def main():

    player_one = set_player('First')
    player_two = set_player('Second')

    player_one.enemy_ocean.ships = player_two.player_ocean.ships
    player_two.enemy_ocean.ships = player_one.player_ocean.ships

    counter_player_one = 0
    counter_player_two = 0
    total_ships_squares = 17

    while counter_player_one != total_ships_squares and counter_player_two != total_ships_squares:

        os.system('clear')
        input()

        while turn_handle(player_one):
            counter_player_one += 1

        os.system('clear')
        input()

        while turn_handle(player_two):
            counter_player_two += 1


if __name__ == '__main__':
    main()

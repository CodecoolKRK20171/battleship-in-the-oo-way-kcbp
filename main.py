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
                is_valid = player.player_ocean.check_if_position_is_valid(ship_data)
                if not is_valid:
                    print('Wrong coordinates. Try again.')

        print(player.player_ocean)



def turn_handle(player):


    print(player.player_ocean)
    print()
    print(player.enemy_ocean)
    print()

    correct_cords = False
    while not correct_cords:
        try:
            cords = player.choose_shot_cords()
        except ValueError as err:
            print(err)
        else:
            is_hit = player.enemy_ocean.insert_shot(cords)
            correct_cords = True

    print(player.enemy_ocean)

    return is_hit



def main():

    player_one = set_player('First')
    os.system('clear')
    player_two = set_player('Second')
    os.system('clear')
    input('Press return to start the battle.')

    player_one.enemy_ocean.ships = player_two.player_ocean.ships
    player_two.enemy_ocean.ships = player_one.player_ocean.ships

    counter_player_one = 0
    counter_player_two = 0
    total_ships_squares = 17


    while True:
        
        os.system('clear')

        while turn_handle(player_one):
            os.system('clear')
            input('You hit!')
            counter_player_one += 1

        if counter_player_one == total_ships_squares:
            print('{} win!'.format(player_one.name))
            break
        
        os.system('clear')
        input('You miss!')

        while turn_handle(player_two):
            os.system('clear')
            input('You hit!')
            counter_player_two += 1


        if counter_player_two == total_ships_squares:
            print('{} win!'.format(player_two.name))
            break

        os.system('clear')
        input('You miss!')       


if __name__ == '__main__':
    main()

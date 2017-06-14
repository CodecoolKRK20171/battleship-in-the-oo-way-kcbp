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

    player_one.enemy_ocean.ships = player_two.player_ocean.ships
    player_two.enemy_ocean.ships = player_one.player_ocean.ships

    # current_player = player_one
    print(player_one.player_ocean + '\n')
    print(player_one.enemy_ocean)
    cords = player_one.choose_shot_cords()
    player_two.enemy_ocean.insert_shoot(cords)

    print(player_one.player_ocean + '\n')
    print(player_one.enemy_ocean)
    # counter_player_one = 0
    # counter_player_two = 0
    # total_ships_squares = 17
# 
    # while counter_player_one != total_ships_squares and 
        #   counter_player_two != total_ships_squares:
# 
        # print(current_player.player_ocean + '\n')
        # print(current_player.enemy_ocean)
        # cords = current_player.choose_shot_cords()
        # player_two.enemy_ocean.insert_shoot(cords)   

if __name__ == '__main__':
    main()
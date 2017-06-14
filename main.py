from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def main():
    print('First player')
    name_1 = input('Give your name: ')
    player_one = Player(name_1)
    for ship_name in Ship.ship_types:
        is_valid = False
        while not is_valid:
            try:
                ship_data = player_one.choose_initial_ship_position(ship_name)
            except ValueError as err:
                print(err)
            else:
                print(ship_data)
                is_valid = player_one.player_ocean.check_if_position_is_valid(ship_data)
                if not is_valid:
                    print('Wrong coordinates. Try again.')
                    
        print(player_one.player_ocean)
    # name_2 = input()
    # player_two =


if __name__ == '__main__':
    main()
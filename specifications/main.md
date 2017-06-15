This is the file which initializes program execution and contains all game logic.

__Functions__

- `set_player(nr)`
    Creates and returns *Player* object with player name given from user. Calls other function to insert player's *Ship* objects into his attribute *player_ocean*.

- `add_ships_by(player)`
    Handles getting from user correct positions for *Ship* objects.

- `shot_handle(player)`
    Handles single user guess. Returns *True* if user hit the *Ship* object, *False* otherwise.

- `is_win(current_player)`
    Returns True if the winning condition is fulfilled. It means if there is no more *Ship* objects in attribute *ships* of attribute *enemy_ocean* of *Player* object.

- `main()`
    Initialize game execution, starts the main loop of the program.

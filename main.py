"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game
import data


if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    player = data.create_player()
    mud.add_player(player)
    while not mud.is_gameover():
        choices = mud.get_options()
        choice = data.prompt_player_choice(choices)
        actions = mud.get_actions(choice)
        mud.execute(actions)
        data.display(mud.status())
    game.epilogue()
    

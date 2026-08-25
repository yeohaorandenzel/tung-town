"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game
import data


if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    name = input("Player what is your name: ")
    player = data.Player(name, data.tung_town_case)
    mud.add_player(player)
    while not mud.is_gameover():
        choices_dict = mud.get_options()
        choice_name = data.prompt_player_choice(choices_dict)
        actions = mud.get_actions(choice_name)
        mud.execute(actions)
    game.epilogue()
    

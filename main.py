"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game
import data
player_moveset = {
    "push":data.Action(data.ActionType.ATTACK, 3),
    "jab":data.Action(data.ActionType.ATTACK, 6)
}
if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    player = data.Player("You", data.tung_town_case, 100, 100, player_moveset)
    mud.add_player(player)
    while not mud.is_gameover():
        choices_dict = mud.get_options()
        choice_name = data.prompt_player_choice(choices_dict)
        actions = mud.get_actions(choice_name)
        mud.execute(actions)
    mud.epilogue()
    

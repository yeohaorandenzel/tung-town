import data
import random
def start_battle(player,enemy):
    data.display("You engage " + enemy.name)
    while player.is_alive() and enemy.is_alive():
        data.display(f"""
        {enemy.name} glares you down

        your HP: {player.health}/{player.max_health}
        {enemy.name}'s HP: {enemy.health}/{enemy.max_health}
        """)
        options_table = {
            "description": f"Moves:",
            "choices": data.move_set_to_choices_table(player.move_set)
        }  
        player_move = data.prompt_player_choice(options_table)
        enemy_move = random.choice(list(enemy.move_set.keys()))
        player.use_move(player_move, enemy)
        enemy.use_move(enemy_move, player)
    if player.is_alive():
        data.display("You come out of the battle victorious")
    else:
        data.display("Oh god it hurts it really doe-")
    
class Game:
    def __init__(self):
        self.player = None
        self.battle = None
        self.last_options = None
    def is_gameover(self):
        return not self.player.is_alive()
    def welcome(self):
        print("Hallo lets play da tung town press any key to start")
        input()
    
    def add_player(self, player):
        self.player = player
        initial_room = player.current_room
        data.display(initial_room.name,"=")
    
    def get_actions(self, choice_name):
        return self.last_options["choices"][choice_name].actions
    
    def get_options(self):
        if self.battle:
            options = self.battle.get_options()
        else:
            current_room = self.player.current_room
            options = {
                "description": current_room.description,
                "choices": current_room.exits
            }
        self.last_options = options
        return options

    def execute(self,actions: list[data.Action]):
        for action in actions:
            if action.type == data.ActionType.MOVE:
                room_to_move_to = data.room_dict[action.val]
                data.display(room_to_move_to.name,"=")
                self.player.current_room = data.room_dict[action.val]
            elif action.type == data.ActionType.DISPLAY_DIA:
                data.display(action.val)
            elif action.type == data.ActionType.START_BATTLE:
                start_battle(self.player, action.val)
            action.act_done()
    def epilogue(self):
        if self.player.is_alive():
            print("You wake up in your bed. Well it must've been a dream, you think.")
        else:
            print("...")
        

if __name__ == "__main__":
    pass
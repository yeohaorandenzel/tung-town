import data
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        print("You engage "+ self.enemy.name)

    def get_options(self):
        
        options = {
            "choices": None
        }
class Game:
    def __init__(self):
        self.player = None
        self.battle = None
        self.last_options = None
    def is_gameover(self):
        return False
    def welcome(self):
        print("Hallo lets play da tung town press any key to start")
        input()
    
    def add_player(self, player):
        self.player = player
    
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
                self.player.current_room = data.room_dict[action.val]
            elif action.type == data.ActionType.DISPLAY_DIA:
                data.display(action.action_val)
            elif action.type == data.ActionType.START_BATTLE:
                self.battle = Battle(self, self.player, action.action_val)
    
    def status(self):
        pass

if __name__ == "__main__":
    pass
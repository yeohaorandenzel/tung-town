import data
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        print("You engage "+ self.enemy.name)
class Game:
    def __init__(self, maze):
        self.player = None
        self.maze = maze
        self.battle = None
    def welcome():
        print("Hallo lets play da tung town press any key to start")
        input()
    
    def add_player(self, player):
        self.player = player

    def get_options(self):
        return self.player.current_room.get_options()

    def execute(self,actions: list[(str,str)]):
        for action in actions:
            type,val = action
            if type == "move_room":
                self.player.current_room = self.player.current_room.exits[val]
            elif type == "display_dialogue":
                data.display(val)
            elif type == "start_battle":
                self.battle = Battle(self, self.player, val)

            
    def status(self):
        pass

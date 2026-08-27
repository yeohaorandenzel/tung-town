class ActionType:
    MOVE = 1
    START_BATTLE = 2
    DISPLAY_DIA = 3
    ATTACK = 4
    HEAL = 5
    SKIP = 6

class Action:
    def __init__(self,type:ActionType,val,one_time = False):
        self.type = type
        self.val = val
        self.one_time = one_time
    def act_done(self):
        if self.one_time:
            self.type = ActionType.SKIP

class Choice:
    def __init__(self,desc,actions):
        self.desc = desc
        self.actions = actions
class Creature:
    def __init__(self,health,name,move_set:dict[str:int],max_health = 100):
        self.health = health
        self.name = name
        self.move_set = move_set
        self.max_health = max_health
    def is_alive(self):
        return self.health > 0
    def take_damage(self,damage):
        if damage >= 0:
            self.health -= damage
        else:
            raise ValueError("Damage must be >= 0")
    def heal(self, heal_amt):
        if heal_amt >= 0:
            self.health += heal_amt
            if self.health > self.max_health:
                self.health = self.max_health
        else:
            raise ValueError("Heal amount must be >= 0")
    def act(self, action:Action,acted_on = None):
        if action.type == ActionType.ATTACK:
            acted_on.take_damage(action.val)
        elif action.type == ActionType.HEAL:
            self.heal(action.val)
    def use_move(self, move_chosen, acted_on):
        action = self.move_set[move_chosen]
        self.act(action, acted_on)
        if action.type == ActionType.ATTACK:
            print(f'{self.name} attacks with {move_chosen} to deal {action.val} damage')
        elif action.type == ActionType.HEAL:
            print(f'{self.name} heals with {move_chosen} to gain {action.val} hp')

class Room:
    def __init__(self, name: str, description: str, max_health: int,exits: dict[str, "Room"]):
        self.name = name
        self.description = description
        self.exits: dict[str, str] = exits
        self.creatures: list[Creature] = []
        self.__max_health = max_health

class Player(Creature):
    def __init__(self, name: str,current_room,max_health,health,move_set):
        super().__init__(health,name,move_set, max_health)
        self.current_room = current_room
    

def prompt_player_choice(choices_dict):
    choice_disp_str = choices_dict["description"] + "\n"
    for choice_name,choice in choices_dict["choices"].items():
        choice_disp_str += choice_name + '->' + choice.desc + '\n'
    display(choice_disp_str)
    valid = False
    while not valid:
        choice_made = input(">").lower()
        if choice_made in choices_dict["choices"].keys():
            valid = True
        else:
            print("Sorry?")
    return choice_made
def display(string,border = "-"):
    print(border*90)
    print(string)
    print(border*90)
def move_set_to_choices_table(move_set):
    choices_table = {}
    for k,v in move_set.items():
        if v.type == ActionType.ATTACK:
            choices_table[k] = Choice(f"Attack dealing {v.val} damage", v)
        elif v.type == ActionType.HEAL:
            choices_table[k] = Choice(f"Healing move that replenishes {v.val} hp", v)
    return choices_table
#Creatures
BombCrocMoveset = {
    "whip":Action(ActionType.ATTACK, 3),
    "bash":Action(ActionType.ATTACK, 6)
}
BombCroc = Creature(70, "Bombardino Crocadilo",BombCrocMoveset,70)
tung_town_case = Room(
    "TownSquare",
    "A desolate town square surrounded by faded grass. A demolished statue of tung tung tung sahur stands at the centre, heavy with strange fruit. Two rectangular creatures stand next to you.",
    100,
    {"north": Choice("Proceed to Scarlet Swamp", [Action(ActionType.MOVE, "scarlet_swamp"),Action(ActionType.DISPLAY_DIA, "As you walk through some tall grass something lunges at you."),Action(ActionType.START_BATTLE, BombCroc, True)])}
)
scarlet_swamp = Room("ScarletSwamp",
                     "Swampy",
                     100,
                     {"south": Choice("Proceed to Tung town",[Action(ActionType.MOVE, "tung_town_case")])}
)
room_dict = {
    "tung_town_case": tung_town_case,
    "scarlet_swamp": scarlet_swamp
}

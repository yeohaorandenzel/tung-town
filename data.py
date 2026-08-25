class ActionType:
    MOVE = 1
    START_BATTLE = 2
    DISPLAY_DIA = 3

class Action:
    def __init__(self,type:ActionType,val):
        self.type = type
        self.val = val

class Choice:
    def __init__(self,desc,actions):
        self.desc = desc
        self.actions = actions
class Creature:
    pass
class Room:
    def __init__(self, name: str, description: str, max_health: int,exits: dict[str, "Room"]):
        self.name = name
        self.description = description
        self.exits: dict[str, str] = exits
        self.creatures: list[Creature] = []
        self.__max_health = max_health

class Player:
    def __init__(self, name: str,current_room):
        self.name = name
        self.current_room = current_room
def prompt_player_choice(choices_dict):
    print(choices_dict["description"])
    for choice_name,choice in choices_dict["choices"].items():
        print(choice_name,choice.desc)
    return input(">")
def display(k):
    pass
tung_town_case = Room(
    "TownSquare",
    "A desolate town square surrounded by faded grass. A demolished statue of tung tung tung sahur stands at the centre, heavy with strange fruit. Two rectangular creatures stand next to you.",
    100,
    {"north": Choice("Scarlet Swamp", [Action(ActionType.MOVE, "scarlet_swamp")])}
)

scarlet_swamp = Room("ScarletSwamp","Swampy",100,{"south": Choice("Tung town",[Action(ActionType.MOVE, "tung_town_case")])})

room_dict = {
    "tung_town_case": tung_town_case,
    "scarlet_swamp": scarlet_swamp
}

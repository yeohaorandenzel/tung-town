class data:

    class Player:
        def __init__(self, name: str, )

    class Room:
        def __init__(self, name: str, description: str, max_health: int):
            self.name = name
            self.description = description
            self.exits: Dict[str, "Room"] = {}
            self.creatures: List["Creature"] = []
            self.__max_health = max_health
    
    class Weapon:
        def __init__(self):
            self.name = "barehand" #default weapon
            self.damage = 1 #barehanded damage

    class Inventory:
        def __init__(self):
            self.number = 5 #current number of items inventory
            self.items = [] #list of all items in inventory

tung_town_case = Room(
    "TownSquare",
    "A desolate town square surrounded by faded grass. A demolished statue of tung tung tung sahur stands at the centre, heavy with strange fruit. Two rectangular creatures stand next to you.",
    100
)

scarlet_swamp = Room(
    "ScarletSwamp",

current_location = "Tung Town Square"
current_turn = player
inventory.number (returns number of items in inventory)
inventory.items (returns a list of items in inventory)
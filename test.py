#Navigation
def test_valid_movement:
    """Test that the Player moves to the correct Room after choosing the
    cardinal direction."""
    first_location = current_location


def test_invalid_movement:
    """Test that when Player chooses a direction that is out of bounds, 
    there is a proper error message displayed and Player stays in place."""

#Combat
def test_turn_order: 
    """Test that combat resolves sequentially, ensuring the player acts
     first and the creature retaliates second only if it remains alive"""


def test_weapon_damage:
    """Test that bare-handed attacks deal 1 damage, while other weapons
     (e.g., Solaris’ Spear) have their respective damage."""
    elif Weapon.name == "barehanded":
        if Weapon.damage != 1:
            return False
    elif Weapon.name == "Solaris' Spear":
        if Weapon.damage != 5:
            return False
    elif Weapon.name == "Sword of Sorrow":
        if Weapon.damage != 2:
            return False
    elif Weapon.name == "Soul Eater":
        if Weapon.damage != 10:
            return False
    return True


def test_damage_buff:
    """Test that damage buff items add temporary buff, buff is removed 
    after use and unequipped after use"""

#Inventory
def test_pickup_item:
    """Tests that items are transferred into the Player's inventory from
    the Room after a successful pickup"""
    initial_inv_no = Inventory.number
    #make choice to pickup
    final_inv_no = Inventory.number
    if  final_inv_no != (initial_inv_no + 1):
        return False
    #add if item is not an element in Inventory.item
    

def test_inv_cap:
    """Tests that an error message is displayed when inventory is at maximum
    capacity, and that item is not picked up"""
    if Inventory.number == 5:
        #make choice to pickup
        if len(Inventory.items) != 5:
            return False


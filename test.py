#Navigation
current_location
current_turn: (returns whose turn)
weapon.name (returns bare handed or weapon)
weapon.damage
inventory.number (returns number of items in inventory)
inventory.items (returns a list of items in inventory)


def test_valid_movement:
    """Test that the Player moves to the correct Room after choosing the
    cardinal direction."""
    current_location

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

def test_damage_buff:
    """Test that damage buff items add temporary buff, buff is removed 
    after use and unequipped after use"""

#Inventory
def test_pickup_item:
    """Tests that items are transferred into the Player's inventory from
    the Room after a successful pickup"""

def test_inv_cap:
    """Tests that an error message is displayed when inventory is at maximum
    capacity, and that item is not picked up"""


"""
put the NPC's into a tuple. you can call each npc individually or all at once.
this makes the random function easier to use as well (for random encounters, if coded.)

targets = (Goblin(), Giant_Rat(), Guard())

#to attack all targets in tuple
for target in targets
    attack(player, targets) (attack function is example.)

#to attack one target in the tuple
for target in targets
attack(player, targets[X] ; X = target in tuple
"""
import Player_Class

"""
#to check if enemies are alive
print(Goblin.goblin_is_alive(enemies[0]))
print(GiantRat.giant_rat_is_alive(enemies[1]))
print(Guard.guard_is_alive(enemies[2])) 
"""


import time
import random
import Monster_Drop_Table_Rewrite
import colorama
import threading
import items_and_item_behaviors

print(items_and_item_behaviors.weapons)

"""
This script is designed for a game where players can interact with multiple NPCs.
Players can attack NPCs, loot them, and manage their inventory.
"""


class Player:
    """This class represents the player character in the game."""

    def __init__(self, default_slots=10):
        """Initialize player attributes."""
        self.hp = 10
        self.damage = 0.5
        # Set up a default inventory with empty slots.
        self.inventory = ["Empty" for _ in range(default_slots)]
        self.worn_equipment()

    def worn_equipment(self):
        """Define the slots for equipment that can be worn."""
        self.head_slot = None
        self.cape_slot = None
        self.neck_slot = None
        self.ammunition_slot = None
        self.weapon_slot = None
        self.shield_slot = None
        self.two_handed_slot = None
        self.body_slot = None
        self.legs_slot = None
        self.hands_slot = None
        self.feet_slot = None

    def player_inventory(self):
        """Display the current contents of the player's inventory."""
        print("---INVENTORY---")
        for slot_number, item in enumerate(self.inventory, 1):
            print(f"Inventory slot {slot_number}: {item}")

    def slot_is_empty(self, slot_number):
        """Check if a specific inventory slot is empty."""
        return self.inventory[slot_number - 1] == "Empty"

    def add_item(self, slot_number, item):
        """Add an item to the player's inventory in a specific slot."""
        if 0 < slot_number <= len(self.inventory):
            if self.slot_is_empty(slot_number):
                self.inventory[slot_number - 1] = item
            else:
                print("There is an item in that slot already.\n")
        else:
            print(f"No slot number {slot_number}.\n")

    def first_empty_slot(self):
        """Find the first empty slot in the inventory. Return None if all slots are full."""
        for slot_number, item in enumerate(self.inventory):
            if item == "Empty":
                return slot_number + 1
        return None

    def add_item_to_first_available_slot(self, item):
        """Add an item to the first available slot in the inventory."""
        slot = self.first_empty_slot()
        if slot:
            self.add_item(slot, item)
        else:
            print("All slots are occupied. Cannot add the item.\n")

    def player_attack_enemies(self):
        """Handle the logic for the player attacking enemies."""
        incoming_damage = self.damage
        deflect_chance = random.randint(0, 99)
        if deflect_chance <= 24:
            print("deflect chance =", deflect_chance, "percent")
            print("Enemy has deflected the attack. (deflect chance =", deflect_chance, "percent)\n")
        else:
            for enemy in enemies:
                enemy.hp -= incoming_damage
            print("full damage inflicted")

    def player_is_alive(self):
        """Check if the player is still alive."""
        return self.hp >= 1


class Goblin:
    """This class represents the Goblin NPC."""

    def __init__(self):
        """Initialize Goblin attributes."""
        self.hp = 1
        self.damage = 1

    def __str__(self):
        return "Goblin"

    def is_alive(self):
        """Check if the Goblin is still alive."""
        return self.hp >= 1

    def goblin_drop_on_death(self):
        """Handle the logic for the Goblin dropping items upon death."""
        if not self.is_alive():
            print("Goblin has dropped bones.")
            pickup = input("Would you like to loot the Goblin? Enter yes or no.\n")
            if pickup.lower() in ["yes", "y"]:
                player.add_item_to_first_available_slot(Monster_Drop_Table_Rewrite.bones.name)
                print(f"The {Monster_Drop_Table_Rewrite.bones.name} have been added to your bag.\n")
            elif pickup.lower() in ["no", "n"]:
                print(f"You leave the {Monster_Drop_Table_Rewrite.bones.name} on the ground.")
            else:
                print("Please enter yes or no.")
                self.goblin_drop_on_death()


class GiantRat:
    """This class represents the Giant Rat NPC."""

    def __init__(self):
        """Initialize Giant Rat attributes."""
        self.hp = 1
        self.damage = 1

    def __str__(self):
        return "Giant Rat"

    def is_alive(self):
        """Check if the Giant Rat is still alive."""
        return self.hp >= 1


class Guard:
    """This class represents the Guard NPC."""

    def __init__(self):
        """Initialize Guard attributes."""
        self.hp = 10
        self.damage = 1

    def __str__(self):
        return "Guard"

    def is_alive(self):
        """Check if the Guard is still alive."""
        return self.hp >= 1

def enemy_attack_player():
    """Handle the logic for enemies attacking the player."""
    incoming_damage = enemies[0].damage
    deflect_chance = random.randint(0, 99)
    if deflect_chance <= 24:
        print("Player has deflected the enemy attack. (deflect chance =", deflect_chance, "percent)")
    else:
        player.hp -= incoming_damage
        print("full damage inflicted")


player = Player()
enemies = (Goblin(), GiantRat(), Guard())

player.add_item(1, "Shield")
player.player_inventory()
loot = items_and_item_behaviors.Items(items_and_item_behaviors.Bones, items_and_item_behaviors.Bones)

# Main game loop
while True:
    if not player.player_is_alive():
        exit()

    for index, enemy in enumerate(enemies):
        if not enemy.is_alive():
            print(f"Player has defeated {enemy}\n")
            enemy.goblin_drop_on_death()
            player.player_inventory()
            items_and_item_behaviors.Bones.examine(items_and_item_behaviors.goblin_always_dropped)
            exit()

    player.player_attack_enemies()
    print([enemy.hp for enemy in enemies])
    time.sleep(1.25)
    enemy_attack_player()
    print(f"Player HP = {player.hp}")
    time.sleep(1.25)

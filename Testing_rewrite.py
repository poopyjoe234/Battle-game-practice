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
import freespacetocode

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

"""
This script is designed for a game where players can interact with multiple NPCs.
Players can attack NPCs, loot them, and manage their inventory.
"""


class Player:
    """This class represents the player character in the game."""

    def __init__(self, default_slots=10):
        """Initialize player attributes."""
        self.hp = 10
        self.damage = 1
        self.base_deflect_chance = 25
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

    def print_worn_equipment(self):
        print(colorama.Fore.LIGHTWHITE_EX)
        worn_equipment = [
            ("Head", self.head_slot),
            ("Cape", self.cape_slot),
            ("Neck", self.neck_slot),
            ("Ammo", self.ammunition_slot),
            ("Weapon", self.weapon_slot),
            ("Shield", self.shield_slot),
            ("Two-handed", self.two_handed_slot),
            ("Body", self.body_slot),
            ("Legs", self.legs_slot),
            ("Hands", self.hands_slot),
            ("Feet", self.feet_slot)
        ]

        for slot_name, slot_item in worn_equipment:
            if slot_item:
                print(f"{slot_name}: {str(slot_item)}")
            else:
                print(f"{slot_name}: Empty")

    def unequip_item(self, equipment_type):
        """Unequip an item and move it to the inventory."""

        equipment_directory = [
            ("Head", self.head_slot),
            ("Cape", self.cape_slot),
            ("Neck", self.neck_slot),
            ("Ammo", self.ammunition_slot),
            ("Weapon", self.weapon_slot),
            ("Shield", self.shield_slot),
            ("Two-handed", self.two_handed_slot),
            ("Body", self.body_slot),
            ("Legs", self.legs_slot),
            ("Hands", self.hands_slot),
            ("Feet", self.feet_slot)
        ]

        for slot_name, slot_item in equipment_directory:
            if slot_name.lower() == equipment_type.lower():
                if slot_item:
                    available_slot = self.first_empty_slot()
                    if available_slot:
                        self.add_item(available_slot, slot_item)
                        if slot_name == "Head":
                            self.head_slot = None
                        elif slot_name == "Cape":
                            self.cape_slot = None
                        elif slot_name == "Neck":
                            self.neck_slot = None
                        elif slot_name == "Ammo":
                            self.ammunition_slot = None
                        elif slot_name == "Weapon":
                            self.weapon_slot = None
                        elif slot_name == "Shield":
                            self.shield_slot = None
                        elif slot_name == "Two-handed":
                            self.two_handed_slot = None
                        elif slot_name == "Body":
                            self.body_slot = None
                        elif slot_name == "Hands":
                            self.hands_slot = None
                        elif slot_name == "Feet":
                            self.feet_slot = None

                        print(f"{slot_item.name} has been unequipped and added to your inventory.")
                        break
                    else:
                        print("Your inventory is full. You cannot unequip the item.")
                else:
                    print(f"There is no item equipped in the {slot_name} slot")
                break



    def player_inventory(self):
        """Display the current contents of the players inventory."""
        print("---INVENTORY---")
        for slot_number, item in enumerate(self.inventory, 1):
            print(f"Inventory slot {slot_number}: {item}")

        print("Type //examine (slot number) to examine an item in your inventory.")
        print("Type //equip (slot number) to equip a weapon or piece of armour.")
        print("Type //equipment to print worn equipment.")
        print("Type //unequip (equipment slot) to unequip a weapon or piece of armour.")
        print("Type //drop (slot number) to unequip a weapon or piece of armour.")
        player_choice = input()

        if player_choice.startswith("//examine"):
            parts = player_choice.split()
            if len(parts) > 1:
                slot = int(player_choice.split()[1]) - 1
                if 0 <= slot < len(self.inventory):
                    item = self.inventory[slot]
                    if isinstance(item, items_and_item_behaviors.Items):  # Check if the item is an instance of the Items class
                        print(f"{item.name}: {item.examine_description}")
                    else:
                        print("The slot is empty or contains an invalid item.")
                else:
                    print("Enter a valid slot number.")
            else:
                print("Please enter a slot number after //examine")

        if player_choice.lower() == "//equipment":
                self.print_worn_equipment()

        elif player_choice.startswith(f"//equip"):
            parts = player_choice.split()
            if len(parts) > 1:
                slot = int(parts[1]) - 1
                if 0 <= slot < len(self.inventory):
                    item_to_equip = self.inventory[slot]
                    if item_to_equip == "Empty":
                        print("There's nothing in this slot to equip.")
                        return

                    if hasattr(item_to_equip, "armour_type"):
                        if item_to_equip.armour_type == "Shield" and not self.shield_slot:
                            self.shield_slot = item_to_equip
                            self.inventory[slot] = "Empty"
                            print(f"{item_to_equip.name} has been equipped.\n")

                    if hasattr(item_to_equip, "weapon_type"):
                        if item_to_equip.weapon_type == "Weapon" and not self.weapon_slot:
                            self.weapon_slot = item_to_equip
                            self.inventory[slot] = "Empty"
                            print(f"{item_to_equip.name} has been equipped.\n")

                    else:
                        print("The item in this slot cannot be equipped.")
                else:
                    print("Slot number is invalid.")
            else:
                print("Slot number is invalid.")

        elif player_choice.startswith(f"//unequip"):
            parts = player_choice.split()
            if len(parts) > 1:
                equipment_slot = player_choice.split()[1].lower()
                self.unequip_item(equipment_slot.lower())
            else:
                print("Please enter an item slot to unequip that item.")

        elif player_choice.startswith(f"//drop"):
            parts = player_choice.split()
            if len(parts) > 1:
                slot = int(parts[1]) - 1
                if 0 <= slot < len(self.inventory):
                    dropped_item = self.inventory[slot]
                    if dropped_item != "Empty":
                        print(f"You have dropped {dropped_item}.")
                        self.inventory[slot] = "Empty"
                    else:
                        print("There's nothing in this slot to drop.")

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

    def total_deflect_chance(self):
        total_chance_of_deflect = self.base_deflect_chance
        if isinstance(self.shield_slot, items_and_item_behaviors.Shield):
            total_chance_of_deflect += self.shield_slot.deflection_chance
        return total_chance_of_deflect

    def player_attack_enemies(self):
        """Handle the logic for the player attacking enemies."""
        incoming_damage = self.damage
        deflect_chance = random.randint(0, 99)
        if deflect_chance <= 24:
            print("deflect chance =", deflect_chance, "percent")
            print("Enemy has deflected the attack. (deflect chance =", deflect_chance, "percent)\n")
        else:
            enemy.hp -= incoming_damage
            print("deflect chance =", deflect_chance, "percent")
            print("full damage inflicted to the enemy.\n")

    def full_player_attack(self):
        print(colorama.Fore.LIGHTYELLOW_EX)
        self.player_attack_enemies()
        print("")
        print("Enemy HP =", enemy.hp)
        print("")

    def player_is_alive(self):
        """Check if the player is still alive."""
        return self.hp >= 1


class Goblin:
    """This class represents the Goblin NPC."""

    def __init__(self):
        """Initialize Goblin attributes."""
        self.hp = 1
        self.damage = 1
        self.loot = []

    def __str__(self):
        return "Goblin"

    def is_alive(self):
        """Check if the Goblin is still alive."""
        return self.hp >= 1


    def goblin_drop_on_death(self):
        """Handle the logic for the Goblin dropping items upon death."""
        if not self.is_alive():
            self.loot = self.goblin_loot_chance()
            while True:
                pickup = input("\nWould you like to loot the Goblin? Enter yes or no.\n")
                if pickup.lower() in ["yes", "y"]:
                    for item in self.loot:
                        player.add_item_to_first_available_slot(item)
                    break
                # print(f"The {Monster_Drop_Table_Rewrite.Bones.name} have been added to your bag.\n")
                # print(f"The {Monster_Drop_Table_Rewrite.Bronze_Square_Shield.name} have been added to your bag.\n")
                elif pickup.lower() in ["no", "n"]:
                    print(f"You leave the loot on the ground.")
                    break
                else:
                    print("Please enter yes or no.")


    def goblin_loot_chance(self):

        loot = []

        bones = Monster_Drop_Table_Rewrite.bones_odds()
        if bones == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bones)

        dagger = Monster_Drop_Table_Rewrite.bronze_dagger_odds()
        if dagger.lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Dagger)

        shield = Monster_Drop_Table_Rewrite.bronze_square_shield()
        if shield == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Square_Shield)

        return loot


    # def goblin_drop_on_death(self):
    #     """Handle the logic for the Goblin dropping items upon death."""
    #     if not self.is_alive():
    #         bones_drop = Monster_Drop_Table_Rewrite.bones_odds()
    #         shield_drop = Monster_Drop_Table_Rewrite.bronze_square_shield()
    #         if shield_drop == "drop":
    #             print(f"Goblin has dropped {Monster_Drop_Table_Rewrite.Bronze_Square_Shield.name}")
    #         if bones_drop == "drop":
    #             print(f"Goblin has dropped {Monster_Drop_Table_Rewrite.Bones.name}.")
    #         pickup = input("\nWould you like to loot the Goblin? Enter yes or no.\n")
    #         if pickup.lower() in ["yes", "y"]:
    #             player.add_item_to_first_available_slot(Monster_Drop_Table_Rewrite.Bones)
    #             time.sleep(.1)"
                # player.add_item_to_first_available_slot(Monster_Drop_Table_Rewrite.Bronze_Square_Shield)
                # print("")
                # print(f"The {Monster_Drop_Table_Rewrite.Bones.name} have been added to your bag.\n")
                # print(f"The {Monster_Drop_Table_Rewrite.Bronze_Square_Shield.name} have been added to your bag.\n")

            # elif pickup.lower() in ["no", "n"]:
            #     print(f"You leave the loot on the ground.")
            # else:
            #     print("Please enter yes or no.")
            #     self.goblin_drop_on_death()


class GiantRat:
    """This class represents the Giant Rat NPC."""

    def __init__(self):
        """Initialize Giant Rat attributes."""
        self.hp = 11
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
        self.hp = 11
        self.damage = 1

    def __str__(self):
        return "Guard"

    def is_alive(self):
        """Check if the Guard is still alive."""
        return self.hp >= 1


def enemy_attack_player():
    """Handle the logic for enemies attacking the player."""
    incoming_damage = enemy.damage
    deflect_roll = random.randint(0, 99)
    if deflect_roll <= player.total_deflect_chance():
        print("deflect chance =", deflect_roll, "percent")
        print("Player has deflected the attack. (deflect chance =", deflect_roll, "percent)\n")
    else:
        player.hp -= incoming_damage
        print("Player roll:", deflect_roll)
        print("full damage inflicted to Player.\n")


def full_enemy_attack():
    print(colorama.Fore.RESET)
    print(colorama.Fore.RED)
    enemy_attack_player()
    print("")
    print(f"Player HP = {player.hp}")
    print("")


player = Player()
enemy = Goblin()


"""Main game loop"""

while True:

    if enemy.is_alive():
        player.full_player_attack()
        enemy.is_alive()
        time.sleep(.5)
        print(colorama.Fore.RESET)

    if not enemy.is_alive():
        time.sleep(1)
        print(colorama.Fore.LIGHTGREEN_EX)
        print(f"Player has defeated {enemy}\n")
        enemy.goblin_drop_on_death()
        player.player_inventory()
        player.print_worn_equipment()
        print(colorama.Fore.RESET)
        break

    if player.player_is_alive():
        full_enemy_attack()
        player.player_is_alive()
        time.sleep(.5)
        print(colorama.Fore.RESET)

    if not player.player_is_alive():
        print("Player has been defeated.")
        time.sleep(1)
        break

    if not enemy.is_alive():
        print(f"Player has defeated {enemy}\n")
        enemy.goblin_drop_on_death()
        player.player_inventory()
        exit()


    # for index, enemy in enumerate(enemy):
    #     if not enemy.is_alive():
    #         print(f"Player has defeated {enemy}\n")
    #         enemy.goblin_drop_on_death()
    #         player.player_inventory()
    #         exit()



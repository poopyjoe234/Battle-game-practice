"""
Refactored Text-Based Battle Game

A turn-based combat RPG where players fight enemies, manage inventory,
equip items, and collect loot. This version maintains the same functionality
as the original but with cleaner, more maintainable code structure.
"""

import time
import random
from typing import List, Optional, Tuple
from colorama import Fore, init

import items_and_item_behaviors
import Monster_Drop_Table_Rewrite

# Initialize colorama
init(autoreset=True)

# Game Constants
DEFAULT_PLAYER_HP = 10
DEFAULT_INVENTORY_SLOTS = 10
BASE_DEFLECT_CHANCE = 25
DEFLECT_THRESHOLD = 24
COMBAT_DELAY = 0.5

# Enemy Configuration
ENEMY_CONFIGS = {
    'goblin': {'hp': 1, 'damage': 1},
    'giant_rat': {'hp': 15, 'damage': 0.5},
    'guard': {'hp': 15, 'damage': 2}
}


class Player:
    """Represents the player character with combat stats, inventory, and equipment."""

    def __init__(self, default_slots: int = DEFAULT_INVENTORY_SLOTS):
        self.hp = DEFAULT_PLAYER_HP
        self.base_damage = 1
        self.added_damage = 0
        self.base_deflect_chance = BASE_DEFLECT_CHANCE
        self.added_deflect_chance = 0
        self.inventory = ["Empty" for _ in range(default_slots)]
        self._init_equipment_slots()

    def _init_equipment_slots(self) -> None:
        """Initialize all equipment slots to None."""
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

    @property
    def damage(self) -> int:
        """Calculate total damage including equipped weapons."""
        return self.base_damage + self.added_damage

    @property
    def deflect_chance(self) -> int:
        """Calculate total deflect chance including equipped shields."""
        return self.base_deflect_chance + self.added_deflect_chance

    def is_alive(self) -> bool:
        """Check if player is still alive."""
        return self.hp > 0

    def take_damage(self, damage: float) -> bool:
        """
        Apply damage to player with deflect chance.
        Returns True if damage was deflected, False otherwise.
        """
        deflect_roll = random.randint(0, 99)
        if deflect_roll <= self.deflect_chance:
            print(f"deflect chance = {deflect_roll} percent")
            print(f"Player has deflected the attack. (deflect chance = {deflect_roll} percent)\n")
            return True
        else:
            self.hp = max(0, self.hp - damage)
            print(f"Player roll: {deflect_roll}")
            print("full damage inflicted to Player.\n")
            return False

    def print_worn_equipment(self) -> None:
        """Display all currently equipped items."""
        print(Fore.LIGHTWHITE_EX)
        equipment_slots = [
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

        for slot_name, slot_item in equipment_slots:
            display_item = str(slot_item) if slot_item else "Empty"
            print(f"{slot_name}: {display_item}")

    def equip_weapon(self, weapon: items_and_item_behaviors.Weapon) -> None:
        """Equip a weapon and apply its damage bonus."""
        self.added_damage += weapon.damage
        self.weapon_slot = weapon
        print(f"Damage increased by {weapon.damage}.")
        print(f"Damage is now {self.damage}")

    def unequip_weapon(self) -> None:
        """Remove equipped weapon and revert damage bonus."""
        if self.weapon_slot:
            self.added_damage -= self.weapon_slot.damage
            self.add_item_to_first_available_slot(self.weapon_slot)
            print(f"Damage decreased by {self.weapon_slot.damage}.")
            self.weapon_slot = None
        else:
            print("There is no item equipped in the Weapon slot")

    def equip_shield(self, shield: items_and_item_behaviors.Shield) -> None:
        """Equip a shield and apply its deflection bonus."""
        self.added_deflect_chance += shield.deflection_chance
        self.shield_slot = shield
        print(f"Deflection chance increased by {shield.deflection_chance}.")
        print(f"Deflection chance is now {self.deflect_chance}.")

    def unequip_shield(self) -> None:
        """Remove equipped shield and revert deflection bonus."""
        if self.shield_slot:
            self.added_deflect_chance -= self.shield_slot.deflection_chance
            self.add_item_to_first_available_slot(self.shield_slot)
            print(f"Deflection chance decreased by {self.shield_slot.deflection_chance}.")
            self.shield_slot = None
        else:
            print("There is no item equipped in the Shield slot")

    def first_empty_slot(self) -> Optional[int]:
        """Find the first empty inventory slot (1-indexed). Returns None if full."""
        for slot_number, item in enumerate(self.inventory, 1):
            if item == "Empty":
                return slot_number
        return None

    def slot_is_empty(self, slot_number: int) -> bool:
        """Check if a specific inventory slot is empty (1-indexed)."""
        if 0 < slot_number <= len(self.inventory):
            return self.inventory[slot_number - 1] == "Empty"
        return False

    def add_item(self, slot_number: int, item) -> bool:
        """Add an item to a specific inventory slot (1-indexed). Returns success status."""
        if 0 < slot_number <= len(self.inventory):
            if self.slot_is_empty(slot_number):
                self.inventory[slot_number - 1] = item
                return True
            else:
                print("There is an item in that slot already.\n")
                return False
        else:
            print(f"No slot number {slot_number}.\n")
            return False

    def add_item_to_first_available_slot(self, item) -> bool:
        """Add an item to the first available inventory slot. Returns success status."""
        slot = self.first_empty_slot()
        if slot:
            self.add_item(slot, item)
            return True
        else:
            print("All slots are occupied. Cannot add the item.\n")
            return False

    def display_inventory_menu(self) -> None:
        """Display the inventory and available commands."""
        print("---INVENTORY---")
        for slot_number, item in enumerate(self.inventory, 1):
            print(f"Inventory slot {slot_number}: {item}")

        print("\nCommands:")
        print("  //examine (slot number) - Examine an item")
        print("  //equip (slot number) - Equip a weapon or armor")
        print("  //equipment - View worn equipment")
        print("  //unequip (weapon|shield) - Unequip an item")
        print("  //drop (slot number) - Drop an item")

    def handle_examine(self, slot_number: int) -> None:
        """Examine an item in the inventory."""
        if 0 <= slot_number < len(self.inventory):
            item = self.inventory[slot_number]
            if isinstance(item, items_and_item_behaviors.Items):
                print(f"{item.name}: {item.examine_description}\n")
            else:
                print("The slot is empty or contains an invalid item.")
        else:
            print("Enter a valid slot number.")

    def handle_equip(self, slot_number: int) -> None:
        """Equip an item from the inventory."""
        if not (0 <= slot_number < len(self.inventory)):
            print("Slot number is invalid.")
            return

        item_to_equip = self.inventory[slot_number]
        if item_to_equip == "Empty":
            print("There's nothing in this slot to equip.")
            return

        # Handle shield equipment
        if hasattr(item_to_equip, "armour_type"):
            if item_to_equip.armour_type == "Shield" and not self.shield_slot:
                self.equip_shield(item_to_equip)
                self.inventory[slot_number] = "Empty"
                print(f"{item_to_equip.name} has been equipped.\n")
                return

        # Handle weapon equipment
        if hasattr(item_to_equip, "weapon_type"):
            if item_to_equip.weapon_type == "Weapon" and not self.weapon_slot:
                self.equip_weapon(item_to_equip)
                self.inventory[slot_number] = "Empty"
                print(f"{item_to_equip.name} has been equipped.\n")
                return

        print("The item in this slot cannot be equipped or slot is occupied.")

    def handle_unequip(self, equipment_type: str) -> None:
        """Unequip an item and return it to inventory."""
        equipment_type = equipment_type.lower()
        if equipment_type == "weapon":
            self.unequip_weapon()
        elif equipment_type == "shield":
            self.unequip_shield()
        else:
            print("Please enter 'weapon' or 'shield'.")

    def handle_drop(self, slot_number: int) -> None:
        """Drop an item from the inventory."""
        if 0 <= slot_number < len(self.inventory):
            dropped_item = self.inventory[slot_number]
            if dropped_item != "Empty":
                print(f"You have dropped {dropped_item}.")
                self.inventory[slot_number] = "Empty"
            else:
                print("There's nothing in this slot to drop.")
        else:
            print("Invalid slot number.")

    def process_inventory_command(self, command: str) -> None:
        """Process a player command in the inventory system."""
        parts = command.split()

        if command.startswith("//examine") and len(parts) > 1:
            try:
                slot = int(parts[1]) - 1
                self.handle_examine(slot)
            except (ValueError, IndexError):
                print("Please enter a valid slot number after //examine")

        elif command.lower() == "//equipment":
            self.print_worn_equipment()

        elif command.startswith("//equip") and len(parts) > 1:
            try:
                slot = int(parts[1]) - 1
                self.handle_equip(slot)
            except (ValueError, IndexError):
                print("Please enter a valid slot number after //equip")

        elif command.startswith("//unequip") and len(parts) > 1:
            equipment_type = parts[1]
            self.handle_unequip(equipment_type)

        elif command.startswith("//drop") and len(parts) > 1:
            try:
                slot = int(parts[1]) - 1
                self.handle_drop(slot)
            except (ValueError, IndexError):
                print("Please enter a valid slot number after //drop")

    def open_inventory(self) -> None:
        """Open the inventory interface for the player."""
        while True:
            self.display_inventory_menu()
            player_choice = input("\nEnter command: ")
            self.process_inventory_command(player_choice)

            # Ask if player wants to continue in inventory
            print("\nWould you like to do anything else in the inventory?")
            continue_choice = input("Press Enter to continue fighting or 'yes' to stay in inventory: ")
            if continue_choice.lower() not in ["yes", "y"]:
                break


class Enemy:
    """Base class for all enemy types."""

    def __init__(self, name: str, hp: float, damage: float):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.loot: List = []

    def __str__(self) -> str:
        return self.name

    def is_alive(self) -> bool:
        """Check if enemy is still alive."""
        return self.hp > 0

    def reset(self) -> None:
        """Reset enemy to initial state."""
        self.hp = self.max_hp
        self.loot = []

    def take_damage(self, damage: int) -> bool:
        """
        Apply damage to enemy with deflect chance.
        Returns True if damage was deflected, False otherwise.
        """
        deflect_roll = random.randint(0, 99)
        if deflect_roll <= DEFLECT_THRESHOLD:
            print(f"deflect chance = {deflect_roll} percent")
            print(f"Enemy has deflected the attack. (deflect chance = {deflect_roll} percent)\n")
            return True
        else:
            self.hp = max(0, self.hp - damage)
            print(f"deflect chance = {deflect_roll} percent")
            print("full damage inflicted to the enemy.\n")
            return False

    def attack(self, player: Player) -> None:
        """Attack the player."""
        print(Fore.RED)
        player.take_damage(self.damage)
        if player.hp <= 0:
            player.hp = 0
        print(f"Player HP = {player.hp}\n")

    def generate_loot(self) -> List:
        """Generate loot for this enemy. Override in subclasses."""
        return []

    def offer_loot(self, player: Player) -> None:
        """Offer loot to the player after defeat."""
        if not self.is_alive():
            self.loot = self.generate_loot()
            while True:
                pickup = input(f"\nWould you like to loot the {self.name}? Enter yes or no: ")
                if pickup.lower() in ["yes", "y"]:
                    for item in self.loot:
                        player.add_item_to_first_available_slot(item)
                    break
                elif pickup.lower() in ["no", "n"]:
                    print("You leave the loot on the ground.")
                    break
                else:
                    print("Please enter yes or no.")


class Goblin(Enemy):
    """Goblin enemy type."""

    def __init__(self):
        config = ENEMY_CONFIGS['goblin']
        super().__init__("Goblin", config['hp'], config['damage'])

    def generate_loot(self) -> List:
        """Generate loot based on Goblin drop table."""
        loot = []

        if Monster_Drop_Table_Rewrite.bones_odds() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bones_goblin)

        if Monster_Drop_Table_Rewrite.bronze_dagger_odds().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Dagger_goblin)

        if Monster_Drop_Table_Rewrite.bronze_sword().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Sword_goblin)

        if Monster_Drop_Table_Rewrite.bronze_square_shield().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Square_Shield_goblin)

        if Monster_Drop_Table_Rewrite.bronze_kite_shield().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Kite_Shield_goblin)

        return loot


class GiantRat(Enemy):
    """Giant Rat enemy type."""

    def __init__(self):
        config = ENEMY_CONFIGS['giant_rat']
        super().__init__("Giant Rat", config['hp'], config['damage'])

    def generate_loot(self) -> List:
        """Generate loot based on Giant Rat drop table."""
        loot = []

        if Monster_Drop_Table_Rewrite.bones_odds() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bones_rat)

        if Monster_Drop_Table_Rewrite.bronze_square_shield().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Square_Shield_rat)

        return loot


class Guard(Enemy):
    """Guard enemy type."""

    def __init__(self):
        config = ENEMY_CONFIGS['guard']
        super().__init__("Guard", config['hp'], config['damage'])

    def generate_loot(self) -> List:
        """Generate loot based on Guard drop table."""
        loot = []

        if Monster_Drop_Table_Rewrite.bones_odds() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bones_guard)

        if Monster_Drop_Table_Rewrite.bronze_sword().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Sword_goblin)

        if Monster_Drop_Table_Rewrite.bronze_kite_shield().lower() == "drop":
            loot.append(Monster_Drop_Table_Rewrite.Bronze_Kite_Shield_goblin)

        return loot


class CombatManager:
    """Manages combat encounters between player and enemies."""

    def __init__(self, player: Player):
        self.player = player

    def player_turn(self, enemy: Enemy) -> None:
        """Execute player's turn in combat."""
        print(Fore.LIGHTYELLOW_EX)
        enemy.take_damage(self.player.damage)
        print(f"Enemy HP = {enemy.hp}\n")

    def enemy_turn(self, enemy: Enemy) -> None:
        """Execute enemy's turn in combat."""
        enemy.attack(self.player)

    def combat_round(self, enemy: Enemy) -> Tuple[bool, bool]:
        """
        Execute one round of combat.
        Returns (player_alive, enemy_alive) tuple.
        """
        # Player attacks first
        if enemy.is_alive():
            self.player_turn(enemy)
            time.sleep(COMBAT_DELAY)

        # Check if enemy is defeated
        if not enemy.is_alive():
            return True, False

        # Enemy counter-attacks
        if self.player.is_alive():
            self.enemy_turn(enemy)
            time.sleep(COMBAT_DELAY)

        return self.player.is_alive(), enemy.is_alive()

    def combat_encounter(self, enemy: Enemy) -> bool:
        """
        Run a full combat encounter until player or enemy is defeated.
        Returns True if player won, False if player lost.
        """
        while True:
            player_alive, enemy_alive = self.combat_round(enemy)

            # Enemy defeated
            if not enemy_alive:
                time.sleep(1)
                print(Fore.LIGHTGREEN_EX)
                print(f"Player has defeated {enemy}!\n")
                enemy.offer_loot(self.player)
                self.player.open_inventory()
                self.player.print_worn_equipment()
                print(Fore.RESET)
                return True

            # Player defeated
            if not player_alive:
                print("Player has been defeated.")
                time.sleep(1)
                return False

    def run_game_loop(self, enemy: Enemy, rounds: int = 1) -> None:
        """
        Run multiple combat encounters with the same enemy type.
        Player and enemy are reset between encounters.
        """
        for round_num in range(1, rounds + 1):
            print(f"\n{'='*50}")
            print(f"Round {round_num} - Fighting {enemy}")
            print(f"{'='*50}\n")

            result = self.combat_encounter(enemy)

            # Reset for next round
            self.player.hp = DEFAULT_PLAYER_HP
            enemy.reset()

            if not result:
                print("\nGame Over!")
                break


def main():
    """Main game entry point."""
    # Initialize game entities
    player = Player()
    goblin = Goblin()
    giant_rat = GiantRat()
    guard = Guard()

    # Create combat manager
    combat_manager = CombatManager(player)

    # Run combat encounters (matching original behavior)
    print("Welcome to the Battle Game!\n")
    print("You will face 3 Goblins in succession...\n")
    time.sleep(1)

    # Fight 3 goblins
    combat_manager.run_game_loop(goblin, rounds=3)

    # Uncomment these lines to enable additional enemy encounters
    # player.hp = DEFAULT_PLAYER_HP
    # combat_manager.run_game_loop(giant_rat, rounds=1)

    # player.hp = DEFAULT_PLAYER_HP
    # combat_manager.run_game_loop(guard, rounds=1)


if __name__ == "__main__":
    main()

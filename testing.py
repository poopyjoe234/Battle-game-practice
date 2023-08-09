import time
import random
import colorama


# Base class for defining common combat attributes for players
class Player_combat_interface:
    def __init__(self):
        self.hp = None
        self.attack_damage = None
        self.attack_speed = None


# Class to define the attributes and methods of the player
class Player:
    def __init__(self):
        self.Player_hp()
        self.Player_damage()
        self.Player_attack_speed()

    def Player_hp(self):
        self.hp = 1  # Player's health points

    def Player_damage(self):
        self.attack_damage = 1  # Player's attack damage

    def Player_attack_speed(self):
        self.attack_speed = 1  # Player's attack speed

    # Method to calculate the chance of deflecting an attack
    def Player_Deflect_chance(self):
        Deflect_chance = random.randint(0, 99)
        if Deflect_chance > 24:
            print(f"{Deflect_chance + 1} percent.")
            print("The next attack will do damage to the Player.")
            print("----------\n")
            time.sleep(1.5)

        else:
            self.hp += 1  # Increase player's health if deflected
            print(f"{Deflect_chance + 1} percent.")
            print("Deflected, the next attack will do no damage to the Player.")
            print("----------\n")
            time.sleep(1.5)

    # Method to handle player's attack on the NPC
    def Player_attack(self, goblin_class):
        Opponent_hp = goblin_class.hp - self.attack_damage
        goblin_class.hp = Opponent_hp
        print(f"Player has done {self.attack_damage} damage to their opponent.\n")
        time.sleep(1)

    # subclass class for defining player inventory system


class Player_inventory_interface:
    def __init__(self):
        self.inventory = [None] * 10  # Initialize 10 empty slots

    def view_inventory(self):
        inventory = self.inventory
        print(inventory)


# Base class for defining common combat attributes for NPCs
class NPC_combat_interface:
    def __init__(self):
        self.hp = None
        self.attack_damage = None
        self.attack_speed = None


# Class to define the attributes and methods of the goblin
class goblin_class(NPC_combat_interface):
    # Initialization and defining attributes
    def __init__(self):
        super().__init__()
        self.goblin_hp()
        self.goblin_attack_speed()
        self.goblin_attack_damage()
        self.goblin_is_alive()

    # Method to handle NPC's attack on the player
    def goblin_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_damage
        Player.hp = Opponent_hp
        print(f"Goblin has done {self.attack_damage} damage to the Player.\n")
        time.sleep(1)

    def goblin_hp(self):
        self.hp = 1  # NPC's health points

    def goblin_attack_damage(self):
        self.attack_damage = 1  # NPC's attack damage

    def goblin_attack_speed(self):
        self.attack_speed = 1  # NPC's attack speed

    # Method to calculate the chance of deflecting an attack by NPC
    def goblin_Deflect_chance(self):
        while True:
            Deflect_chance = random.randint(0, 99)
            if Deflect_chance > 24:
                print(f"{Deflect_chance + 1} percent.")
                print("The next attack will do damage to Goblin.")
                print("----------\n")
                time.sleep(1.5)
                break

            else:
                self.hp += 1  # Increase NPC's health if deflected
                print(f"{Deflect_chance + 1} percent.")
                print("Deflected, the next attack will do no damage to Goblin.")
                print("----------\n")
                time.sleep(1.5)
                break

    def goblin_is_alive(self):
        if self.hp <= 0:
            print("death to goblin")


# Function to handle the battle sequence
def Battle():
    # Battle loop
    while True:
        print(colorama.Fore.LIGHTWHITE_EX)
        time.sleep(.4)
        print("Battling...\n")
        Computer_player.goblin_Deflect_chance()
        Player_player.Player_attack(Computer_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Computer HP: {Computer_player.hp}\n")
        if Computer_player.hp <= 0:
            print("Player has defeated Goblin.\n")
            Computer_player.goblin_is_alive()
            return 1
        else:
            pass

        print(colorama.Fore.RED)
        time.sleep(.4)
        print("Battling...\n")
        Player_player.Player_Deflect_chance()
        Computer_player.goblin_attack(Player_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Player HP: {Player_player.hp}\n")
        if Player_player.hp <= 0:
            print("NPC has defeated Player.\n")
            return 2
        else:
            pass


# main loop to run the battle; change the integer in the range function for the amount of loops.
for i in range(1):
    Player_player_wins = 0
    NPC_wins = 0

Computer_player = goblin_class()
Player_player = Player()
result = Battle()

if result == 1:
    Player_player_wins += 1
else:
    result == 2
    NPC_wins += 1

print(f"Player 1 wins: {Player_player_wins}")
print(f"NPC wins: {NPC_wins}\n")


# subclass class for defining player inventory system
class Player_inventory_interface:
    def __init__(self):
        self.inventory = [None] * 10  # Initialize 10 empty slots

    class Worn_Equipment:
        def __init__(self):
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

    def print_inventory(self):
        for index, empty_slot in enumerate(self.inventory):
            # The enumerate function takes an iterable (like a list)
            # and returns both the index (position) and the value of each item
            print(f"Slot {index + 1}: {'Empty.' if empty_slot is None else empty_slot}")


Player_player = Player()
Goblin = goblin_class()
inventory = Player_inventory_interface()
Player_inventory_interface.print_inventory(inventory)

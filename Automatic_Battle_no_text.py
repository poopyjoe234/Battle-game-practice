import time
import random
import colorama
import Monster_Drop_Table
import items_and_item_behaviors


# Base class for defining common combat attributes for players
class Player_combat_interface:
    def __init__(self):
        self.hp = None  # Health Points
        self.attack_damage = None  # Damage for each attack
        self.attack_speed = None  # Attack speed (not used in code)


# Class for the player character
class Player(Player_combat_interface):
    def __init__(self):
        super().__init__()
        self.Player_hp()  # Initialize player's health
        self.Player_damage()  # Initialize player's attack damage
        self.Player_attack_speed()  # Initialize player's attack speed

    def Player_hp(self):
        self.hp = 10  # Set player's initial health points

    def Player_damage(self):
        self.attack_damage = 1  # Set player's initial attack damage

    def Player_attack_speed(self):
        self.attack_speed = 1  # Set player's initial attack speed

    # Calculate chance to deflect an attack and either reduce or increase HP accordingly
    def deflect_attack(self, goblin_attack):
        if goblin_attack == True:
            pass

        else:
            pass

    # Handle player's attack on the NPC, reducing NPC's health
    def Player_attack(self, goblin_class):
        while True:
            Deflect_chance = random.randint(0, 99)  # Generate random chance
            if Deflect_chance > 24.05:
                Opponent_hp = goblin_class.hp - self.attack_damage
                goblin_class.hp = Opponent_hp
                return True

            else:
                return False


# Class to manage player's inventory
class Player_inventory_interface:
    def __init__(self):
        self.inventory = None

    # Initialize player's inventory with two empty slots
    def player_inventory(self):
        self.inventory = {"Inventory slot 1": "Empty", "Inventory slot 2": "Empty"}

    # Print content of the first inventory slot
    def print_inventory(self):
        print(self.inventory["Inventory slot 1"])

    # Handle item pickup after victory against a goblin
    def pickup_item_on_victory(self, goblin_is_alive):
        if not goblin_is_alive:
            pass

    # Nested class for worn equipment
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


# Base class for defining common combat attributes for NPCs
class NPC_combat_interface:
    def __init__(self):
        self.hp = None  # Health Points
        self.attack_damage = None  # Damage for each attack
        self.attack_speed = None  # Attack speed (not used in code)


# Class for the goblin NPC
class goblin_class(NPC_combat_interface):
    def __init__(self):
        super().__init__()
        self.goblin_hp()  # Initialize goblin's health
        self.goblin_attack_speed()  # Initialize goblin's attack speed
        self.goblin_attack_damage()  # Initialize goblin's attack damage
        self.goblin_is_alive()  # Check if goblin is alive

    # Handle goblin's attack on the player, reducing player's health
    def goblin_attack(self, Player_player):
        while True:
            Deflect_chance = random.randint(0, 99)  # Generate random chance
            if Deflect_chance > 24:
                Opponent_hp = Player_player.hp - self.attack_damage
                Player_player.hp = Opponent_hp
                return True

            else:
                return False


    def deflect_attack(self, Player_attack):
        if Player_attack == True:
            pass
        else:
            pass

    def goblin_hp(self):
        self.hp = 10  # Set goblin's initial health points

    def goblin_attack_damage(self):
        self.attack_damage = 1  # Set goblin's initial attack damage

    def goblin_attack_speed(self):
        self.attack_speed = 1  # Set goblin's initial attack speed

    # Calculate chance to deflect an attack and either reduce or increase HP accordingly

    # Check if goblin is alive based on HP
    def goblin_is_alive(self):
        if self.hp <= 0:
            goblin_is_alive = False
            return goblin_is_alive


# Function to manage the battle sequence
def Battle():
    # Battle loop, continues until one opponent is defeated
    while True:
        # Randomly choose who attacks first
        first_attack = random.choice(['Player', 'Goblin'])

        if first_attack == 'Player':
            Player_player.Player_attack(Computer_player)  # Player's attack on Goblin
            if Computer_player.hp <= 0:
                return 1
            Computer_player.goblin_attack(Player_player)
            if Player_player.hp <= 0:
                return 2
        else:
            Computer_player.goblin_attack(Player_player)
            if Player_player.hp <= 0:
                return 2
            Player_player.Player_attack(Computer_player)  # Player's attack on Goblin
            if Computer_player.hp <= 0:
                return 1


Player_player_wins = 0
NPC_wins = 0

# Main loop to run the battle; change the integer in the range function for the number of battles
for i in range(10000):
    Computer_player = goblin_class()
    Player_player = Player()
    result = Battle()

    # Increment win counters based on battle result
    if result == 1:
        Player_player_wins += 1
    elif result == 2:
        NPC_wins += 1

# Print final battle results
print(colorama.Fore.LIGHTYELLOW_EX)
print(f"Player 1 wins: {Player_player_wins}")
print(f"NPC wins: {NPC_wins}\n")
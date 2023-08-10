import time
import random
import colorama
import Monster_Drop_Table


# Base class for defining common combat attributes for players
class Player_combat_interface:
    def __init__(self):
        self.hp = None              # Health Points
        self.attack_damage = None   # Damage for each attack
        self.attack_speed = None    # Attack speed (not used in code)


# Class for the player character
class Player(Player_combat_interface):
    def __init__(self):
        super().__init__()
        self.Player_hp()            # Initialize player's health
        self.Player_damage()        # Initialize player's attack damage
        self.Player_attack_speed()  # Initialize player's attack speed

    def Player_hp(self):
        self.hp = 1  # Set player's initial health points

    def Player_damage(self):
        self.attack_damage = 1  # Set player's initial attack damage

    def Player_attack_speed(self):
        self.attack_speed = 1  # Set player's initial attack speed

    # Calculate chance to deflect an attack and either reduce or increase HP accordingly
    def Player_Deflect_chance(self):
        Deflect_chance = random.randint(0, 99)  # Generate random chance
        if Deflect_chance > 24:
            print(f"{Deflect_chance + 1} percent.")
            print("The next attack will do damage to the Player.")
            print("----------\n")
            time.sleep(1.5)
        else:
            self.hp += 1  # Increase player's health if deflected, since no proper deflect method is implemented
            print(f"{Deflect_chance + 1} percent.")
            print("Deflected, the next attack will do no damage to the Player.")
            print("----------\n")
            time.sleep(1.5)

    # Handle player's attack on the NPC, reducing NPC's health
    def Player_attack(self, goblin_class):
        Opponent_hp = goblin_class.hp - self.attack_damage
        goblin_class.hp = Opponent_hp
        print(f"Player has done {self.attack_damage} damage to their opponent.\n")
        time.sleep(1)

# Class to manage player's inventory
class Player_inventory_interface:
    def __init__(self):
        self.inventory = None

    # Initialize player's inventory with two empty slots
    def player_inventory(self):
        self.inventory = {'Inventory slot 1': 'Empty', 'Inventory slot 2': 'Empty'}

    # Print content of the first inventory slot
    def print_inventory(self):
        print(self.inventory['Inventory slot 1'])

    # Handle item pickup after victory against a goblin
    def pickup_item_on_victory(self, goblin_is_alive):
        if not goblin_is_alive:
            pickup = input("Would you like to pickup the dropped items?\n")
            if pickup.lower() == "yes":
                item_to_pickup = goblin_item_drops.always_dropped(goblin_is_alive)
                if item_to_pickup:
                    for key, value in self.inventory.items():
                        if value == "Empty":
                            self.inventory[key] = item_to_pickup
                            print(f"Picked up {item_to_pickup} and added to the {key}.")
                            break
                    else:
                        print("No space in inventory to pick up the item.")
                else:
                    print("No item to pick up.")

    # Nested class for worn equipment
    class Worn_Equipment:
        def __init__(self):
            self.head_slot = None
            # More equipment slots defined here...

# Base class for defining common combat attributes for NPCs
class NPC_combat_interface:
    def __init__(self):
        self.hp = None              # Health Points
        self.attack_damage = None   # Damage for each attack
        self.attack_speed = None    # Attack speed (not used in code)

# Class for the goblin NPC
class goblin_class(NPC_combat_interface):
    def __init__(self):
        super().__init__()
        self.goblin_hp()            # Initialize goblin's health
        self.goblin_attack_speed()  # Initialize goblin's attack speed
        self.goblin_attack_damage() # Initialize goblin's attack damage
        self.goblin_is_alive()      # Check if goblin is alive

    # Handle goblin's attack on the player, reducing player's health
    def goblin_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_damage
        Player.hp = Opponent_hp
        print(f"Goblin has done {self.attack_damage} damage to the Player.\n")
        time.sleep(1)

    def goblin_hp(self):
        self.hp = 1  # Set goblin's initial health points

    def goblin_attack_damage(self):
        self.attack_damage = 1  # Set goblin's initial attack damage

    def goblin_attack_speed(self):
        self.attack_speed = 1  # Set goblin's initial attack speed

    # Calculate chance to deflect an attack and either reduce or increase HP accordingly
    def goblin_Deflect_chance(self):
        while True:
            Deflect_chance = random.randint(0, 99)  # Generate random chance
            if Deflect_chance > 24:
                print(f"{Deflect_chance + 1} percent.")
                print("The next attack will do damage to Goblin.")
                print("----------\n")
                time.sleep(1.5)
                break
            else:
                self.hp += 1  # Increase goblin's health if deflected
                print(f"{Deflect_chance + 1} percent.")
                print("Deflected, the next attack will do no damage to Goblin.")
                print("----------\n")
                time.sleep(1.5)
                break

    # Check if goblin is alive based on HP
    def goblin_is_alive(self):
        if self.hp <= 0:
            goblin_is_alive = False
            return goblin_is_alive


# Function to manage the battle sequence
def Battle():
    # Battle loop, continues until one opponent is defeated
    while True:
        print(colorama.Fore.LIGHTWHITE_EX)
        time.sleep(.4)
        print("Battling...\n")
        Computer_player.goblin_Deflect_chance()  # Goblin's chance to deflect
        Player_player.Player_attack(Computer_player)  # Player's attack on Goblin
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Computer HP: {Computer_player.hp}\n")
        if Computer_player.hp <= 0:
            print("Player has defeated Goblin.\n")
            goblin_is_alive_status = Computer_player.goblin_is_alive()
            goblin_item_drops.always_dropped(goblin_is_alive_status)
            player_inventory.pickup_item_on_victory(goblin_is_alive_status)  # Pick up item if Goblin defeated
            player_inventory.print_inventory()  # Print player's inventory
            return 1
        else:
            pass

        print(colorama.Fore.RED)
        time.sleep(.4)
        print("Battling...\n")
        Player_player.Player_Deflect_chance()  # Player's chance to deflect
        Computer_player.goblin_attack(Player_player)  # Goblin's attack on Player
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Player HP: {Player_player.hp}\n")
        if Player_player.hp <= 0:
            print("NPC has defeated Player.\n")
            return 2
        else:
            pass


# Main loop to run the battle; change the integer in the range function for the number of battles
for i in range(1):
    Player_player_wins = 0
    NPC_wins = 0

# Initialize player inventory, goblin, and player classes

# Create an instance of Player_inventory_interface to manage the player's inventory
player_inventory = Player_inventory_interface()
# Call the player_inventory method to initialize the player's inventory with empty slots
player_inventory.player_inventory()

# Create an instance of the goblin_class to represent the goblin NPC opponent
Computer_player: goblin_class = goblin_class()

# Retrieve the goblin's item drops from the Monster_Drop_Table module
goblin_item_drops = Monster_Drop_Table.goblin_drops()

# Create an instance of the Player class to represent the human player character
Player_player = Player()

# Start the battle sequence by calling the Battle function, and store the result (1 for player win, 2 for NPC win)
result = Battle()

# Increment win counters based on battle result
if result == 1:
    Player_player_wins += 1
else:
    result == 2
    NPC_wins += 1

# Print final battle results
print(colorama.Fore.LIGHTYELLOW_EX)
print(f"Player 1 wins: {Player_player_wins}")
print(f"NPC wins: {NPC_wins}\n")

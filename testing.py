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
        self.hp = 10  # Player's health points

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
    def Player_attack(self, NPC_class):
        Opponent_hp = NPC_class.hp - self.attack_damage
        NPC_class.hp = Opponent_hp
        print(f"Player has done {self.attack_damage} damage to their opponent.\n")
        time.sleep(1)

    # subclass class for defining player inventory system
    class Player_inventory_interface:
        def __init__(self):
            self.inventory_slot_one = None
            self.inventory_slot_two = None
            self.inventory_slot_three = None
            self.inventory_slot_four = None
            self.inventory_slot_five = None
            self.inventory_slot_six = None
            self.inventory_slot_seven = None
            self.inventory_slot_eight = None
            self.inventory_slot_nine = None
            self.inventory_slot_ten = None

        def inventory_slot_1(self):
            pass

        def inventory_slot_2(self):
            pass

        def inventory_slot_3(self):
            pass

        def inventory_slot_4(self):
            pass

        def inventory_slot_5(self):
            pass

        def inventory_slot_6(self):
            pass

        def inventory_slot_7(self):
            pass

        def inventory_slot_8(self):
            pass

        def inventory_slot_9(self):
            pass

        def inventory_slot_10(self):
            pass


# Base class for defining common combat attributes for NPCs
class NPC_combat_interface:
    def __init__(self):
        self.hp = None
        self.attack_damage = None
        self.attack_speed = None

# Class to define the attributes and methods of the NPC
class NPC_class(NPC_combat_interface):
    # Initialization and defining attributes
    def __init__(self):
        super().__init__()
        self.NPC_hp()
        self.NPC_attack_speed()
        self.NPC_attack_damage()
        self.NPC_Deflect_chance()

    # Method to handle NPC's attack on the player
    def NPC_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_damage
        Player.hp = Opponent_hp
        print(f"NPC has done {self.attack_damage} damage to the Player.\n")
        time.sleep(1)

    def NPC_hp(self):
        self.hp = 10  # NPC's health points

    def NPC_attack_damage(self):
        self.attack_damage = 1  # NPC's attack damage

    def NPC_attack_speed(self):
        self.attack_speed = 1  # NPC's attack speed

    # Method to calculate the chance of deflecting an attack by NPC
    def NPC_Deflect_chance(self):
        while True:
            Deflect_chance = random.randint(0, 99)
            if Deflect_chance > 24:
                print(f"{Deflect_chance + 1} percent.")
                print("The next attack will do damage to NPC.")
                print("----------\n")
                time.sleep(1.5)
                break
            else:
                self.hp += 1  # Increase NPC's health if deflected
                print(f"{Deflect_chance + 1} percent.")
                print("Deflected, the next attack will do no damage to NPC.")
                print("----------\n")
                time.sleep(1.5)
                break

# Function to handle the battle sequence
def Battle():
    # Battle loop
    while True:
        print(colorama.Fore.LIGHTWHITE_EX)
        time.sleep(.4)
        print("Battling...\n")
        Computer_player.NPC_Deflect_chance()
        Player_player.Player_attack(Computer_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Computer HP: {Computer_player.hp}\n")
        if Computer_player.hp <= 0:
            print("Player has defeated NPC.\n")
            return 1

        time.sleep(.4)
        print(colorama.Fore.RED)
        print("Battling...\n")
        Player_player.Player_Deflect_chance()
        Computer_player.NPC_attack(Player_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Player HP: {Player_player.hp}\n")
        if Player_player.hp <= 0:
            print("NPC has defeated Player.\n")
            return 2

# Main loop to run the battle; change the integer in the range function for the amount of loops.
for i in range(1):

    Player_player_wins = 0
    NPC_wins = 0

    Computer_player = NPC_class()
    Player_player = Player()
    result = Battle()

    if result == 1:
        Player_player_wins += 1
    else:
        result == 2
        NPC_wins += 1

print(f"Player 1 wins: {Player_player_wins}")
print(f"NPC wins: {NPC_wins}")

import time
import random
import colorama



class Player_combat_interface:
    def __init__(self):
class Player:
    def __init__(self):
        self.hp = None
        self.attack_damage = None
        self.attack_speed = None
        self.Player_hp()
        self.Player_damage()
        self.Player_attack_speed()

    def Player_hp(self):
        self.hp = 10

    def Player_damage(self):
        self.attack_damage = 1

    def Player_attack_speed(self):
        self.attack_speed = 1

    def Player_Deflect_chance(self):
        Deflect_chance = random.randint(0, 99)
        if Deflect_chance > 24:
            print(f"{Deflect_chance + 1} percent.")
            print("The next attack will do damage to the Player.")
            print("----------\n")
            time.sleep(1.5)

        else:
            self.hp += 1
            print(f"{Deflect_chance + 1} percent.")
            print("Deflected, the next attack will do no damage to the Player.")
            print("----------\n")
            time.sleep(1.5)

    def Player_attack(self, Computer):
        Opponent_hp = Computer.hp - self.attack_damage
        Computer.hp = Opponent_hp
        print(f"Player has done {self.attack_damage} damage to their opponent.\n")
        time.sleep(1)

    def Incoming_damage(self):
        Incoming_damage = None

class NPC_combat_interface:
    def __init__(self):
        self.hp = None
        self.attack_damage = None
        self.attack_speed = None


class NPC_class(NPC_combat_interface):
    def __init__(self):
        super().__init__()
        self.NPC_hp()
        self.NPC_attack_speed()
        self.NPC_attack_damage()
        self.NPC_Deflect_chance()

    def NPC_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_damage
        Player.hp = Opponent_hp
        print(f"NPC has done {self.attack_damage} damage to the Player.\n")
        time.sleep(1)

    def NPC_hp(self):
        self.hp = 10

    def NPC_attack_damage(self):
        self.attack_damage = 1
    def NPC_attack_speed(self):
        self.attack_speed = 1

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
                self.hp += 1
                print(f"{Deflect_chance + 1} percent.")
                print("Deflected, the next attack will do no damage to NPC.")
                print("----------\n")
                time.sleep(1.5)
                break

def Battle():
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
            break

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
            break

    time.sleep(3)


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


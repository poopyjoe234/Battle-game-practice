import random
import colorama

class Player:
    def __init__(self):
        self.hp = 10
        self.attack_dmg = 1
        self.attack_speed = 1

    def Player_Deflect_chance(self):
        Deflect_chance = random.randint(0, 99)
        if Deflect_chance > 24:
            print(f"{Deflect_chance + 1} percent.")
            print("The next attack will do damage to Player.")
            print("----------\n")

        else:
            self.hp += 1
            print(f"{Deflect_chance + 1} percent.")
            print("Deflected, the next attack will do no damage to Player.")
            print("----------\n")

    def Player_attack(self, Computer):
        Opponent_hp = Computer.hp - self.attack_dmg
        Computer.hp = Opponent_hp
        print(f"Player has done {self.attack_dmg} damage to their opponent.\n")


class Computer:
    def __init__(self):
        self.hp = 10
        self.attack_dmg = 1
        self.attack_speed = 1

    def Computer_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_dmg
        Player.hp = Opponent_hp
        print(f"Computer has done {self.attack_dmg} damage to their opponent.\n")

    def Computer_Deflect_chance(self):
        while True:
            Deflect_chance = random.randint(0, 99)
            if Deflect_chance > 27:
                print(f"{Deflect_chance + 1} percent.")
                print("The next attack will do damage to Computer.")
                print("----------\n")
                break

            else:
                self.hp += 1
                print(f"{Deflect_chance + 1} percent.")
                print("Deflected, the next attack will do no damage to Computer.")
                print("----------\n")
                break

def Battle():
    while True:
        print(colorama.Fore.LIGHTWHITE_EX)
        print("Battling...\n")
        Computer_player.Computer_Deflect_chance()
        Player_player.Player_attack(Computer_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Computer HP: {Computer_player.hp}\n")
        if Computer_player.hp <= 0:
            print("Player has defeated Computer.\n")
            return 1

        print(colorama.Fore.RED)
        print("Battling...\n")
        Player_player.Player_Deflect_chance()
        Computer_player.Computer_attack(Player_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Player HP: {Player_player.hp}\n")
        if Player_player.hp <= 0:
            print("Computer has defeated Player.\n")
            return 2

Player_player_wins = 0
Computer_player_wins = 0

for i in range(10):
    Computer_player = Computer()
    Player_player = Player()
    result = Battle()

    if result == 1:
        Player_player_wins += 1
    elif result == 2:
        Computer_player_wins += 1

print(f"Player wins: {Player_player_wins}")
print(f"Computer wins: {Computer_player_wins}")

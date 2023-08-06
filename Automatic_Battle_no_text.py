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
            return "The next attack will do damage to Player."
        else:
            self.hp += 1
            return "Deflected, the next attack will do no damage to Player."

    def Player_attack(self, Computer):
        Opponent_hp = Computer.hp - self.attack_dmg
        Computer.hp = Opponent_hp


class Computer:
    def __init__(self):
        self.hp = 10
        self.attack_dmg = 1
        self.attack_speed = 1

    def Computer_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_dmg
        Player.hp = Opponent_hp

    def Computer_Deflect_chance(self):
        while True:
            Deflect_chance = random.randint(0, 99)
            if Deflect_chance > 27:
                return "The next attack will do damage to Computer."
                break
            else:
                self.hp += 1
                return "Deflected, the next attack will do no damage to Computer."
                break

def Battle():
    while True:
        Computer_player.Computer_Deflect_chance()
        Player_player.Player_attack(Computer_player)
        if Computer_player.hp <= 0:
            return 1

        Player_player.Player_Deflect_chance()
        Computer_player.Computer_attack(Player_player)
        if Player_player.hp <= 0:
            return 2

Player_player_wins = 0
Computer_player_wins = 0

for i in range():
    Computer_player = Computer()
    Player_player = Player()
    result = Battle()

    if result == 1:
        Player_player_wins += 1
    elif result == 2:
        Computer_player_wins += 1

print(f"Player wins: {Player_player_wins}")
print(f"Computer wins: {Computer_player_wins}")

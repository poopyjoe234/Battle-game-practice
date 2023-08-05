import time
import random
import colorama


class Player:
    def __init__(self):
        self.hp = None
        self.dmg = None
        self.attack_speed = None
        self.Player_hp()
        self.Player_dmg()
        self.Player_attack_speed()

    def Player_hp(self):
        self.hp = 10

    def Player_dmg(self):
        self.attack_dmg = 1

    def Player_attack_speed(self):
        self.attack_speed = 1

    def Player_Deflect_chance(self):
        Deflect_chance = random.randint(0, 99)
        if Deflect_chance > 25:
            print(f"{Deflect_chance} percent.")
            print("The next attack will do damage to Player.")
            print("----------\n")
            time.sleep(1.5)

        else:
            self.hp += 1
            print(f"{Deflect_chance} percent.")
            print("Deflected, the next attack will do no damage to Player.")
            print("----------\n")
            time.sleep(1.5)

    def Player_attack(self, Computer):
        Opponent_hp = Computer.hp - self.attack_dmg
        Computer.hp = Opponent_hp
        print(f"Player has done {self.attack_dmg} damage to their opponent.\n")
        time.sleep(1)


class Computer:
    def __init__(self):
        self.hp = None
        self.attack_dmg = None
        self.attack_speed = None
        self.Computer_hp()
        self.Computer_dmg()
        self.Computer_attack_speed()

    def Computer_hp(self):
        self.hp = 10

    def Computer_dmg(self):
        self.attack_dmg = 1

    def Computer_attack_speed(self):
        self.attack_speed = 1

    def Computer_attack(self, Player):
        Opponent_hp = Player.hp - self.attack_dmg
        Player.hp = Opponent_hp
        print(f"Computer has done {self.attack_dmg} damage to their opponent.\n")
        time.sleep(1)

    def Computer_Deflect_chance(self):
        while True:

            Deflect_chance = random.randint(0, 99)
            if Deflect_chance > 25:
                print(f"{Deflect_chance} percent.")
                print("The next attack will do damage to Computer.")
                print("----------\n")
                time.sleep(1.5)
                break

            else:
                self.hp += 1
                print(f"{Deflect_chance} percent.")
                print("Deflected, the next attack will do no damage to Computer.")
                print("----------\n")
                time.sleep(1.5)
                break


# determine if the attack is blocked before the attack
Computer_player = Computer()
Player_player = Player()


def Battle():
    while True:
        print(colorama.Fore.LIGHTWHITE_EX)
        time.sleep(.4)
        print("Battling...\n")
        Computer_player.Computer_Deflect_chance()
        Player_player.Player_attack(Computer_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Computer HP: {Computer_player.hp}\n")
        if Computer_player.hp <= 0:
            print("Player has defeated Computer.\n")
            break

        time.sleep(.4)
        print(colorama.Fore.RED)
        print("Battling...\n")
        Player_player.Player_Deflect_chance()
        Computer_player.Computer_attack(Player_player)
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f"Player HP: {Player_player.hp}\n")
        if Player_player.hp <= 0:
            print("Computer has defeated Player.\n")
            break

    time.sleep(3)



Battle()

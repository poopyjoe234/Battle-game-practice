import time
import random
import colorama
import threading

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
"""
#to check if enemies are alive
print(Goblin.goblin_is_alive(enemies[0]))
print(GiantRat.giant_rat_is_alive(enemies[1]))
print(Guard.guard_is_alive(enemies[2])) 
"""


class Player:
    def __init__(self):
        self.hp = 10
        self.damage = 1

    def player_attack_enemies(self):

        incoming_damage = self.damage
        deflect_chance = random.randint(0, 99)

        if deflect_chance <= 24:
            print("deflect chance =", deflect_chance, "percent")
            print("Enemy has deflected the attack. (deflect chance =", deflect_chance, "percent)")
        else:
            enemies[0].hp -= incoming_damage
            enemies[1].hp -= incoming_damage
            enemies[2].hp -= incoming_damage
            print("full damage inflicted")

    def Player_is_alive(self):
        if self.hp >= 1:
            player_is_alive = True
            return player_is_alive
        else:
            player_is_alive = False
            return player_is_alive


class Goblin:  # 0 in the tuple
    def __init__(self):
        self.hp = 1
        self.damage = 1

    def is_alive(self):
        if self.hp >= 1:
            is_alive = True
            return is_alive
        else:
            is_alive = False
            return is_alive


class GiantRat:  # 1 in the tuple
    def __init__(self):
        self.hp = 1
        self.damage = 1

    def is_alive(self):
        if self.hp >= 1:
            is_alive = True
            return is_alive
        else:
            is_alive = False
            return is_alive


class Guard:  # 2 in the tuple
    def __init__(self):
        self.hp = 10
        self.damage = 1

    def is_alive(self):
        if self.hp >= 1:
            is_alive = True
            return is_alive
        else:
            is_alive = False
            return is_alive


def enemy_attack_player():
    incoming_damage = enemies[0].damage
    deflect_chance = random.randint(0, 99)

    if deflect_chance <= 24:
        print("deflect chance =", deflect_chance, "percent")
        print("Player has deflected the enemy attack. (deflect chance =", deflect_chance, "percent)")
    else:
        player.hp -= incoming_damage
        print("full damage inflicted")


############
############
############
############


player = Player()
enemies = (Goblin(), GiantRat(), Guard())

while True:
    if player.Player_is_alive() == False:
        exit()

    for index, enemy in enumerate(enemies):
        if not enemies[index].is_alive():
            print(f"Player has defeated {enemy}")
            exit()

    else:
        player.player_attack_enemies()
        print(enemies[0].hp, enemies[1].hp, enemies[2].hp)
        time.sleep(1.25)
        enemy_attack_player()
        print(player.hp)
        time.sleep(1.25)

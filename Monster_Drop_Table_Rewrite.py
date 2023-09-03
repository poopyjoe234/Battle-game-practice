import random

import items_and_item_behaviors


""" Drop rates """


def drop_roll():
    roll = random.randint(0,100)
    return roll


def bones_odds():
    print("bones are dropped.")
    return "drop"


def bronze_sword():
    roll = drop_roll()
    if int(roll) <= 15:
        print(roll)
        print("sword is dropped.")
        return "drop"
    else:
        return "not dropped"


def bronze_dagger_odds():
    roll = drop_roll()
    if int(roll) <= 39:
        print(roll)
        print("dagger is dropped.")
        return "drop"
    else:
        return "not dropped"


def bronze_kite_shield():
    roll = drop_roll()
    if int(roll) <= 15:
        print(roll)
        print("kite shield is dropped.")
        return "drop"
    else:
        return "not dropped"


def bronze_square_shield():
    roll = drop_roll()
    if int(roll) <= 39:
        print(roll)
        print("square shield is dropped.")
        return "drop"
    else:
        return "not dropped"


"""
GOBLIN DROP TABLE
"""
Bones_goblin = items_and_item_behaviors.Bones()
Bronze_Dagger_goblin = items_and_item_behaviors.Weapon.bronze_dagger()
Bronze_Sword_goblin = items_and_item_behaviors.Weapon.bronze_sword()
Bronze_Square_Shield_goblin = items_and_item_behaviors.Shield.bronze_square_shield()
Bronze_Kite_Shield_goblin = items_and_item_behaviors.Shield.bronze_kite_shield()

"""
GIANT RAT DROP TABLE
"""
Bones_rat = items_and_item_behaviors.Bones()
Bronze_Square_Shield_rat = items_and_item_behaviors.Shield.bronze_square_shield()


"""
GUARD DROP TABLE
"""

Bones_guard = items_and_item_behaviors.Bones()
Bronze_Kite_Shield_guard = items_and_item_behaviors.Shield.bronze_kite_shield()
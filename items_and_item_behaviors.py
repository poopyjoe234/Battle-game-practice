

"""
#format for adding items and the super class.

class (ITEM NAME)(Items):
    def __init__(self):
        super().__init__(
            name="ITEM NAME",
            examine_description="ITEM DESCRIPTION",
"""

class Items:
    def __init__(self, name, examine_description):
        self.name = name
        self.examine_description = examine_description

    def __str__(self):
        return self.name

    def drop(self):
        print(f"You have dropped the {self.name} from your inventory.")


class Bones(Items):
    def __init__(self):
        super().__init__(
            name="Bones",
            examine_description="Bones from an enemy. If they were yours, you would be dead.",
        )

    def examine(self):
        while True:
            examine_item = input("enter //examine bones\n")
            if examine_item == f"//examine {self.name.lower()}":
                print(f"Item: {self.name}\nDescription: {self.examine_description}")
                break
            else:
                pass


goblin_always_dropped = Bones()


class Helmet(Items):
    pass


class Cape(Items):
    pass


class NeckArmour(Items):
    pass


class Ammo(Items):
    pass


class Weapon(Items):
    def __init__(self, name, examine_description, damage, weapon_type, accuracy):
        super().__init__(name, examine_description)
        self.damage = damage
        self.weapon_type = weapon_type
        self.accuracy = accuracy

    def bronze_dagger(self):
        self.name = "Bronze Dagger"
        self.examine_description = "A dagger made of bronze."
        self.damage = 1
        self.weapon_type = Weapon
        self.accuracy = None

    def bronze_sword(self):
        self.name = "Bronze Sword"
        self.examine_description = "A short sword made of bronze."
        self.damage = 2
        self.accuracy = None


weapons = Weapon.bronze_dagger()


class Shield(Items):
    def __init__(self, name, examine_description, armour_type, deflection_chance, drop_chance):
        super().__init__(name, examine_description)
        self.name = name
        self.examine_description = examine_description
        self.armour_type = armour_type
        self.deflection_chance = deflection_chance
        self.drop_chance = drop_chance

    def bronze_square_shield(self):
        self.name = "Bronze Square shield"
        self.examine_description = "A square shield made of bronze, it helps block enemy attacks."
        self.armour_type = Shield
        self.deflection_chance = 1.

    def bronze_kite_shield(self):
        self.name = "Bronze Square shield"
        self.examine_description = "A square shield made of bronze, it helps block enemy attacks."
        self.armour_type = Shield
        self.deflection_chance = 2



class BodyArmour(Items):
    pass


class LegArmour(Items):
    pass


class Hands(Items):
    pass


class Feet(Items):
    pass


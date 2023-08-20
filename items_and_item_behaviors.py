

"""
#format for adding items (similar to bones) and the super class.

class (ITEM NAME)(Items):
    def __init__(self):
        super().__init__(
            name="ITEM NAME",
            examine_description="ITEM DESCRIPTION",
"""
"""
To add items to a class:

@classmethod
    def NAME_OF_ITEM(cls):
        name = "Item name"
        examine_description = "examine description"
        damage = damage the item does
        weapon_type = cls (this will be the same as the parent class)
        accuracy = (item accuracy)
        return cls(name, examine_description, damage, weapon_type, accuracy) #add any other args here
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


class Helmet(Items):
    def __str__(self):
        return self.name
    pass


class Cape(Items):
    def __str__(self):
        return self.name
    pass


class NeckArmour(Items):
    def __str__(self):
        return self.name
    pass


class Ammo(Items):
    def __str__(self):
        return self.name
    pass


class Weapon(Items):
    def __init__(self, name, examine_description, damage, weapon_type, accuracy):
        super().__init__(name, examine_description)
        self.damage = damage
        self.weapon_type = weapon_type
        self.accuracy = accuracy

    def __str__(self):
        return self.name

    @classmethod
    def bronze_dagger(cls):
        name = "Bronze Dagger"
        examine_description = "A dagger made of bronze."
        damage = 1
        weapon_type = "Weapon"
        accuracy = None
        return cls(name, examine_description, damage, weapon_type, accuracy)

    @classmethod
    def bronze_sword(cls):
        name = "Bronze Sword"
        examine_description = "A short sword made of bronze."
        damage = 2
        weapon_type = "Weapon"
        accuracy = None
        return cls(name, examine_description, damage, weapon_type, accuracy)


class Shield(Items):
    def __init__(self, name, examine_description, armour_type, deflection_chance, drop_chance):
        super().__init__(name, examine_description)
        self.name = name
        self.examine_description = examine_description
        self.armour_type = armour_type
        self.deflection_chance = deflection_chance
        self.drop_chance = drop_chance

    def __str__(self):
        return self.name

    @classmethod
    def bronze_square_shield(cls):
        name = "Bronze Square shield"
        examine_description = "A square shield made of bronze, it helps block enemy attacks."
        armour_type = "Shield"
        deflection_chance = 2
        drop_chance = None
        return cls(name, examine_description, armour_type, deflection_chance, drop_chance)

    @classmethod
    def bronze_kite_shield(cls):
        name = "Bronze Kite shield"
        examine_description = "A Kite shield made of bronze, it helps block enemy attacks better than a square shield."
        armour_type = "Shield"
        deflection_chance = 4
        drop_chance = None
        return cls(name, examine_description, armour_type, deflection_chance, drop_chance)


class BodyArmour(Items):
    def __str__(self):
        return self.name
    pass


class LegArmour(Items):
    def __str__(self):
        return self.name
    pass


class Hands(Items):
    def __str__(self):
        return self.name
    pass


class Feet(Items):
    def __str__(self):
        return self.name
    pass

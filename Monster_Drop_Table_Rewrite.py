class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        pass

    def examine(self):
        print(self.description)

    def drop(self):
        print(f"You've dropped {self.name}")

class Bones(Item):
    def __init__(self):
        super().__init__(name="Bones", description="Bones from an enemy.")

    def bury(self):
        print("You bury the bones")


drop = Bones()

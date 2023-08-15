class items:
    def __init__(self, name, examine_description):
        self.name = name.lower()
        self.examine_description = examine_description

    # def examine(self):
    #     while True:
    #         examine_item = input("input\n")
    #         if examine_item == f"//examine {self.name}":
    #             print(f"Item: {self.name}\nDescription: {self.examine_description}")
    #             break

    def drop(self):
        print(f"You have dropped the {self.name} from your inventory.")


class Bones(items):
    def __init__(self):
        super().__init__(
            name="Bones",
            examine_description="Bones from an enemy. If they were yours, you would be dead.",
        )

    def examine(self):
        # while True:
        examine_item = input("enter //examine bones\n")
        if examine_item == f"//examine {self.name}":
            print(f"Item: {self.name}\nDescription: {self.examine_description}")
            # break
        else:
            pass


goblin_always_dropped = Bones()
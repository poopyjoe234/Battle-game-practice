import colorama


class goblin_drops:
    def __init__(self):
        self.always_dropped = None

    def always_dropped(self):
        always_dropped = "Bones"
        print(colorama.Fore.GREEN)
        print(f"Goblin dropped {always_dropped}\n")
        print(colorama.Fore.RESET)
        return always_dropped

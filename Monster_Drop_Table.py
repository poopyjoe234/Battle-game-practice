import colorama



class goblin_drops:
    def __init__(self):
        self.always_dropped = None

    def always_dropped(self, goblin_is_alive):
        print(colorama.Fore.LIGHTGREEN_EX)
        always_dropped = "Bones"
        if not goblin_is_alive:
            print(f"Goblin has dropped {always_dropped}.")
            enemy_always_dropped = True
            print(colorama.Fore.RESET)
            return enemy_always_dropped

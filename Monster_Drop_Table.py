import colorama



class goblin_drops:
    def always_dropped(self, goblin_is_alive):
        print(colorama.Fore.LIGHTGREEN_EX)
        always_dropped_item = "Bones"
        if not goblin_is_alive:
            print(f"Goblin has dropped {always_dropped_item}.")
            print(colorama.Fore.RESET)
            return always_dropped_item

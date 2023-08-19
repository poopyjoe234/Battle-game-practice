import colorama
import items_and_item_behaviors


class goblin_drops:
    def always_dropped(self, goblin_is_alive):
        print(colorama.Fore.GREEN)
        always_dropped_item = items_and_item_behaviors.goblin_always_dropped.name
        if not goblin_is_alive:
            print(f"Goblin has dropped {always_dropped_item}.")
            print(colorama.Fore.RESET)
            return always_dropped_item


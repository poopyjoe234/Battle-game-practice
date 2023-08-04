from osrsbox.items_api.all_items import AllItems

def display_item_by_id(item_id: int, all_items: AllItems):
    try:
        # Look up the item by ID
        item = all_items.lookup_by_item_id(item_id)

        # Display the item name and ID
        print(f"Name: {item.name}")
        print(f"ID: {item.id}")
        print("------------")
        print("Equipment Stats:")

        # Check if the item is equipable, and if so, display the equipment stats
        if item.equipable_by_player:
            equipment = item.equipment
            print(f"attack_stab: {equipment.attack_stab}")
            print(f"attack_slash: {equipment.attack_slash}")
            print(f"attack_crush: {equipment.attack_crush}")
            print(f"attack_magic: {equipment.attack_magic}")
            print(f"attack_ranged: {equipment.attack_ranged}")
            print(f"defence_stab: {equipment.defence_stab}")
            print(f"defence_slash: {equipment.defence_slash}")
            print(f"defence_crush: {equipment.defence_crush}")
            print(f"defence_magic: {equipment.defence_magic}")
            print(f"defence_ranged: {equipment.defence_ranged}")
            print(f"melee_strength: {equipment.melee_strength}")
            print(f"ranged_strength: {equipment.ranged_strength}")
            print(f"magic_damage: {equipment.magic_damage}")
            print(f"prayer: {equipment.prayer}")
            print(f"slot: {equipment.slot}")
            print("requirements:", end=" ")
            for skill, level in equipment.requirements.items():
                print(f"{skill}: {level}", end=" ")
            print()  # Newline after requirements
        else:
            print("This item is not equipable.")

        # Check if the item is an equipable weapon, and if so, display the attack speed
        if item.equipable_weapon:
            weapon = item.weapon
            print(f"Attack Speed: {weapon.attack_speed}")
    except KeyError:
        print(f"Item with ID {item_id} not found.")

# Load all items
all_items = AllItems()

# Define a list of item IDs you want to search for
item_ids_to_search = [1075, 1087, 1103, 1117, 1139, 1155, 1173, 1189, 8844, 7454, 1277, 1291, 1205, 1321, 3095, 1237]

# Display the item details for each item ID in the list
for item_id in item_ids_to_search:
    display_item_by_id(item_id, all_items)
    print("\n\n")  # Print two newline characters between each item







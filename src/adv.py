from room import Room
from player import Player
from item import Item
import random
import textwrap
import pdb
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

rooms = list(room.keys())


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def print_error():
    print("\n \n Illegal Move! Room doesn't exist. Try again. \n \n")

items = [Item("sword"), Item("axe"), Item("coins"), Item("ladder"), Item("emerald"), Item("ruby"), Item("bow"), Item("book")]
player_items = random.sample(items, 2)
p = Player(room['outside'], player_items)
items = list(set(items).difference(set(player_items)))


while items:
    item = random.choice(items)
    random_room = room[random.choice(rooms)]
    items.remove(item)
    random_room.add(item)



while True:
    print(p.current_room)
    user_input = input("What direction do you want to go? ")

    if len(user_input.split(' ')) > 1:
        user_input_list = user_input.split(' ')
        command = user_input_list[0]
        item = user_input_list[1].lower()
        if command == "take" or command == "get":
            p.take(item)
        elif command == "drop":
            p.drop(item)

    user_input = user_input.lower()[0]
    direction = f'{user_input}_to'
    if user_input == 'q':
        break
    elif user_input == 'n' and hasattr(p.current_room, direction):
        p.current_room = p.current_room.n_to
    elif user_input == 's' and hasattr(p.current_room, direction):
        p.current_room = p.current_room.s_to
    elif user_input == 'e' and hasattr(p.current_room, direction):
        p.current_room = p.current_room.e_to
    elif user_input == 'w' and hasattr(p.current_room, direction):
        p.current_room = p.current_room.w_to
    elif user_input == 'i' or user_input == 'inventory':
        if p.items: item_names = [p.item.name for p.item in p.items]
        if p.items: print(f" \n {', '.join(item_names)} \n")
    elif user_input == 't' or user_input == 'g' or user_input == 'd':
        pass
    else:
        print_error()

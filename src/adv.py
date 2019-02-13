from room import Room
from player import Player
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
p = Player('outside', room['outside'])

def print_error():
    print("Illegal Move! Room doesn't exist. Try again.")


def print_current_room():
    print(p.current_room.name)
    wrapped_lines = textwrap.wrap(p.current_room.description)
    for line in wrapped_lines:
        print(line)


while True:
    user_input = input("What direction do you want to go? ")
    if user_input == 'n' or user_input == 's' or user_input == 'w' or user_input == 'e':
        print_current_room()
    if user_input == 'q':
        i = 0
        break
    elif user_input == 'n':
        p.current_room = room[p.place].n_to
        p.place = [k for k,v in room.items() if v == room[p.place].n_to][0]
    elif user_input == 's':
        p.current_room = room[p.place].s_to
        p.place = [k for k,v in room.items() if v == room[p.place].s_to][0]
    elif user_input == 'e':
        p.current_room = room[p.place].e_to
        p.place = [k for k,v in room.items() if v == room[p.place].e_to][0]
    elif user_input == 'w':
        p.current_room = room[p.place].w_to
        p.place = [k for k,v in room.items() if v == room[p.place].w_to][0]
    else:
        print_error()

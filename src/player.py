# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, place, current_room):
        self.current_room = current_room
        self.place = place
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, place, current_room, items=[]):
        self.current_room = current_room
        self.place = place
        self.items = items


    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            item.on_drop()
            self.current_room.add(item)
        else:
            print("Player does not have such item")

    def take(self, item):
        self.current_room.remove(item)
        self.items.append(item)
        item.on_take()

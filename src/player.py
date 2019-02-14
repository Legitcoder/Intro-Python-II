# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items


    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            item.on_drop()
            self.current_room.add(item)
        else:
            print(f"Player does not have {item.name}")

    def take(self, item):
        self.current_room.remove(item)
        self.items.append(item)
        item.on_take()

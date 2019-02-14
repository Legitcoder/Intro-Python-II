# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items


    def print_items(self):
        print(self.items)


    def drop(self, item_name):
        try:
            item = [self.item for self.item in self.items if item_name == self.item.name][0]
        except:
            print(f"Player does not have {item_name}")
            return
        self.items.remove(item)
        item.on_drop()
        self.current_room.add(item)


    def take(self, item_name):
        try:
            item = [self.current_room.item for self.current_room.item in self.current_room.items if item_name == self.current_room.item.name][0]
        except:
            print(f"Item {item_name} does not exist in room")
            return
        self.current_room.remove(item)
        self.items.append(item)
        item.on_take()

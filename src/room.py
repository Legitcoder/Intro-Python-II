# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items


    def add(self, item):
        self.items.append(item)


    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Item does not exist in {self.name}")
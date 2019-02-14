# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        item_names = [item.name for item in self.items]
        items_list_str = ', '.join(item_names) if self.items else ""
        return f"{self.name}, {self.description} \n{items_list_str}"

    def add(self, item):
        self.items.append(item)


    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Item does not exist in {self.name}")
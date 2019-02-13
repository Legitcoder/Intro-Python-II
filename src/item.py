class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def on_take(self):
        print(f'{self.name} Taken.')


    def on_drop(self):
        print(f'{self.name} Dropped.')
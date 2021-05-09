class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p
        
class DeskTable(Table):
    def square(self):
        return self.width * self.length
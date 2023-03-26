#challenge
class Shape:
    def __init__(self):
        self.what_am_i()

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l):
        self.length = l
        self.what_am_i()
    
    def calculate_perimeter(self):
        print(2 * (self.length / 2) * 3.14)

class Square(Shape):
    def __init__(self, l):
        self.length = l
        self.what_am_i()

    def calculate_perimeter(self):
        print(2 * (self.length / 2) * 3.14)

    def change_size(self, num):
        self.length -= num
        print(self.length)

r = Rectangle(10)
s = Square(100)

r.calculate_perimeter()
s.calculate_perimeter()
s.change_size(40)
s.what_am_i()

class Horse:
    def __init__(self, weight, height, rider):
        self.weight = weight
        self.height = height
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

man = Rider("satoru")
horse = Horse(300, 200, man)

print(horse.rider.name)

#challenge

class Square:

    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)

    def culc(self, other):
        return self is other

s1 = Square(10, 20)
s2 = Square(40, 80)

print(Square.square_list[0].width)
print(Square.square_list[1].width)

print(s2)

print(s2.culc(s1))
print(s2.culc(s2))

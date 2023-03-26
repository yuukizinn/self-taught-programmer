#Pythonのどのクラスもオブジェクトで、typeクラスのインスタンス
#すべてのクラスはobjectクラスを継承する
#クラスを作るクラスをメタクラスと呼ぶ

#クラス変数とインスタンス変数
class Rectangle:
    recs = [] #クラス変数
    #インスタンスオブジェクトのどこからでもアクセスできる　グローバル変数が不要
    #クラスのインスタンス間でデータを共有できる
    #通常、クラス変数に持たせるのは定数
    
    def __init__(self, w, l):
        self.width = w #インスタンス変数＝インスタンスオブジェクト
        self.length = l
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
r4 = r3

print(r1.recs)
print(r2.recs)
print(r3.recs)
print(Rectangle.recs)


#特殊メソッド
#オブジェクトをprint関数に渡すと、__repr__メソッドを呼び出す
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name #reprをオーバーライド

    def __add__(self, other):
        return self.name + self.name

lion = Lion("Dilbert")
print(lion)
print(lion + r1)
#足し算の式を評価する時、左側のオブジェクトの__add__メソッドを呼び出す
#演算子の右側のオブジェクトをそのメソッドに渡し、メソッドの戻り値を式の評価結果として使う

#isキーワード
#前後のオブジェクトが同一のオブジェクトならTrueを返す

print(r1 is r2)
print(r4 is r3)

#ある変数がNoneかどうかを調べる時にも使う

x = 10
if x is None:
    print("xはNone :( ")
else:
    print("xはNoneじゃない")

x = None
if x is None:
    print("xはNone")
else:
    print("xはNoneじゃない :( ")
    
    


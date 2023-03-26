#カプセル化
#①オブジェクトによって複数の変数とメソッドをまとめること
#②データをクラス内に隠蔽し、外から見えないようにする

class Rectangle:
    def __init__(self, w=100, l=1):
        self.width = w
        self.len = 1
        self.nums = [1, 2, 3, 4, 5]
        self._private = True

    def area(self):
        return self.width * self.len

    def change_data(self, index, n):
        self.nums[index] = n

    def _unsafe_method(self):
        print(self._private)

#クラスの外側からオブジェクトを利用するコードをclientと呼ぶ
data_one = Rectangle()
data_one.nums[0] = 10
print(data_one.nums)

#カプセル化はメソッドを通じて操作させる
data_one.change_data(0, 50)
print(data_one.nums)

#Pythonの変数はすべてパブリック変数
#clientからアクセスしてほしくない変数やメソッドにはアンダースコアを一つつける


#抽象化
#対象から小さな特徴を除いて、本質的な特徴だけを集めた状態にする手順


#ポリモーフィズム
#同じインターフェース（関数、メソッド）でありながら
#データ型に合わせて異なる動作をする機能
print(type("Hello World!"))
print(type(1))
print(type(0.1))

#ポリモーフィズムなし
#shapes = [tr1, sq1, cr1]
#for a_shape in shapes:
#    if isinstance(a_shape, Triangle):
#        a_shape.draw_triangle()
#    if isinstance(a_shape, Square):
#        a_shape.draw_Square()
#    if isinstance(a_shape, Circle):
#        a_shape.draw_Circle()
#ポリモーフィズムあり
#for a_shape in shapes:
#    a_shape.draw()

#ダックタイピング
#あるオブジェクトが期待する属性を持っていて、期待する動作をしてくれるならそれでいい
#それがアヒルのように歩き、アヒルのように鳴くのなら、それはアヒルだ


#継承
#クラスを作る時にほかのクラスからメソッドや変数を引き継ぐ
#同じコードを何度も書かなくて良くなり、より扱いやすくなる
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape): #子クラスを定義するときに親クラスをパラメータに指定する
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))
        #メソッドオーバーライド
        #子クラスが親クラスのメソッドを別の実装で置き換える
        
a_square = Square(20, 20)
a_square.print_size()


#コンポジション
#has-a関係　別のクラスのオブジェクトを変数として持たせる

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)
#PersonクラスのmickオブジェクトをDogクラスの変数ownerに持たせる
#stanオブジェクトは、Personオブジェクトをインスタンス変数ownerに持つ







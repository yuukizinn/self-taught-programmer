#関数
def f(x, y, z):
    return x + y + z
def g():
    z = 1 + 1
z = f(1, 2, 3)
print(z)

result = g()
print(result)

#組み込み関数:最初から用意されている関数
print(len("MONTH"))
print(str(100))
print(int("1"))
print(float("10"))

#関数を再利用する
def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")
even_odd(2)
even_odd(3)

#必須引数とオプション引数
#定義は必須引数が先
def add_it(x, y = 10):
    return x + y

print(add_it(1))
print(add_it(1,20))

#スコープ
#グローバル変数
yy = 100
def h():
    global yy
    yy += 1
    print(yy)
h()

#input関数
print("#input関数")
age = int(input("your age:"))
if age < 21:
    print("you are kids")

#例外処理
print("#例外処理")
try:
    a = int(input("type a number"))
    b = int(input("type a another"))
    print(a / b)
except(ZeroDivisionError):
    print("ZeroDivisionErrorです。")
except(ValueError):
    print("ValueErrorです。")

#ドキュメンテーション文字列
print("#ドキュメンテーション文字列")
def add(l, m):
    """
    Returns l + m.
    :param l: int.
    :param m: int.
    :return: int sum of l and m.
    """
    return l + m

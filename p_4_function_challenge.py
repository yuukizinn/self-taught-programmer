#challenge
def function1(l=10):
    var1 = l / 2
    return var1

def function2(m):
    var2 = m * 4
    return var2

exe1 = function1(8)
exe2 = function2(exe1)

print(exe2)

try:
    a = input("文字列を入れてください")
    is_float = float(a)

    print(is_float)
except(ValueError):
    print("文字列エラーです")

#モジュール
#コードを収めたPythonファイル

#組み込みモジュール
#Python本体に含まれているモジュール

#インポート
#使用するモジュールをPythonに伝える

import math
import random
import statistics
import keyword

#math
print(math.pow(2,3))

#random
print(random.randint(0,100))

#statistics
nums = [1, 5, 3, 12, 45, 33, 2, 2]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))

#keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

#自作モジュールをインポート
#すべてのコードが実行される
import p_8_module_1

#関数呼び出し
p_8_module_1.print_hello()

#モジュールを変数に格納
f = p_8_module_1
f.print_hello()

#print_hello関数重複
def print_hello():
    print("hello2")
print_hello()

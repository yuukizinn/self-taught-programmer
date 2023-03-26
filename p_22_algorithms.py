#アルゴリズム
#特定の問題を解決するための、再現可能な一連の手順

#fizzbuzz
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#探索アルゴリズム
#リストのようなデータ構造の中から欲しいデータを探す処理

#線形探索
#データ構造の中の要素を一つ一つ確認して探しているものを見つける
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found
numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)

#回文
def palindrome(word):
    word = word.lower()
    return word[::-1] == word
print(palindrome("Mother"))
print(palindrome("Mom"))

#アナグラム
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)
print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))

#出現する文字列を数える
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("Dynasty")

#組み込みモジュールcollections
from collections import defaultdict

def count_characters2(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)

count_characters2("Dynasty")

#collections.Counter
from collections import Counter
print(Counter("Dynasty"))

#分割統治法
#大きな問題を小さな問題に分割して解決する手法　小さな問題は比較的に解決できるだろうという点に着目　再帰法

#反復法　繰り返すことで問題を解決する手法
#再帰法　関数からその関数自身を呼び出す手法　再帰関数
#反復法で解決できる問題は再帰法に置き換えられる 再帰法はより洗練された解決法となることが多い

#再帰のルール
#再帰終了条件を持たなければならない
#状態を変えながら再帰終了条件に進んでいかなければならない
#再帰的に関数自身を呼び出さなければならない

def bottles_of_beer(bob):
    """Prints Bottle of Beer on the Wall lyrics.

    :param bob: Must be a positive integer.
    """
    if bob < 1: #再帰終了条件の用意
        print("""No more bottles of beer on the wall.
            No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1 #再帰終了条件に進んでいく
    print("""{} bottles of beer on the wall.
        take one down, pass it around,
        {} bottles of beer on the wall.
        """.format(tmp, tmp, bob))
    bottles_of_beer(bob) #再帰的に関数自身を呼び出す

bottles_of_beer(99)


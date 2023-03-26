#三重クォート文字列
"""line one
   line two
   line three
    
"""

#インデックス
print("#インデックス")
author = "Kafka"
print(author[0])
print(author[1])
print(author[2])
print(author[-3])
print(author[-1])

#文字列操作
print("#文字列操作")
print("cat" + "in" + "box")
print("lemon" * 3)
print("dog".upper())
print("bird".capitalize())

#書式化
print("#書式化")
aa = "三郎"
print("こんにちは、{}。さようなら、{}。".format("太郎", aa))

#分割
print("#分割")
print("あいう。えお。かきくけ。こ。さしすせそ。".split("。"))

#結合
print("#結合")
print("+".join(aa))
words = [" one", "two", "three", "four", "five ", "."]
one = "　".join(words)
print(one)

#空白除去
print("#空白除去")
two = one.strip()
print(two)

#置換
print("#置換")
three = two.replace("one", "zzz")
print(three)
print(one)

#文字を探す
print("#文字を探す")
print(one.index("e"))
print(one.index("four"))

#包含
print("#包含")
print("four" in one)
print("zzz" not in one)

#改行
print("#改行")
print("one\ntwo\nthree")

#スライス
print("#スライス")
my_list =["cat", "dog", "bird"]
my_str ="死の代わりにひとつの光があった。"
print(my_list[0:1])
print(my_str[:8])
print(my_str[8:])
print("明日があるさ明日がある"[:])

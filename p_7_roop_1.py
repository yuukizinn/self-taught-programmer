#forループ
#反復処理（イテレーション）
#イテラブルなオブジェクトの要素を順番に取り出すこと
print("#forループ")
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    sho = show
    for sh in sho:
        print(sh)

#ミュータブルなイテラブル更新
print("#ミュータブルなイテラブル更新")
i = 0
for show in shows:
    new = shows[i]
    new = new.upper()
    shows[i] = new
    i += 1
print(shows)

#enumerate関数
#各要素のインデックス値を自動的に用意する
print("#enumerate関数")
for i, new in enumerate(shows):
    shows[i] = shows[i].lower()
#    new = shows[i]
#    new = new.lower()
#    shows[i] = new
print(shows)

#組み込み関数range
#整数を順番に生成する
print("#range関数")
for k in range(8,11):
    print(k)

#whileループ
#式がTrueに評価されている間、コードの実行を繰り返す
print("#whileループ")
x = 5
while x > 0:
    print('{}'.format(x))
    x -= 1
print("end")

#break文
#ループを終了するための文
print("#break文")
for i in range(0, 100):
    print(i)
    break

#continue文
print("#continue文")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#入れ子のループ
print("#入れ子のループ")
for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

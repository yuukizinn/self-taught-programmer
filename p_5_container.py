#コンテナ
#データ構造を保持する書類棚のようなもの

#メソッド
#特定のデータ型に関連付けられている関数
#オブジェクトに付けて呼び出す
print("#メソッド")
print("Hello".upper())
print("Hello".replace("o", "@"))

#イテラブル（繰り返し可能）
#繰り返し処理で要素を１つずつ取り出せるオブジェクト
#文字列・リスト・タプル

#ミュータブル（変更可能）
#オブジェクトを追加したり削除したりできる
#リスト・辞書

#イミュータブル（変更不可能）
#タプル・辞書のキー・文字列

#リスト
#好きな順番でオブジェクトを保存しておけるコンテナ
print("#リスト")
fruit1 = list()
fruit2 = []
fruit3 = ['"Apple"', "Orange", "Pear"]
print(fruit3)

#どんなオブジェクトでも格納可
fruit3.append("Banana")
fruit3.append(False)
fruit3.append(100)
fruit3.append(1.1)
fruit3.append(80)
print(fruit3)
#インデックス値
print(fruit3[2])

fruitx = []
fruitx = fruit3.pop()
fruitx = fruitx + fruit3.pop()
print(fruit3)
print(fruitx)

#in演算子
print("#in演算子")
print('"Apple"' in fruit3)
print('"Apple"' not in fruit3)

#len関数
print("#len関数")
print(len(fruit3))

#タプル
print("#タプル")
my_tuple1 = tuple()
my_tuple2 = ()
my_tuple3 = ("M.Juckson", 1958, True)
#数値優先のカッコと区別
my_tuple4 = (9,)
print(my_tuple3[2])

#辞書
#２つのオブジェクトを関連付けて保持する組み込みのコンテナ
#取り出し用のラベルをキー、キーに対応付けられた値をバリュー
print("#辞書")
my_dict1 = dict()
my_dict2 = {}
fruits = {"Apple": "Red",
         "Banana": "Yellow"}
print(fruits)
fruits["Orange"] = "OrangeCollor"
print(fruits["Orange"])
print("orange" not in fruits)
del fruits["Apple"]
print(fruits)

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live",
         }
n = "1"
#n = input("数字を入力してください")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません")
    
#コンテナの中のコンテナ
#コンテナにはコンテナを格納できる
#タプルの要素にリストなどのミュータブルな要素を持たせた場合、
#イミュータブルではなくなるため辞書のキーには使えなくなる
print("#コンテナの中のコンテナ")
lists = []
lists.append(fruit3)
lists.append(my_tuple3)
lists.append(fruits)
lists.append("a")
print(lists)

list1 = lists[0]
list2 = lists[0]
list1.append("ringo")
print(fruit3) #"ringo"が入っている
print(list1)  #"ringo"が入っている
print(list2)  #"ringo"が入っている

my_lists = (lists, "bbb")
print(my_lists)

#辞書のバリューとして、リスト、タプル、辞書を追加できる
ny = {
    "座標": (40.7128, 74.0084),
    "セレブ": [
        "ウッディ・アレン",
        "ジェイ・Z",
        "ケヴィン・ベーコン"
        ],
    "事実": {
        "州": "ニューヨーク",
        "国": "アメリカ",
        }
    }
print(ny["事実"]["州"])

#ファイル読み書き

#osモジュール
print("#OSモジュール")
import os
path = os.path.join("E:\\", "データ保存用","学習","Python","st.txt")
print(path)
print(os.getcwd())

#組み込み関数open
print("#組み込み関数open")
#ファイルオブジェクトを作成し、変数へ格納
st = open(path, "w")
#ファイルオブジェクトに書き込み
st.write("Hi from Python!!")
#クローズ
st.close()

#encording引数
print("#encoding引数")
st = open("st2.txt", "w+", encoding="utf-8")
st.write("Pythonからこんにちは！")
print(st.read() + "→読み込めてない") #読み込めない
st.close()

st = open("st2.txt", "r", encoding="utf-8")
print(st.read() + "→読み込めた") #読み込める
st.close()

#with文
#処理がwithブロックを抜けた時に指定した処理を実行する
print("#with文")
with open("st3.txt", "w+", encoding="utf-8") as g:
    g.write("with文①")

with open("st3.txt", "r", encoding="utf-8") as g:
    b = g.read() #with文①
print(b)

with open("st3.txt", "r", encoding="utf-8") as h:
    c = print(h.read())
print(c) #None print出力は入らない

my_list = []
with open("st.txt", "r", encoding="utf-8") as h: #encording必須
    my_list.append(h.read())
    my_list.append(h.read()) #readはファイルを開いた後一回だけ　空が格納
print(my_list)

#CSVファイル
print("#CSVファイル")
import csv
#csvモジュールはwith文の中で実行する

#CSVwriter
with open("st.csv", "w", newline="") as i:
    w = csv.writer(i, delimiter="|")
    #ファイルオブジェクトとデリミタを受け取ってcsvオブジェクトを返す
    w.writerow(["one", "two", "three"])
    #writerowメソッド
    #引数としてリストを受け取り、writerメソッドに指定されたデリミタで区切られ、
    #その内容をcsvファイルに書き出す
    w.writerow(["four", "five", "six"])

#CSVreader
with open("st.csv", "r") as j:
    print(j) #ファイルオブジェクト
    r = csv.reader(j, delimiter=" ")
    #csvを1行単位で扱えるイテラブルが返される
    print(r) #csvオブジェクト
    for row in r:
        print(",".join(row))
        

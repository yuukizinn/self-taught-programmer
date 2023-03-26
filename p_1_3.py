#coding: utf-8

#python
#読みやすいプログラミング言語
#webサーバからデスクトップアプリケーションまで

#対話シェル
#IDLE
#Interactive DeveLopment Environment

#繰り返し
for i in range(3):
    print("Hello,World")

#改行1
print("""
ながい
長い
コード
""")

#改行2
print\
 ("長い\
ながい\
コード")

#データ型
print("Hello") #str
print(2 + 2) #int
print(2.2 + 2.2) #float
print(True) #bool
print(None) #NoneType

#クォート
print("'hello'")
print('"hello"')

#算術演算子
print(13 // 5)
print(13 % 5)
print(13 / 5)
print(13 ** 5)

#比較演算子
print(13 == 13)
print(13 != 13)

#論理演算子
print(1 == 1 and 2 == 2)
print(1 == 2 or 2 == 2)
print(not 1 == 1 and 2 == 2)

#条件文
#if文
home = "アメリカ"
if home == "アメリカ":
    print("Hello,America1")
elif home == "アメリカ":
    print("Hello,America2")
else:
    print("Hello,World")

#単純文:１行のコード
#複合文:１つ以上の節
#節:１行のヘッダー部分とそれに続く１つ以上のスイート部分
#ヘッダー:キーワードが含まれる１行のコード
#スイート:１つのスイートは１行のコードで構成される
#ヘッダーがスイートを制御する

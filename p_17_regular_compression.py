
#正規表現
#regular expression
#reモジュール findall関数

import re

#re.IGNORECASE 大文字小文字無視
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)

#re.MULTILINE 複数行のテキストを複数行として扱う
zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
greatidea -- let's
do more of those!"""
m = re.findall("If", zen, re.MULTILINE)
print(m)

#複数コマンドの一致 "[]"
string = "Two too."
m = re.findall("t[wo]o", string, re.IGNORECASE)
print(m)

#数値との一致 "\d"
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

#貪欲な正規表現 .*
#非貪欲な正規表現 .*?
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
print(found)
for match in found:
    print(match)

#エスケープ \
line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)

#game
text = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、
科学者たちはそのような長い __体の一部__ をどうやって
獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんど
は脚と __体の一部__ によるものです。"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語（＝ヒント）
    の部分は後を２つのアンダースコアで挟んでください。ヒントの単語には
    アンダースコアを含めないでください。__hint_hint__ はだめです。
     __hint__ はOKです。
     """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

#mad_libs(text)


#challenge
txt = "the ghost that says boo haunts the loo"
e = re.findall(".oo", txt)
print(e)

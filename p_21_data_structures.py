#データ構造
#情報を取りまとめて格納するためのフォーマット

#スタック
#要素の追加や削除を終端にしか行えないリスト
#ポップ
#スタックから要素を削除すること
#プッシュ
#スタックに要素を追加すること

#LIFO(ラストイン・ファーストアウト)
#最後に入れた要素だけを取り出せるデータ構造

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

stack2 = Stack()
for i in range(0, 6):
    stack2.push(i)
print(stack2.peek())
print(stack2.size())

#スタックを使って文字列を逆順にする
stack3 = Stack()
for c in "Hello":
    stack.push(c)
reverse = ""
while stack.size():
    reverse += stack.pop()
print(reverse)

#キュー
#最初に入れた要素が一番最初に取り出されるデータ構造
#FIFO(ファーストイン・ファーストアウト)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def deqeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()
for i in range(0, 5):
    a_queue.enqueue(i)
while a_queue.size():
    print(a_queue.deqeue())
print()
print(a_queue.size())

#collentions.deque


import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def simulate_line(till_show, max_time):
    #till_show = 後何秒で映画が始まるのか
    #max_time = チケットを買うのにかかる最大の秒数
    pq = Queue()
    tix_sold = [] #チケットを購入できた人を覚えておくためのもの

    for i in range(100):
        pq.enqueue("person" + str(i))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r) #Pythonの処理を一時停止　チケットを購入するのに時間がかかっていることを表現
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold

sold = simulate_line(10, 1)
print(sold)

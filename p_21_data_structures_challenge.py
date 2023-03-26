
#challenge

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

reverse = ""

stack = Stack()
for i in "Hello":
    stack.push(i)
print(stack.items)

for i in range(len(stack.items)):
    reverse += stack.pop()

print(stack.items)
print(reverse)


stack2 = Stack()
stack2.items = [1, 2, 3, 4, 5]
reverse_list = []

for i in range(len(stack2.items)):
    reverse_list.append(stack2.items.pop())
print(reverse_list)


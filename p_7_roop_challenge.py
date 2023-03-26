#challenge
#5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

for i in list1:
    for j in list2:
        print(i * j)

#4
answer = [1, 52, 51, 542, 675]
while True:
    a = input("input number or put 'q' to end\n")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a in answer:
        print("正解です！")
        break
    else:
        print("不正解です！")

#        for i in answer:
#            if i == x:
#                print("正解です！")
#                break
#            if i != x:
#                print("不正解です")
                

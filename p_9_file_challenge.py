#challenge
import csv

'''
#2
answer = input("好きな食べ物はなんですか\n")
with open("p_9_challenge.txt", "w") as b:
    b.write(answer)
with open("p_9_challenge.txt", "r") as c:
    print(c.read())
'''

#3
my_list = [
    ["Top Gun", "Risky Business", "MinorityReport"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
    ]
with open("p_9_chalenge.csv", "w", newline="") as d:
    #newlineオプション
    x = csv.writer(d, delimiter=",")
    count = 0
    for row in my_list:
        print(count)
        count += 1
        x.writerow(row)
        print(",".join(row))

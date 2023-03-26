#challenge
print("#1")
var1 = "カミュ"
for i in var1:
    print(i)

print("#2")
print("私は昨日{}を書いて、{}に送った！".format(input("入力１"), input("入力２")))

print("#3")
var2 = "aldous Huxley was born in 1894"
print(var2.capitalize())

print("#4")
var3 = "どこで？　だれが？　いつ？"
my_list = var3.split("　")
print(my_list)

print("#5")
my_list2 = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(my_list2)[0:-2] + ".")

print("#6")
var4 = "A screaming comes across the sky."
print(var4.replace("s", "$"))

print("#7")
var5 = "Hemingway" 
print(var5.index("m"))

print("#9")
print("three" + "three" + "three")
print("three" * 3)

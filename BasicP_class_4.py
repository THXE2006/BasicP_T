# def pnt_hello(x) :
#     print("hello world :" , x)

# x = 10

# pnt_hello(x)

# def cal(a , b) :
#     print(a + b)

# x = 10
# y = 20

# # print(cal(x , y))

# sum = cal(x , y)

# print(sum)

# def eat(rice , spoon) :
#     if rice == True :
#         if spoon == True :
#             return "กินได้"
#         else :
#             return "ขาดช้อน"
#     else :
#         return "ขาดข้าว"

# print(eat(True , False))

# def eat(rice , spoon) :
#     if rice == True :
#         if spoon == True :
#             print("กินได้")
#         else :
#             print("ขาดช้อน")
#     else :
#         print("ขาดข้าว")

# eat(True , False)

# def calculator(num1 , num2 , cmd) :
#     if cmd == "sum" :
#         return num1 + num2
#     elif cmd == "minus" :
#         return num1 - num2

# print(calculator(999 , 99 , "sum"))

# def star(row) :
#     i = 0
#     # j = 0
#     x = ""
#     while True :
#         if i < row :
#             x += "*"
#             i += 1
#             if i == row :
#                 print(x)
#         else :
#             break

# star(3)

# box = []

# x = 0
# text = ""

# while x < 11 :
#     box.append(x)
#     print(box)
#     x += 1

# for i in box :
#     text = text + str(i) + " "

# print(text)

# box_fruit = ["pizza" , "mango" , "cola" , "lemon" , "yellow" , "car" , "apple"]

# find = input("อยากหาอะไรพิมพ์มาได้เลย :\n")

# def find_fruit(fruit) :
#     x = 1
#     for i in box_fruit :
#         if i == fruit :
#             print(f"{x}.อร่อย")
#             x += 1
#         else :
#             print(f"{x}.ไม่แซ่บ")
#             x += 1

# find_fruit(find)

# students = {"Name" : "Thee",
#             "Age" : 19 ,
#             "Phone" : "06XXXXXXXX" ,
#             "ID" : 68130500057}
# students["Age"] = 20
# # print(students["Age"])
# for i in students :
#     print(i + " : " + str(students[i]))
#     if i == "Age" and students[i] > 18 :
#         print("อายุผ่านเกณฑ์")
#     elif i == "Age" and students[i] < 18 :
#         print("ไม่ผ่านเกณฑ์")

# students = [{"name": "Thanasorn Dusadeeroj", "age": 15, "ID": 67130500014},
#             {"name": "satit", "age": 19, "ID": 6713050047}]


# for i in students :
#     if i["age"] < 18 :
#         print(i["name"] + " ไม่ผ่าน")
#     else :
#         print(i["name"] + " ผ่าน")
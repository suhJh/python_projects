count = 1
while count <= 5:
    print(count);
    count = count + 1


while True:
    stuff = input("String to capiralize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())   

while True:
    stuff = input("Integer, please [q to quit]: ")
    if stuff == "q":
        break
    number = int(stuff)
    if number % 2 == 0:
        continue
    print(number, "squared is ", number * number)
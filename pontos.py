import math 
x1 = int(input("digite x1"))
y1 = int(input("digite y1"))
x2 = int(input("digite x2"))
y2 = int(input("digite y2"))
distance = math.sqrt((x1- x2)**2 + (y1 - y2)**2)
if distance >= 10:
    print("longe")
else:
    print("perto")

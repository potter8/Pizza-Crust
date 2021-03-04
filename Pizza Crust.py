import math

r, c = map(int, input().split())
#(Area of cheese divided by  area of pizza) * 100
cheeseArea = math.pi * ((r-c) ** 2)
pizzaArea = math.pi * (r ** 2)

crust = (cheeseArea / pizzaArea) * 100
print(crust)


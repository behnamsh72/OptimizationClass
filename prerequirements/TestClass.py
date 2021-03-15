import random

y = 35
x = y * y
g = random.randint(0, 100)
while (g * g - x > 1):
    s = g * g
    f = x / g
    g = (g + x / g) / 2

print(g)

import random

a = [random.randint(0,100) for n in range(random.randint(0,50))]
b = [random.randint(0,100) for n in range(random.randint(0,50))]
print("Random list A:", a)
print("Random list B:", b)

c = []
[c.append(n) for n in a if n in b if n not in c]
print("Overlapped list C (no duplicates): ",c)

import random

a = random.sample(range(100),random.randint(10,50))
b = random.sample(range(100),random.randint(10,50))

c = []
[c.append(n) for n in a if n in b if n not in c]
print("Random list A: ",a)
print("Random list B: ",b)
print("Overlapped list (no duplicates): ",c)

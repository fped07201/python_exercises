import random

a = [random.randint(0,100) for n in range(random.randint(0,50))]
print("Initial list: " + str(a))
b = [x for x in a if x%2==0]
print("Even list: " + str(b))

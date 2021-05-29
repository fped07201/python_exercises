import random

def new_list(list):
    return [list[0],list[-1]]

a = random.sample(range(50),random.randint(10,50))
b = new_list(a)

print("Random generated list: ",a)
print("Processed list (first and last element: ",b)

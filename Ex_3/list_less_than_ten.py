import random

len = int(input("Enter len of random array: "))
a = [random.randint(0,100) for n in range(len) ]
print("Random generated array: ",a)
cmp_num = int(input("Enter a number to compare with generated array elements (<): "))

b = [x for x in a if x<cmp_num]
print("New array after comparison: ",b)

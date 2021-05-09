num = int(input("Enter a number to calculate divisors: "))
divisors = [x for x in range(1,num) if (num%x == 0)]
print("List of divisors: ", divisors)

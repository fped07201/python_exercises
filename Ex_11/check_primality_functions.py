number=int(input("Enter a number: "))
prime=True
for n in range(2,number):
    if number%n==0:
        prime=False

if prime:
    print("Number " + str(number) + " is prime.")
else:
    print("Number " + str(number) + " is not prime.")


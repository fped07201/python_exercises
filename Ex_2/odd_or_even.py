num = input("Enter a number: ")
check = input("Enter number to divide: ")

if (int(num)%2) :
    print("Number " + num + " is odd")
elif (int(num)%4==0):
    print("Number " + num + " is divisible by 4")
else :
    print("Number " + num + " is even")

if (int(num)%int(check)==0):
    print("Number " + num + " is divisible by " + check)
else :
    print("Number " + num + " is not divisible by " + check)

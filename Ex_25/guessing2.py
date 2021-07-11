import random

min = 0
max = 100
tries = 0
result = 0

print("Choose a number between 0 and 100 (both included)")

while(True):
    # Check min, max and result integrity before guessing number
    if min == max:
        print("Don't cheat the game, the number must be",min,"!!!")
        break
    elif min>max:
        print("Don't cheat the game, current min is", min, "and current max is", max)
        break
    elif min>100 or max>100:
        print("Don't cheat the game, max number is 100")
        break
    elif min<0 or max<0:
        print("Don't cheat the game, min number is 0")
        break
    elif result == -1:
        print("Invalid option (h/l/e)")
    else:
        guess = random.randint(min,max)
        tries+=1
    
    result = input("Is your number higher, lower or equal to " + str(guess) + " (h/l/e)? ").lower()
    if result == "e":
        break
    elif result == "h":
        min = guess+1
    elif result == "l":
        max = guess-1
        guess = random.randint(min,max)
    else:
        result =-1 

print("Number of tries: ",tries)

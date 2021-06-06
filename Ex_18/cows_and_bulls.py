import random
import string

def checkGuess(guess, secret):
    cows = 0
    bulls = 0
    if(len(guess) != 4):
        return [False, cows, bulls] 
    for n in guess:
        if n not in string.digits:
            return [False, cows, bulls]
    for i in range(4):
        if(secret[i] == guess[i]):
            cows+=1
        elif guess[i] in secret: 
            bulls+=1

    return [True, cows, bulls]
    
if __name__=="__main__":
    bulls=0
    cows=0
    num_guesses=0
    secret_number = ''.join(str(n) for n in random.sample(range(0,10),4))
    print("Welcome to the Cows and Bulls game!")
    while(cows < 4):
        guess = input("Enter a 4-digit number: ")    
        [flag, cows, bulls] = checkGuess(guess, secret_number)
        if flag == False:
            print("Invalid guess!!")
        else:
            num_guesses+=1
            print("Cows: %d, Bulls: %d" % (cows, bulls))

    print("Number of needed guesses: %d" % num_guesses)

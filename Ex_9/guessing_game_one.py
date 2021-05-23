import random

counter=0
ran_number = random.randint(1,9)
while True:
    guess_number = input("Try guessing the number between 1 and 9: ").lower()
    if guess_number == "exit":
        print("Yout tried %d times." % counter)
        break
    else:
        try:
            guess_number = int(guess_number)
        except:
            print("Not a digit input!!")
            continue 
        else:
            counter+=1
            if ran_number==guess_number:
                print("You are right, attempt: %d!!!" % counter)
                break
            elif guess_number > ran_number:
                print("Too high!!!")
            else:
                print("Too low!!!")

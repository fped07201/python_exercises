import random
import string

def generatePWD(length):
    return ''.join([random.choice(string.ascii_letters+string.digits+string.punctuation) for n in range(length)])

pwd = generatePWD(int(input("Enter password length: ")))
print(pwd)

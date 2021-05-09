string = input("Enter a string to check palindrome: ")
strip_string = (''.join([c for c in string if c != ' '])).lower() # Remove whitespace and lowercase
palindrome = True
for i in range(int(len(strip_string)/2)):
    if strip_string[i] != strip_string[-i-1]:
        palindrome = False
        break

if palindrome:
    print(string + "--> This is a palindrome!")
else:
    print(string + "--> This is not a palindrome!")

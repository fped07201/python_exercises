string = input("Enter a string to check palindrome: ")
strip_string = (''.join([c for c in string if c != ' '])).lower() # Remove whitespace and lowercase
reverse_strip_string = strip_string[::-1]
if strip_string == reverse_strip_string:
    print(string + "--> This is a palindrome!")
else:
    print(string + "--> This is not a palindrome!")

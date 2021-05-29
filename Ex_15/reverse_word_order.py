def reverseString(in_string):
    splitted_string = in_string.split();
    return " ".join(splitted_string[::-1])

input_string = input("Enter a string: ")
reverse_string = reverseString(input_string)
print("Reversed string: ",reverse_string)

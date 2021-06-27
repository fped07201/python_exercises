with open('Training_01.txt', 'r') as open_file:
    file_lines = open_file.read().splitlines()

dict = {}
for element in file_lines:
    element = element[3:-26]
    if element in dict:
        dict[element] +=1
    else:
        dict[element]=1

print(dict)

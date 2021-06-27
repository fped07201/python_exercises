with open('namelist.txt', 'r') as open_file:
    file_lines = open_file.read().splitlines()

dict = {}

for element in file_lines:
    if element in dict:
        dict[element] +=1
    else:
        dict[element]=1

print(dict)

with open('primenumbers.txt', 'r') as open_file:
    pnums = open_file.read().splitlines()

with open('happynumbers.txt', 'r') as open_file:
    hnums = open_file.read().splitlines()

print("Prime numbers: ",pnums,"\n")
print("Happy numbers: ",hnums,"\n")

overlap_nums = [n for n in pnums if n in hnums]

print("Overlapped numbers: ", overlap_nums, "\n")

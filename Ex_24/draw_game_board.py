def printrow(n):
    print(" ---"*n)

def printcolumn(n):
    print("|   "*n+"|" )

def printboard(n):
    for i in range(n):
        printrow(n)
        printcolumn(n)
    printrow(n)

if __name__ == "__main__":
    size = int(input("Enter board size NxN: "))
    printboard(size)


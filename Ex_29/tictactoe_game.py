################ Local variables ################

game = [[0, 0, 0],
	    [0, 0, 0],
    	[0, 0, 0]]

################ Print board functions ################

def printRow(n):
    print(" ---"*n)

def printColumn(col):
    symbols = [' ','X','O']
    column = "| "
    for i in col:
        column += symbols[i] + " | "
    print(column)

def printBoard(board):
    n = len(board)
    for i in range(n):
        printRow(len(board[i]))
        printColumn(board[i])
    printRow(n)

################ User input functions ################

def checkEmptyCell(game):
    for i in game:
        for j in i:
            if j == 0:
                return True
    return False

def checkValidCoord(coord):
    try:
        aux_coord = [int(i.strip()) for i in coord.split(",")]
    except:
        print("Bad coordinates format!!")
        return [False,0,0]
    if len(aux_coord) != 2:
        print("Invalid coordinates length!")
        return [False,0,0]
    for i in aux_coord:
        if i < 1 or i > 3 :
            print("Coordinates out of range!")
            return [False,0,0]
    return [True, aux_coord[0]-1, aux_coord[1]-1]

def playerPlay(player):
    result = False
    while result == False :
        coordinates = input("Player "+str(player)+" enter your move (format: row,col):")
        [result, row, col] = checkValidCoord(coordinates)
        if result:
            if(game[row][col] == 0):
                game[row][col] = player
            else:
                result = False
                print("Position already ocuppied")

def checkContinuePlaying():
    while True:
        cont = input("Play another game? (y/n): ")
        if cont == 'y':
            return True
        elif cont == 'n':
            return False
        else:
            print("Invalid option, enter 'y' or 'n'")


################ Check winner functions ################

def checkRowWinner(board,player):
    for i in range(len(board)):
        winner = True
        for j in range(len(board[i])):
            if board[i][j] != player:
                winner = False
                continue
        if winner:
            return True
    return False

def checkColumnWinner(board,player):
    for i in range(len(board[0])):
        winner = True
        for j in range(len(board)):
            if board[j][i] != player:
                winner = False
                continue
        if winner:
            return True
    return False


def checkDiagonalWinner(board,player):
    winner = True
    for i in range(len(board)):
        if board[i][i] != player:
             winner = False
             continue
    if winner:
        return True
    
    for i in range(len(board)):
        if board[-1-i][-1-i] != player:
             winner = False
             continue
    if winner:
        return True
    return False

def checkWinner(board,player):
    if checkRowWinner(board,player): return True
    elif checkColumnWinner(board,player): return True
    elif checkDiagonalWinner(board,player): return True
    else: return False

################ MAIN ################

if __name__ == "__main__":
    player = 1
    wins = [0,0,0]
    printBoard(game)
    while True:
        playerPlay(player)
        printBoard(game)
        if checkWinner(game, player):
            print("Player " +str(player) + " wins!!!!!\nCONGRATULATIONS!!!!!!!!!")
            wins[player] = wins[player] + 1
            print("Player 1 wins: ",wins[1])
            print("Player 2 wins: ",wins[2])
            print("Draws: ",wins[0])
            if checkContinuePlaying() :
                game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
                player = 2
            else:
                break
        if checkEmptyCell(game) == False:
            print("Game is over! No more moves left.")
            wins[0] = wins[0] + 1
            print("Player 1 wins: ",wins[1])
            print("Player 2 wins: ",wins[2])
            print("Draws: ",wins[0])
            if checkContinuePlaying() :
                game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
                player = 2
            else:
                break
        player = player ^ 0x3


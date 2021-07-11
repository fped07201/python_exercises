winner_is_2 = [[2, 2, 0],
	       [2, 1, 0],
	       [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	       [2, 1, 0],
	       [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	            [2, 1, 0],
	            [2, 1, 1]]

winner_is_also_1_2 = [[1, 1, 1],
	              [2, 2, 0],
	              [2, 1, 1]]

winner_is_also_1_3 = [[1, 2, 1],
	              [2, 1, 0],
	              [1, 1, 1]]

no_winner = [[1, 2, 0],
	     [2, 1, 0],
	     [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	          [2, 1, 0],
	          [2, 1, 0]]

def checkRowWinner(matrix,player):
    for i in range(len(matrix)):
        winner = True
        for j in range(len(matrix[i])):
            if matrix[i][j] != player:
                winner = False
                continue
        if winner:
            return True
    return False

def checkColumnWinner(matrix,player):
    for i in range(len(matrix[0])):
        winner = True
        for j in range(len(matrix)):
            if matrix[j][i] != player:
                winner = False
                continue
        if winner:
            return True
    return False


def checkDiagonalWinner(matrix,player):
    winner = True
    for i in range(len(matrix)):
        if matrix[i][i] != player:
             winner = False
             continue
    if winner:
        return True
    
    for i in range(len(matrix)):
        if matrix[-1-i][-1-i] != player:
             winner = False
             continue
    if winner:
        return True
    return False

def checkWinner(matrix,player):
    if checkRowWinner(matrix,player): return True
    elif checkColumnWinner(matrix,player): return True
    elif checkDiagonalWinner(matrix,player): return True
    else: return False

if __name__ == "__main__":
    print("* winner_is_2")
    if(checkWinner(winner_is_2,1)): print("	Winner is 1")
    elif(checkWinner(winner_is_2,2)): print("	Winner is 2")
    else: print("	no winner")

    print("* winner_is_1")
    if(checkWinner(winner_is_1,1)): print("	Winner is 1")
    elif(checkWinner(winner_is_1,2)): print("	Winner is 2")
    else: print("	no winner")
    
    print("* winner_is_also_1")
    if(checkWinner(winner_is_also_1,1)): print("	Winner is 1")
    elif(checkWinner(winner_is_also_1,2)): print("	Winner is 2")
    else: print("	no winner")

    print("* winner_is_also_1_2")
    if(checkWinner(winner_is_also_1_2,1)): print("	Winner is 1")
    elif(checkWinner(winner_is_also_1_2,2)): print("	Winner is 2")
    else: print("	no winner")
    
    print("* winner_is_also_1_3")
    if(checkWinner(winner_is_also_1_3,1)): print("	Winner is 1")
    elif(checkWinner(winner_is_also_1_3,2)): print("	Winner is 2")
    else: print("	no winner")

    print("* no_winner")
    if(checkWinner(no_winner,1)): print("	Winner is 1")
    elif(checkWinner(no_winner,2)): print("	Winner is 2")
    else: print("	no winner")

    print("* also_no_winner")
    if(checkWinner(also_no_winner,1)): print("	Winner is 1")
    elif(checkWinner(also_no_winner,2)): print("	Winner is 2")
    else: print("	no winner")

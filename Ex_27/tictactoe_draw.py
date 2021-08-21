game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

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

if __name__ == "__main__":
    print(game)
    player = 1
    while checkEmptyCell(game):
        playerPlay(player)
        player = player ^ 3
        print(game)

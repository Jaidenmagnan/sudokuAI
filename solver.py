from sys import argv

#create your board
def createBoard():
    with open(argv[1], 'r') as f:
        board = []
        skipLine = 0
        for line in f:
            row = []
            if skipLine > 0:
                for num in line:
                    if not num =='\n':
                        row.append(int(num))
                board.append(row)
            skipLine += 1
        return board

#prints your board
def printBoard(board):
    for row in range(9):
        print()
        for column in range(9):
            print(board[row][column], end="  ")

#checks a win by looking for zeros
def checkWin(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return False
    
    return True

#Decides if a number is valid in an array
def valid(board, num, row, col):
    possible = getPossibleValues(board, row, col)
    for value in possible:
        if value == num:
            return True
    else:
        return False

#gets all possible values of a tile
def getPossibleValues(board, rownum, colnum):
    notPossible = set()

    for row in range(9):
        for col in range(9):
            if row == rownum:
                notPossible.add(board[row][col])
            if col == colnum:
                notPossible.add(board[row][col])

    if rownum > 0 and rownum < 3:
        rownum = 0 
    elif rownum  > 3 and rownum < 6:
        rownum = 3
    elif rownum > 6:
        rownum = 6

    if colnum > 0 and colnum < 3:
        colnum = 0
    elif colnum > 3 and colnum < 6:
        colnum = 3
    elif colnum > 6:
        colnum = 6
    
    #this is sort of unorganized but it works for getting box values
    for right in range(3):
        for down in range(3):
            notPossible.add(board[rownum + right][colnum + down])

    
    possible = [1,2,3,4,5,6,7,8,9]
    for num in notPossible:
        if num in possible:
            possible.remove(num)

    return possible

#Uses backtracking to solve set
def backTracker(board):
    check = getEmpty(board)
    if not check:
        return True;
    else:
        row, col = getEmpty(board)

    for i in range(1,10):
        if valid(board, i, row, col):
            board[row][col] = i

            if backTracker(board):
                return True

            board[row][col] = 0


    return False

#Gets next empty tile
def getEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

#Skims out board by placing in obvious answers
def smartSearch(board):
    while not checkWin(board):
        changes = 0
        for row in range(9):
            for col in range(9):
                tile = board[row][col]
                if tile == 0:
                    possible = getPossibleValues(board, row, col)
                    if len(possible) == 1:
                        board[row][col] = possible[0]
                        changes += 1
        if changes == 0:
            break
    return board
    

def main():
    #to access a board first specify the row, then column board[row][column]
    board = createBoard()
    printBoard(board)
    getPossibleValues(board, 0, 0)

    #windles down possible combinations
    board = smartSearch(board)

    print()
    backTracker(board)
    printBoard(board)
    

main()

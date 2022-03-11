from array import *
from sys import argv

#returns a soduko board from the text file
def readSudoku():
    with open(argv[1], 'r') as f:
        skipline = 0

        row = [0,0,0,0,0,0,0,0,0]
        board = []

        for line in f:
            i = 0;
            row = [0,0,0,0,0,0,0,0,0]
            if skipline>0:
                for num in line:
                    if(num != "\n"):
                        row[i] = num
                        i += 1
                if(row != [0,0,0,0,0,0,0,0,0]):
                    board.append(row)
            
            skipline += 1
    return board


def printBoard(board):
    for y in range(9):
        for x in range(9):
            print(board[y][x] + " ",end = "")
        print()



def findIndexofValue(possible, find):
    i = 0
    for value in possible:
        if find == value:
            return i
        i += 1

def findPossibleValues(board, x, y):

    row=board[y]
    column = []
    box = []
    
    #get column values
    for value in board:
        column.append(value[x])

    box_x = x
    box_y = y

    #get box values
    if x==1 or x==2:
        box_x = 0
    elif x==4 or x==5:
        box_x = 3
    elif x==7 or x==8:
        box_x = 6
    
    if y==1 or y==2:
        box_y = 0
    elif y==4 or y==5:
        box_y = 3
    elif y==7 or y==8:
        box_y = 6

    #add to box array
    box.append(board[box_y][box_x + 1])
    box.append(board[box_y][box_x + 2])
    box.append(board[box_y + 1][box_x])
    box.append(board[box_y + 1][box_x + 1])
    box.append(board[box_y + 1][box_x + 2])
    box.append(board[box_y + 2][box_x])
    box.append(board[box_y + 2][box_x + 1])
    box.append(board[box_y + 2][box_x + 2])

    notPossible = {}
    notPossible = set()

    for num in row:
        notPossible.add(int(num))
    for num in column:
        notPossible.add(int(num))
    for num in box:
        notPossible.add(int(num))
    
    possible = {}
    possible = set()

    for i in range(1, 10):
        if i in notPossible:
            continue
        else:
            possible.add(i)



    return possible




def main():
    board = readSudoku()
    #board is arranged in [columns][rows]

    solved = False
    counter = 0
    while not solved:
        for y in range(9):
            for x in range(9):
                if board[y][x] == '0':
                    possible = findPossibleValues(board, x, y)
                        #print("x" + str(x) + "y" + str(y) + str(possible))
                    if len(possible) == 1:
                        for num in possible:
                            board[y][x] = str(num)
        counter += 1
        if counter == 1000:
            solved = True

    #print(findPossibleValues(board, 8, 7))
    printBoard(board)


    

    



main()
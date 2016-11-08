import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]   # What do you need to add a whole row here?
    return A

def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(width, height):
    A = createBoard(width,height)
    for col in range (1, width-1):
        for row in range(1,height-1):
            A[row][col]=1
        #print(row,col)
    return A

def randomCells(width, height):
    A = createBoard(width,height)
    for col in range (1, width-1):
        for row in range(1,height-1):
            A[row][col] = random.choice([0,1])
        #print (row,col)
    return A


def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for col in range (width):
        for row in range(height):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for col in range (1,height-1):
        for row in range(1,width-1):
            if A[col][row] == 1:
                newA[row][col] = 0
    return newA

def countNeighbors(row,col,A):
    count = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            count += A[row][col]
        count -= A[row][col]
    return count

def next_life_generation(A):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            Neighborcount = countNeighbors(row,col,A)
            if Neighborcount > 3:
                newA[row][col] = 0
            elif Neighborcount < 2:
                newA[row][col]= 0
            elif Neighborcount == 3:
                newA[row][col] = 1
    return newA

A = randomCells(10,10)
printBoard(A)
for row in range(10):
    A = next_life_generation(A)
    printBoard(A)
    print ' '

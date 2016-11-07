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

def countNeighbors(row,col,A):
    count = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            count += A[row][col]
        count -= A[row][col]
        return count

def populateBoard(width,height,percA, percB):
    A = createBoard(width, height)
    numCells = width * height
    numA = int(percA*numCells)
    numB = int(percB*numCells)
    numEmpty = numCells -(numA + numB)

    population = numA*['A']+numB*['B']+numEmpty*[' ']
    population = random.sample(population,len(population))
    i = 0

    for row in range(height):
        for col in range(width):
            A[row][col]= population[i]
            i += 1
    return A

A = populateBoard(10,10,.4,.4)
printBoard(A)

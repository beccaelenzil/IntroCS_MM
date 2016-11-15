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

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for col in range (width):
        for row in range(height):
            newA[row][col] = A[row][col]
    return newA


def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

def countNeighbors(row,col,A):
    total_count = 0
    like_count = 0

    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if A[row][col] == A[r][c]:
                like_count += 1
            if A[r][c] != ' ':
                total_count += 1
    like_count -= 1
    total_count -= 1
    return [like_count,total_count]

def emptyIndex(A):
    height = len(A)
    width = len(A[0])
    emptylist = []
    for row in range (height):
        for col in range (width):
            if A[row][col] == ' ':
                emptylist.append([row,col])
    return emptylist


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

def next_life_generation(A, threshold):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    emptyList = emptyIndex(A)
    i = 0
    for row in range(1,height-1):
        for col in range(1,width-1):
            [like, total] = countNeighbors(row,col,A)
            # I added  " and A[row][col] != ' ' " so that we do not move around empty spaces
            if float(like)/total < threshold and i < len(emptyList) and total > 0 and A[row][col] != ' ':
                newA[row][col] = ' '
                #print "I moved"
                #print emptyList[i][0], emptyList[i][1]
                newA[emptyList[i][0]][emptyList[i][1]] = A[row][col]
                i += 1
    static = (newA == A)
    return [static, A]

def Segregation (A, thershold, percA, percB):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    i = 0



def segregationIndex(A):
    """
    takes in a matrix and returns a segregation index
    """
    segregation = copy(A)
    segregationList = []

    height = len(A)
    width = len(A[0])

    for row in range(1,height-1):
        for col in range(1,width-1):
            if A[row][col] != ' ':
                [sameNeighbors, totalNeighbors] = countNeighbors(row,col,A)
                segregation[row][col] = float(sameNeighbors)/float(totalNeighbors)
                # I could make a heat map of segregation

                # put it into a list so we can easily take the average
                segregationList.append(segregation[row][col])

    # take the average of the segregationIndex for each cell to get a single metric
    segregationIndex = sum(segregationList)/len(segregationList)

    return [segregation, segregationIndex]

A = populateBoard(10,10,.3,.3)
printBoard(A)
print " "
static = False
i = 0
'''
while static == False and i<1000:
    [static, A] = next_life_generation(A,0.3)
    #printBoard(A)
    print " "
    i += 1
    print i
'''

[seg, segI] = segregationIndex(A)
print segI

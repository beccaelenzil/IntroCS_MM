import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwPos(start,nSteps):
    currentPosition = start
    for i in range (0, nSteps):
        currentPosition = currentPosition + rs()
        print 'current position is ' + str(currentPosition)
    return currentPosition

rwPos( 40, 4 )

#hi >= start >= low

def rwsteps( start, low, hi ):
    currentposition = start
    #start = 0
    while currentposition >= low and currentposition <= hi:
        beforespace = currentposition + low-1
        afterspace = hi- currentposition-1
        print "|"+beforespace*" "+ "S"+afterspace*" "+"|"
        currentposition = currentposition + rs()
    return currentposition

rwsteps( 10, 5, 15 )

def rwposPlain (start, nsteps):
    currentPosition = start
    for i in range (0, nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition

print rwposPlain( 20, 4 )

def ave_signed_displacement( numtrials ):
    '''
    tales in number of simbs of 100 steps
    returns average distance from start
    '''
    posList = []
    for i in range(numtrials):
        pos = rwposPlain(0,100)
        posList.append (pos)
    avePos = sum(posList)/float(numtrials)
    return avePos

def ave_sq_d(numtrials):
    posList = []
    for n in range(numtrials):
        pos = rwposPlain(0,100)
        posList.append(pos**2)
    avePos = sum(posList)/float(numtrials)
    return avePos

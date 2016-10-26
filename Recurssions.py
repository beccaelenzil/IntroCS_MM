
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1)+fib(n-2)

print fib(3)

print "fib(5) == 3 = ",fib(5)," : ", 3 == fib(5)
print "fib(11) == 55 = ",fib(11)," : ", 55 == fib(11)

def fibIter(n):
    fibSeq = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range (2,n):
            fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
            #print fibSeq
        return fibSeq[-1]

print fibIter(5)

def listReverseIter(L):
    K = []
    for i in range (len(L)-1,-1,-1):
        K.append(L[i])
    return K

def listReverse(L):
    if len(L)== 1:
        return L
    else:
        listReverse(L[0:-1])
        return L[-1] + list


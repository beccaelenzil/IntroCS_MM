def power(b,p):
    result = 1
    for x in range(p):
        result = result*b
    return result
#print "power(2,5): should be 32 == ", power(2,5)
#print "power(5,2): should be 25 == ", power(5,2)
#print "power(42,0): should be 1 == ", power(42,0)
#print "power(0,42): should be 0 == ", power(0,42)
#print "power(0,0): should be 1 == ", power(0,0)

# python 2
import time
def summedOdds( list ):
    result = 0
    for element in list:
        #time.sleep(5)
        #print element
        if element % 2 == 1:
            result = result + element  # or result += e
            #print "It's an odd element"
            #print "so I updated the result to", result
    return result


print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )


def mult (m,n):
    result = 0
    for x in range (n):
        result = result + m
    return result
    if m == 0 or n == 0:
        if n < 0:
            for i in range (-1 * n):
                return result * -1
print "mult(6,7)    42 ==", mult(6,7)
print "mult(-6,7)  -42 ==", mult(-6,7)

def dot (l,k):
    result = 0
    if len(l) != len(k):
        return 0
    else:
        for i in range (len(k)):
            #print i
            result = result + l[i] * k[i]

    return result
print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )

def count_evens(L):
    result = 0

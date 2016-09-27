def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)


def sq(x):

    return x*x
print 'sq(6) is 36: ', sq(6)

def interp(low,high,fraction):
    """
    output: a value that is a fraction of the way between low and high
    input: low, high, fraction.
    """
    diff= high-low
    part= fraction*diff
    return low+part

print interp(1.0,9.0,0.25)

def checkends(s):
    if s[0] == s[-1]:
        return True

    else:
        return False

def flipside(s):
    length= len(s)

    return s[length/2:]+s[:length/2]


print flipside('homework')

def convertFromSeconds( s ):
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s/(60*60)
    s = s % (60*60)
    minutes = s/60
    seconds = s % 60
    return [days, hours, minutes, seconds]
print convertFromSeconds(200000)
print convertFromSeconds(100000)

def front3(str):
    """
    Given a string, we'll say that the
    front is the first 3 chars of the string.
    If the string length is less than 3,
    the front is whatever is there. Return a new
    string which is 3 copies of the front.
    """
    return str[:3]*3
    print front3(str) ('a')

def power(b,p):
    result = 1
    for x in range (p):
        result = result*b
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)

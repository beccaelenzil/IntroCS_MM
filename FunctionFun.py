def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)


def sq(x):

    return 6*x
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
    minutes = s/60
    seconds = s % (60*60)
    return [days, hours, minutes, seconds]
print convertFromSeconds(200000)

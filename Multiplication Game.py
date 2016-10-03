import random

def instructions ():
  print "hello, I'm a computer. We're going to practice mulitplication!"

def play():
  for i in range(5):
    userAnswer = -1
    factor1 = random.randint (0, 12 )
    factor2 = random.randint (0, 12 )
    correctAnswer = factor1 * factor2
    while userAnswer != correctAnswer:
      userAnswer = raw_input (" please enter the product of " + str ( factor1 ) + " and " + str (  factor2 ) + " : ")
      try:
        userAnswer = int(userAnswer)
      except:
        print " Enter an integer "
      if userAnswer == correctAnswer:
        print "correct"
      else:
        print "incorrect"
      print "game over! Keep practing"


def main():
    instructions()
    play()
main()

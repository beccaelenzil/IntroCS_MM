import random

def instructions ():
  print "hello, I'm a computer. We're going to practice mulitplication!"

def play():
  for i in range(5):
    userAnswer = -1
    factor1 = random.randint (0, 15 )
    factor2 = random.randint (0, 15 )
    correctAnswer = factor1 * factor2
    while userAnswer != correctAnswer:
      userAnswer = raw_input (" please enter the product of " + str ( factor1 ) + " and " + str (  factor2 ) + " : ")

      # Becca moved some pieces around to make the logic work.
      try:
        userAnswer = int(userAnswer)
        if userAnswer == correctAnswer:
          print "correct"
        else:
          print "incorrect"
      except:
        print " Enter an integer "

  print "game over! Keep practing"

def main():
    instructions()
    play()
main()

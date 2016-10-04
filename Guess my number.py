import random
#range = 0-100

def instructions ():
    print " Can you guess my number? "
def play():
    #for i in range (0, 100):
    userAnswer = -1
    correctAnswer = random.randint(0,100)
    #print correctAnswer
    while userAnswer != correctAnswer:

        userAnswer = raw_input("Guess my number: ")
        userAnswer = int(userAnswer)

        if userAnswer > correctAnswer:
            print "too high. Guess lower"
        elif userAnswer < correctAnswer:
            print "too low. Guess higher"
        else:
            print "correct. Good job!"




def main():
    instructions ()
    play ()
main ()

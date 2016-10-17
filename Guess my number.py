import random
#range = 0-100

def instructions ():
    print " Can you guess my number? "
    low = raw_input("Pick a low number for your range")
    high = raw_input ("Pick a high number for your range")
    return [low,high]
def play(low,high):

    #for i in range (0, 100):
    userAnswer = -1
    correctAnswer = random.randint(low,high)
    #print correctAnswer
    while userAnswer != correctAnswer:

        userAnswer = raw_input("Guess my number: ")
        while userAnswer.isdigit() == False:
            userAnswer = raw_input (" only numbers are allowed, guess my number: ")
        userAnswer = int(userAnswer)

        if userAnswer > correctAnswer:
            print "too high. Guess lower"
        elif userAnswer < correctAnswer:
            print "too low. Guess higher"
        else:
            print "correct. Good job!"




def main():
    [low,high] = instructions ()
    play (low,high)
main ()

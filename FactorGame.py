import random

def instructions():
    print "Can guess the factorization of this number?"

def play(score):
    for i in range(5):
        userAnswer = -1
        factor1 = random.randint (2, 12)
        factor2 = random.randint (2, 12)
        correctAnswer = factor1 * factor2

        userFactor1 = raw_input("please enter one factor of "+str(factor1*factor2)+": ")
        while userFactor1.isdigit() == False:
            userFactor1 = raw_input("please enter one factor of "+str(factor1*factor2)+": ")
        userFactor2 = raw_input("please enter the other factor of "+str(factor1*factor2)+":")
        while userFactor2.isdigit() == False:
            userFactor2 = raw_input("please enter the other factor of "+str(factor1*factor2)+":")


        userFactor1 = int(userFactor1)
        userFactor2 = int(userFactor2)

        userAnswer = userFactor1 * userFactor2
        if userAnswer == correctAnswer:
            print "correct!"
            score += 1
            print "your score is", score
        else:
            print "incorrect"

    playagain = raw_input ("play again? enter yes or no")
    while playagain != "yes" and playagain != "no":
        playagain = raw_input ("play again? enter yes or no")
    playagain = playagain.lower()
    return [playagain, score]

def main():
    score = 0
    instructions()
    [playagain, score] = play(score)
    while playagain == "yes":
        [playagain, score] = play(score)
    print "your final score is", score


main()

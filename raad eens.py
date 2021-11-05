import random

debug = True

z = 0
randomNum = 0

score = 0

def randomNumFunc(textPrint):
    randomNum = random.randint(1,1000)
    scoreAdd = False
    x = 0
    if debug:
        print(randomNum)
    print(textPrint)
    while x < 10:
        guess = str(input('What is your guess?\n'))
        if guess == 'q' or guess == 'quit':
            pass
        else:
            guess = int(guess)
        if guess == 'q' or guess == 'quit':
            print("Thank you for playing, goodbye.")
            exit()
        elif guess == randomNum:
            x += 11
            print('You guessed correctly.')
            scoreAdd = True
        else:
            if guess > randomNum - 20 and guess < randomNum + 20:
                print('You are extremly warm but guessed incorrectly, try again.\n')
            elif guess > randomNum - 50 and guess < randomNum + 50: 
                print('You are warm but guessed incorrectly, try again.\n')
            else:
                print('You guessed incorrectly, try again.\n')
            x += 1

        
    x = 0
    if scoreAdd:
        global score
        score += 1
    print('Your current score is',score)


while z <= 20:
    if z == 0:
        randomNumFunc("A random number has been selected. your objective is to guess the number within 10 tries. Good luck.")
    else:
        randomNumFunc('A new number has been selected. Good luck')
    if z < 20:
        again = input('want to play again?\n')
        if again == 'yes' or again == 'y':
            z += 1
        else:
            z += 100
            print('Thank you for playing.')
    elif z == 20:
        print('Thank you for playing.')
    

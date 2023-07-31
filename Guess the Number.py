import random

print('Guess the random number! Ready to play?')
print('Your number will fall between 1-10. You will receive 5 guesses. Make sure to only input integers, or I will waste one of your guesses!')

options=[1,2,3,4,5,6,7,8,9,10]
correct=str(random.choice(options))
guesses=5

while guesses>=0:

    if guesses>1:
        print('Make a guess:')
        selection=input()
        if selection==correct:
            print('Congratulations! You guessed, '+correct+' the correct number!')
            break
        else:
            print('Not quite! Try again.')
            guesses=guesses-1
    if guesses==1:
        print('Last chance!')
        selection=input()
        if selection==correct:
            print('Congratulations! You guessed '+correct+' on the very last try! How lucky!')
            break
        else:
            print('Not quite...')
            guesses=guesses-1
    if guesses==0:
        print('You ran out of guesses! The number was '+correct+'. Better luck next time!')
        break
            

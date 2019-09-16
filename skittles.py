#Code that makes a user guess a number of skittles
import random
skittles = random.randint(0,1023)

print("Guess the number of skittles! It could be from 0 to 1023")
userGuess = int(input("What's your guess? "))

while userGuess != skittles:
    if userGuess > skittles:
        print("You're too high!")
        userGuess = int(input("What's your guess? "))
    elif userGuess < skittles:
        print("You're too low!")
        userGuess = int(input("What's your guess? "))
    else:
        break

print("Congratulations, you're right!")
                

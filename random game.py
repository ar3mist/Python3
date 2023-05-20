import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it on first time ")
else:
    if guess < answer:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you have guessed correctly : ")
    else:
        print("You missed 'Better luck next time' ")
print("The random number is {}:".format(answer))

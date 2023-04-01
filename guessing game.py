answer = 5

print("Please guess any number between 1 to 10: ")
guess = int(input())

if guess < answer:
    print("Guess Higher ")
elif guess > answer:
    print("Guess lower")
else:
    print("You got it on the first time ")
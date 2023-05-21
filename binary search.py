low = 0
high = 10

print("Enter any number between {} to {}".format(low, high))

input("Press enter to start ")

count = 1
while True:
    print("\t Guessing between {} to {} ".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess {} .Should I guess higher or lower ?"
                     "Enter L or H, or C if my guess is correct: "
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!! ".format(count))
        break
    else:
        print("please enter L or H or C")

    count = count + 1

    # count += 1 Augmented assignment also used here






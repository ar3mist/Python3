name = input("Enter your name : ")

age = int(input("How old are you {} ? ".format(name)))



if age > 18:
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote")
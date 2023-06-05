current_choice = '-'
computer_parts = []   # creating an empty list

while current_choice != '0':
    if current_choice in "12345":
        print("Adding {} ".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Monitor")
        elif current_choice == '2':
            computer_parts.append("Keyboard")
        elif current_choice == '3':
            computer_parts.append("Mouse")
        elif current_choice == '4':
            computer_parts.append("graphic card")
    else:
        print("Please Enter the item to buy")
        print("1: Monitor")
        print("2: Keyboard")
        print("3: mouse")
        print("4: graphic card")
        print("0: Exit and Finish")

    current_choice = input()
print(computer_parts)






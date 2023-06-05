available_list = ["Monitor",
                  "Keyboard",
                  "Mouse",
                  "graphic card",
                  "HDMI",
                  "Exit"]
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
        elif current_choice == '5':
            computer_parts.append("HDMI")
    else:
        print("Please Enter the item to buy")
        for part in available_list:
            print("{0}: {1} ".format(available_list.index(part) + 1, part))

    current_choice = input()
print(computer_parts)






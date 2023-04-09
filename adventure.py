available_direction = ["North", "South", "West", "East"]

chosen_exit = None

while chosen_exit not in available_direction:
    chosen_exit = input("Enter the direction: ")
    if chosen_exit == "quit":
        print("Game over ")
        break
print("Aren't you glad you to get out of there: ")
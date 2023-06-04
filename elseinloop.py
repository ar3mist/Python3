numbers = [1, 45, 31, 16, 60]

for i in numbers:
    if i % 8 == 0:
        print("The numbers are unacceptable ")
        break
else:
    print("All those numbers are fine ")

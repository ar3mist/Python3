menu = [
    ["egg", "beacon"],
    ["egg", "bread", "beacon"],
    ["egg", "spam"],
    ["egg", "beacon", "spam"],
    ["egg", "beacon", "bread", "spam", "apple"],
    ["spam", "beacon", "bread", "spam"],
    ["spam", "egg", "spam", "bread"]
]

for meal in menu:
    for index in range(len(meal) -1, -1, -1 ):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

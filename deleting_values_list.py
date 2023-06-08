data = [1, 2, 3, 5, 12, 15, 17, 132, 434, 676, 890, 342, 123, 530, 650, ]

min_data = 100
max_data = 200

stop = 0
for index, value in enumerate(data):
    if value >= min_data:
        stop = index
        break
print(stop)

del data[:stop]
print(data)
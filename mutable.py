computer_parts = ['Monitor', 'Keyboard', 'Mouse', 'CPU']

other_parts = computer_parts

print(id(computer_parts))
print(id(other_parts))

computer_parts += ['RAM']
print(computer_parts)

print(id(computer_parts))
print(id(other_parts))
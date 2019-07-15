list = [2, 3, 1, 5, 2, 1, 3, 9, 9]

for remove in list:
    if list.count(remove) == 2:
        list.remove(remove)

print(list)

#Mosh way
list = [2, 3, 1, 5, 2, 1, 3, 9, 9]
unique = []

for number in list:
    if number not in unique:
        unique.append(number)

print(unique)

x, y, z, a, b = unique
print(x)


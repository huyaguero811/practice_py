#for item in [1, 2, 3, 4]:
#    print(item)
#for huy in range(5, 10, 2):
#    print(huy)

price = [10, 20, 30]
huy = 0
total = 0
for huy in price:
    total += huy

print(total)

#for x in range(4):
 #   for y in range(2):
  #      print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
#for huy in numbers:
 #   print("x" * huy)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Huy'
print(names[2:-1])

lists = [3, 4, 2, 1, 5, 10, 11, 0]
max = lists[0]
for b in lists:
    if max < b:
        max = b

print(max)




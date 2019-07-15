matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#matrix[0][0] = 21
#print(matrix[0][0])

#for list in matrix:
 #   for item in list:
  #      print(item)

numbers = [5, 2, 3, 5, 1, 9]
numbers.append(20)
numbers.insert(1, 11)
numbers.remove(2)
print(numbers)

numbers.pop()    #remove the last item of the list
print(numbers)

print(numbers.index(5))  #index the position of the number, if the number not on the list -> error

print(20 in numbers)  #check for the existence of the number

print(numbers.count(5))

numbers.sort()  #sắp xếp theo thứ tự dãy số trong list theo thứ tự tăng dần
print(numbers)

numbers.reverse() #sắp xếp theo thứ tự giảm dần
print(numbers)

numberss2 = numbers.copy()
numbers.append(100)

print(numbers)

numbers.clear()
print(numbers)

print("shitty adsss")


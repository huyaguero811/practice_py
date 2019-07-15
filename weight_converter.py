weight = float(input("Weight: "))
w_type = input("L(bs) or (K)g: ")
# lbs = float(weight) * 0.45
# kg = float(weight) / 0.45

if w_type.upper() == "L":      #the upper method will make the data input uppercase
    converted = weight * 0.45
    print(f'You are {converted} kgs')

elif w_type.upper() == "K":
    converted = weight / 0.45      # // will give us an integer
    print(f'You are {converted} pounds')

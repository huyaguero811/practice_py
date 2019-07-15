is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink more water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

good_credit = False
price = 1000000
if good_credit:
    print("You'll need to put down 10%")
    print(f"The put down payment price is: ${price * 0.1}")
else:
    print("You'll have to double it, 20%")
    print(f"The price is: ${price * 0.1}")

# Logical Operator
high_income = True
good_credit = False

if high_income and not good_credit:
    print("Eligible for loan")
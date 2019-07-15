translate = {
    '1' : "One",
    '2' : "Two",
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',

}



phone = input("Phone: ")
output = ""
for number in phone:
    output += translate.get(number, '!') + " "

print(output)

print(translate.get('Wtf', 'adf'))

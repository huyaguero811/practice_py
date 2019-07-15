message = input(">")
words = message.split(' ')

emojis = {
    ':)' : '😊',
    ':(' : '☹',
    ':))' : '😂'
}
output = ""
for each in words:
 #   for a in emojis:
 #       if each == a:                         Đây là cách của Huy!
 #           each = emojis.get(a)

    output += emojis.get(each, each) + " "

print(output)
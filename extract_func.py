def emojis(message):
    words = message.split(' ')

    emojis = {
        ':)': '😊',
        ':(': '☹',
        ':))': '😂'
    }
    output = ""
    for each in words:
        output += emojis.get(each, each) + " "
    return output


message = input('>')
print(emojis(message))
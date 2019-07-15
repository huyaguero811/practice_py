
start = "Car started.. Ready to go"
stop = "Car stopped"

started = False
while True:
    command = input(">").upper()
    if command == "START":
        if started:
            print("Hey, you've already start the engine!")
        else:
            started = True
            print(start)
    elif command == "STOP":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print(stop)
    elif command == "QUIT":
        break
    elif command == "HELP":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    else:
        print("I dont understand")


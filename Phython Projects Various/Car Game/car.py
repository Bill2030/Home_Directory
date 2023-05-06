print("Welcome to car game")
command = ""
while command != "quit":
    command = input(">")
    if command == "start":
        print("car started and ready to go !")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
        start - for the car to get started
        stop - for the car to stop
        quit - for the car to quit
        """)
    elif command == "quit":
        exit()
else:
    print("I dont understand this")


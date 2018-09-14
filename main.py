print("To start, type \'start\'")
fromUser = input()
while True:
    if fromUser == "start":
        print("START GAME!")
    elif fromUser == "quit": # else if
        print("So soon?")
        break # Ends the while loop    
    else:
    elif fromUser.split()[0] == go:
        print("Go somewhere")
    elif fromUser == "attack":
        print("Attack a thing")
    else:
        print("To start, type'start'")
    fromUser = input()

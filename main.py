print("To start, type \'start\'")
fromUser = input()
while True:
    if fromUser == "start":
        print("START GAME!")
    elif fromUser == "quit": # else if
        print("Game over!!!!!!!")
        break # Ends the while loop    
    else:
        print("To start, type'start'")
    fromUser = input()
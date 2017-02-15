import random
def fair_or_cheat_mode():
	""" extra credit: determines whether the computer cheats (return 0) or plays fair (return 1) """
    return random.randrange(2)
def winner(user, mode):
    """ takes user's choice, computer mode (fair or cheating), generates computer's choice based on the mode, 
        and returns the winner """
    rps = {1: "rock", 2: "paper", 3: "scissors"}
    if mode:
        computerchoice = random.randrange(1,4)
    else:
        if user == 3:
            computerchoice = user - 2
        else:
            computerchoice = user + 1
    if user == computerchoice:
        return "%s vs %s: It's a draw!" % (rps[user], rps[computerchoice])
    elif (user - computerchoice == -1) or (user - computerchoice == 2):
        return "The computer's %s beats your %s!" % (rps[computerchoice], rps[user])
    else:
        return "Your %s beats the computer's %s!" % (rps[user], rps[computerchoice])
def convert_input(input):
    """ returns user input to int that can be used to call winner(),
        or translate the mode the computer was playing in """
    choices = {"r": 1, "p": 2, "s": 3, 0: "cheating", 1: "playing fair"}
    return choices[input]
if __name__ == '__main__':
    # ask user for a choice until player quits
    playing = True
    while playing:
        userchoice = input("Choose (r)ock, (p)aper, or (s)cissors: ")
        if userchoice.strip().lower()[0] not in "rps":
            print("Invalid choice.")
            continue
        else: 
            # picks the computer mode for this particular game
            mode = fair_or_cheat_mode()
            print(winner(convert_input(userchoice.strip().lower()[0]), mode))
            # lets user know if the computer was playing fair or cheating
            print("The computer was %s" % convert_input(mode))
            user_continues = input("Play again? (Y/N) ")
            if user_continues.strip()[0] in "Yy":
                continue
            else:
                playing = False

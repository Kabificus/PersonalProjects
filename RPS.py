import random


def rps_actions():
    user_action = input("Rock, paper, or scissors? (Quit to exit)").lower()
    possible_choices = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_choices)
    while user_action == "quit":
        exit()
    wins, ties, losses = run_rps(user_action, computer_action)
    return wins, ties, losses


def tally_holder():
    win = 0
    tie = 0
    loss = 0
    while win < 2 or tie < 3 or loss < 2:
        wins, ties, losses = rps_actions()
        win = win + wins
#        print(wins)
        tie = tie + ties
#        print(tie)
        loss = loss + losses
#        print(loss)
        if win == 2:
            break
        if tie == 3:
            break
        if loss == 2:
            break
    if win == 2:
        print("You won overall!")
    elif tie == 3:
        print("You tied 3 times, you make me sick")
    elif loss == 2:
        print("Sorry, you lost the game")
    else:
        print("ERROR")
    restart_game()


def run_rps(var1, var2):
    xyz = 0
    abc = 0
    jkl = 0
    if var1 == var2:
        print(f"Both players selected the same option. It's a tie!")
        print("Just a heads up, this is annoying; don't do it again")
        abc = abc + 1
        return xyz, abc, jkl
    elif var1 == "rock":
        if var2 == "scissors":
            print("Rock crushes scissors. You win!")
            xyz = xyz + 1
            return xyz, abc, jkl
        elif var2 == "paper":
            print("Rock gets covered by paper. You lose!")
            jkl = jkl + 1
            return xyz, abc, jkl
    elif var1 == "paper":
        if var2 == "rock":
            print("Paper covers rock. You win!")
            xyz = xyz + 1
            return xyz, abc, jkl
        elif var2 == "scissors":
            print("Paper gets cut up by scissors. You lose!")
            jkl = jkl + 1
            return xyz, abc, jkl
    elif var1 == "scissors":
        if var2 == "paper":
            print("Scissors cuts paper. You win!")
            xyz = xyz + 1
            return xyz, abc, jkl
        elif var2 == "rock":
            print("Scissors gets crushed by rock. You lose!")
            jkl = jkl + 1
            return xyz, abc, jkl
    else:
        print(f"{var1} is not a valid response")
        return xyz, abc, jkl


def restart_game():
    retry = input("Press anything to play again (Quit to exit)").lower()
    while retry != "quit":
        tally_holder()
    else:
        exit()


tally_holder()

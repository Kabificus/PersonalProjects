space = [False, False, False, False, False, False, False, False, False]
spot = [False, False, False, False, False, False, False, False, False]

def instructions():
    print("In tic-tac-toe the goal is to get 3 shapes in a row")
    print("In this simulator, your inputs are always 'X'")
    print("Additionally, your inputs can be selected by inputting numbers")
    print("The following is the format for inputs")
    for i in range(1, 4):
        if i < 3:
            print(i, end=' | ')
        else:
            print(i)
    for i in range(4, 7):
        if i < 6:
            print(i, end=' | ')
        else:
            print(i)
    for i in range(7, 10):
        if i < 9:
            print(i, end=' | ')
        else:
            print(i)
    print("When prompted, type in the block where you want to place your input")


def jones():
    for i in range(0, 9):
        while i != 2 or i != 5 or i != 8:
            if i == 2 or i == 5 or i == 8:
                if space[i] is False:
                    print('_')
                    break
                if space[i] is True:
                    if spot[i] is True:
                        print('X')
                        break
                    if spot[i] is False:
                        print('O')
                        break
            if space[i] is False:
                print('_ |', end=' ')
                break
            if space[i] is True:
                if spot[i] is True:
                    print('X |', end=' ')
                    break
                if spot[i] is False:
                    print('O |', end=' ')
                    break
    print()
    runCheck()
    chooseSpace()



def chooseSpace():
    reason = input('Which space would you like to place the "X"?')
    if isinstance(reason, int) is True:
        print("ERROR: That response is not valid, try to input a integer between 1-10")
        chooseSpace()
    if len(reason) >= 2:
        print("ERROR: That's too many numbers, input them one at a time")
        chooseSpace()
    choice = int(reason) - 1
    if space[choice] is True:
        print('That space is already occupied')
        chooseSpace()
    else:
        space[choice] = True
        spot[choice] = True
    jones()


def runCheck():
    if space[0] is True:
        verticalCheck(0)
        horizonalCheck(0)
        diagonalCheck(0)
    if space[1] is True:
        verticalCheck(1)
    if space[2] is True:
        verticalCheck(2)
        reverseDiagonalCheck(2)
    if space[3] is True:
        horizonalCheck(3)
    if space[6] is True:
        horizonalCheck(6)


def diagonalCheck(tooth):
    winCheck = 0
    loseCheck = 0
    for s in range(tooth, 9, 4):
        if spot[s] is True:
            winCheck += 1
        else:
            loseCheck -= 1
    finalCheck(winCheck, loseCheck)


def horizonalCheck(tooth):
    winCheck = 0
    loseCheck = 0
    for s in range(tooth, tooth + 3):
        if spot[s] is True:
            winCheck += 1
        else:
            loseCheck += 1
    finalCheck(winCheck, loseCheck)

def verticalCheck(tooth):
    winCheck = 0
    loseCheck = 0
    for s in range(tooth, 9, 3):
        if spot[s] is True:
            winCheck += 1
        else:
            loseCheck -= 1
    finalCheck(winCheck, loseCheck)

def reverseDiagonalCheck(tooth):
    winCheck = 0
    loseCheck = 0
    for s in range(tooth, 9, 2):
        if spot[s] is True:
            winCheck += 1
        else:
            loseCheck -= 1
    finalCheck(winCheck, loseCheck)


def finalCheck(win, lose):
    if win == 3:
        print('You won!')
        quit()
    elif lose == 3:
        print('You lose!')
        quit()
    else:
        return


chooseSpace()
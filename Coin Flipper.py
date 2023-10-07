import random

Heads = 0
Tails = 0
headStreak = 0
tailStreak = 0
lastHeads = False
lastTails = False
lastStreakHeads = 0
lastStreakTails = 0

chosenFlips = input("How many coin flips would you like to do?")

while chosenFlips.isdigit() == False:
    print("Thats not a valid response")
    chosenFlips = input("Please put in a numerical value:")
#    if chosenFlips.isdigit() == True:
#        break

for c in range(int(chosenFlips)):
    possibleChoices = ["Heads", "Tails"]
    coinFlip = random.choice(possibleChoices)
    if coinFlip == "Tails":
        Tails += 1
        tailStreak += 1
        lastTails = True
        if lastHeads == True:
            if lastStreakHeads < headStreak:
                lastStreakHeads = headStreak
            lastHeads = False
            headStreak = 0

    elif coinFlip == "Heads":
        Heads += 1
        headStreak += 1
        lastHeads = True
        if lastTails == True:
            if lastStreakTails < tailStreak:
                lastStreakTails = tailStreak
            lastTails = False
            tailStreak = 0

    print(coinFlip)

longestStreak = max(lastStreakTails, lastStreakHeads)
winner = max(Heads, Tails)

print(Heads, "heads and", Tails, "tails")

if Heads == Tails:
    print("It's a tie!")
elif winner == Heads:
    print("Heads wins!")
elif winner == Tails:
    print("Tails wins!")

if lastStreakHeads == lastStreakTails:
    print("The longest streak was tied for", lastStreakTails,"on both sides")
elif longestStreak == lastStreakHeads:
    print("The longest streak was", lastStreakHeads, "heads!")
elif longestStreak == lastStreakTails:
    print("The longest streak was", lastStreakTails, "tails!")
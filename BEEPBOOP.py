import random
import winsound

money = 50


def roll():
    global money
    if money <37:
        money = 38

    
    winsound.Beep(money*5,int(money/2))
    
    fruits = ["Cherry","Bell","Lemon","Orange","Star","Skull"]

    win1 = random.randint(0,5)
    win2 = random.randint(0,5)
    win3 = random.randint(0,5)

    if win1 == 0 and win2 == 0 and win3 == 0:
        money = money + 4
    elif win1 == 1 and win2 == 1 and win3 == 1:
        money = money + 30
    elif win1 == 2 and win2 == 2 and win3 == 2:
        money = money + 5
    elif win1 == 3 and win2 == 3 and win3 == 3:
        money = money + 5
    elif win1 == 4 and win2 == 4 and win3 == 4:
        money = money + 5
    elif win1 == 5 and win2 == 5 and win3 == 5:
        money = money - 25

    if win1 == 0 and win2 == 0:
        money = money + 2
    elif win1 == 1 and win2 == 1:
        money = money + 5
    elif win1 == 2 and win2 == 2:
        money = money + 2
    elif win1 == 3 and win2 == 3:
        money = money + 2
    elif win1 == 4 and win2 == 4:
        money = money + 2
    elif win1 == 5 and win2 == 5:
        money = money - 20

    if win3 == 0 and win2 == 0:
        money = money + 2
    elif win3 == 1 and win2 == 1:
        money = money + 5
    elif win3 == 2 and win2 == 2:
        money = money + 2
    elif win3 == 3 and win2 == 3:
        money = money + 2
    elif win3 == 4 and win2 == 4:
        money = money + 2
    elif win3 == 5 and win2 == 5:
        money = money - 20

    if win3 == 0 and win1 == 0:
        money = money + 2
    elif win3 == 1 and win1 == 1:
        money = money + 5
    elif win3 == 2 and win1 == 2:
        money = money + 2
    elif win3 == 3 and win1 == 3:
        money = money + 2
    elif win3 == 4 and win1 == 4:
        money = money + 2
    elif win3 == 5 and win1 == 5:
        money = money - 20
        
    print(money)

    save = open("CasinoLog (Maybe fill up school storage)","a")
    save.write(fruits[win1])
    save.write(" ")
    save.write(fruits[win2])
    save.write(" ")
    save.write(fruits[win3])
    save.write("\n")
    save.close()

    
    roll()
roll()

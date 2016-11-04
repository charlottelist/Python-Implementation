#Charlotte List and Matt Lau-Hansen
#YAHTZEE
#Final Project
#December 2, 2014



from graphics import *
from buttonclass import Button
from random import *
from time import *
from math import *
from dieview import *
#from grid import *

def selectionSort(nums):
    n = len(nums)

    for i in range(n):
        minpos = i
        for j in range(i,n):
            if nums [j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
    return nums

def fourOfAKind(dieList):
    #returns the sum of the die if these dice represent 4 of a  kind, else returns 0
    total = 0
    for x in range(0, 6):
        num = dieList.count(x)
        if num == 4:
            for item in dieList:
                total = total + item
            return total
        
    return total

def threeOfAKind(dieList):
    #returns the sum of the die if these dice represent 3 of a  kind, else returns 0
    total = 0
    for x in range(0, 7):
        num = dieList.count(x)
        if num == 3:
            for item in dieList:
                total = total + item
            return total
        
    return total
        
def fullHouse(dieList):
    #returns 25 if these dice represent a full house (2 of a kind and 3 of a kind), else returns 0
    for i in range(0, 7):
        for x in range(0, 7):
            if exactlyN(dieList, i, 2) == True and exactlyN(dieList, x, 3):
                return 25
    return 0
            
                
def hasN(dieList, n):
    #returns total if the dice contain at least n of one number, false otherwise
    num = dieList.count(n)
    if num >=1:
        total = num * n
        return total
    else:
        return 0
##
def exactlyN(dieList, t, n):
    #returns True if the dice contain n number of a certain value, false if otherwise
    num = dieList.count(t)
    if num == n:
        return True
    else:
        return False

def yahtzee(dieList):
    for i in range(0,7):
        if exactlyN(dieList, i, 5) == True:
            return 50
    return 0
def smallStraight(dieList):
    sortlist = dieList
    sortlist = selectionSort(sortlist)
    newlist = []
    straight = []
    straight1 = []
    straight2 = []
    smallstraight1 = [1,2,3,4]
    smallstraight2 = [2,3,4,5]
    smallstraight3 = [3,4,5,6]
    for item in sortlist:
        if item not in newlist:
            newlist.append(item)
    for item in newlist:
        for value in smallstraight1:
            if value == item:
                straight.append(item)
    for item in newlist:
        for value in smallstraight2:
            if value == item:
                straight1.append(item)
    for item in newlist:
        for value in smallstraight3:
            if value == item:
                straight2.append(item)
    if len(straight) == 4:
        return 30
    elif len(straight1) == 4:
        return 30
    elif len(straight2) == 4:
        return 30
    else:
        return 0

    

def largeStraight(dieList):
    newlist = []
    for item in dieList:
        if item not in newlist:
            newlist.append(item)
    if len(newlist) ==5:
        if max(newlist)-min(newlist) ==4:
            return 40
        else:
            return 0
    else:
        return 0
    
        

def main():
    win = GraphWin("Play Yahtzee1!", 1200, 600) #make a graphical window
    win.setCoords(0, 0, 200, 100) #change the coordinates to make it easier to work with
    win.setBackground("lightblue")
    title = Text(Point(50, 90), "Play Yahtzee!")
    title.setStyle("bold")
    title.setSize(36)
    title.draw(win)

    Play = Button(win, Point(50, 50), 20, 20, "Click to Play!")
    rulesFile = open("rules.txt", "r", encoding = "utf-8")
    string = rulesFile.read()
    rules = Text(Point(150, 50), string)
    rules.draw(win)
    
    pt = win.getMouse()
    
    while Play.isClicked(pt) == False:
        pt = win.getMouse()
        
    rules.undraw()
    Play.label.undraw()
    Play.rect.undraw()

    playerButton = Button(win, Point(50, 10), 10, 10, "Roll Dice")
    nextTurn = Button(win, Point(70, 10), 10, 10, "Next Turn")
    nextTurn.deactivate()
    playerButton.activate()
    quitButton = Button(win, Point(5, 95), 5, 5, "Quit")
    pt = win.getMouse()
    scoreChart = Text(Point(150, 90), "Yahtzee Score Card")
    scoreChart.setStyle("bold")
    scoreChart.draw(win)

    scoreLabels = ["Total", "Lower Total", "Chance", "Yahtzee", "Full House", \
                   "Large Straight", "Small Straight", "Four of a Kind", "Three of a Kind", "Upper Total", \
                   "Sixes", "Fives", "Fours", "Threes", "Twos", "Ones"]

    scoreButtons = []
    ptX = 140
    ptY = 10
    for i in range(16):
        b = Button(win, Point(ptX, ptY), 15, 5, scoreLabels[i])
        scoreButtons.append(b)
        ptY = ptY + 5

    a = 0
    playerScores = [0]*16
    turnCount = 1

    while quitButton.isClicked(pt) == False:
        a = 0
        numRolls = Text(Point(50, 70), "Roll Number:"+str(a+1)+"/3")
        if a !=0 and a<3:
            playagain = True
        elif a == 0:
            die1 = DieView(win, Point(10, 40), 10)
            die2 = DieView(win, Point(30, 40), 10)
            die3 = DieView(win, Point(50, 40), 10)
            die4 = DieView(win, Point(70, 40), 10)
            die5 = DieView(win, Point(90, 40), 10)
            listDie = [die1, die2, die3, die4, die5]
            totalpoints = 0
            pointValue = []

            scoreList = [0, 0, 0, 0, 0]
            allDie = [0, 1, 2, 3, 4]
            b = 0
            playerDie = [0, 0, 0, 0, 0]
            pointList = []
            playagain = True
        
        while playagain == True:


            b = 0
            indexList = []
            if playerButton.isClicked(pt) == True and a < 3:

                numRolls.draw(win)
                if indexList == []:
                    for item in listDie:
                        point = randrange(1,7)
                        scoreList[b] = point
                        item.setValue(point)
                        b = b + 1
                else:
                    for x in allDie:
                        if x not in indexList:
                            point = randrange(1, 7)
                            scoreList[b] = point
                            listDie[x].setValue(point)
                            b = b + 1

                playerButton.deactivate()
                prompt = Text(Point(50, 50), "Click on the dice you want to keep, then roll again.")
                prompt.setStyle("bold")
                prompt.setSize(18)
                prompt.draw(win)
                keepDice = Button(win, Point(50, 60), 10, 10, "Keep Dice")
                keepDice.activate()


                listScores = []
                c = 10
                for x in range(0, 16):
                    scoreText = Text(Point(150, c), playerScores[x])
                    listScores.append(scoreText)
                    scoreText.draw(win)
                    c = c + 5

                pt = win.getMouse()

                sortDie = []

                while keepDice.isClicked(pt) == False:

                    #die 1
                    xmin = 5
                    ymin = 35
                    ymax = 45
                    newX = 10
                    newY = 20
                    for i in range(0, 5):
                        if pt.getX() <= xmin + 10 and pt.getX()>= xmin and pt.getY() <= ymax and pt.getY() >= ymin:
                            totalpoints = totalpoints + scoreList[i]
                            sortDie.append(listDie[i])
                            listDie[i].undraw(win)
                            playerDie[i] = DieView(win, Point(newX, newY), 5)
                            playerDie[i].setValue(scoreList[i])
                            indexList.append(i)
                            pointList.append(scoreList[i])
                        xmin = xmin + 20
                        newX = newX +20
                    
                    pt = win.getMouse()
                #end while keepDice not clicked
                keepDice.deactivate()
                numRolls.undraw()
                a = a + 1
                numRolls = Text(Point(50, 70), "Roll Number:"+str(a+1)+"/3")

                playerButton.activate()
                if a == 3:
                    playerButton.deactivate()
                    #nextTurn.activate()
                    scorePrompt = Text(Point(120, 50), "Click a category to score.")
                    scorePrompt.draw(win) #activate score buttons
                points = 0
                for item in pointList:
                    points = points + item
            
            #end if roll dice is clicked and a<3


 #           pt = win.getMouse()

            #check which score button is clicked

##            if pt.getX() >140 and pt.getX() <155 and pt.getY() >10 and pt.getY() < 90:
                ones = hasN(pointList, 1)
                twos = hasN(pointList, 2)
                threes = hasN(pointList, 3)
                fours = hasN(pointList, 4)
                fives = hasN(pointList, 5)
                sixes = hasN(pointList, 6)
                threekind = threeOfAKind(pointList)
                fourkind = fourOfAKind(pointList)
                uppertotal = ones+twos+threes+fours+fives+sixes
                fullhouse = fullHouse(pointList)
                Yahtzee = yahtzee(scoreList) + yahtzee(pointList)
                smallstraight = smallStraight(pointList)
                largestraight = largeStraight(pointList)
                chance = ones+twos+threes+fours+fives+sixes
                lowertotal = threekind + fourkind +fullhouse +Yahtzee +smallstraight + largestraight
                totalFINAL = uppertotal +lowertotal
                funcList = [totalFINAL, lowertotal, chance, Yahtzee, fullhouse, largestraight, smallstraight,\
                         fourkind, threekind, uppertotal, sixes, fives, fours, threes, twos, ones]
                
            for i in range(0, 16):
                if scoreButtons[i].isClicked(pt) == True:
                    scoreButtons[i].deactivate()
                    playerScores[i] = funcList[i]
                    nextTurn.activate()
                    scorePrompt.undraw()

            pt = win.getMouse()
                
            if nextTurn.isClicked(pt):
                playagain = False
                for item in playerDie:
                    item.undraw(win)
                nextTurn.deactivate()
                playerButton.activate()
                prompt.undraw()
                numRolls.undraw()
                turnCount = turnCount + 1
                if turnCount > 13:
                    playerButton.deactivate()
                    playerScores[9] = playerScores[10] + playerScores[11] + playerScores[12] + \
                                      playerScores[13] + playerScores[14] + playerScores[15]
                    playerScores[1] = playerScores[2] + playerScores[3] + playerScores[4] + playerScores[5] \
                                      + playerScores[6] + playerScores[7]+ playerScores[8]
                    playerScores[0] = playerScores[1] + playerScores[9]
                    d = 10
                    for item in listScores:
                        item.undraw()
                    for x in range(0, 16):
                        scoreText = Text(Point(150, d), playerScores[x])
                        scoreText.draw(win)
                        d = d + 5
                    thankyou = Text(Point(140, 5), "Thank you for playing. Quit to close")
                    thankyou.draw(win)
            for item in listScores:
                item.undraw()

                

        #end while play again is True
    
        pt = win.getMouse()
    #end quitButton not clicked



    win.close()


main()

#13 times
# then done


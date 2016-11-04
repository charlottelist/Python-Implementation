#Charlotte and Scott
#Programming Assignment 5
#COM 110
#Due: November 11, 2014

from playingcard import PlayingCard
from deck import Deck
from buttonclass import Button
from graphics import *
from random import *
from blackjack import BlackJack

def main():
    
    win = GraphWin("Play Black Jack!", 800, 600) #make a graphical window
    win.setBackground("red") #set the color to red
    intro = Text(Point(400, 200), "Black Jack!") #intro to the user
    intro.setStyle("bold") #set the style
    intro.setSize(36) #change the size
    intro.draw(win) #draw it
    prompt = Text(Point(400, 300), "Click to play!") #prompt the user
    prompt.setSize(18)
    prompt.draw(win)
    startbutton = Button(win, Point(400, 400), 100, 50, "Play!") #start button to play
    startbutton.activate()
    askMoney = Text(Point(400, 500), "How much money do you want to play with?")
    askMoney.draw(win)
    moneyBox = Entry(Point(400, 525), 10)
    moneyBox.draw(win)
    pt = win.getMouse() #wait for click
    while startbutton.isClicked(pt) == False: #if the click is not on the button, get another click
        pt = win.getMouse()
    totalMoney = int(moneyBox.getText())
    intro.undraw() #clear the window
    prompt.undraw()
    startbutton.rect.undraw()
    startbutton.label.undraw()
    askMoney.undraw()
    moneyBox.undraw()
    play = True #set play to true, user wants to play
    while play == True: #while this is true, run the game
        win.setBackground("lightblue") #change the color
        button1 = Button(win, Point(300, 300), 100, 50, "Hit") #set up buttons
        button2 = Button(win, Point(500, 300), 100, 50, "Stand")
        button3 = Button(win, Point(400, 500), 50, 50, "Quit")
        playagain = Button(win, Point(700, 500), 100, 100, "Play again!")
        playagain.deactivate() #not active button
        button1.deactivate() #deactivate buttons
        button2.deactivate()
        button3.deactivate()
        
        askforbet = Text(Point(700, 100), "Place bet here.")
        askforbet.draw(win)
        inputBox = Entry(Point(700, 125), 10)
        inputBox.draw(win)
        betButton = Button(win, Point(700, 200), 50, 50, "Bet!")

        dealerText = Text(Point(100, 100), "Dealer") #set up the text 
        dealerText.draw(win)
        playerText = Text(Point(100, 400), "Player") #set up the text
        playerText.draw(win)
        
        deck1 = Deck() #make the deck of cards to be used in the game
        dealerHand = [] #set up the dealer's hand
        playerHand = [] #set up the dealer's hand
        game = BlackJack(dealerHand, playerHand) #set up the black jack game
        game.initDeal(win, 200, 100, 200, 400) #deal out the first two cards to each
        dealercardHide = Image(Point(200, 100), "b1fv.gif") #back of card to hide dealer's card
        dealercardHide.draw(win)

        dealerTotal = Text(Point(100, 125), "Total: "+str(game.evaluateHand(dealerHand)))
 #       dealerTotal.draw(win) #total up the hand of the dealer

        playerTotal = Text(Point(100, 425), "Total: "+str(game.evaluateHand(playerHand)))
        playerTotal.draw(win) #total up the hand of the player
        playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
        playerMoney.draw(win)
        pt = win.getMouse() #wait for mouse click

        while button1.isClicked(pt) == False and button2.isClicked(pt) == False and \
              button3.isClicked(pt) == False and betButton.isClicked(pt)==False: #if click is not on button, get another mouse click
            pt = win.getMouse()

        if betButton.isClicked(pt) == True:
            bet = inputBox.getText()
            while bet == "":
                tryAgain = Text(Point(700, 255), "You forgot to enter a bet!")
                tryAgain.draw(win)
                pt = win.getMouse()
                if betButton.isClicked(pt) == True:
                    bet = inputBox.getText()
                tryAgain.undraw()
            bet = int(bet)
            while bet > totalMoney:
                tryAgain = Text(Point(700, 255), "You don't have that much money. \nTry again.")
                tryAgain.draw(win)
                inputBox.setText("")
                pt = win.getMouse()
                if betButton.isClicked(pt):
                    bet = int(inputBox.getText())
                tryAgain.undraw()
            betButton.deactivate()
            playerBet = Text(Point(100, 575), "Bet:  $"+str(bet))
            playerBet.draw(win)
            button1.activate()
            button2.activate()
            button3.activate()
            pt = win.getMouse()
        xPos = 400 #set x value of cards
        cardHitlist = [] #make a list to store all new cards that are dealt
        while button1.isClicked(pt) == True: #if a hit
            cardHit = game.hit(win, xPos, 400) #hit 
            cardHitlist.append(cardHit) #add card to the list
            #how to get a second hit card to be next to it, not on top?
            playerTotal.undraw()
            playerTotal = Text(Point(100, 425), "Total: "+str(game.evaluateHand(playerHand)))
            playerTotal.draw(win) #update the total
            dealerCardlist = []
            if game.evaluateHand(playerHand) > 21: #if the player's score is over 21
                dealercardHide.undraw() #show the dealers card
                dealerTotal.draw(win)
                resultText = Text(Point(400, 200), "You busted! The dealer wins.") #busted
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                button1.deactivate() #deactivate buttons
                button2.deactivate()
                playagain.activate()
                totalMoney = totalMoney - bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
                pt = win.getMouse() #get another click, can play again
            elif game.evaluateHand(playerHand) == 21: #if equal to 21
                dealercardHide.undraw() #show dealers card
                dealerTotal.draw(win)
                resultText = Text(Point(400, 200), "Your total is "+str(game.evaluateHand(playerHand))+"."
                                  "  You win!")
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                button1.deactivate() #deactivate other buttons
                button2.deactivate()
                playagain.activate()
                totalMoney = totalMoney + bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
                pt = win.getMouse() #wait for click, can play again
            elif game.evaluateHand(playerHand) < 21: #if less than 21, can go again!
                pt = win.getMouse()
            xPos = xPos + 100 #add 100 pixels to x value so cards are not on top of each other

        while button2.isClicked(pt) == True: #if stand
            dealerCardlist = game.dealerPlays(win, game, 400, 100) #dealer plays out hand
            dealercardHide.undraw()
            dealerTotal.undraw()
            dealerTotal = Text(Point(100, 125), "Total: "+str(game.evaluateHand(dealerHand)))
            dealerTotal.draw(win) #update dealer total
            button1.deactivate() #deactivate buttons
            button2.deactivate()
            if game.evaluateHand(dealerHand) > 21: #if dealer hand is over 21, they busted
                dealercardHide.undraw()
                resultText = Text(Point(400, 200), "The dealer busted. You win!") #you win yay!
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                totalMoney = totalMoney + bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
            elif game.evaluateHand(dealerHand) == 21: #if dealer hand equals 21, they win. sorry
                dealercardHide.undraw()
                resultText = Text(Point(400, 200), "The dealer's total is "+str(game.evaluateHand(dealerHand))+"."
                                      " Your total is "+str(game.evaluateHand(playerHand))+".  The dealer wins.")
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                totalMoney = totalMoney - bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
            elif game.evaluateHand(dealerHand) < 21 and game.evaluateHand(playerHand) > \
                game.evaluateHand(dealerHand): #player wins if their hand is bigger than dealers hand
                dealercardHide.undraw()
                resultText = Text(Point(400, 200), "The dealer's total is "+str(game.evaluateHand(dealerHand))+"."
                                      "Your total is "+str(game.evaluateHand(playerHand))+".  You win!")
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                totalMoney = totalMoney + bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
            elif game.evaluateHand(dealerHand) < 21 and game.evaluateHand(playerHand) < \
                 game.evaluateHand(dealerHand): #if both hands less than 21, player hand less than dealer
                #then the dealer wins
                dealercardHide.undraw()
                resultText = Text(Point(400, 200), "The dealer's total is "+str(game.evaluateHand(dealerHand))+"."
                                      "Your total is "+str(game.evaluateHand(playerHand))+".  The dealer wins.")
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
                totalMoney = totalMoney - bet
                playerMoney.undraw()
                playerMoney = Text(Point(100, 550), "Money: $ "+str(totalMoney))
                playerMoney.draw(win)
            elif game.evaluateHand(dealerHand) < 21 and game.evaluateHand(playerHand) == \
                 game.evaluateHand(dealerHand): #if a tie
                dealercardHide.undraw()
                resultText = Text(Point(400, 200), "It's a tie.") #stand off
                resultText.setStyle("bold")
                resultText.setSize(20)
                resultText.draw(win)
            playagain.activate() #activate the play again button, so they can play again
            pt = win.getMouse() #wait for click

            
        if playagain.isClicked(pt) == True: #if the button is clicked player wants to play again
##            if totalMoney == 0:
##                resultText.undraw()
##                resultText = Text(Point(400, 200), "You lost all your money. Game over.") #stand off
##                resultText.setStyle("bold")
##                resultText.setSize(20)
##                resultText.draw(win)
##                playagain.rect.undraw()
##                playagain.label.undraw()
##                button1.rect.undraw()
##                button1.label.undraw()
##                button2.rect.undraw()
##                button2.label.undraw()
##                button3.activate()
##                dealerTotal.undraw()
##                playerTotal.undraw()
##                askforbet.undraw()
##                inputBox.undraw()
##                betButton.rect.undraw()
##                betButton.label.undraw()
##                playerMoney.undraw()
##                playerBet.undraw()
##                playerText.undraw()
##                dealerText.undraw()
##                for card in cardHitlist: #undraw the cards that were hit
##                    card.undraw()
##                for card in dealerCardlist: #undraw the cards that the dealer got
##                    card.undraw()
 #       else:
            play = True
            resultText.undraw() #clear the previous game
            playagain.rect.undraw()
            playagain.label.undraw()
            button1.rect.undraw()
            button1.label.undraw()
            button2.rect.undraw()
            button2.label.undraw()
            button3.rect.undraw()
            button3.label.undraw()
            dealerTotal.undraw()
            playerTotal.undraw()
            askforbet.undraw()
            inputBox.undraw()
            betButton.rect.undraw()
            betButton.label.undraw()
            playerMoney.undraw()
            playerBet.undraw()
            playerText.undraw()
            dealerText.undraw()
            for card in cardHitlist: #undraw the cards that were hit
                card.undraw()
            for card in dealerCardlist: #undraw the cards that the dealer got
                card.undraw()
            #need to undraw the new cards before replaying
        if button3.isClicked(pt) == True:
            play = False #if clicks quit, end the game
            gwin = GraphWin("Results!", 300, 300)
            gwin.setBackground("black")
            score = Text(Point(150, 100), "Your score is: $"+str(totalMoney)+".")
            score.setFill("white")
            score.draw(gwin)
            info = Text(Point(150, 175), "The high scores have been recorded in the file\n"
                        "highscores.txt on your computer. See where you ranked!")
            info.setFill("white")
            info.draw(gwin)
            outputFileName = "highscores.txt"
            outputFile = open(outputFileName, "a")
            outputFile.write("\nScore:  $"+str(totalMoney)+".")
            close = Text(Point(150, 250), "Click anywhere to close.")
            close.setFill("white")
            close.draw(gwin)
            gwin.getMouse()
            gwin.close()
        
    win.close()
        

main()

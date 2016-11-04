#Programming Assignment 5
#Black Jack
#Scott and Charlotte
#November 8, 2014

from playingcard import PlayingCard
from deck import Deck
from buttonclass import Button
from graphics import *
from random import *
#create a class with subclass deck
class BlackJack(Deck):
    def __init__(self, dHand = [], pHand = []):
        """constructor that initializes instance variables it also gives the playingDeck an initial shuffle"""
        self.dealerHand = dHand
        self.playerHand = pHand
        self.playingDeck = Deck()
        self.playingDeck.shuffleCards()

    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        """deals out initial cards, 2 per player and displays dealer and player hands on graphical win"""
        xposD2 = xposD +100 #move the cards over so they are not on top of each other
        xposP2 = xposP + 100
        card = self.playingDeck.dealCard() #deal a card from the deck
        self.dealerHand.append(card) #add the card to the dealers hand
        rank = card.getRank() #get the number
        suit = card.getSuit() #get the suit
        dealerCardimage = Image(Point(xposD, yposD), suit+str(rank)+".gif") #put the picture
        dealerCardimage.draw(gwin)

        card1 = self.playingDeck.dealCard() #add another card to the dealer's hand
        self.dealerHand.append(card1)
        rank1 = card1.getRank()
        suit1 = card1.getSuit()
        dealerCard1image = Image(Point(xposD2, yposD), suit1+str(rank1)+".gif")
        dealerCard1image.draw(gwin)
        
        pcard = self.playingDeck.dealCard() #deal a card to the player's hand
        self.playerHand.append(pcard)
        prank = pcard.getRank()
        psuit = pcard.getSuit()
        playerCardimage = Image(Point(xposP, yposP), psuit+str(prank)+".gif")
        playerCardimage.draw(gwin)

        pcard1 = self.playingDeck.dealCard() #deal a second card to the player's hand
        self.playerHand.append(pcard1)
        prank1 = pcard1.getRank()
        psuit1 = pcard1.getSuit()
        playerCardimage1 = Image(Point(xposP2, yposP), psuit1+str(prank1)+".gif")
        playerCardimage1.draw(gwin)

    def hit(self, gwin, xPos, yPos): 
        """adds a new card to the player's hand and places it at position xPos, yPos"""
        card = self.playingDeck.dealCard() #deal top card from deck
        self.playerHand.append(card)
        rank = card.getRank()
        suit = card.getSuit()
        hitCardimage = Image(Point(xPos, yPos), suit+str(rank)+".gif") #add the card to the screen
        hitCardimage.draw(gwin)
        return hitCardimage #return the picture so it can be later removed to replay the game
    def evaluateHand(self, hand):
        """totals the card in the hand that is passed in and returns total"""
        total = 0 #set accumulator variable
        for card in hand: #loop through cards
            rank = card.getRank() #get ranks
            if rank > 10: #face value cards set to 10
                rank = 10
            if rank == 1 and total + 11 <= 21: #ace is equal to 11 if total is under 11
                    rank = 11
            total = total + rank #keep adding to the value
            
        if total > 21: #set ace to one if the total goes over 11
            for card in hand:
                rank = card.getRank()
                if rank == 1:
                    total = total - 10
        return total #return the total value

    def dealerPlays(self, gwin, game, xPos, yPos):
        """dealer deals cards to herself, stopping when hitting soft 17"""
        total = game.evaluateHand(self.dealerHand) # get the dealer's total
        dealerCardlist = []
        while total <=17: #if a soft 17
            card = self.playingDeck.dealCard()
            self.dealerHand.append(card) #deal the dealer a card
            rank = card.getRank()
            suit = card.getSuit()
            dealerCardimage = Image(Point(xPos, yPos), suit+str(rank)+".gif") #add the picture
            dealerCardimage.draw(gwin)
            total = game.evaluateHand(self.dealerHand)
            xPos = xPos + 100 #move the next one over so they don't overlap
            dealerCardlist.append(dealerCardimage)
        return dealerCardlist #return a list of cards so they can be un drawn later to replay

    
def main(): #testing out the game
    
    win = GraphWin("Play Black Jack!", 800, 600)

    button1 = Button(win, Point(300, 300), 100, 50, "Hit")
    button2 = Button(win, Point(500, 300), 100, 50, "Stand")
    button3 = Button(win, Point(400, 500), 50, 50, "Quit")
    button1.activate()
    button2.activate()
    button3.activate()

    dealerText = Text(Point(100, 100), "Dealer")
    dealerText.draw(win)
    playerText = Text(Point(100, 400), "Player")
    playerText.draw(win)

    deck1 = Deck()
    game = BlackJack(dHand = [], pHand= [])
    game.initDeal(win, 200, 100, 200, 400)
##    deck1.shuffleCards()
##    dealerCard1 = deck1.dealCard()
##    dealerCard2 = deck1.dealCard()
   
##    rank1 = dealerCard1.getRank()
##    suit1 = dealerCard1.getSuit()
##    rank2 = dealerCard2.getRank()
##    suit2 = dealerCard2.getSuit()

##    dealerCard1image = Image(Point(200, 100), suit1+str(rank1)+".gif")
##    dealerCard1image.draw(win)
##
##    dealerCard2image = Image(Point(300, 100), suit2+str(rank2)+".gif")
##    dealerCard2image.draw(win)
##    
##    playerCard1 = deck1.dealCard()
##    playerCard2 = deck1.dealCard()
##
##    rank3 = playerCard1.getRank()
##    suit3 = playerCard1.getSuit()
##    rank4 = playerCard2.getRank()
##    suit4 = playerCard2.getSuit()
##
##    playerCard1image = Image(Point(200, 400), suit3+str(rank3)+".gif")
##    playerCard1image.draw(win)
##
##    playerCard2image = Image(Point(300, 400), suit4+str(rank4)+".gif")
##    playerCard2image.draw(win)

    pt = win.getMouse()
    
    if button3.isClicked(pt) == True:

        win.close()

if __name__ == "__main__":
    main()


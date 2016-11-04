#Programming Assignment 5
#Deck Class
#Scott and Charlotte
#November, 6, 2014

from playingcard import PlayingCard
from random import *

class Deck(PlayingCard):
    def __init__(self):
        """constructor that initializes the deck of cards""" 
        self.cardList = []
        for s in ["d", "c", "h", "s"]: #loop through the suits
            for r in range(1, 14): #loop through the ranks
                card = PlayingCard(r, s) #make a card each time
                self.cardList.append(card) #add tuple with suit and number to list
                
    def shuffleCards(self): #shuffle the deck
        """shuffles the deck of cards by sorting the list into a random order"""
        shuffle(self.cardList)
 
    
    def dealCard(self):
        """deals one card to a hand"""
        card1 = self.cardList[0] #take the first card from the deck, index
        self.cardList.remove(card1) #remove the card from the list
        return card1 #return the list
    
    def cardsLeft(self):
        """returns the value of number of cards left in the deck"""
        cardsLeft = len(self.cardList) #length of the list, number of cards in the deck
        return cardsLeft

    def carddeck(self): #checking the deck
        return self.cardList

    
def main(): #testing the class
    deck1 = Deck()
    deck1.shuffleCards()
    deck1.dealCard()
    asd = deck1.carddeck()
    for i in range(len(asd)):
        print(asd[i])
    print(deck1.cardsLeft())

if __name__ == "__main__":
    main()

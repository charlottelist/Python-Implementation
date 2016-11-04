#Playing Card Class
#Scott and Charlotte

#make a class
class PlayingCard:
    def __init__(self, rank, suit):
        """constructor that sets up the instance variables for rank and suit"""
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """returns the number value of the card"""
        return self.rank

    def getSuit(self):
        """returns the suit of the card"""
        return self.suit

    def BJValue(self):
        """this method changes the value of face value cards to 10"""
        bValue = self.rank
        if bValue > 10:
            bValue = 10
        return bValue

    def __str__(self):
        """method that reads the cards"""
        suits = {"s": "Spades", "d": "Diamonds", "c": "Clubs", "h": "Hearts"}
        listRanks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", \
                     "Ten", "Jack", "Queen", "King")
        
        a  = suits[self.suit]
        b = listRanks[self.rank - 1]
        return b+" of "+a

def main():
    card1 = PlayingCard(9, "c") #test the card
    card2 = PlayingCard(13, "h") #test the card
    
    print(card1.getRank()) #test the get rank method
    print(card2.BJValue()) #test the black jack rank method

    print(card1) #test the naming the card method


if __name__ == "__main__":
    main()

from random import shuffle
import random

class Card:                         #Creating a Card class with the attribures of suits and numbers
    def __init__(self, suit, number):
        self._suit = suit
        self.number = number

    def __repr__(self):             #Makes the object able to print as a string
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
        return self.number


class Deck:                         #Creating a deck class with no attributes

    def __init__(self):
        self._cards = []
        # self.populate()
        # print(self._cards)

    def __len__(self):              #This makes it so you can use the length method
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value



    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        cards = []  # Create an empty list of cards
        for suit in suits:  # For each suit...
            for number in numbers:  # For each number...
                    # Create a new Card object and add it to the list
                cards.append(Card(suit, number))
        self._cards = cards  # Then point self._cards at this list
        # random.shuffle(cards)  #Shuffles the cards

    def shuffle(self):              #Method to shuffle the deck
        import random
        random.shuffle(self._cards)

    def printt(self):               #Just doing a print of the deck to see if it is populating correctly
        print("Initial Cards in Deck: " + str(self._cards))

    def deal(self):                 #This is dealing the cards out, and popping the cards from the deck
        return self._cards.pop()

    def showRemainingDeck(self):    #This is just printing the remaining deck to verify it is working properly
        print ("Remaining Cards in Deck: " + str(self._cards))


class Player(object):               #Creating a player class
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):             #Makes the object able to print as a string
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
        return self


    # Draw n number of cards from a deck

    def draw(self, deck, num=1):    #This method draws cards from the deck, with an attribute of number of cards (n)
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False        #Returns true if n cards are drawn, false if less than that
        return True


    def showHand(self):             # Display all the cards in the players hand
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self

    def showQuant(self):            # Shows the quantity of cards in an opponents hand.  In real game play, it wouldn't display the opponents actual cards
        print ("{}'s hand: {}".format(self.name, len(self.hand)) + " cards")

    def discard(self):              #This method gets rid of the card in the player's hand
        return self.hand.pop()

    # def checkBook(self):            #Trying to get any kind of check book method working to check if all 4 cards are the same



def main():

    my_deck = Deck()
    my_deck.populate()
    my_deck.shuffle()
    my_deck.printt()
    player1 = Player("Player 1")
    player2 = Player("Computer 1")
    player3 = Player("Computer 2")
    player1.draw(my_deck, 5)        #With this attribute, you can specify how many cards a player will be dealt
    player1.showHand()
    player2.draw(my_deck, 7)
    player2.showHand()
    player2.showQuant()
    player3.draw(my_deck, 7)
    player3.showHand()
    player3.showQuant()
    my_deck.showRemainingDeck()

    print (player1.hand)
    v = type(player1.hand)
    print (v)
    u = player1.hand[3]
    print (u)
    r = type(u)
    print ("r is " + str(r))
    # t = player1.hand.pop
    # print (t)
    # str1 = ''.join(player1.hand)
    # print (str1)
    if u in player2.hand:
        print ("it's there")



    w = 0
    print("\n\nWelcome to Go Fish. Read Read Me file for instructions.")
    while w < 1:                    #Need to work on playability...adding rounds, etc.
        player1.showHand()
        player2.showQuant()         #Human player can only see quantity of cards of each player
        player3.showQuant()
        print("1: Computer 1     2: Computer 2")
        choice = int(input("Please select an opponent to select a card from \n"))  #Need to add cards to hand and discard
        cardChoice = int(input("Which card do you want to ask for? \n"))
        print(player2.hand)
        if cardChoice in player2.hand:
            print("It's sure there")

        w += 1

main()

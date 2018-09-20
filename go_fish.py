from random import shuffle
import random
from random import randint


class Card(object):                         #Creating a Card class with the attribures of suits and numbers
    def __init__(self, number):
        self.number = str(number)

    def __str__(self):  # Makes the object able to print as a string
        return self.number

    def __repr__(self):  # Makes the object able to print as a string
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
        return self.number

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.number == other.number
        else:
            return False

class Deck(object):                         #Creating a deck class with no attributes

    NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        # for suit in suits:  # For each suit...
        for number in numbers * 4:  # For each number...
                    # Create a new Card object and add it to the list
                self._cards.append(Card(number))
        # self._cards = cards  # Then point self._cards at this list
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
    def __init__(self, name, species):
        self.name = name
        self.hand = []
        self.books = 0
        self.book_card = []  #Not using this, but this would list the cards of books that you have made
        self.species = species

    def __repr__(self):             #Makes the object able to print as a string
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
        return self.name

    def __str__(self):             #Makes the object able to print as a string
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
        return self.name


    # Draw n number of cards from a deck

    def draw(self, deck, num=1):    #This method draws cards from the deck, with an attribute of number of cards (n)
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False        #Returns true if n cards are drawn, false if less than that
        return True


    def display_score(self):             # Display all the cards in the players hand
        print ("  {}:  cards: {}  books: {}  cards {}".format(self.name, len(self.hand), self.books, self.hand))
        return self

    def display_comp(self):    #Displays the computer player's info, so you can't actually see what cards they have
        print ("{}:  cards: {}  books: {}".format(self.name, len(self.hand), self.books))
        return self

    # def showQuant(self):            # Shows the quantity of cards in an opponents hand.  In real game play, it wouldn't display the opponents actual cards
    #     print ("{}'s hand: {}".format(self.name, len(self.hand)) + " cards")

    # def discard(self):              #This method gets rid of the card in the player's hand
    #     return self.hand.pop()

    def checkCard(self, guess, Player):  #This is finished and working

        guess_card = Card(guess)  #Turning into card object

        posHand = []
        for i, c in enumerate(Player.hand):  # enumerate is helping to find the actual index mapping, that's why there is 2 values
            if guess_card == c:
                posHand.append(i)

        z = len(posHand)  #Just using for diagnosis

        if not posHand:
            print("\n" + Player.name + " has no " + str(guess_card) + "'s")
            return False
        else:
            print("\n" + Player.name + " has " + str(z) + " x " + str(guess_card) + "'s\n")
            return True

    def getCards(self, guess, Player):  # Might not need to use this method now, as it can be part of checkCards
        guess_card = Card(guess)  # This is creating a Card object with the value currently being the hard-coded number 5
        posHand = []
        cards_to_remove = []   #Making a temp list so cards can be removed from the hand
        for i, c in enumerate(Player.hand):  # enumerate is helping to find the actual index mapping, that's why there is 2 values
            if guess_card == c:
                self.hand.append(c)
                cards_to_remove.append(c)    #The selected cards are added to the cards_to_remove temp list

        for c in cards_to_remove:   #The cards are removed from the selected player's hand
            Player.hand.remove(c)

    def checkBook(self):  #This is finished, for a guess of 5.  Should I iterate through the whole deck?, but also need to add remove book method

        possibles = [Card(n) for n in Deck.NUMBERS]

        books = 0
        for i in possibles:
            if self.hand.count(i) == 4:
                self.hand.remove(i)
                self.hand.remove(i)
                self.hand.remove(i)
                self.hand.remove(i)

                self.book_card.append(i)
                self.books +=1

    # def play_round(self, other_player1, other_player2):    #This is testing a method to have other methods run
    #     self.showHand()
    #     other_player1.showQuant()
    #     other_player2.showQuant()

    def go_fish(self, deck):
        print ("Go Fish!")
        print (str(len(deck)) + " cards remaining in the deck")
        self.draw(deck, 1)  #Draws one card from the deck
        self.checkBook()


def main():

    my_deck = Deck()
    my_deck.populate()
    my_deck.shuffle()

    player1 = Player("Player 1","human")
    player2 = Player("Computer 1","bot")
    player3 = Player("Computer 2","bot")
    player1.draw(my_deck, 6)        #With this attribute, you can specify how many cards a player will be dealt

    player2.draw(my_deck, 6)

    player3.draw(my_deck, 6)

    players = []
    players.append(player1)
    players.append(player2)
    players.append(player3)

    def showGameboard():
        player1.display_score()
        player2.display_comp()
        player3.display_comp()

        # player1.display_score()
        # player2.display_score()
        # player3.display_score()


    def check_end_game():  #This function checks for the end of the game, and runs after each play
        pl1books = int(player1.books)
        pl2books = int(player2.books)
        pl3books = int(player3.books)
        r = [pl1books,pl2books,pl3books]
        allbooks = (pl1books + pl2books + pl3books)
        if allbooks == 13:
            print ("GAME OVER")
            print("Player 1 has " + str(x) + " books.")
            print("Computer 1 has " + str(y) + " books.")
            print("Computer 2 has " + str(z) + " books.")

            raise SystemExit

    rand_card = [Card(n) for n in Deck.NUMBERS]

    t = 0  #This sets the index position to dicate who's turn it is

    while True:  # This changes the player

        player_turn = players[t]
        print("\nIt is " + str(player_turn) + "'s turn\n")

        if player_turn.species == "bot":  # while play again, that would be their turns
            play_again = True
            while play_again:
                if player_turn == players[1]:
                    player2.checkBook()
                    check_end_game()
                    showGameboard()
                    player_random = [players[0], players[2]]  #Puts the other two oppenents into a list
                    player_select = random.choice(player_random)  #Chooses a random oponent that is not current player
                    if player2.hand:
                        d = (random.choice(player2.hand))  # This is a random card from player 2 (current player's) hand
                        f = (str(d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
                        print("\n" + str(players[1]) + " asking for a " + str(d) + " from " + str(player_select))
                    else:
                        d = random.choice(rand_card)
                        f = (str(d))
                        print("\n" + str(players[1]) + " asking for a " + str(d) + " from " + str(player_select))


                    if player2.checkCard(f, player_select) == True:
                        player2.getCards(f, player_select)

                    else:
                        if my_deck:
                            player2.go_fish(my_deck)
                            t += 1
                            if t == 3:
                                t = 0
                            play_again = False

                        elif not my_deck and not player2.hand:
                            t += 1
                            play_again = False

                        else:
                            t += 1
                            if t == 3:
                                t = 0
                            play_again = False
                elif player_turn == players[2]:
                    player3.checkBook()
                    check_end_game()
                    showGameboard()
                    player_random = [players[0], players[1]]  #Puts the other two oppenents into a list
                    player_select = random.choice(player_random)  #Chooses a random oponent that is not current player
                    if player3.hand:
                        d = (random.choice(player3.hand))  # This is a random card from player 2 (current player's) hand
                        f = (str(d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
                        print("\n" + str(players[2]) + " asking for a " + str(d) + " from " + str(player_select))
                    else:
                        d = random.choice(rand_card)
                        f = (str(d))
                        print("\n" + str(players[2]) + " asking for a " + str(d) + " from " + str(player_select))

                    if player3.checkCard(f, player_select) == True:
                        player3.getCards(f, player_select)

                    else:
                        if my_deck:
                            player3.go_fish(my_deck)
                            t += 1
                            if t == 3:
                                t = 0
                            play_again = False

                        elif not my_deck and not player3.hand:
                            t += 1
                            play_again = False

                        else:
                            t += 1
                            if t == 3:
                                t = 0
                            play_again = False

        else:  # this is for the human player
            play_again = True  # When I want to break the loop and end their turn, set this to False
            while play_again:
                player1.checkBook()
                check_end_game()
                showGameboard()
                print("\nPlease select an opponent to select a card from")
                choice = int(input("1: Computer1  2: Computer 2\n"))
                cardChoice = input("Which card do you want to ask for? \n")
                if choice == 1:
                    # player1.checkCard(cardChoice, player2)
                    if player1.checkCard(cardChoice, player2) == True:
                        player1.getCards(cardChoice, player2)

                    else:
                        if my_deck:
                            player1.go_fish(my_deck)
                            player1.display_score()
                            t += 1
                            play_again = False

                        elif not my_deck and not player1.hand:
                            t += 1
                            play_again = False

                        else:
                            player1.display_score()
                            t += 1
                            play_again = False

                if choice == 2:
                    if player1.checkCard(cardChoice, player3) == True:
                        player1.getCards(cardChoice, player3)
                        # player1.showHand()
                        # player2.showHand()
                        # player3.showHand()
                    else:
                        if my_deck:
                            player1.go_fish(my_deck)
                            player1.display_score()
                            t += 1
                            play_again = False
                        else:
                            player1.display_score()
                            t += 1
                            play_again = False

            pass

main()


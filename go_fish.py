from random import shuffle
import random
from random import randint

class Card(object):                         #Creating a Card class with the attribures of suits and numbers
    def __init__(self, number):
        self.number = str(number)

    # __lt__ would sort/compare the cards

    def __str__(self):  # Makes the object able to print as a string
        if self.number in ["11", "12", "13", "14"]:
            if self.number == 11:
                return "J"
            if self.number == 12:
                return "Q"
            if self.number == 13:
                return "K"
            if self.number == 14:
                return "A"
        # return self.number + " of " + self.suit  The suit is not necessary for this game's purposes
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
        self.book_card = []
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

    def display_comp(self):
        print ("{}:  cards: {}  books: {}".format(self.name, len(self.hand), self.books))
        return self

    def showQuant(self):            # Shows the quantity of cards in an opponents hand.  In real game play, it wouldn't display the opponents actual cards
        print ("{}'s hand: {}".format(self.name, len(self.hand)) + " cards")

    def discard(self):              #This method gets rid of the card in the player's hand
        return self.hand.pop()

    def checkCard(self, guess, Player):  #This is finished and working
        # guess = "5"
        guess_card = Card(guess)

        # print(type(guess_card))
        # print("guess_card above")
        posHand = []
        for i, c in enumerate(Player.hand):  # enumerate is helping to find the actual index mapping, that's why there is 2 values
            if guess_card == c:
                posHand.append(i)

        z = len(posHand)
                # print("It's there")

        if not posHand:
            print("\n" + Player.name + " has no " + str(guess_card) + "'s")
            return False
        else:
            print("\n" + Player.name + " has " + str(z) + " x " + str(guess_card) + "'s\n")
            return True

        # bosHand = []
        # for i, c in enumerate(Player.hand):  # enumerate is helping to find the actual index mapping, that's why there is 2 values
        #     if guess_card == c:
        #         self.hand.append(c)
        #         print ("c is " + str(c))
        #         Player.hand.remove(c)
        #         print ("The card was added to player 1's hand")

        # if not bosHand:
        #     print("nothing in the list")
        # else:
        #     print("Player 2 has that card")


    def getCards(self, guess, Player):  # Might not need to use this method now, as it can be part of checkCards
        guess_card = Card(guess)  # This is creating a Card object with the value currently being the hard-coded number 5
        posHand = []
        cards_to_remove = []
        for i, c in enumerate(Player.hand):  # enumerate is helping to find the actual index mapping, that's why there is 2 values
            if guess_card == c:
                self.hand.append(c)
                # print ("c is " + str(c))
                # Player.hand.remove(c)
                cards_to_remove.append(c)
                # print("The card was added to " + self.name + "'s hand")

        for c in cards_to_remove:
            Player.hand.remove(c)

        # if not posHand:
        #     print("nothing in the list")
        # else:
        #     print("Player 2 has that card")


    def checkBook(self):  #This is finished, for a guess of 5.  Should I iterate through the whole deck?, but also need to add remove book method

        possibles = [Card(n) for n in Deck.NUMBERS]
        # print(possibles)

        books = 0
        for i in possibles:
            if self.hand.count(i) == 4:
                for num in range(4):
                    self.hand.remove(i)
                self.books += 1
                # print ("Player has " + str(self.books) + " books of " + str(i))
                self.book_card.append(i)
        # print (self.name + " has " + str(self.books) + " books")
        # print (self.hand)

    def play_round(self, other_player1, other_player2):    #This is testing a method to have other methods run
        self.showHand()
        other_player1.showQuant()
        other_player2.showQuant()

    def go_fish(self, deck):
        print ("Go Fish!")
        self.draw(deck, 1)

    # def draw_card(self, deck):

    def show_gameboard(self, other_player1, other_player2):
        self.showHand()
        other_player1.showQuant()
        other_player2.showQuant()




def main():

    my_deck = Deck()
    my_deck.populate()
    my_deck.shuffle()
    # my_deck.printt()
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
    # print (str(players))
    # player1.showQuant()
    # player2.showQuant()

    def showGameboard():
        player1.display_score()
        player2.display_comp()
        player3.display_comp()
    t = 0  #This sets the index position to dicate who's turn it is

    # print(player_turn)
    # print("Player on deck above")
    # t += 1
    # player_turn = players[t]
    # print(player_turn)
    # print("Player on deck above")

    while True:  # This changes the player
        player_turn = players[t]

        print("\nIt is " + str(player_turn) + "'s turn\n")
        # showGameboard()

        if player_turn.species == "bot":  # while play again, that would be their turns
            play_again = True
            while play_again:
                if player_turn == players[1]:
                    showGameboard()
                    player_random = [players[0], players[2]]  #Puts the other two oppenents into a list
                    player_select = random.choice(player_random)  #Chooses a random oponent that is not current player
                    d = (random.choice(player2.hand))  # This is a random card from player 2 (current player's) hand
                    f = (str(d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
                    print("\n" + str(players[1]) + " asking for a " + str(d) + " from " + str(player_select))

                    if player2.checkCard(f, player_select) == True:
                        player2.getCards(f, player_select)
                        # player1.display_score()
                        # player2.display_comp()
                        # player3.display_comp()
                    else:
                        player2.go_fish(my_deck)
                        t += 1
                        if t == 3:
                            t = 0
                        play_again = False
                elif player_turn == players[2]:
                    showGameboard()
                    player_random = [players[0], players[1]]  #Puts the other two oppenents into a list
                    player_select = random.choice(player_random)  #Chooses a random oponent that is not current player
                    d = (random.choice(player3.hand))  # This is a random card from player 2 (current player's) hand
                    f = (str(d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
                    print("\n" + str(players[2]) + " asking for a " + str(d) + " from " + str(player_select))



                    if player3.checkCard(f, player_select) == True:
                        player3.getCards(f, player_select)
                        # player1.display_score()
                        # player2.display_comp()
                        # player3.display_comp()
                    else:
                        player3.go_fish(my_deck)
                        t += 1
                        if t == 3:
                            t = 0
                        play_again = False


        else:  # this is for the human player
            play_again = True  # When I want to break the loop and end their turn, set this to False
            while play_again:
                showGameboard()
                player1.checkBook()
                print("\nPlease select an opponent to select a card from")
                choice = int(input("1: Computer1  2: Computer 2\n"))
                cardChoice = input("Which card do you want to ask for? \n")
                if choice == 1:
                    # player1.checkCard(cardChoice, player2)
                    if player1.checkCard(cardChoice, player2) == True:
                        player1.getCards(cardChoice, player2)

                    else:
                        player1.go_fish(my_deck)
                        player1.display_score()
                        t += 1
                        play_again = False

                    # if False:
                    #     player1.getCards(cardChoice, player2)
                    #     player1.showHand()
                    #     player2.showHand()
                    #     player3.showHand()
                    # if True:
                    # # if False:
                    #     player1.showHand
                    #     print ("Nope, no cards, go fish")
                    #     player1.go_fish(my_deck)
                    #     player1.showHand

                if choice == 2:
                    if player1.checkCard(cardChoice, player3) == True:
                        player1.getCards(cardChoice, player3)
                        # player1.showHand()
                        # player2.showHand()
                        # player3.showHand()
                    else:
                        player1.go_fish(my_deck)
                        player1.display_score()
                        t += 1
                        play_again = False




                # x = int(input("number"))
                # if x == 3:
                #     t += 1
                #     player1.go_fish(my_deck)
                #     player1.showHand()
            pass

        # After I do the game play, make a check, I would do a break to end the game, then write the actions I wanted outside of the loop to show the end of the game

        # if player_turn == players[0]:
        #     while True:
        #         print("1: Computer1 has " + (str(len(player2.hand))) + " cards  2: Computer 2 has " + (
        #             str(len(player2.hand))) + " cards")
        #         print ("Hiyeee")
        #         choice = int(input("Please select an opponent to select a card from \n"))
        #         cardChoice = input("Which card do you want to ask for? \n")
        #         if choice == 1:
        #             player1.checkCard(cardChoice, player2)
        #             if True:
        #                 player1.getCards(cardChoice, player2)
        #         player1.play_round(player2, player3)
        #         x = int(input("number"))
        #         if x == 3:
        #             t += 1
        #             player1.go_fish(my_deck)
        #             player1.showHand()
        #             break
        #
        # b = 0
        # if player_turn == players[1]:
        #     while True:
        #         player_random = [players[0], players[2]]
        #         player_select = random.choice(player_random)
        #         print("Asking cards from " + str(player_select))
        #         # player1.show_gameboard(player2, player3)
        #         player1.showHand()
        #         player2.showHand()
        #         player3.showHand()
        #         d = (random.choice(player2.hand))  # This is a random card from player 2's hand
        #         print(d)
        #         print("Above is d, which is the card randomly selected from the current guessers hand")
        #         # print (type(d))
        #         f = (str(
        #             d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
        #         # print (type(f))
        #         # print ("f type is above")
        #         # print ("Above is random choice card")
        #         print(player_select)
        #         print("Above is player_select, which is the randomized target of computer 1's guess")
        #
        #         # print(type(player_select))
        #         # print ("Above is the player that has been selected")
        #         player2.checkCard(f, player_select)
        #         if True:
        #             player2.getCards(f, player_select)
        #             player1.showHand()
        #             player2.showHand()
        #             player3.showHand()
        #             break
        #         else:
        #             break
        #
        # if player_turn == players[2]:
        #     while True:
        #         player_random = [players[0], players[1]]
        #         player_select = random.choice(player_random)
        #         print("Asking cards from " + str(player_select))
        #         # player1.show_gameboard(player2, player3)
        #         player1.showHand()
        #         player2.showHand()
        #         player3.showHand()
        #         d = (random.choice(player3.hand))  # This is a random card from player 2's hand
        #         print(d)
        #         print("Above is d, which is the card randomly selected from the current guessers hand")
        #         # print (type(d))
        #         f = (str(
        #             d))  # Turns the card object into a string, so it can then be passed to the function to be turned back into a card
        #         print(player_select)
        #         print("Above is player_select, which is the randomized target of computer 1's guess")
        #         player3.checkCard(f, player_select)
        #         if True:
        #             player3.getCards(f, player_select)
        #             player1.showHand()
        #             player2.showHand()
        #             player3.showHand()
        #             break
        #         else:
        #             break
                # player1.showHand()
                # player2.showHand()
                # player3.showHand()
                # break

                # print (player_select)  #This is the chosen player
                # print(random.choice(player_select.hand))  #This is a random card from the chosen player
                # player_select.showHand()
                # q = player_select.hand
                # print (q)
                # print ("Above is q")
                # e = len(q)
                # print (e)
                # print ("e is above")
                # r = randint(0,e - 1)
                # print (r)
                # print("r is above")
                # t = player_select.hand[r]
                # print (t)
                # print("t is above")


                # print("1: Computer1 has " + (str(len(player2.hand))) + " cards  2: Computer 2 has " + (str(len(player2.hand))) + " cards")
                # choice = int(input("Please select an opponent to select a card from \n"))
                # cardChoice = input("Which card do you want to ask for? \n")
                # if choice == 1:
                #     player1.checkCard(cardChoice, player2)
                # player1.play_round(player2, player3)
                # x = int(input("number"))
                # if x == 3:
                #     t +=1


    #method calls running from here
    # player1.checkCard("5", player2)
    # player1.getCards("5", player2)
    # player1.checkBook()
    # player1.showHand()
    # player2.showHand()

main()


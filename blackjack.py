# blackjack.py
import random

suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:
    """ This Class is used to assign a rank for every card in suit """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """ This class will create / suffle and pick a card  """
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s, r))

    def __str__(self):
        deck_det = ''
        for card in self.deck:
            deck_det += "\n" + card.__str__()
        return deck_det

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        current_card = self.deck.pop()
        return current_card


class Hand:
    """ this class is used to pick a card from deck and distribute to the player """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """ this class is used to add/ minus the chips value """

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet: "))
        except ValueError:
            print("Bet amount should be integer")
        else:
            if chips.bet > chips.total :
                print("Sorry, You have insufficient bet amount. You have {} ".format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        inp_h_s = input("Enter your choice h for hit or s for stand :")
        if inp_h_s[0].lower() == "h":
            hit(deck, hand)
        elif inp_h_s[0].lower() == "s":
            print("Player Stand..Now dealer playing")
            playing = False
        else:
            print("Sorry, you have chosen wrong option. please choose h or s :")
            continue
        #print(*hand.cards)
        break


def show_some(player, dealer):
    print("*" * 30)
    print(" Dealer's hand")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\n Player's hand" , *player.cards, sep='\n ')
    print("*"*30)

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)
    print("*" * 30)

def player_busts(player, dealer, chips):
    print("Player Busts")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("player Wins, Dealer Busts")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("player Busts , Dealer Wins")
    chips.lose_bet()


def push(player, dealer):
    print("Both player and dealer had a tie. It's a push. ")


while True:
    print("Welcome to BlackJack.")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)
    print("\nPlayer's winnings stand at", player_chips.total)
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
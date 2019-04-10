import random

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q L A'.split()


class Deck():

    def __init__(self):
        print("\nCreated New Deck!")
        self.deck_of_cards = [(s,r) for s in SUITE for r in RANKS]


    def shuffle_deck(self):
        print("Shuffling Deck!\n")
        random.shuffle(self.deck_of_cards)

    def split_deck(self):
        return (self.deck_of_cards[:26], self.deck_of_cards[26:])


class Hand():

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, new_cards):
        self.cards.extend(new_cards)

    def remove(self):
        return self.cards.pop()


class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        turn = self.hand.remove()
        print("{} has placed: {}".format(self.name, turn))
        return turn

    def play_after_draw(self):
        war = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war.append(self.hand.remove())
            return war


    def valid_player(self):
        return len(self.hand.cards) != 0


# Game Logic

print(""
      "Welcome to the WAR Game!!"
      "")

# Create Deck and split in two halves
mydeck = Deck()
mydeck.shuffle_deck()
half1, half2 = mydeck.split_deck()

# Create both players
comp = Player("Computer", Hand(half1))

name = input("Please enter your name? ")
user = Player(name, Hand(half2))
print("\n")

total_rounds = 0
war_count = 0

while comp.valid_player() and user.valid_player():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings::")
    print(user.name+" has the count: "+str(len(user.hand.cards)))
    print(comp.name+" has the count: "+str(len(comp.hand.cards)))
    print("Play a card!")
    print("\n")


    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    if c_card[1] == p_card[1]:
        war_count += 1

        print("War!")
        table_cards.extend(user.play_after_draw())
        table_cards.extend(comp.play_after_draw())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("'GAME OVER!!'... Number of rounds: " + str(total_rounds))
print("War happened "+str(war_count)+" times.")
print("Does computer still have cards? : ", str(comp.valid_player()))
print("Does user still have cards? : ", str(user.valid_player()))

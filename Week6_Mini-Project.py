# Mini-project #6 - Blackjack

import simplegui
import random
# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome1 = ""
outcome2 = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
    'T':10, 'J':10, 'Q':10, 'K':10}
many_cards = False

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + \
            CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []    # create Hand object  

    def __str__(self):
        str_rep = "Hand contains "
        for i in range(len(self.hand)):
            str_rep += str(self.hand[i]) + " "
        return str_rep    # return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)    # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value
        # if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        Aces = 0
        for cards in self.hand:
            rank = str(cards)[1]
            if rank is "A":
                Aces += 1
                hand_value += VALUES[rank]
            else:
                hand_value += VALUES[rank]
        if Aces == 0:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                hand_value += 10
                return hand_value
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        global p_hand, d_hand, many_cards
        if len(self.hand) == 2:
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[0].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[1].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 96, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        elif len(self.hand) == 3:
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[0].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[1].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 96, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[2].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 192, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        elif len(self.hand) == 4:
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[0].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[1].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 96, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[2].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 192, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[3].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 288, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        elif len(self.hand) == 5 or many_cards is True:
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[0].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[1].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 96, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[2].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[0].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 192, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[3].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 288, pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card_pos = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[4].rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(p_hand.hand[1].suit))
            canvas.draw_image(card_images, card_pos, CARD_SIZE, [pos[0] + \
                    CARD_CENTER[0] + 384, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            many_cards = True

        

p_hand = Hand()
d_hand = Hand()
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        # create a Card object using Card(suit, rank)
        # and add it to the card list for the deck
        for suit in SUITS: 
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck      
        random.shuffle(self.deck)    # use random.shuffle()
        
    def deal_card(self):
        card_dealed = self.deck[-1]    # deal a card object from the deck
        self.deck.remove(card_dealed)
        return card_dealed

    def __str__(self):
        global game_deck
        str_rep = "Deck contains "
        for i in range(len(self.deck)):
            str_rep += str(self.deck[i]) + " "
        return str_rep    # return a string representing the deck

game_deck = Deck()

#define event handlers for buttons
def deal():
    global outcome1, outcome2, in_play, score
    global game_deck, p_hand, d_hand
    # your code goes here
    if in_play == True:
        outcome1 = "You lost when trying to deal a new hand."
        outcome2 = "New deal?"
        score -= 1
        in_play = False
        return
    in_play == True
    game_deck = Deck()
    game_deck.shuffle()
    p_hand = Hand()
    d_hand = Hand()
    for x in range(2):
        p_card = game_deck.deal_card()
        d_card = game_deck.deal_card()
        p_hand.add_card(p_card)
        d_hand.add_card(d_card)
    in_play = True
    outcome1 = ""
    outcome2 = "Hit or Stand?"

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global p_hand, game_deck, in_play, outcome1, outcome2, score
    if p_hand.get_value() <= 21 and in_play is True:
        p_hand.add_card(game_deck.deal_card())
    if p_hand.get_value() > 21 and in_play is True:
        in_play = False
        outcome1 = "You went bust and lose."
        outcome2 = "New deal?"
        score -= 1
        stand()


def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 
    # 17 or more
    # assign a message to outcome, update in_play and score
    global d_hand, game_deck, p_hand, in_play, score, outcome1, outcome2
    if in_play is True:
        in_play = False
        if p_hand.get_value() > 21:
            return
        while d_hand.get_value() <= 17:
            d_hand.add_card(game_deck.deal_card())
        if d_hand.get_value() > 21:
            outcome1 = "The Dealer went bust and you win."
            outcome2 = "New deal?"
            score += 1
            return outcome1, outcome2
        elif d_hand.get_value() == p_hand.get_value():
            if d_hand.get_value() == 21 and p_hand.get_value() == 21:
                outcome1 = "The Dealer won the Blackjack tie and you lose."
                outcome2 = "New deal?"
                score -= 1
                return outcome1, outcome2
            else:
                outcome1 = "The Dealer won the tie and you lose."
                outcome2 = "New deal?"
                score -= 1
                return outcome1, outcome2
        elif d_hand.get_value() == 21:
            outcome1 = "The Dealer got blackjack and you lose."
            outcome2 = "New deal?"
            score -= 1
            return outcome1, outcome2
        elif p_hand.get_value() == 21:
            outcome1 = "You got blackjack and you win."
            outcome2 = "New deal?"
            score += 1
            return outcome1, outcome2
        elif d_hand.get_value() > p_hand.get_value():
            outcome1 = "The Dealer had a higher hand value and you lose."
            outcome2 = "New deal?"
            score -= 1
            return outcome1, outcome2
        elif d_hand.get_value() < p_hand.get_value():
            outcome1 = "The Dealer had a lower hand value and you win."
            outcome2 = "New deal?"
            score += 1
            return outcome1, outcome2


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [72, 72], 40, "#00F7FF")
    canvas.draw_text("Score " + str(score), [400, 67], 25, "Black")
    canvas.draw_text("Dealer", [50, 160], 30, "Black")
    canvas.draw_text("Player", [50, 385], 30, "Black")
    p_hand.draw(canvas, [50, 425])
    d_hand.draw(canvas, [50, 200])
    card_back_pos = (108, 48)
    if in_play == True:
        canvas.draw_image(card_back, card_back_pos, CARD_BACK_SIZE, \
            (86, 248), CARD_BACK_SIZE)
    canvas.draw_text(outcome1, [200, 160], 20, "Black")
    canvas.draw_text(outcome2, [200, 385], 20, "Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
in_play = True
frame.start()

# remember to review the gradic rubric

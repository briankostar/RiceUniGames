# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message= "Hit or Stand?"
dealer_value = 0
player_value = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):

        hand = ""
        for card in self.hand:
            hand += card.get_suit() + card.get_rank() + " "
        return "Hand contains" + " " + hand
    
    def add_card(self, card):
        self.hand.append(card)
        
    def get_value(self):
        value = 0
        number_of_ace = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]
            if card.get_rank() == "A":
                number_of_ace += 1
        #if the card object in hand is A    
        if number_of_ace == 0 :    
            return value
        else:    
            if value + 10 <= 21:
                return value + 10
            else:
                return value
    
    def draw(self, canvas, pos):
        #draw each cards in hand, separated by pos
        x = 0
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, (pos[0]+x, pos[1]))
            x += 100
            
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(suit+rank)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        #return a card object
        card = self.deck.pop()
        suit = card[0]
        rank = card[1]
        deal_card = Card(suit, rank)
        return deal_card
    
    def __str__(self):
        deck = ""
        for i in range(len(self.deck)):
            deck += " " + self.deck[i]
        return "Deck contains" + deck

def deal():
    #shuffles and hands two cards to player and dealer
    #create new player and dealer
    global outcome, in_play, dealer_hand, player_hand, player_value, dealer_value, score, message
    
    if in_play:
        score -= 1
        message = "Dealer Wins!"
    else:
        in_play = True
        message = "Hit or Stand?"
        #draw new deck
        new_deck = Deck()
        new_deck.shuffle()
        #player draws 2 cards
        player_hand = Hand()
        player_hand.add_card(new_deck.deal_card())
        player_hand.add_card(new_deck.deal_card())
        player_value = player_hand.get_value()
        #dealer draws 2 cards
        dealer_hand = Hand()
        dealer_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        dealer_value = dealer_hand.get_value()

def hit():
    global score, message, in_play, player_hand, player_value 
    
    if in_play:
        player_hand.add_card(new_deck.deal_card())
        player_value = player_hand.get_value()
    else: 
        message = "New Deal?"
    if in_play and player_hand.get_value() > 21:
        message = "You Busted!"
        score -= 1
        in_play = False
        
def stand():   
    global score, message, in_play, dealer_hand, dealer_value
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(new_deck.deal_card())
            dealer_value = dealer_hand.get_value() 
        if dealer_hand.get_value() > 21:
            message = "Dealer Busted!"
            score += 1
            in_play = False
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                message = "You win!"
                score += 1
                in_play = False
            else:
                message = "Dealer wins!"
                score -= 1
                in_play = False
    else:
        message = "New Deal?"
    # assign a message to outcome, update in_play and score

def reset():
    global score
    score = 0
        
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack", (210, 70), 45, "Black")
    canvas.draw_text("Dealer: ", (75, 170), 30, "Black")
    canvas.draw_text("Player: "+ str(player_value), (75, 340), 30, "Black")
    canvas.draw_text("Score: " + str(score), (435, 125), 30, "Black")
    
    canvas.draw_line((10, 300),(590,300), 5, "Maroon")
    canvas.draw_polygon([(10,10), (590,10), (590,590), (10,590)], 10, "Maroon")
    
    if in_play:
        dealer_hand.draw(canvas, [75,180])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [110,230], CARD_SIZE)
    else:
        dealer_hand.draw(canvas, [75,180])
        canvas.draw_text("Dealer: " + str(dealer_value), (75, 170), 30, "Black")
        
    player_hand.draw(canvas, [75,350])
    canvas.draw_text(str(message), (200, 530), 35, "Black")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
#frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)

new_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

# get things rolling
deal()
frame.start()

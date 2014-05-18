# implementation of card game - Memory

import simplegui
import random

turns = 0
deck = []
exposed = []
state = 0    
flipped_card = []
last_two_card_index = []

# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global state
    global flipped_card
    global last_two_card_index
    set1 = range(8)
    set2 = range(8)
    deck = set1 + set2 
    random.shuffle(deck)    
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]    
    state = 0
    flipped_card = [0, 0]
    last_two_card_index = [0, 0]

def flip_card(pos):
    global flipped_card, state
    #go through 16 cards' position, if position matches, and not flipped already, flip card
    x = 0
    for i in range(16):
        if (pos[0] >= 0 + x) and (pos[0] < 50 + x) and (exposed[i] == False) :
            exposed[i] = True
            #store the last two cards that are exposed
            flipped_card.pop(0)
            flipped_card.append(deck[i])
            last_two_card_index.pop(0)
            last_two_card_index.append(i)
        x += 50
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed
    global state
    global flipped_card
    
    #ignore click if card is already flipped. find index of pos and see if card is flipped
    x = 0
    index = 0
    for i in range(16):
        
        if (pos[0] >= 0 + x) and (pos[0] < 50 + x):
            index = i
        x += 50   
        
    if exposed[index] == False:
        if state == 0:
            flip_card(pos)
            state = 1
        elif state == 1:
            flip_card(pos)
            state = 2
        else:
            if flipped_card[0] != flipped_card[1]:
            #if cards dont match, only flip those last 2 cards
               exposed[last_two_card_index[0]] = False
               exposed[last_two_card_index[1]] = False
            flip_card(pos)
            state = 1
# cards are logically 50x100 pixels in size    
def draw(canvas):
   
    x = 0
    i = 0
    for n in deck:
        if exposed[i]:
            canvas.draw_text(str(n), (20 + x,60), 30, "white")
        else:
            canvas.draw_polygon([(0 + x,0), (50 + x,0), (50 + x,100), (0 + x,100)], 3, "White", "Green")
        x += 50
        i += 1
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

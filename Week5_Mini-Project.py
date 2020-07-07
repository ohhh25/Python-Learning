# implementation of card game - Memory

import simplegui
import random
card1 = 0
card2 = 0
turns = 0
# helper function to initialize globals
def new_game():
    global cards, exposed, state, turns, card1, card2, label
    # creating the cards and randomizing the location
    cards = [0, 1, 2, 3, 4, 5, 6, 7] * 2
    random.shuffle(cards)
    # creating the exposed Boolean list values
    exposed = [False] * 16
    # creating the state of the game
    state = 0
    turns = 0
    card1 = 0
    card2 = 0
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card1, card2, turns, label
    pos_list = []
    index = pos[0] // 50
    pos_list.append(pos)
    for i in pos_list:
        if exposed[index] == True:
            pass
        elif exposed[index] == False:
            exposed[index] = True
            pos_list.pop(0)
            if state == 0:
                state = 1
                card1 = index
            elif state == 1:
                state = 2
                card2 = index
                turns += 1
                label.set_text("Turns = " + str(turns))
            elif state == 2:
                state = 1
                if cards[card1] == cards[card2]:
                    card1 = index
                    card2 = 0
                else:
                    exposed[card1] = False
                    exposed[card2] = False
                    card1 = index
                    card2 = 0
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        # drawing the numbers on the card if exposed is True
        if exposed[card_index] is True:
            # creating hte position of the card
            card_pos = (50 * card_index) + 5
            canvas.draw_text(str(cards[card_index]), [card_pos, 75], 80, \
                             "White")
        # drawing the cards and separtors if exposed is False
        else:
            # creating the start and end positions of the cards
            start = card_index * 50
            end = (card_index + 1) * 50
            canvas.draw_polygon([[start, 0], [end, 0], [end, 100], \
                                 [start, 100]], 1, "Green", "Green")
            # drawing the card separtors
            canvas.draw_line([start, 0], [start, 100], 1, "Red")
            canvas.draw_line([end, 0], [end, 100], 1, "Red")
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

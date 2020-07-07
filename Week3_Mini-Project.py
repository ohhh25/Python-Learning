# template for "Stopwatch: The Game"

import simplegui
# define global variables
#tenths of seconds
t = 0
#points Boolean
points = False
#times won
perfect = 0
#number of trys
trys = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """
    Formatting Time.
    """
    #creating units of time variables
    tenths_of_seconds = t
    seconds = t / 10
    minutes = t / 600
    #formatting logic
    if len(str(tenths_of_seconds)) == 1:
        return str(minutes) + ":0" + str(seconds) + "." \
         + str(tenths_of_seconds)
    elif len(str(seconds)) == 1:
        return str(minutes) + ":0" + str(seconds) + "." \
         + str(tenths_of_seconds)[len(str(tenths_of_seconds)) - 1:]
    elif seconds >= 60:
        seconds = seconds % 60
        if len(str(seconds)) == 1:
            return str(minutes) + ":0" + str(seconds) + "." \
             + str(tenths_of_seconds)[len(str(tenths_of_seconds)) - 1:]
        else:
            return str(minutes) + ":" + str(seconds) + "." \
             + str(tenths_of_seconds)[len(str(tenths_of_seconds)) - 1:]
    else:
        return str(minutes) + ":" + str(seconds) + "." \
         + str(tenths_of_seconds)[len(str(tenths_of_seconds)) - 1:]

def score():
    global perfect, trys
    if timer.stop and t % 10 == 0 and points == True:
        perfect += 1
        trys += 1
    elif timer.stop and points == True:
        trys += 1
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    global points
    points = True
    
def Stop():
    timer.stop()
    score()
    global points
    points = False
    
def Reset():
    global t
    t = 0
    timer.stop()
    global points, perfect, trys
    points = False
    perfect = 0
    trys = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    
#define draw handler
def stopwatch(canvas):
    canvas.draw_text(format(t), [67, 133], 67, "White")
    canvas.draw_text(str(perfect) + "/" + str(trys), [233, 33], 33, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.add_button("Start", Start, 200)
frame.add_button("Stop", Stop, 200)
frame.add_button("Reset", Reset, 200)

# define draw handler
frame.set_draw_handler(stopwatch)

# start frame
frame.start()
timer.stop()

# Please remember to review the grading rubric

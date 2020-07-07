# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

#my extra globals
PAD1_T = 160
PAD1_B = 240
PAD2_T = 160
PAD2_B = 240
score1 = 0
score2 = 0
paddle1_pos = [[0, PAD1_T], [8, PAD1_T], [8, PAD1_B], [0, PAD1_B]]
paddle2_pos = [[600, PAD2_T], [592, PAD2_T], [592, PAD2_B], [600, PAD2_B]]
ball_pos = [300, 200]
ball_vel = [0, 0]
vel_inc = 5
paddle1_vel = 0
paddle2_vel = 0
gutter = True
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    if direction == LEFT:
        ball_vel = [random.randrange(-3, -1), random.randrange(1, 3)]
    elif direction == RIGHT:
        ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2# these are ints
    global PAD1_T, PAD1_B, PAD2_T, PAD2_B
    spawn_ball(RIGHT)
    paddle1_vel = 0
    paddle2_vel = 0
    PAD1_T = 160
    PAD1_B = 240
    PAD2_T = 160
    PAD2_B = 240
    score1 = 0
    score2 = 0
    paddle1_pos = [[0, PAD1_T], [8, PAD1_T], [8, PAD1_B], [0, PAD1_B]]
    paddle2_pos = [[600, PAD2_T], [592, PAD2_T], [592, PAD2_B], [600, PAD2_B]]
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global PAD1_T, PAD1_B, PAD2_T, PAD2_B
    global gutter
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    PAD1_T += paddle1_vel
    PAD1_B += paddle1_vel
    PAD2_T += paddle2_vel
    PAD2_B += paddle2_vel
    if PAD1_T <= 0:
        PAD1_T = 0
        PAD1_B = 80
    elif PAD1_B >= 400:
        PAD1_B = 400
        PAD1_T = 320
    if PAD2_T <= 0:
        PAD2_T = 0
        PAD2_B = 80
    elif PAD2_B >= 400:
        PAD2_B = 400
        PAD2_T = 320
   
    
    paddle1_pos = [[0, PAD1_T], [8, PAD1_T], [8, PAD1_B], [0, PAD1_B]]
    paddle2_pos = [[600, PAD2_T], [592, PAD2_T], [592, PAD2_B], [600, PAD2_B]]
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "White", "White")
    canvas.draw_polygon(paddle2_pos, 1, "White", "White")
    
    # keeping ball on screen
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # determine whether paddle and ball collide    
    if ball_pos[1] >= PAD1_T and ball_pos[1] <= PAD1_B and ball_pos[0] - BALL_RADIUS <= 8:
        gutter = False
        ball_vel[0] = - ball_vel[0] * 1.1
    elif ball_pos[1] >= PAD2_T and ball_pos[1] <= PAD2_B and ball_pos[0] + BALL_RADIUS >= 592:
        gutter = False
        ball_vel[0] = - ball_vel[0] * 1.1

    # outcomes when ball hits gutter
    if ball_pos[0] - BALL_RADIUS <= 8 and gutter == True:
        spawn_ball(RIGHT)
        score2 += 1
    elif ball_pos[0] + BALL_RADIUS >= 592 and gutter == True:
        spawn_ball(LEFT)
        score1 += 1
        
    # draw scores
    canvas.draw_text(str(score1), [200, 50], 50, "White")
    canvas.draw_text(str(score2), [350, 50], 50, "White")
    gutter = True
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel_inc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel_inc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel_inc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel_inc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += vel_inc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= vel_inc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += vel_inc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= vel_inc
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


# start frame
new_game()
frame.start()

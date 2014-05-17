# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
#need to randomize ball_vel
ball_vel = []
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #random pixel movement/second (60 since draw handler draws 60 times a sec)
    if direction == RIGHT:
        ball_vel = [random.randrange(200, 240)/60, -random.randrange(60, 180)/60]
    if direction == LEFT:
        ball_vel = [-random.randrange(120, 240)/60, -random.randrange(60, 180)/60]
   

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    
    x = random.randrange(0,2)
    if x == 1:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #bounce ball on the y-axis    
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > (HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    #bounce ball on the x-axis if it hits the gutter and if y-position is within the paddle & give points  
        
    if ball_pos[0] < (BALL_RADIUS+8):
        if ball_pos[0] < (BALL_RADIUS+8) and (ball_pos[1]) >= (paddle1_pos-40) and (ball_pos[1]) <= (paddle1_pos + 40):
            ball_vel[0] = -ball_vel[0]*1.1
            c.draw_text("Ping!", [ball_pos[0]+30, ball_pos[1]], 24, "White")
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] > (WIDTH - BALL_RADIUS - 8):
        if ball_pos[0] > (WIDTH-BALL_RADIUS-8) and (ball_pos[1]) >= (paddle2_pos-40) and (ball_pos[1]) <= (paddle2_pos + 40) :
            ball_vel[0] = -ball_vel[0]*1.1
            c.draw_text("Pong!", [ball_pos[0]-75, ball_pos[1]], 24, "White")
        else:
            spawn_ball(LEFT)
            score1 += 1
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 3, "white", "white")
       
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos + paddle1_vel < 40:
        paddle1_pos = 40
    elif paddle1_pos + paddle1_vel > 360:
        paddle1_pos = 360
    
    paddle2_pos += paddle2_vel
    if paddle2_pos + paddle2_vel < 40:
        paddle2_pos = 40
    elif paddle2_pos + paddle2_vel > 360:
        paddle2_pos = 360
    
    # draw paddles
    
    c.draw_polygon([[0, paddle1_pos+40], [8, paddle1_pos+40], [8,paddle1_pos-40], [0,paddle1_pos-40]], 1, 'White', 'White')
    c.draw_polygon([[591, paddle2_pos+40], [600, paddle2_pos+40], [600,paddle2_pos-40], [591,paddle2_pos-40]], 1, 'White', 'White')
    # draw scores
    
    c.draw_text(str(score1), [135,100], 45, "White")
    c.draw_text(str(score2), [435,100], 45, "White")
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle2_pos
   
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle2_pos
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
        
def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)


# start frame
new_game()
frame.start()

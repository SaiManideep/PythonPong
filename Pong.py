import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = 0.0
paddle2_pos = 0.0
paddle1_vel = 0.0
paddle2_vel = 0.0
score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    horiz_vel = random.randrange(120, 240)/60.0
    if direction == "LEFT":
        horiz_vel = -horiz_vel
    vert_vel = -random.randrange(60, 180)/60.0
    ball_vel = [horiz_vel, vert_vel] 

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2  
    score1 = 0
    score2 = 0
    spawn_ball(random.choice(["LEFT","RIGHT"]))
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
      
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],
                [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] - paddle1_pos) > (HEIGHT - 3 * PAD_HEIGHT) and (ball_pos[1] - paddle1_pos) < (HEIGHT - 2 * PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            else:
            score2 = score2 + 1
            spawn_ball("RIGHT")
    if ball_pos[0] >= ((WIDTH - 1) - PAD_WIDTH - BALL_RADIUS):
        if (ball_pos[1] - paddle2_pos) > (HEIGHT - 3 * PAD_HEIGHT) and (ball_pos[1] - paddle2_pos) < (HEIGHT - 2 * PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score1 = score1 + 1
            spawn_ball("LEFT")
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    if (paddle1_pos + paddle1_vel) >= -(HEIGHT/2.0 - HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel) <= (HEIGHT/2.0 - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel) >= -(HEIGHT/2.0 - HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel) <= (HEIGHT/2.0 - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    c.draw_polygon([(0, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle1_pos), 
                    (PAD_WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle1_pos), 
                    (PAD_WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle1_pos), 
                    (0, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle1_pos)], 1, 'White', 
                    'White')
    c.draw_polygon([(WIDTH - PAD_WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH, HEIGHT/2.0 - HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle2_pos), 
                    (WIDTH - PAD_WIDTH, HEIGHT/2.0 + HALF_PAD_HEIGHT + paddle2_pos)], 
                    1, 'White', 'White')
    

    c.draw_text(str(score1), (220, 100), 45, 'White', "sans-serif")
    c.draw_text(str(score2), (350, 100), 45, 'White', "sans-serif")    

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button_reset = frame.add_button('Restart', new_game, 100)

new_game()
frame.start()

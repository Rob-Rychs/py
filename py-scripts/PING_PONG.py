# works in codeskulptor.org
# PING-PONG GAME 
import simplegui
import random
# Initialize globals
WIDTH = 600
HEIGHT = 400
a = 1 
BALL_RADIUS = 20
PONG_WIDTH=10
PONG_HEIGHT=70
paddle_speed = 5 #paddle speed
speed_factor = 1 
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle_a = [PONG_WIDTH/2,HEIGHT/2]
paddle_b = [WIDTH-PONG_WIDTH/2,HEIGHT/2] 
vel_ball = [-5.0,  0.5]
vel_a = 0
vel_b = 0
SCORE_A=0
SCORE_B=0
def draw(canvas):
    
    global a,PONG_WIDTH,HEIGHT,PONG_HEIGHT,WIDTH,ball_pos,SCORE_A,SCORE_B,vel_a,vel_b,paddle_a,paddle_b,vel_ball,speed_factor
    
    #table_layout
    canvas.draw_line((PONG_WIDTH,0),(PONG_WIDTH,HEIGHT),1,"white")
    canvas.draw_line((WIDTH/2,0),(WIDTH/2,HEIGHT),1,"white")
    canvas.draw_line((WIDTH-PONG_WIDTH,0),(WIDTH-PONG_WIDTH,HEIGHT),1,"white")
    
    #draw ball
    canvas.draw_circle(ball_pos,20,3,"red","white")
    
    #draw_paddle
    canvas.draw_line([paddle_a[0],paddle_a[1] - PONG_HEIGHT/2],[paddle_a[0],paddle_a[1] + PONG_HEIGHT/2],PONG_WIDTH,"white")
    canvas.draw_line([paddle_b[0],paddle_b[1] - PONG_HEIGHT/2],[paddle_b[0],paddle_b[1] + PONG_HEIGHT/2],PONG_WIDTH,"white")
    
    #draw_score
    canvas.draw_text(str(SCORE_A),[WIDTH/2-WIDTH/6,HEIGHT/2-HEIGHT/3],40,"white");
    canvas.draw_text(str(SCORE_B),[WIDTH/2+WIDTH/6,HEIGHT/2-HEIGHT/3],40,"white");
    
    #Update paddle_position
    if paddle_a[1] + vel_a >= PONG_HEIGHT/2 and paddle_a[1] + vel_a <= HEIGHT-PONG_HEIGHT/2:
        paddle_a[1] += vel_a 
    if paddle_b[1] + vel_b >= PONG_HEIGHT/2 and paddle_b[1] + vel_b <= HEIGHT-PONG_HEIGHT/2:
        paddle_b[1] += vel_b
        
    #update ball position
    ball_pos[0] += vel_ball[0]*speed_factor
    ball_pos[1] += vel_ball[1]*speed_factor
    
    #update ball position
    if ball_pos[0]-20 <= PONG_WIDTH:
        if paddle_a[1] - PONG_HEIGHT/2 <= ball_pos[1] <= paddle_a[1] + PONG_HEIGHT/2:
            vel_ball[0] *= -1
            speed_factor += 0.2
        else:
            ball_pos = [WIDTH/2,HEIGHT/2]
            SCORE_B += 1
            speed_factor = 1
    if ball_pos[0]+20 >= WIDTH - PONG_WIDTH:
        if paddle_b[1] - PONG_HEIGHT/2 <= ball_pos[1] <= paddle_b[1] + PONG_HEIGHT/2:
            vel_ball[0] *= -1
            speed_factor += 0.2
        else:
            ball_pos = [WIDTH/2,HEIGHT/2]
            SCORE_A += 1
            speed_factor = 1
    if ball_pos[1] - 20 <= 0:
        vel_ball[1] *= -1
    if ball_pos[1] + 20 >= HEIGHT:
        vel_ball[1] *= -1
    
def keydown(key):
    global paddle_a,paddle_b,vel_a,vel_b,paddle_speed
    
    if key == simplegui.KEY_MAP['up']:
        vel_b = -paddle_speed
    if key == simplegui.KEY_MAP['down']:
        vel_b = paddle_speed
    if key == simplegui.KEY_MAP['w']:
        vel_a = -paddle_speed
    if key == simplegui.KEY_MAP['s']:
        vel_a = paddle_speed
def keyup(key):
    global vel_a,vel_b
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        vel_b = 0
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        vel_a = 0
def reset():
    #start again
    global SCORE_A,SCORE_B,speed_factor,WIDTH,HEIGHT,ball_pos
    SCORE_A=SCORE_B=0
    ball_pos = [WIDTH/2,HEIGHT/2]
    speed_factor = a = 1
frame = simplegui.create_frame("PING-PONG",WIDTH,HEIGHT)
frame.add_button("Restart",reset,100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()

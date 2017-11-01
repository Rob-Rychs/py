#CODESKULPTOR

import simplegui

ball_pos = [100,100]


def draw(canvas):
    canvas.draw_circle(ball_pos, 20 , 1, "Red", "White")

def keydown(key):
    global ball_pos
    
    if(ball_pos[0]<=20):
        ball_pos[0] = 20
    if(ball_pos[0]>=180):
        ball_pos[0] = 180
    if(ball_pos[1]<=20):
        ball_pos[1]=20
    if(ball_pos[1]>=180):
        ball_pos[1]=180
    
    
        
    if (key == simplegui.KEY_MAP["left"]):
        ball_pos[0] -= 4
    elif (key == simplegui.KEY_MAP["right"]):
        ball_pos[0] += 4
    elif (key == simplegui.KEY_MAP["down"]):
        ball_pos[1] += 4
    elif (key == simplegui.KEY_MAP["up"]):
        ball_pos[1] -= 4        
    
frame = simplegui.create_frame("Positional ball control", 200, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.start()

#CODESKULPTOR

import simplegui
import random

paddle1_c1 = [980,250]
paddle1_c2 = [1000,250]
paddle1_c3 = [1000,350]
paddle1_c4 = [980,350]
time1 = 0
blue = 0

paddle2_c1 = [0,250]
paddle2_c2 = [20,250]
paddle2_c3 = [20,350]
paddle2_c4 = [0,350]
time2 = 0
red = 0

balltime=0
center_point = [500,300]

vel = [0.020,0.021,0.022,0.023,0.024,0.025,0.026,0.027,0.028,0.029,0.030,0.031,0.032,0.033,0.034,0.035,0.036,0.037,0.038,0.039]
x_vel = random.choice(vel)
y_vel = random.choice(vel)

start = 0

rules = ["The blue paddle is controlled by keys W and S.","The red paddle is controlled by up and down arrow keys.","One who scores 5 points first, WINS. Press START to start the game"]

win = ""

setnewgame = ""

def draw(canvas):
    
    global paddle1_c1,paddle1_c2,paddle1_c3,paddle1_c4,center_point,x_vel,y_vel,balltime,red,blue,vel,win,start,setnewgame
    canvas.draw_text(rules[0],[44,50],30,"White")
    canvas.draw_text(rules[1],[44,90],30,"White")
    canvas.draw_text(rules[2],[44,130],30,"White")
    canvas.draw_text(win,[400,300],40,"White")
    canvas.draw_text(setnewgame,[260,560],20,"White")
    canvas.draw_line([980,0],[980,600],2,"White")
    canvas.draw_line([20,0],[20,600],2,"White")
    canvas.draw_line([20,2],[980,2],4,"White")
    canvas.draw_line([20,598],[980,598],4,"White")
    canvas.draw_polygon([paddle1_c1,paddle1_c2,paddle1_c3,paddle1_c4],3,"White","Red")
    canvas.draw_polygon([paddle2_c1,paddle2_c2,paddle2_c3,paddle2_c4],3,"White","Blue")
    canvas.draw_text(str(blue),[250,300],40,"White")
    canvas.draw_text(str(red),[750,300],40,"White")
    
    if(start == 1):
        
        if(red == 5):
            win = "RED WINS !!"
            start = 0
            setnewgame = "To Play Again, Press SET NEW GAME and then press START"
        elif(blue == 5):
            win = "BLUE WINS !!"
            start = 0
            setnewgame = "To Play Again, Press SET NEW GAME and then press START"
            
        if(center_point[0] <= 40 and center_point[1] >= paddle2_c2[1] and center_point[1] <= paddle2_c3[1]):
            x_vel = -x_vel
        elif(center_point[0]<= 20):
            center_point = [500,300]
            balltime=0
            red += 1
            plusminus=[1,-1]
            x_vel = random.choice(vel)
            y_vel = random.choice(plusminus) * random.choice(vel)

        
        if(center_point[0] >= 960 and center_point[1] >= paddle1_c1[1] and center_point[1] <= paddle1_c4[1]):
            x_vel = -x_vel
        elif(center_point[0]>= 980):
            center_point = [500,300]
            balltime=0
            blue += 1
            plusminus=[1,-1]
            x_vel = -random.choice(vel)
            y_vel = random.choice(plusminus) * random.choice(vel)
         
        if(center_point[1]<=20 or center_point[1]>=580):
            y_vel = -y_vel
    
        balltime+=.2
    
        center_point[0] = center_point[0] + x_vel*balltime
        center_point[1] = center_point[1] + y_vel*balltime
    
        canvas.draw_circle(center_point,20,1,"Yellow","Yellow")

def timer1func():
    global time1,paddle1_c1,paddle1_c2,paddle1_c3,paddle1_c4
    time1+=1
    paddle1_c1[1] = paddle1_c1[1] - .8*time1
    paddle1_c2[1] = paddle1_c2[1] - .8*time1
    paddle1_c3[1] = paddle1_c3[1] - .8*time1
    paddle1_c4[1] = paddle1_c4[1] - .8*time1
     
    if(paddle1_c1[1] <= 2):
        timer1.stop()
        
def timer2func():
    global time1,paddle1_c1,paddle1_c2,paddle1_c3,paddle1_c4
    time1+=1
    paddle1_c1[1] = paddle1_c1[1] + .8*time1
    paddle1_c2[1] = paddle1_c2[1] + .8*time1
    paddle1_c3[1] = paddle1_c3[1] + .8*time1
    paddle1_c4[1] = paddle1_c4[1] + .8*time1
    
    if(paddle1_c3[1] >= 592):
        timer2.stop()
        
def timer3func():
    global time2,paddle2_c1,paddle2_c2,paddle2_c3,paddle2_c4
    time2+=1
    paddle2_c1[1] = paddle2_c1[1] - .8*time2
    paddle2_c2[1] = paddle2_c2[1] - .8*time2
    paddle2_c3[1] = paddle2_c3[1] - .8*time2
    paddle2_c4[1] = paddle2_c4[1] - .8*time2
     
    if(paddle2_c1[1] <= 1.5):
        timer3.stop()
        
def timer4func():
    global time2,paddle2_c1,paddle2_c2,paddle2_c3,paddle2_c4
    time2+=1
    paddle2_c1[1] = paddle2_c1[1] + .8*time2
    paddle2_c2[1] = paddle2_c2[1] + .8*time2
    paddle2_c3[1] = paddle2_c3[1] + .8*time2
    paddle2_c4[1] = paddle2_c4[1] + .8*time2
    
    if(paddle2_c3[1] >= 596):
        timer4.stop()
        
def move(key):
    global paddle1_c1,paddle1_c3,paddle2_c1,paddle2_c3
    
    if(paddle1_c1[1] >= 1.5):
        if(key == simplegui.KEY_MAP['up']):
            timer1.start()
        
    if(paddle1_c3[1] <= 596):
        if(key == simplegui.KEY_MAP['down']):
            timer2.start()
            
    if(paddle2_c1[1] >= 1.5):
        if(key == simplegui.KEY_MAP['W']):
            timer3.start()
        
    if(paddle2_c3[1] <= 596):
        if(key == simplegui.KEY_MAP['S']):
            timer4.start()
        
def stop(key):
    global time1,time2
    if(key == simplegui.KEY_MAP['up']):
        timer1.stop()
        time1 = 0
    if(key == simplegui.KEY_MAP['down']):
        timer2.stop()
        time1 = 0
        
    if(key == simplegui.KEY_MAP['W']):
        timer3.stop()
        time2 = 0
    if(key == simplegui.KEY_MAP['S']):
        timer4.stop()
        time2 = 0

def start():
    global start,rules
    start = 1
    rules = ["","",""]

def reset():
    global blue,red,center_point,paddle1_c1,paddle1_c2,paddle1_c3,paddle1_c4, paddle2_c1,paddle2_c2,paddle2_c3,paddle2_c4,time1,time2,balltime,win,setnewgame
    
    blue,red,time1,time2,balltime=0,0,0,0,0
    
    center_point = [500,300]
    paddle1_c1 = [980,250]
    paddle1_c2 = [1000,250]
    paddle1_c3 = [1000,350]
    paddle1_c4 = [980,350]
    
    paddle2_c1 = [0,250]
    paddle2_c2 = [20,250]
    paddle2_c3 = [20,350]
    paddle2_c4 = [0,350]
    
    win = ""
    
    setnewgame = ""

frame=simplegui.create_frame("Pong",1000,600);
frame.set_draw_handler(draw)
timer1=simplegui.create_timer(40,timer1func)
timer2=simplegui.create_timer(40,timer2func)
timer3=simplegui.create_timer(40,timer3func)
timer4=simplegui.create_timer(40,timer4func)
frame.set_keydown_handler(move)
frame.set_keyup_handler(stop)
frame.add_button("START",start,200)
frame.add_button("SET NEW GAME",reset,200)
frame.start()



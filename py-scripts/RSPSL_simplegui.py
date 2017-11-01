#CODESKULPTOR

import simplegui
import random

pno = -1
cno = -1
message="Click to Shoot !!"

def number_to_name(number):
    if(number==0):
        choice="ROCK"
    elif(number==1):
        choice="SPOCK"
    elif(number==2):
        choice="PAPER"
    elif(number==3):
        choice="LIZARD"
    else:
        choice="SCISSORS"
        
    return choice

def rspls(pno):
    global message
    cno=random.randint(0,4)
    my_choice=number_to_name(pno)
    computer_choice=number_to_name(cno)
    
    res=(pno-cno)%5
    
    if(res==1 or res==2):
            message="You chose "+my_choice+". Computer chose "+computer_choice+". YOU WIN !!"
    elif(res==3 or res==4):
            message="You chose "+my_choice+". Computer chose "+computer_choice+". YOU LOSE !!"
    else:
            message="You chose "+my_choice+". Computer chose "+computer_choice+". TIED !!"
        
    
def canny(canvas):
    canvas.draw_text(message, [20,150], 30, "Red")
    
                       
def mychoice0():
    global pno
    pno=0
    rspls(pno)

def mychoice2():
    global pno
    pno=2
    rspls(pno)
    
def mychoice4():
    global pno
    pno=4
    rspls(pno)
    
def mychoice3():
    global pno
    pno=3
    rspls(pno)
    
def mychoice1():
    global pno
    pno=1
    rspls(pno)
    

frame=simplegui.create_frame("Rock-Paper-Scissors-Lizard-Spock",850,300)
button0 = frame.add_button("Rock",mychoice0,150)
button2 = frame.add_button("Paper",mychoice2,150)
button4 = frame.add_button("Scissors",mychoice4,150)
button3 = frame.add_button("Lizard",mychoice3,150)
button1 = frame.add_button("Spock",mychoice1,150)
frame.set_draw_handler(canny)
frame.start()

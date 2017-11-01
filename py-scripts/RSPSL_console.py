#CODESKULPTOR


import simplegui
import random

pno = -1
cno = -1
win = None

def number_to_name(number):
    if(number==0):
        choice="rock"
    elif(number==1):
        choice="Spock"
    elif(number==2):
        choice="paper"
    elif(number==3):
        choice="lizard"
    else:
        choice="scissors"
        
    return choice

def rspls(pno):
    global win
    cno=random.randint(0,4)
    my_choice=number_to_name(pno)
    computer_choice=number_to_name(cno)
    print "You chose ",my_choice
    print "Computer chose ",computer_choice
    
    res=(pno-cno)%5
    
    if(res==1 or res==2):
       print "YOU WIN !"
    elif(res==3 or res==4):
       print "YOU LOSE !"
    else:
       print "TIE"
    print ""
                   
                     
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
    

    
frame=simplegui.create_frame("Rock-Paper-Scissors-Lizard-Spock",300,300)
button0 = frame.add_button("Rock",mychoice0,150)
button2 = frame.add_button("Paper",mychoice2,150)
button4 = frame.add_button("Scissors",mychoice4,150)
button3 = frame.add_button("Lizard",mychoice3,150)
button1 = frame.add_button("Spock",mychoice1,150)
frame.start()

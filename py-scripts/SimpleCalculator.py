#CODESCULPTOR

import simplegui

num1 = 0.0
num2 = 0.0
res = 0.0

def firstNumberEnter(num):
    global num1
    num1 = float(num)
    
def secondNumberEnter(num):
    global num2
    num2 = float(num)
    
def likhdo(canvas):
    canvas.draw_text(str(res),[50,112],40,"Red")
    
def rearrange():
    global num1,num2,res
    if(res == "Can't divide by zero !"):
        text1.set_text(str(num1))
    else:
        num1=res
        text1.set_text(str(res))
       
    num2=0
    text2.set_text("")
   
def add():
    global num1,num2,res
    res = num1 + num2
    rearrange()
    

def subtract():
    global num1,num2,res
    res = num1 - num2
    rearrange()
    

def multiply():
    global num1,num2,res
    res = num1 * num2
    rearrange()
    
    
def divide():
    global num1,num2,res
    if(num2==0):
        res = "Can't divide by zero !"
    else:
        res = num1 / num2
    rearrange()
    
    


frame = simplegui.create_frame("Calculator", 400, 250)
frame.add_button("Add",add,100)
frame.add_button("Subtract",subtract,100)
frame.add_button("Multiply",multiply,100)
frame.add_button("Divide",divide,100)
frame.set_draw_handler(likhdo)
text1 = frame.add_input("Enter first number here :",firstNumberEnter,200)
text2 = frame.add_input("Enter second number here :",secondNumberEnter,200)
frame.start()

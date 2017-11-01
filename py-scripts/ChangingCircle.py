#CODESKULPTOR

import simplegui

radius = 10
use_radius = 10


def increase():
    global radius
    radius += 1
    label.set_text("Value : "+str(radius))
    label2.set_text("Radius : "+str(radius))
    

def decrease():
    global radius
    if(radius > 1):
        radius -= 1
        
    label.set_text("Value : "+str(radius))
    label2.set_text("Radius : "+str(radius))

def change_circle():
    global use_radius
    use_radius=radius
    

def draw(canvas):
    canvas.draw_circle([100,100],use_radius,4,"Red")
    

frame=simplegui.create_frame("hello",200,200)
label = frame.add_label("Value : "+str(radius))
frame.add_button("Increase",increase)
frame.add_button("Decrease",decrease)
label2 = frame.add_label("Radius : 10")
frame.add_button("Change Circle",change_circle)
frame.set_draw_handler(draw)
frame.start()

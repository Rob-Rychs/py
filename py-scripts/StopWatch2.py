#CODESKULPTOR

import simplegui

centisecond = "00"
second = "00"
minute = "00"
count = 0
prev_time = 0.0

def centisecond_update():
    global centisecond
    if(centisecond=="99"):
        centisecond = "00"
    else:
        if(centisecond[1] == "9"):
            centisecond = str(int(centisecond[0])+1)+"0"
        else:
            centisecond = centisecond[0]+str(int(centisecond[1])+1)
        
def second_update():
    global second
    if(second=="59"):
        second = "00"
    else:
        if(second[1] == "9"):
            second = str(int(second[0])+1)+"0"
        else:
            second = second[0]+str(int(second[1])+1)

def minute_update():
    global minute
    if(minute[1] == "9"):
        minute = str(int(minute[0])+1)+"0"
    else:
        minute = minute[0]+str(int(minute[1])+1)
        
def draw(canvas):
    canvas.draw_text(minute+" : "+second+" . "+centisecond,[90,120],80,"Blue")
       
def start():
    timer_centisecond.start()
    timer_second.start()
    timer_minute.start()

def restart():
    global centisecond, second, minute
    centisecond = "00"
    second = "00"
    minute = "00"

def take_lap():
    global count, prev_time
    count += 1
    print "LAP "+str(count) 
    print "Present time = "+minute+" : "+second+" . "+centisecond
    time = int(minute)*60 + int(second) + 0.01*int(centisecond)
    if(count == 1):
        lap_time = time - prev_time
    else:
        lap_time = time - prev_time
    
    prev_time = time
    print "Lap time     = ",str(lap_time // 60)[0], " minute(s) and",lap_time % 60,"second(s)"
    print 
    

def pause():
    if(pause_button.get_text()== "Pause"):
        pause_button.set_text("Resume")
        timer_centisecond.stop()
        timer_second.stop()
        timer_minute.stop()
    else:
        pause_button.set_text("Pause")
        start()

def reset():
    timer_centisecond.stop()
    timer_second.stop()
    timer_minute.stop()
    restart()
    start_button.set_text("Start")    
        
frame=simplegui.create_frame("Stopwatch",520,200)
frame.set_canvas_background("Yellow")

start_button = frame.add_button("Start",start,100)
frame.add_button("Restart",restart,100)
frame.add_button("Lap",take_lap,100)
pause_button = frame.add_button("Pause",pause,100)
frame.add_button("Reset",reset,100)

timer_centisecond = simplegui.create_timer(10,centisecond_update)
timer_second = simplegui.create_timer(1000,second_update)
timer_minute = simplegui.create_timer(60*1000,minute_update)

frame.set_draw_handler(draw)
frame.start()

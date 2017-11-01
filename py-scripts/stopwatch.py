# works in codeskulptor.org
import simplegui
minutes = 0
seconds = 0
millisec = 0 
#def start_handler():
#def tick():
def tick():
    """timer"""
    global millisec,minutes,seconds
    millisec += 100
    if millisec == 1000:
        seconds += 1
        millisec = 0
    if seconds == 60:
        minutes += 1
        seconds = 0
def start_handler():
    timer.start()
def stop_handler():
    timer.stop()
def reset_handler():
    global millisec,seconds,minutes
    millisec=seconds=minutes=0
    timer.stop()
def draw_handler(canvas):
    """draw handler"""
    canvas.draw_text(str(minutes)+":",[100,100],40,"white")
    canvas.draw_text(str(seconds/10),[140,100],40,"white")
    canvas.draw_text(str(seconds%10)+":",[164,100],40,"white")
    canvas.draw_text(str(millisec/100),[200,100],40,"white")
timer = simplegui.create_timer(100,tick) 
frame = simplegui.create_frame("Stopwatch",300,300)
frame.add_button("start",start_handler,100)
frame.add_button("stop",stop_handler,100)
frame.add_button("reset",reset_handler,100)
frame.set_draw_handler(draw_handler)
frame.start()

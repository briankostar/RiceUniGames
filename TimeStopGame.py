#"Stopwatch: The Game"
import simplegui


# define global variables
time = 0
str_time = "00:00:0"
timer_status = True
wins = 0
plays = 0
msecond = "0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t = t*10
    global msecond
    minute = int(t / 6000)
    second = int(t / 100) % 60
    msecond = t % 100
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)
    
    msecond = str(int(msecond/10))
        
    return minute + ":" + second + ":" + msecond    
    

def time_handler():
    global time
    time += 0.1
    global str_time
    str_time = format(time)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    time_handler()
    global timer_status
    timer_status = True

def stop():
    timer.stop()
    global timer_status
    global wins
    global plays
    if timer_status:
        if msecond == "0":
            wins += 1
        else:
            plays += 1
    timer_status = False

def reset():
    global time
    global wins
    global plays
    time = 0
    wins = 0
    plays = 0

# define draw handler
def draw(canvas):
    canvas.draw_text(str_time, [75,120], 50, "White") 
    canvas.draw_text(str(wins), [230,35], 35, "Yellow")
    canvas.draw_text("/", [255,35], 35, "Yellow")
    canvas.draw_text(str(plays), [270,35], 35, "Yellow")
    
# create frame
f = simplegui.create_frame("Stopwatch Game", 300, 200)
timer = simplegui.create_timer(10, time_handler)

# register event handlers
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", reset, 100)
f.set_draw_handler(draw)

# start frame
f.start()

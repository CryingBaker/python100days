from tkinter import Tk,Button,Label,Canvas,PhotoImage
import time
from pomotimer import Timer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = [0,25,0]
SHORT_BREAK_MIN = [0,5,0]
LONG_BREAK_MIN = [0,20,0]

time = []
reset = False
pause = False
timer_id = None
type = "work"
next = "short-break"

def start_timer():
    global time
    global pause
    global timer_id
    global type
    global next
    print(time)
    if type == "work":
        label.config(foreground = GREEN)
        label.config(text = "Timer")
    elif type == "short-break":
        label.config(foregrounf = PINK)
        label.config(text="Break")
    elif type == "long-break":
        label.config(foreground = RED)
        label.config(text="Break")
    if pause == True:
        return
    elif time[1] > 0 or time[2] > 0:
        if time[2]!=0:
            time[2] -= 1
        elif time[2] == 0:
            time[1] -= 1
            time[2] = 59
        elif time[1] == 0:
            time[0] -= 1
            time[1] = 59
        timer_id = window.after(1000,start_timer)
        timer_text = format_time(time)
        canvas.itemconfig(timer,text=timer_text)
    else:
        if not reset:
            if type == "work":
                checklist_label.config(text=f"{checklist_label["text"]}✔")
                if len(checklist_label["text"])%5 == 0:
                    next = "long-break"
                else:
                    next = "short-break"
            temp = type
            type = next
            next = temp
            if type == "work":
                time = list(WORK_MIN)
            elif type == "short-break":
                time = list(SHORT_BREAK_MIN)
            elif type == "long-break":
                time = list(LONG_BREAK_MIN)
            start_timer()

def format_time(time):
    time_seconds = str(time[2])
    time_minutes = str(time[1])
    # time_hours = str(time[0])
    if len(time_seconds) != 2:
        time_seconds += "0"
        time_seconds = time_seconds[::-1]
    if len(time_minutes) != 2:
        time_minutes += "0"
        time_minutes = time_minutes[::-1]
    # if len(time_hours) != 2:
    #     time_hours += "0"
    #     time_hours = time_hours[::-1]
    return f"{time_minutes}:{time_seconds}"

def clicked_btn1():
    global time
    global reset
    global pause
    if btn_1["text"] == "Start":
        time = list(WORK_MIN)
        reset = False
        start_timer()
        btn_1["text"] = "Pause"
    elif btn_1["text"] == "Pause":
        btn_1["text"] = "Resume"
        pause = True
    elif btn_1["text"] == "Resume":
        btn_1["text"] = "Pause"
        pause = False
        start_timer()

def clicked_btn2():
    global time
    global pause
    global reset
    global timer_id
    timer_text = format_time([0,0,0])
    canvas.itemconfig(timer,text=timer_text)
    reset = True
    btn_1["text"] = "Start"
    label.config(text = "Timer")
    label.config(foreground=GREEN)
    type = "work"
    next = "short-break"
    pause = False
    time = [0,0,0]
    checklist_label.config(text="")

window = Tk()
window.title("Pomodoro App")
window.config(background=YELLOW)
window.config(padx=100,pady=50)

label = Label(text="Timer",font=(FONT_NAME,40),background=YELLOW,foreground=GREEN)

canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(background=YELLOW)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = "00:00"
timer = canvas.create_text(100,130, text=timer_text,fill="white",font=(FONT_NAME,35,"bold"))

btn_1 = Button(text="Start",width=3,border=0,highlightthickness=0,command = clicked_btn1)

btn_2 = Button(text="Reset",width =3, border=0,highlightthickness=0,command=clicked_btn2)

checklist_label_text = ""
checklist_label = Label(text=checklist_label_text,foreground=GREEN,background=YELLOW)

label.grid(column=1,row=0)
canvas.grid(column=1,row=1) 
btn_1.grid(column=0,row=2)
btn_2.grid(column=2,row=2)
checklist_label.grid(column=1,row=3)

window.mainloop()
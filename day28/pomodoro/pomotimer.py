FONT_NAME = "Courier"

class Timer:
    def __init__(self,window,timer_text,canvas):
        self.window = window
        self.timer_text = timer_text
        self.time_label_canvas = canvas
    
        def start_timer(self,time):
            while time[1] > 0 or time[2] > 0:
                if time[1]>0:
                    time[1] -= 1
                    time[2] = 59
                elif time[0]>0:
                    time[0] -= 1
                    time[1] = 59
                self.window.after(1000,self.start_timer,time)
                self.format_time(time)
                self.time_label_canvas.create_text(100,130, text=self.timer_text,fill="white",font=(FONT_NAME,35,"bold"))
                
        def format_time(self,time):
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
            self.timer_text = f"{time_minutes}:{time_seconds}"


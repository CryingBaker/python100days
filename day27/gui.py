import tkinter
import time

def clicked():
    my_label["text"] = input.get()

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=300, height = 300)

my_label = tkinter.Label(text="Not Clicked",font=("Arial",24,"bold"))
my_label.grid(column = 0,row = 0)

my_button = tkinter.Button(text="Submit",command=clicked)
my_button.grid(column = 1, row = 1)

input = tkinter.Entry()
input.grid(column = 4,row = 2)

new_button = tkinter.Button(text = "new button")
new_button.grid(column = 2, row = 0)




window.mainloop()

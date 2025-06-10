from tkinter import Tk, Label, Entry, Button


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output["text"] = round(km,2)


window = Tk()
window.title("Mile to Km Converter")
miles_input = Entry(width=10)
miles_label = Label(text="Miles")
is_equal_to_label = Label(text="is equal to")
km_output = Label(text="0")
km_label = Label(text="km")
convert_button = Button(text="Calculate", command=convert)

is_equal_to_label.grid(column=0, row=1)
miles_input.grid(column=1, row=0)
km_output.grid(column=1, row=1)
convert_button.grid(column=1, row=2)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)

window.mainloop()

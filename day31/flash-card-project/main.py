import random
from tkinter import Tk,PhotoImage,Button,Canvas
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
CANVAS_IMAGE_POSITION_X = 400
CANVAS_IMAGE_POSITION_Y = 263
CANVAS_LANGUAGE_POSITION_X = 400
CANVAS_LANGUAGE_POSITION_Y = 150

canvas_data = {
    "image" : 0,
    "language" : 0,
    "word" : 0
}

word_list_dict = {}
current_word = -1

def change_canvas_content(language,word,card_pos):
    canvas.delete(canvas_data["image"])
    canvas.delete(canvas_data["language"])
    canvas.delete(canvas_data["word"])
    canvas_data["image"] = canvas.create_image(CANVAS_IMAGE_POSITION_X,CANVAS_IMAGE_POSITION_Y,image = card_pos)
    canvas_data["language"]= canvas.create_text(CANVAS_LANGUAGE_POSITION_X,CANVAS_LANGUAGE_POSITION_Y,text = language,font = ("Arial",40,"italic"),fill="black")
    canvas_data["word"]= canvas.create_text(CANVAS_IMAGE_POSITION_X,CANVAS_IMAGE_POSITION_Y,text = word, font = ("Arial",60,"bold"),fill = "black")

def load_data():
    global word_list_dict
    try:
        file = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        file = pandas.read_csv("data/french_words.csv")
    finally:
        word_list_dict = file.to_dict(orient="index")
        print(word_list_dict)

def choose_random_word():
    global current_word
    global current_french_word
    global current_english_word
    choice = random.choice(list(word_list_dict.keys()))
    current_word = choice
    current_french_word = word_list_dict[choice]["French"]
    current_english_word = word_list_dict[choice]["English"]

def show_french_word():
    choose_random_word()
    change_canvas_content("French",current_french_word,card_front)
    window.after(3000,show_english_word)

def show_english_word():
    change_canvas_content("English",current_english_word,card_back)
    window.after(3000,show_french_word)

def knowanswer():
    word_list_dict.pop(current_word)

def save_data():
    data = pandas.DataFrame.from_dict(word_list_dict,orient="index")
    data.to_csv("data/words_to_learn.csv",index=False)

window = Tk()

window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
window.minsize(width = 800, height= 651)
window.title("Flashy")

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file = "images/wrong.png")

canvas = Canvas(height= 526, width=800,highlightthickness=0,background=BACKGROUND_COLOR)

wrong_button = Button(image = wrong, highlightthickness=0, background=BACKGROUND_COLOR, border = 0)

right_button = Button(image= right, highlightthickness=0, background=BACKGROUND_COLOR,border = 0,command = knowanswer)

canvas.grid(column=0,row = 0, columnspan=2)
wrong_button.grid(column = 0, row = 1)
right_button.grid(column=1, row = 1 )

load_data()
show_french_word()

window.mainloop()

save_data()
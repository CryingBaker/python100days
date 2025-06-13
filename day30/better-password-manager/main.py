from tkinter import Tk,PhotoImage,Canvas,Label,Entry,Button
import tkinter
import tkinter.messagebox
from password_generator import generate_password
from extra_features import get_mostfrequent_email,search,NotFoundError
import json
import pyperclip

DEFAULT_ALPHABETS = 10
DEFAULT_NUMBERS = 3
DEFAULT_SYMBOLS = 3

# ---------------------------- WEBSITE SEARCHER -------------------------------#
def search_website():
    website = website_input.get()
    try:
        password = search(website)
    except NotFoundError:
        tkinter.messagebox.showerror("Not Found","Website not found")
    else:
        tkinter.messagebox.showinfo("Password",f"Username/Email : {password["username"]}\nPassword: {password["password"]}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password = generate_password(DEFAULT_ALPHABETS,DEFAULT_NUMBERS,DEFAULT_SYMBOLS)
    password_input.delete(0,tkinter.END)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    data = {
        website:{
            "username":username,
            "password":password,
        }
    }
    if len(website) <= 0 or len(username)<= 0 or len(password)<=0:
        tkinter.messagebox.showerror("Empty Fields","Please fill all fields!") 
    else:
        should_continue = tkinter.messagebox.askokcancel("Are you sure?",f"Details:\nWebsite:{website}\nUsername:{username}\nPassword:{password}\nAre you sure you want to add this password?")
        if should_continue:
            try:
                password_file = open("passwords.json","r") 
            except FileNotFoundError:
                password_file = open("passwords.json","w")
                json.dump(data,password_file,indent=4)
                password_file.close()
            else:
                passwords = json.load(password_file)
                print(f"Before updating {passwords}")
                passwords.update(data)
                print(f"After updating {passwords}")
                password_file.close()
                password_file = open("passwords.json","w")
                json.dump(passwords,password_file,indent = 4)
        website_input.delete(0,tkinter.END)
        password_input.delete(0,tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(background="white")
window.config(padx=50,pady=50)

logo = PhotoImage(file = "logo.png")
canvas = Canvas(width=200,height=200,highlightthickness=0,background="white")
canvas.create_image(100,100,image = logo)

website_label = Label(text = "Website:",highlightthickness=0,background="white",foreground="black")

username_label = Label(text = "Email/Username:",highlightthickness=0,border=0,background="white",foreground="black")

password_label = Label(text = "Password:",highlightthickness=0,border=0,background="white",foreground="black")

website_input = Entry(background="white",highlightthickness=0,foreground="black",width=21)
website_input.focus()

username_input = Entry(background="white",highlightthickness= 0,foreground="black",width=39)
most_frequent_email = ""
most_frequent_email = get_mostfrequent_email()
username_input.insert(0,most_frequent_email)

password_input = Entry(highlightthickness=0,background="white",foreground="black",width = 21)

search_btn = Button(text="Search", highlightthickness=0,background="white",foreground="black",width=14,command=search_website)

generate_btn = Button(text="Generate Password", highlightthickness=0,background="white",foreground="black",width=14,command=gen_password)

add_btn = Button(text="Add", highlightthickness=0,border=0,background="white",foreground="black",width=36,command = save_password)

canvas.grid(column = 1, row = 0)
website_label.grid(column=0,row=1)
username_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)
website_input.grid(column=1,row=1)
search_btn.grid(column=2,row=1)
username_input.grid(column=1,row=2,columnspan=2)
password_input.grid(column=1,row=3)
generate_btn.grid(column = 2, row = 3)
add_btn.grid(column=1,row = 4,columnspan=2)

window.mainloop()

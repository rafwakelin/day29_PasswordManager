from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    """Generates a random password and saves it on the clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '@', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(1, 1))]
    pw_numbers = [choice(numbers) for _ in range(randint(3, 4))]
    password_list = pw_numbers + pw_symbols + pw_letters
    shuffle(password_list)

    password = "".join(password_list)

    pw_entry.delete(0, END)
    pw_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the provided information to a txt file"""
    website = website_entry.get()
    username = username_entry.get()
    password = pw_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(message="Please fill all the fields")
    else:
        proceed = messagebox.askokcancel(message=f"Data to access {website}.\nUsername: {username}\nPassword: "
                                                 f"{password}\nWould you like to save?")
        if proceed:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "wrafael.queiroz@icloud.com")
pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

pw_button = Button(text="Generate Password", command=new_password)
pw_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

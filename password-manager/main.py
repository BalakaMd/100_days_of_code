from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import os
import pyperclip
import json

base_dir = os.path.dirname(__file__)
canvas_image_path = os.path.join(base_dir, './logo.png')
json_data_path = os.path.join(base_dir, './data.json')


# ---------------------------- PASSWORD SEARCH  ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()
    password = ...
    email = ...

    def enter_password():

        def check_password():
            if entry_password.get() == "240218":
                messagebox.showinfo(title="Done", message=f"Email: {email}\n Password: {password}")
            else:
                messagebox.showinfo(title="Opps", message=f"Sorry, incorrect password :(")
            new_window.destroy()

        new_window = Toplevel(window)
        new_window.title("Please enter a password")
        new_window.resizable(width=False, height=False)
        x_2 = (new_window.winfo_screenwidth() - new_window.winfo_reqwidth()) / 2
        y_2 = (new_window.winfo_screenheight() - new_window.winfo_reqheight()) / 2
        new_window.wm_geometry("+%d+%d" % (x_2, y_2))

        lbl_password = Label(new_window, text="Enter a password")
        lbl_password.grid(row=0, column=0)

        entry_password = Entry(new_window)
        entry_password.focus()
        entry_password.grid(row=0, column=1)

        btn_ok = Button(new_window, text="Ok", default=ACTIVE, command=check_password)
        btn_ok.grid(row=2, column=0, columnspan=2)

    try:
        with open(json_data_path, "r") as data_file:
            data = json.load(data_file)
        password = data[website]["password"]
        email = data[website]["email"]
        enter_password()
    except (KeyError, FileNotFoundError):
        messagebox.showinfo(title="Oops", message="Please make sure you enter a valid Website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(json_data_path, "r") as data_fle:
                data = json.load(data_fle)
                data.update(new_data)
            with open(json_data_path, "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open(json_data_path, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=90, pady=50)
window.resizable(width=False, height=False)
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 3
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3
window.wm_geometry("+%d+%d" % (x, y))

# Create a canvas
canvas_image = PhotoImage(file=canvas_image_path)
canvas = Canvas(width=200, height=224)
canvas.create_image(145, 100, image=canvas_image)
canvas.grid(row=0, column=1)

# Create a labels
website_logo = Label(text="Website:")
website_logo.grid(row=1, column=0)

username_logo = Label(text="Email/Username:")
username_logo.grid(row=2, column=0)

password_logo = Label(text="Password:")
password_logo.grid(row=3, column=0)

# Create an entry
website_entry = Entry(width=19)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_entry = Entry(width=37)
username_entry.insert(0, "md.balaka@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry()
password_entry.grid(row=3, column=1)

# Create a button
btn_add = Button(text="Add", width=35, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

btn_generate = Button(text="Generate Password", command=generate_password)
btn_generate.grid(row=3, column=2)

btn_search = Button(text="Search", width=13, command=find_password)
btn_search.grid(row=1, column=2)

window.mainloop()

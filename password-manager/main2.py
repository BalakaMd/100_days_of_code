import os
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from random import choice, shuffle, randint
import pyperclip


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.config(padx=90, pady=50)
        self.root.resizable(width=False, height=False)

        # Create a canvas
        canvas_image_path = os.path.join(os.path.dirname(__file__), './logo.png')
        self.canvas_image = PhotoImage(file=canvas_image_path)
        self.canvas = tk.Canvas(width=200, height=224)
        self.canvas.create_image(145, 100, image=self.canvas_image)
        self.canvas.grid(row=0, column=1)

        # Create labels, entries, and buttons
        self.website_entry = tk.Entry(width=19)
        self.website_entry.focus()
        self.website_entry.grid(row=1, column=1)

        self.username_entry = tk.Entry(width=37)
        self.username_entry.insert(0, "md.balaka@gmail.com")
        self.username_entry.grid(row=2, column=1, columnspan=2)

        self.password_entry = tk.Entry()
        self.password_entry.grid(row=3, column=1)

        self.btn_add = tk.Button(text="Add", width=35, command=self.save)
        self.btn_add.grid(row=4, column=1, columnspan=2)

        self.btn_generate = tk.Button(text="Generate Password", command=self.generate_password)
        self.btn_generate.grid(row=3, column=2)

        self.btn_search = tk.Button(text="Search", width=13, command=self.find_password)
        self.btn_search.grid(row=1, column=2)

        self.json_data_path = os.path.join(os.path.dirname(__file__), './data.json')

    def generate_password(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!#$%&()*+'

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = ''.join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save(self):
        website = self.website_entry.get().capitalize()
        email = self.username_entry.get()
        password = self.password_entry.get()
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
                with open(self.json_data_path, "r") as data_fle:
                    data = json.load(data_fle)
                    data.update(new_data)
                with open(self.json_data_path, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open(self.json_data_path, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)

    def find_password(self):
        website = self.website_entry.get().capitalize()

        def enter_password():
            def check_password():
                if entry_password.get() == "240218":
                    messagebox.showinfo(title="Done", message=f"Email: {email}\n Password: {password}")
                else:
                    messagebox.showinfo(title="Opps", message=f"Sorry, incorrect password :(")
                new_window.destroy()

            new_window = tk.Toplevel(self.root)
            new_window.title("Please enter a password")
            new_window.resizable(width=False, height=False)
            x_2 = (new_window.winfo_screenwidth() - new_window.winfo_reqwidth()) / 2
            y_2 = (new_window.winfo_screenheight() - new_window.winfo_reqheight()) / 2
            new_window.wm_geometry("+%d+%d" % (x_2, y_2))

            lbl_password = tk.Label(new_window, text="Enter a password")
            lbl_password.grid(row=0, column=0)

            entry_password = tk.Entry(new_window)
            entry_password.focus()
            entry_password.grid(row=0, column=1)

            btn_ok = tk.Button(new_window, text="Ok", default=tk.ACTIVE, command=check_password)
            btn_ok.grid(row=2, column=0, columnspan=2)

        try:
            with open(self.json_data_path, "r") as data_file:
                data = json.load(data_file)
            password = data[website]["password"]
            email = data[website]["email"]
            enter_password()
        except (KeyError, FileNotFoundError):
            messagebox.showinfo(title="Oops", message="Please make sure you enter a valid Website")


def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

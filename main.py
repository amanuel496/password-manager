import tkinter
from tkinter import END
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_STYLE = "Arial"
FONT_SIZE = 10


# Password Generator Project

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(password_entry):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website_entry, username_entry, password_entry):
    # Save the password info
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website and username and password:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            # Wipe out the contents from GUI
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
def main():
    window = tkinter.Tk("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tkinter.Canvas(width=200, height=200)
    logo_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    website_label = tkinter.Label(text="Website", font=(FONT_STYLE, FONT_SIZE))
    website_label.grid(row=1, column=0)

    email_label = tkinter.Label(text="Email/Username", font=(FONT_STYLE, FONT_SIZE))
    email_label.grid(row=2, column=0)

    password_label = tkinter.Label(text="Password", font=(FONT_STYLE, FONT_SIZE))
    password_label.grid(row=3, column=0)

    website_entry = tkinter.Entry(width=39)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()

    username_entry = tkinter.Entry(width=39)
    username_entry.grid(row=2, column=1, columnspan=2)
    username_entry.insert(END, "johnwick@gmail.com")

    password_entry = tkinter.Entry(width=21)
    password_entry.grid(row=3, column=1)

    generate_password_btn = tkinter.Button(text="Generate Password", command=lambda: generate_password(password_entry))
    generate_password_btn.grid(row=3, column=2)

    add_btn = tkinter.Button(text="Add", width=34,
                             command=lambda: save_password(website_entry, username_entry, password_entry))
    add_btn.place(x=add_btn.winfo_x() + 50, y=add_btn.winfo_y())
    add_btn.grid(row=4, column=1, columnspan=2)

    '''This statement is used to shift the "Add button" to the right
    window.grid_columnconfigure(1, weight=1)
    
    ToDo: Check why it's not working
    '''

    window.mainloop()


if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Invalid", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)

# PASSWORD FINDER


def find_password():
    website = website_input.get()

    with open("data.json") as data_file:
        data = json.load(data_file)

        if website in data:
            email = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists.")


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=220, height=220)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_input = Entry(width=40)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username")
username_label.grid(column=0, row=2)
username_input = Entry(width=40)
username_input.insert(0, "default")
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password = Button(text="Genereate Password",
                           command=generate_password)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

add = Button(text="Add Password", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()

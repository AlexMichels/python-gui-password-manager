from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


FONT = "Arial"
FONTSIZE = 15
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_3.delete(0, "end")
    entry_3.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_txt():
    website_str = entry_1.get()
    user_str = entry_2.get()
    pw_str = entry_3.get()
    pw_dict = {website_str: {"email": user_str, "password": pw_str}}
    if user_str == "" or pw_str == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
                data.update(pw_dict)
        except FileNotFoundError:
            data = pw_dict
        with open("password.json", "w") as file:
            json.dump(data, file, indent=4)
            entry_1.delete(0, "end")
            entry_3.delete(0, "end")
            entry_2.delete(0, "end")
            entry_2.insert(END, "michels@dialogplus.nrw")

# ---------------------------- SEARCH ------------------------------- #
def search():
    website_str = entry_1.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=website_str, message="No Data File Found")
    else:
        try:
            searched_dict = data[website_str]
        except KeyError as error_message:
            messagebox.showinfo(title=website_str, message=f"No details for {error_message} exist")
        else:
            searched_email = searched_dict["email"]
            searched_pw = searched_dict["password"]
            messagebox.showinfo(title=website_str, message=f"Email: {searched_email} \n Password:  {searched_pw} ")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=40)

# canvas, bild
canvas = Canvas(height=200, width=189)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
label_1 = Label(text="Website:", font=(FONT, FONTSIZE, "normal"))
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:", font=(FONT, FONTSIZE, "normal"))
label_2.grid(column=0, row=2)

label_3 = Label(text="Password", font=(FONT, FONTSIZE, "normal"))
label_3.grid(column=0, row=3)

# Entry
entry_1 = Entry(width=20)
entry_1.grid(column=1, row=1, pady=1)
entry_1.focus()

entry_2 = Entry(width=35)
entry_2.insert(END, "michels@dialogplus.nrw")
entry_2.grid(column=1, row=2, columnspan=2, pady=1)

entry_3 = Entry(width=20)
entry_3.grid(column=1, row=3, pady=1)

# Button
generate_password_button = Button(text="Generate Password", width=11, command=password_generate)
generate_password_button.grid(column=2, row=3, pady=1)

add_button = Button(text="Add", width=33, command=add_to_txt)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=11, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
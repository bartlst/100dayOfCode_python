from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for _ in range(nr_letters)]

    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + number_list + symbols_list
    random.shuffle(password_list)
    password = "".join(password_list)
    input_pass_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    new_data = {input_web_box.get(): {
        "email": input_username_box.get(),
        "password": input_pass_box.get()
    }}
    if input_web_box.get() == "" or input_username_box.get() == "" or input_pass_box.get() == "":
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        if_save = messagebox.askokcancel(title=input_web_box.get(), message=f"These are the details entered: "
                                                                  f"\n Website: {input_web_box.get()}"
                                                                  f"\n E-mail: {input_username_box.get()} "
                                                                  f"\n Password: {input_pass_box.get()} ")

        if if_save:
            try:
                with open('secret_file.json', mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

            except FileNotFoundError:
                with open('secret_file.json', mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open('secret_file.json', mode="w") as file:
                    json.dump(data, file, indent=4)

            finally:
                input_pass_box.delete(0, END)
                input_web_box.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    try:
        with open('secret_file.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "File not exist")
    else:
        try:
            password = data[input_web_box.get()]["password"]
            email = data[input_web_box.get()]["email"]
        except KeyError:
            messagebox.showinfo("Error", "Password for this website not exist")
        else:
            messagebox.showinfo(title=input_web_box.get(), message=f"\n E-mail: {email}\n Password: {password} ")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=60, pady=60)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text='Website:', font=("arial", 14))
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username:', font=("arial", 14))
username_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=("arial", 14))
password_label.grid(row=3, column=0)


# input box

input_web_box = Entry()
input_web_box.config(width=32)
input_web_box.grid(column=1, row=1)

input_username_box = Entry()
input_username_box.config(width=50)
input_username_box.grid(column=1, row=2, columnspan=2)
input_username_box.insert(0, "example@mail.com")

input_pass_box = Entry()
input_pass_box.config(width=32)
input_pass_box.grid(column=1, row=3)

# buttons

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)


search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1)
search_button.config(width=14)

window.mainloop()


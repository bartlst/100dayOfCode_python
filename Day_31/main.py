from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- RANDOM WORD ------------------------------- #

def random_word():
    word_list = pandas.read_csv('data/french_words.csv')
    french_word = {"" for index, row in word_list.iterrows()}
    canvas.itemconfigure(word_text, text=random.choice(french_word).French)

# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# card
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_back)
title_text = canvas.create_text(400, 150, text="Title", fill="white", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="white", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons

right_bt_img = PhotoImage(file='images/right.png')
wrong_bt_img = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_bt_img, highlightthickness=0, command=random_word)
wrong_button = Button(image=wrong_bt_img, highlightthickness=0, command=random_word)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)



window.mainloop()
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_data = pandas.read_csv('data/french_words_to_learn.csv')
except FileNotFoundError:
    word_data = pandas.read_csv('data/french_words.csv')

to_learn = word_data.to_dict(orient="records")
current_card = None
flip_timer = None

# ---------------------------- RANDOM WORD ------------------------------- #

def flip_card(word):
    canvas.itemconfigure(canvas_image, image=card_front)
    canvas.itemconfigure(word_text, text=word["English"], fill="black")
    canvas.itemconfigure(title_text, text="English", fill="black")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    print(len(to_learn))
    canvas.itemconfigure(canvas_image, image=card_back)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(word_text, text=current_card["French"], fill="white")
    canvas.itemconfigure(title_text, text="French", fill="white")
    flip_timer = window.after(3000, flip_card, current_card)


def is_known():
    print(current_card)
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/french_words_to_learn.csv', index=False)
    next_word()

# ---------------------------- UI SETUP ------------------------------- #

# window


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# card
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_back)
title_text = canvas.create_text(400, 150, text="Title", fill="white", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="white", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons

right_bt_img = PhotoImage(file='images/right.png')
wrong_bt_img = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_bt_img, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_bt_img, highlightthickness=0, command=next_word)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip_card, current_card)
next_word()
window.mainloop()

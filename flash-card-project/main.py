from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
OLD_BACKGROUND_IMG = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/images/card_front.png"
NEW_BACKGROUND_IMG = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/images/card_back.png"
CROSS_IMG = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/images/wrong.png"
CHECK_IMG = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/images/right.png"
CSV_FILE = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/data/french_words.csv"
LEARN_FILE = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/flash-card-project/data/words_to_learn.csv"
try:
    data = pandas.read_csv(LEARN_FILE)
except FileNotFoundError:
    orginal_data = pandas.read_csv(CSV_FILE)
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn) 
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_bg)
    flip_timer = window.after(3000, flip)

def flip():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_bg)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_bg = PhotoImage(file=OLD_BACKGROUND_IMG)
back_bg = PhotoImage(file=NEW_BACKGROUND_IMG)
card_bg = canvas.create_image(400, 263, image=front_bg)
title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file=CROSS_IMG)
wrong_btn = Button(image=cross_img, command=next_card)
wrong_btn.grid(row=1, column=0)

check_img = PhotoImage(file=CHECK_IMG)
right_btn = Button(image=check_img, command=is_known)
right_btn.grid(row=1, column=1)

flip_timer = window.after(3000, flip)
next_card()


window.mainloop()
from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel",40, "italic")
FONT_DESCRIPTION = ("Ariel",40, "bold")


current_card = {}

try:
    data = pd.read_csv('data/wordtolearn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/projectfile.csv')
    word_dict = data.to_dict(orient='records')
else:
    word_dict = data.to_dict('records')


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = choice(word_dict)
    canvas.itemconfig(card_title, text='Persian', font=FONT_TITLE, fill='black')
    canvas.itemconfig(card_description, text=current_card['Persian'], font=FONT_DESCRIPTION, fill='black')
    canvas.itemconfig(card_bg, image=card_front)
    flip_time = window.after(3000, display)


def is_known():
    word_dict.remove(current_card)
    df = pd.DataFrame(word_dict)
    df.to_csv('data/wordtolearn.csv', index=False)
    next_card()


def display():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text='English', font=FONT_TITLE, fill = 'white')
    canvas.itemconfig(card_description, text=current_card['English'], font=FONT_DESCRIPTION, fill = 'white')


window = Tk()
window.title("Know the Word")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=display)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263,  image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,150, text="title", font=FONT_TITLE)
card_description = canvas.create_text(400,263,text="description", font=FONT_DESCRIPTION)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file='images/wrong.png')
left_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
left_btn.grid(row=1, column=0)

next_card()



window.mainloop()
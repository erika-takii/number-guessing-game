# 1. create the UI 
#  - window
#  - button (exit, start, guess)
#  - label (title, result/hint)
#  - entry field
# 2. create logic of game
#  - global variable (TARGET, RETRIES)
#  - initialize
#  - logic part

import tkinter as tk #tkinter: module
import random #module

# global variable to store the target number and the number of retires
# manage shared state across different functions in the application
TARGET = 1
RETRIES = 0

# define a function that updates the result label accordingly
def update_result(text):
    result.configure(text=text)

# initialize the game status
def new_game():
    guess_button.config(state='normal') #normal: can be clicked
    global TARGET, RETRIES
    TARGET = random.randint(0, 100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")

# logic part of the game
def play_game():
    global RETRIES

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1
        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "too high"
        else:
            hint = "too low"
        result += "\n\nHINT :" + hint

    else:
        result = f"Correct! You guessed the number in {RETRIES} attempts."
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)

# create a blank window
# window: instance(object) created by tkinter library
window = tk.Tk() 
window.geometry("600x400")
window.config(bg="#000000")
window.resizable(width=False, height=False)
window.title("Number Guessing Game")

# exit button (fg: foreground color)
exit_button = tk.Button(window, text = "Exit Game", font=("Arial, 14"), fg="White", bg="red", command=exit)
exit_button.place(x=300,y=320)

# title (Label: class)
title = tk.Label(window, text = "Number Guessing Game", font=("Arial, 24"))
title.place(x=130, y=50)

# result and hints
result = tk.Label(window, text = "Click on Play to start a new game", font=("Arial", 12),fg = "White", bg="Blue")
result.place(x=165, y=210)

# play button
play_button= tk.Button(window, text="Play Game", font=("Arial, 14"), fg="White", bg="Green", command=new_game)
play_button.place(x=170, y=320)

# guess button
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675", command=play_game)
guess_button.place(x=350, y=147) 

# entry field (StringVar:inastance linked to number_form)
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
number_form.place(x=160, y=150)

window.mainloop()

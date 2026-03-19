import tkinter as tk
from tkinter import messagebox
import random

# window configuration
window = tk.Tk()
window.geometry("400x450")
window.title("Number Guess Game")
window.resizable(False, False)

title = tk.Label(window, text="NUMBER GUESS", font=("Arial", 14))
title.pack(pady=10)

rules = tk.Label(window, text="Between 1-100", font=("Arial", 12))
rules.pack(pady=10)

guessPcs = tk.Label(window, text="Guess Number: 0", font=("Arial", 11))
guessPcs.pack(pady=10)

hint = tk.Label(window, text="", fg="red", font=("Arial", 11))
hint.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

result = tk.Label(window, text="PLAYING...", font=("Arial", 11))
result.pack(pady=10)


# game
def main():
    def new():
        global randomNumber, guesspcsnumber
        randomNumber = random.randint(1, 100)
        print(randomNumber)

        guesspcsnumber = 0
        guessPcs.config(text="Guess Number: 0")
        result.config(text="PLAYING...", fg="black", font=("Arial", 11))
        hint.config(text="")

    def show():
        print(randomNumber)

    def guess():
        def go():
            global guesspcsnumber
            try:
                guessNumber = int(entry.get())
            except ValueError:
                hint.config(text="Please Enter A Valid Number")
                return

            guesspcsnumber += 1
            guessPcs.config(text="Guess Number: " + str(guesspcsnumber))

            if guessNumber == randomNumber:
                result.config(text="CORRECT GUESS!", fg="green", font=("Arial", 13))
                hint.config(text="")

                messagebox.showinfo("Correct", ("Guess Number: " + str(guesspcsnumber)))

            elif guessNumber < randomNumber:
                hint.config(text="Guess A Larger Number")

            else:
                hint.config(text="Guess A Smaller Number")


        btn = tk.Button(window, text="Guess", command=go)
        btn.pack(pady=10)

        newbtn = tk.Button(window, text="New Game", command=new)
        newbtn.pack(pady=10)

        showbtn = tk.Button(window, text="SHOW ANSWER", fg="red", command=show)
        showbtn.pack(pady=10)

    new()
    guess()

main()
window.mainloop()

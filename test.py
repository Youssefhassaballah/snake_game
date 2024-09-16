from tkinter import *
import runpy


def play():
    cm = mood.get()
    print(cm)

window = Tk()
window.title("snake game")
window.config(pady=50, padx=50)

mood = StringVar(window)
mood.set("classic game")

w = OptionMenu(window, mood, "classic game", "wall game")
w.grid(row=1, column=1)

play_b = Button(text="play", width=15, command=play)
play_b.grid(row=1, column=2)

mainloop()
print(mood.get())

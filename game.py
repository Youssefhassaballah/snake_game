from tkinter import *
import runpy



def play():
    cm = mood.get()
    if cm == "classic game":
        runpy.run_path("mood1.py")
    elif cm == "wall game":
        runpy.run_path("mood2.py")


window = Tk()
window.title("snake game")
window.config(pady=50, padx=50)

image_file = PhotoImage(file="snake_photo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)


mood = StringVar(window)
mood.set("classic game")

w = OptionMenu(window, mood, "classic game", "wall game")
w.grid(row=1, column=1)

choose_mode = Label(text="choose mode:")
choose_mode.grid(row=1, column=0)

play_b = Button(text="play", width=15, command=play)
play_b.grid(row=1, column=2)

window.mainloop()

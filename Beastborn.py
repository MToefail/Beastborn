import tkinter as tk #source: https://www.youtube.com/watch?v=ibf5cx221hk
from scenes import scenes
from PIL import Image, ImageTk


def start_game():
    titlescreen.pack_forget() #source: https://stackoverflow.com/questions/25101618/forget-versus-grid-forget-python?utm_source
    start.pack_forget()
    scenes.intro_game(root)


root = tk.Tk()
root.geometry("1200x800")
root.title("Beastborn")

titlescreen = tk.Label(
    root, 
    text="Beastborn", 
    font=('impact', 50))
    
titlescreen.pack(padx=20, pady=20)

start = tk.Button(root, text="Start New Game", font=('impact', 25), command=start_game)
start.pack(padx=200, pady=200)

root.mainloop()
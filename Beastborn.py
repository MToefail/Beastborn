import tkinter as tk
from PIL import Image, ImageTk
from scenes.scenes import title_screen

window = tk.Tk()
window.title("Beastborn")

window.attributes("-fullscreen", True)

window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

#BACKGROUND
background_label = tk.Label(window)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
current_bg = None


# CONTENT
content_frame = tk.Frame(window, bg="#000000")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

#STORY TEXT
story_text = tk.StringVar()
text_label = tk.Label(
    content_frame,
    textvariable=story_text,
    wraplength=1000,
    bg="#000000",
    fg="white",
    font=("Arial", 18),
    justify="center"
)
text_label.pack(pady=(0, 40))

#BUTTON
button_frame = tk.Frame(content_frame, bg="#000000")
button_frame.pack()



#ENGINE
def set_story(text):
    story_text.set(text)

    if text.startswith("BEASTBORN"):
        text_label.config(font=("Arial Black", 48))
    else:
        text_label.config(font=("Arial", 18))



def set_background(image_path):
    global current_bg
    try:
        window.update_idletasks()
        w = window.winfo_width()
        h = window.winfo_height()

        img = Image.open(image_path)
        img = img.resize((w, h), Image.Resampling.LANCZOS)
        current_bg = ImageTk.PhotoImage(img)
        background_label.config(image=current_bg)
    except Exception as e:
        print(f"Could not load background: {image_path}", e)



def clear_buttons():
    for widget in button_frame.winfo_children():
        widget.destroy()


def make_choice_buttons(choices):
    clear_buttons()
    for item in choices:
        if len(item) == 3:
            text, command, sfx_file = item
        else:
            text, command = item
            sfx_file = "assets/sfx/click.wav"  # default sound

        def wrapped_command(cmd=command, sfx=sfx_file):
            play_sfx(sfx)
            cmd()

        btn = tk.Button(
            button_frame,
            text=text,
            command=wrapped_command,
            bg="#222",
            fg="white",
            font=("Arial", 16),
            width=35
        )
        btn.pack(pady=10)

#MUSIC
import pygame
pygame.mixer.init()

def play_music(file, loop=True):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1 if loop else 0)
    except Exception as e:
        print(f"Could not play music: {file}", e)

def stop_music():
    pygame.mixer.music.stop()

#SFX
def play_sfx(file):
    try:
        sound = pygame.mixer.Sound(file)
        sound.play()
    except Exception as e:
        print(f"Could not play SFX: {file}", e)


#ENGINE OBJECT
class Engine:
    set_story = staticmethod(set_story)
    set_background = staticmethod(set_background)
    make_choice_buttons = staticmethod(make_choice_buttons)
    clear_buttons = staticmethod(clear_buttons)
    play_music = staticmethod(play_music)
    stop_music = staticmethod(stop_music)



#START
title_screen(Engine)
window.mainloop()




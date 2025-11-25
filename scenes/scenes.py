import tkinter as tk

# intro
def intro_game(root):
    for widget in root.winfo_children():
        widget.destroy()

    intro = tk.Label(
        root,
        text="""You awaken in a collapsed subway tunnel.
Dust fills the air. You hear distant screeches.
Where will you go?""",
        font=('impact', 25)
    )
    intro.pack(pady=20)

#intro choice

    choice_int1 = tk.Button(
        root,
        text="Climb the broken ladder to the streets",
        font=('impact', 25),
        command=lambda: streets(root)
    )
    choice_int1.pack(pady=10)

    choice_int2 = tk.Button(
        root,
        text="Crawl into the maintenance tunnel",
        font=('impact', 25),
        command=lambda: tunnel(root)
    )
    choice_int2.pack(pady=10)

    choice_int3 = tk.Button(
        root,
        text="Break into the hospital sector",
        font=('impact', 25),
        command=lambda: hospital(root)
    )
    choice_int3.pack(pady=10)


# street
def streets(root):
    for widget in root.winfo_children():
        widget.destroy()

    streets_label = tk.Label(
        root,
        text="""The streets are burning.
Creatures move between abandoned cars.
What do you do?""",
        font=('impact', 25)
    )
    streets_label.pack(pady=20)

    choice_str1 = tk.Button(
        root,
        text="Run toward the police barricade",
        font=('impact', 25),
        command=lambda:police(root)
    )
    choice_str1.pack(pady=10)

    choice_str2 = tk.Button(
        root,
        text="Hide inside a destroyed bus",
        font=('impact', 25)
    )
    choice_str2.pack(pady=10)

    choice_str3 = tk.Button(
        root,
        text="Search abandoned apartments",
        font=('impact', 25)
    )
    choice_str3.pack(pady=10)

# tunnel
def tunnel(root):
    for widget in root.winfo_children():
        widget.destroy()

    tunnel_label = tk.Label(
        root,
        text="""You crawl into the maintenance tunnels
        Something crawls in the dark
        Your move?""",
        font=('impact', 25)
    )
    tunnel_label.pack(pady=20)

    choice_tun1 = tk.Button(
        root,
        text="Sneak past quietly",
        font=('impact', 25)
    )
    choice_tun1.pack(pady=10)

    choice_tun2 = tk.Button(
        root,
        text="Throw a rock",
        font=('impact', 25)
    )
    choice_tun2.pack(pady=10)

    choice_tun3 = tk.Button(
        root,
        text="Charge forward",
        font=('impact', 25)
    )
    choice_tun3.pack(pady=10)

# hospital
def hospital(root):
    for widget in root.winfo_children():
        widget.destroy()

    hospital_label = tk.Label(
        root,
        text="""You break into the ruined hospital
        A sealed sample glows bright green
        What do you do?""",
        font=('impact', 25)
    )
    hospital_label.pack(pady=20)

# hospital choices

    choice_hos1 = tk.Button(
        root,
        text="Search the labs",
        font=('impact', 25)
    )
    choice_hos1.pack(pady=10)

    choice_hos2 = tk.Button(
        root,
        text="Look for survivors",
        font=('impact', 25)
    )
    choice_hos2.pack(pady=10)

    choice_hos3 = tk.Button(
        root,
        text="Open the glowing sample",
        font=('impact', 25)
    )
    choice_hos3.pack(pady=10)


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import SeeamDictLib

# Assuming name is fetched from a file
name = "User"

# Setting up app assets directory
assets_path = "GameDetails/"
logo_path = os.path.join(assets_path, "SeeamLogo.png")

# Define primary color scheme
BG_COLOR = "#2c3e50"
BTN_COLOR = "#3498db"
TEXT_COLOR = "#ecf0f1"
TITLE_FONT = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Helvetica", 14)
LABEL_FONT = ("Helvetica", 12)

def run_script(script_name):
    """Simulate script execution (in a real scenario this would call a subprocess)."""
    print(f'Running script: {script_name}')

def fetch_requirements():
    """Simulate fetching requirements."""
    print("Fetching requirements.txt...")







class GetG(object):
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.age = ""
        self.whip = {}

    def writing(self):
        self.whip[p.name] = p.age, p.address, p.phone
        target = open('deed.txt', 'a')
        target.write(str(self.whip))
        print self.whip

    def reading(self):
        s = open('deed.txt', 'r').read()
        self.whip = eval(s)
        name = raw_input("> ")
        if name in self.whip:
            print self.whip[name]

p = GetG()


























def display_game_details(game_name):
    """Update main content area to display selected game details."""
    # Clear current content
    for widget in main_content.winfo_children():
        widget.destroy()

    game_info = game_data.get(game_name, {})
    if not game_info:
        return

    # Thumbnail Image
    thumbnail_path = game_info["thumbnail"]
    if os.path.exists(thumbnail_path):
        thumbnail_img = Image.open(thumbnail_path).resize((200, 100))
        thumbnail_photo = ImageTk.PhotoImage(thumbnail_img)
        thumbnail_label = tk.Label(main_content, image=thumbnail_photo, bg=BG_COLOR)
        thumbnail_label.image = thumbnail_photo  # Keep reference
        thumbnail_label.pack(pady=(10, 10))

    # Game Description
    description_label = tk.Label(
        main_content,
        text=game_info["description"],
        font=LABEL_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        wraplength=500,
        justify="left"
    )
    description_label.pack(pady=10)

    # Play Button
    play_button = tk.Button(
        main_content,
        text="Play",
        command=lambda: run_script(game_info["script_path"]),
        font=BUTTON_FONT,
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        bd=0,
        width=15
    )
    play_button.pack(pady=20)

def create_buttons_with_sidebar_and_details():
    # Main window setup
    window = tk.Tk()
    window.title("Epic App Launcher")
    window.geometry("1280x720")
    window.configure(bg=BG_COLOR)

    # Sidebar frame for game list
    sidebar = tk.Frame(window, width=300, bg="#1e272e")
    sidebar.pack(side="left", fill="y")

    # Add buttons to the sidebar for each game
    sidebar_label = tk.Label(
        sidebar,
        text="Available Games",
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg="#1e272e"
    )
    sidebar_label.pack(pady=20)

    for game_name in game_data.keys():
        button = tk.Button(
            sidebar,
            text=game_name,
            command=lambda name=game_name: display_game_details(name),
            font=BUTTON_FONT,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            relief="flat",
            bd=0,
            width=20
        )
        button.pack(pady=10)

    # Main content area
    global main_content
    main_content = tk.Frame(window, bg=BG_COLOR)
    main_content.pack(side="left", fill="both", expand=True)

    # Welcome content in main content area
    welcome_label = tk.Label(
        main_content,
        text=f'Welcome, {name}! Select a game to see details.',
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    welcome_label.pack(pady=20)

    window.mainloop()

# Uncomment to run the app
create_buttons_with_sidebar_and_details()

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import SeeamDictLib as sdl

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

# Adjust directory paths
games_dir = "allthegames"

def display_game_details_from_dir(game_name):
    """Update main content area to display selected game details based on directory structure."""
    # Clear current content
    for widget in main_content.winfo_children():
        widget.destroy()

    # Define paths for game assets
    game_dir = os.path.join(games_dir, game_name)
    thumbnail_path = os.path.join(game_dir, "thumbnail.png")
    description_path = os.path.join(game_dir, "description.txt")
    script_path = os.path.join(game_dir, "main.py")

    # Thumbnail Image
    if os.path.exists(thumbnail_path):
        thumbnail_img = Image.open(thumbnail_path).resize((200, 100))
        thumbnail_photo = ImageTk.PhotoImage(thumbnail_img)
        thumbnail_label = tk.Label(main_content, image=thumbnail_photo, bg=BG_COLOR)
        thumbnail_label.image = thumbnail_photo  # Keep reference
        thumbnail_label.pack(pady=(10, 10))

    # Game Description
    if os.path.exists(description_path):
        with open(description_path, "r") as desc_file:
            description = desc_file.read()
    else:
        description = "No description available."

    description_label = tk.Label(
        main_content,
        text=description,
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
        command=lambda: run_script(script_path),
        font=BUTTON_FONT,
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        bd=0,
        width=15
    )
    play_button.pack(pady=20)

def create_buttons_with_dynamic_sidebar():
    # Main window setup
    window = tk.Tk()
    window.title("Epic App Launcher")
    window.geometry("1280x720")
    window.configure(bg=BG_COLOR)

    # Sidebar frame for game list
    sidebar = tk.Frame(window, width=300, bg="#1e272e")
    sidebar.pack(side="left", fill="y")

    # Sidebar label
    sidebar_label = tk.Label(
        sidebar,
        text="Available Games",
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg="#1e272e"
    )
    sidebar_label.pack(pady=20)

    # Dynamically add buttons for each game in the directory
    if os.path.exists(games_dir):
        for game_folder in os.listdir(games_dir):
            game_path = os.path.join(games_dir, game_folder)
            if os.path.isdir(game_path):
                button = tk.Button(
                    sidebar,
                    text=game_folder,
                    command=lambda name=game_folder: display_game_details_from_dir(name),
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

    # Initial content in main content area
    welcome_label = tk.Label(
        main_content,
        text=f'Welcome, {name}! Select a game to see details.',
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    welcome_label.pack(pady=20)

    window.mainloop()

create_buttons_with_dynamic_sidebar()

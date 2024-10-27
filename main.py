import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import SeeamDictLib
import os

# Assuming name is fetched from a file
name = "User"

# Setting up app assets directory
assets_path = "assets"
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

def create_buttons():
    # Main window setup
    window = tk.Tk()
    window.title("Epic App Launcher")
    window.geometry("1280x720")
    window.configure(bg=BG_COLOR)
    window.attributes('-fullscreen', False)  # Disable fullscreen for design stage

    # Top frame for logo and title
    top_frame = tk.Frame(window, bg=BG_COLOR)
    top_frame.pack(pady=20)

    # Load and display the logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo = logo.resize((150, 75))
        logo_image = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(top_frame, image=logo_image, bg=BG_COLOR)
        logo_label.image = logo_image  # Keep reference
        logo_label.pack(pady=(0, 10))

    # Title label
    title_label = tk.Label(
        top_frame,
        text=f'What will we be playing today, {name}?',
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    title_label.pack()

    # Frame for the buttons
    button_frame = tk.Frame(window, bg=BG_COLOR)
    button_frame.pack(pady=30)

    # Fetch button
    fetch_button = tk.Button(
        window, text="Fetch requirements.txt",
        command=fetch_requirements,
        bg=BTN_COLOR, fg=TEXT_COLOR,
        font=BUTTON_FONT, width=25,
        relief="flat", bd=0
    )
    fetch_button.pack(pady=10)

    # Grid configuration for game buttons
    row, col = 0, 0
    for i in range(5):  # Simulating 5 script buttons
        button = tk.Button(
            button_frame,
            text=f"Game {i + 1}",
            command=lambda game=f"Game {i + 1}": run_script(game),
            font=BUTTON_FONT,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            relief="flat",
            bd=0,
            width=20
        )
        button.grid(row=row, column=col, padx=10, pady=10)
        col += 1
        if col > 2:  # Limit to 3 buttons per row
            col = 0
            row += 1

    window.mainloop()

# Uncomment to run the app
create_buttons()

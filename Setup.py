# Importing necessary libraries
import os
import requests
import tkinter as tk
from tkinter import simpledialog

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)


'''
def fetch_requirements():
    url = "https://codeberg.org/psyclown/SEEAM/raw/branch/main/requirements.txt"  # Replace with your URL
    response = requests.get(url)
    with open('requirements.txt', 'wb') as file:
        file.write(response.content)
    os.system("pip install -r requirements.txt")
fetch_requirements()
'''

os.system("pip install -r InstallReqs.txt")

import winshell
import urllib
# Function to save name to a file
def save_name():
    name = simpledialog.askstring("Input", "What is your name?")
    if name:
        with open("assets/userdata.txt", "w") as file:
            file.write(name)


def Install(url,path):
    url = "https://codeberg.org/psyclown/SEEAM/raw/branch/main/main.py"  # Replace with your URL
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)


# Setting up the GUI
root = tk.Tk()
root.withdraw()  # Hide the main window
save_name()

Install('https://codeberg.org/psyclown/SEEAM/raw/branch/main/main.py','main.py')
urllib.request.urlretrieve("https://codeberg.org/psyclown/SEEAM/raw/branch/main/assets/SeeamLogo.png", "assets/SeeamLogo.png")
urllib.request.urlretrieve("https://codeberg.org/psyclown/SEEAM/raw/branch/main/assets/logo.ico", "assets/shortcut.ico")


import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()
path = os.path.join(desktop, "SEEAM.lnk")
target = (dname + 'main.py')
wDir = (dname)
icon = (dname + "assets/logo.ico")
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

os.system('python main.py')
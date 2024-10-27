# Import tkinter and webview libraries 
from tkinter import *
import webview
import webview.window 
  
# define an instance of tkinter 
tk = Tk() 
  
#  size of the window where we show our website 
tk.geometry("1920x1080")
tk.attributes('-fullscreen',True) 
  
# Open website 
webview.create_window('Minecraft', 'https://psyclownyt02.github.io/mc-1.5.2/', fullscreen=True) 
webview.start() 
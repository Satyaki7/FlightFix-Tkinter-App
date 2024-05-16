import customtkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from my_package123 import main_loop



a = tk
b = ttk


from my_package123 import *

window = tk.CTk()
window.title("Testing")

logimg = Image.open('my_package123/backoppp.png')
image = ImageTk.PhotoImage(logimg.resize((900, 600)))
label = b.Label(window, image=image)
label.pack()

def return_handling(h):
   print(h)
   if h == "signin":
      signin.signop(a,b,window)

login.loginop(a,b,window,return_handling)
window.mainloop()
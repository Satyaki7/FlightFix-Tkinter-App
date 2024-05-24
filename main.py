import customtkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from my_package123 import authenticating
from my_package123.authenticating import authenticate
import CTkTable as op

a = tk
b = ttk
z = op

from my_package123 import *

# new_window = tk.CTk()
# new_window.geometry("900x600")
# new_window.title("New Window")
# dashboard.dashboardop(a,b,new_window,z)
# new_window.mainloop()

window = tk.CTk()
window.title("Testing")


logimg = Image.open('assets/backoppp.png')
image = ImageTk.PhotoImage(logimg.resize((900, 600)))
label = b.Label(window, image=image)
label.pack()


def return_handling(h):
   print(h)
   if h == "signin":
      signin.signop(a,b,window,return_handling)
   if h == "dashboard":
      window.destroy()
      # Create a new window
      new_window = tk.CTk()
      new_window.geometry("900x600")
      new_window.title("New Window")
      dashboard.dashboardop(a,b,new_window,return_handling,z)
      new_window.mainloop()


authenticating.initialop()
login.loginop(a,b,window,return_handling)
window.mainloop()
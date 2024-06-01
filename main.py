import customtkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import Image, ImageTk

import CTkTable as op

a = tk
b = ttk
z = op
win = 0
from my_package123 import *

new_window = tk.CTk()
new_window.geometry("900x600")
new_window.title("New Window")
new_window.configure(fg_color="white")

def destroy_all_widgets():
    for widget in new_window.winfo_children():
        widget.destroy()

def returnop(h):
   if h == "Flight":
      destroy_all_widgets()
      booking.book(a,b,new_window,returnop,z)
   if h == "Cust":
      destroy_all_widgets()
      cust.customer(a,b,new_window,returnop,z)
   if h == "Dash":
      destroy_all_widgets()
      dashboard.dashboardop(a,b,new_window,returnop,z)
      new_window.mainloop()
dashboard.dashboardop(a,b,new_window,returnop,z)
new_window.mainloop()


# new_window = tk.CTk()
# new_window.geometry("900x600")
# new_window.title("New Window")
# dashboard.dashboardop(a,b,new_window,,z)
# new_window.mainloop()

# window = tk.CTk()
# window.title("Testing")


# logimg = Image.open('assets/backoppp.png')
# image = ImageTk.PhotoImage(logimg.resize((900, 600)))
# label = b.Label(window, image=image)
# label.pack()



# def return_handling(h):
#    print(h)
#    if h == "signin":
#       signin.signop(a,b,window,return_handling)
#    if h == "dashboard":
#       window.destroy()
#       # Create a new window
#       new_window = tk.CTk()
#       new_window.geometry("900x600")

#       new_window.title("New Window")
#       new_window.configure(fg_color="white")

#       def returnop(h):
#          if h == "Flight":
#             booking.book(a,b,new_window,returnop,z)
#          if h == "Cust":
#             cust.customer(a,b,new_window,returnop,z)
#          if h == "Dash":
#             dashboard.dashboardop(a,b,new_window,returnop,z)
#             new_window.mainloop()
#       dashboard.dashboardop(a,b,new_window,returnop,z)
#       new_window.mainloop()


# authenticating.initialop()
# login.loginop(a,b,window,return_handling)
# window.mainloop()
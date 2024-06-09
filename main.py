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

# window = tk.CTk()
# window.geometry("900x600")
# window.title("New Window")
# window.configure(fg_color="white")

# def destroy_all_widgets():
#     for widget in window.winfo_children():
#         widget.grid_forget()

# def returnop(h):
#    if h == "Flight":
#       destroy_all_widgets()
#       booking.book(a,b,window,returnop,z)
#    if h == "Cust":
#       destroy_all_widgets()
#       cust.customer(a,b,window,returnop,z)
#    if h == "Dash":
#       dashboard.dashboardop(a,b,window,returnop,z)
#       window.mainloop()
# dashboard.dashboardop(a,b,window,returnop,z)
# window.mainloop()


# window = tk.CTk()
# window.geometry("900x600")
# window.title("New Window")
# dashboard.dashboardop(a,b,window,returnop,z)
# window.mainloop()

window = tk.CTk()
window.title("Testing")


logimg = Image.open('assets/backoppp.png')
image = ImageTk.PhotoImage(logimg.resize((900, 600)))
label = b.Label(window, image=image)
label.pack()

def destroy_all_widgets():
    for widget in window.winfo_children():
       try:
           window.grid_forget()
       except SomeExceptionType as e:
           # Code that runs if an exception occurs in the try block
           window.pack_forget()
         

def return_handling(h):
   print(h)
   if h == "signin":
      signin.signop(a,b,window,return_handling)
      
   if h == "dashboard":
      destroy_all_widgets()
      # Create a new window
      # window = window
      # window.geometry("900x600")

      # window.title("New Window")
      # window.configure(fg_color="white")
      def returnop(h):
         if h == "Flight":
            n = destroy_all_widgets()
            booking.book(a,b,n,returnop,z)
         if h == "Cust":
            n = destroy_all_widgets()
            cust.customer(a,b,n,returnop,z)
         if h == "Dash":
            dashboard.dashboardop(a,b,window,returnop,z)
            
      dashboard.dashboardop(a,b,window,returnop,z)
      window.mainloop()


authenticating.initialop()
login.loginop(a,b,window,return_handling)
window.mainloop()
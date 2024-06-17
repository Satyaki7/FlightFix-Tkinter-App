import customtkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import Image, ImageTk

a = tk
b = ttk

from my_package123 import *

# window = tk.CTk()
# window.geometry("900x600")
m = "Monkey D Luffy"

def username_entry(u):
   global m
   m = u
   print(m)
def destroy_all_widgets():
    for widget in window.winfo_children():
        widget.destroy()

# def returnop(h):
#    if h == "Flight":
#       destroy_all_widgets()
#       booking.book(a,b,window,returnop)
#    if h == "Cust":
#       destroy_all_widgets()
#       cust.customer(a,b,window,returnop)
#    if h == "Dash":
#       destroy_all_widgets()
#       dashboard.dashboardop(a,b,window,returnop,m)
# dashboard.dashboardop(a,b,window,returnop,m)
# window.mainloop()


window = tk.CTk()
window.title("Testing")

def destroy_all_widgets():
    for widget in window.winfo_children():
      widget.destroy()
         

def return_handling(h):
   print(h)
   if h == "signin":
      signin.signop(a,b,window,return_handling)
      
   if h == "dashboard":
      
      def returnop(h):
         if h == "Flight":
            destroy_all_widgets()
            booking.book(a,b,window,returnop)
         if h == "Cust":
            destroy_all_widgets()
            cust.customer(a,b,window,returnop)
         if h == "Dash":
            destroy_all_widgets()
            dashboard.dashboardop(a,b,window,returnop,m)
      destroy_all_widgets()
      dashboard.dashboardop(a,b,window,returnop,m)
      window.mainloop()


authenticating.initialop()
login.loginop(a,b,window,return_handling,username_entry)
window.mainloop()
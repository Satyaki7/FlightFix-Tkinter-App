import customtkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

def on_entry_click(event):
   if username.get() == "Username":
      username.delete(0, tk.END)
      username.configure(foreground="black")

def on_focus_out(event):
   if username.get() == "":
    username.insert(0, "Username")
    username.configure(foreground="gray")

def on_entry_click1(event):
   if password.get() == "Password":
      password.delete(0, tk.END)
      password.configure(foreground="black")

def on_focus_out1(event):
   if password.get() == "":
      password.insert(0, "Password")
      password.configure(foreground="gray")

#window 
window = tk.CTk()
window.title("Testing")
window.geometry('900x600')

logimg = Image.open('backoppp.png')
image = ImageTk.PhotoImage(logimg.resize((900,600)))
label = ttk.Label(window, image=image)
label.pack()

# Main frame
frame_width = 300
frame_height = 300
frame = tk.CTkFrame(window, width=frame_width, height=frame_height,fg_color = "#F6F7F2",corner_radius=10,border_width=2,border_color="black")

frame.place(relx=0.622, rely=0.5, anchor="center")
frame.pack_propagate (False)

# Entry boxes
sign = tk.CTkLabel(frame, text="Sign In", font=("Arial", 24))
sign.place(relx=0.5, rely=0.3, anchor="center")
username = ttk.Entry(frame)
password = ttk.Entry(frame)
username.insert(0,"Username")
username.bind("<FocusIn>", on_entry_click)
username.bind("<FocusOut>", on_focus_out)
username.place(relx=0.5, rely=0.5, anchor="center")
password.insert(0,"Password")
password.bind("<FocusIn>", on_entry_click1)
password.bind("<FocusOut>", on_focus_out1)
password.place(relx=0.5, rely=0.65, anchor="center")

#buttons
wid = 20
hei = 10
signin_button = ttk.Button(frame, text="SignIn",bootstyle="primary")
signup_button = ttk.Button(frame, text="SignUp",bootstyle="primary-outline")
signin_button.place(relx=0.4, rely=0.8)
signup_button.place(relx=0.6, rely=0.8)

window.mainloop()

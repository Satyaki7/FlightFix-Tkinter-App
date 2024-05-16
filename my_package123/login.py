from tkinter.constants import COMMAND
from PIL import Image, ImageTk
from .signin import signop
from my_package123 import signin

def loginop(a,b,window,return_callback):
   def breakop():
      return_callback("signin")   
   
   def on_entry_click(event):
      if username.get() == "Username":
         username.delete(0, a.END)
         username.configure(foreground="black")

   def on_focus_out(event):
      if username.get() == "":
         username.insert(0, "Username")
         username.configure(foreground="gray")

   def on_entry_click1(event):
      if password.get() == "Password":
         password.delete(0, a.END)
         password.configure(foreground="black")

   def on_focus_out1(event):
      if password.get() == "":
         password.insert(0, "Password")
         password.configure(foreground="gray")

   #window
   window.geometry('900x600')

   # Main frame
   frame_width = 300
   frame_height = 300
   frame = a.CTkFrame(window,width=frame_width,height=frame_height,fg_color="#F6F7F2",corner_radius=10,border_width=2,border_color="black")

   frame.place(relx=0.622, rely=0.5, anchor="center")
   frame.pack_propagate(False)

   # Entry boxes
   sign = a.CTkLabel(frame, text="Log In", font=("Arial", 24))
   sign.place(relx=0.5, rely=0.3, anchor="center")
   username = b.Entry(frame)
   password = b.Entry(frame)
   username.insert(0, "Username")
   username.bind("<FocusIn>", on_entry_click)
   username.bind("<FocusOut>", on_focus_out)
   username.place(relx=0.5, rely=0.5, anchor="center")
   password.insert(0, "Password")
   password.bind("<FocusIn>", on_entry_click1)
   password.bind("<FocusOut>", on_focus_out1)
   password.place(relx=0.5, rely=0.65, anchor="center")

   #buttons
   wid = 20
   hei = 10
   signin_button = b.Button(frame, text="SignIn", bootstyle="primary")
   signup_button = b.Button(frame,text="SignUp",bootstyle="primary-outline",command =  breakop)
   signin_button.place(relx=0.4, rely=0.8)
   signup_button.place(relx=0.6, rely=0.8)



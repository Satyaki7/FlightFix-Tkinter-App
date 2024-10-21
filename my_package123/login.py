from tkinter.constants import COMMAND
from typing import Text
from PIL import Image, ImageTk
from .authenticating import on_login
from .authenticating import on_signup


def loginop(a,b,window,return_callback,u):

   def transfer():
      f= on_login(username.get(),password.get())
      if f == True:
         v = username.get()
         u(v)
         return_callback("dashboard")
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
   window.geometry('960x600')
   window.title("Login")
   window.grid_columnconfigure(0, weight=0)
   window.grid_columnconfigure(1, weight=0)
   window.grid_columnconfigure(2, weight=1)
   window.grid_rowconfigure(0, weight=0)
   window.configure(fg_color='#f5f5f5')
   
   # Create a red frame on the left
   pic_frame = a.CTkFrame(window, width=375, height=600,fg_color="transparent",corner_radius=20)
   pic_frame.grid(row=0, column=0, padx=0, pady=0,sticky = "nsew")
   pic_frame.grid_columnconfigure(0, weight=0)
   pic_frame.grid_rowconfigure(0, weight=0)
   
   logimg = Image.open('assets/Fix.png')
   picop = a.CTkImage(logimg,size=(375, 600))
   lable_pic = a.CTkLabel(pic_frame, image=picop,text = "")
   lable_pic.grid(row=0, column=0,sticky= "nsew")
   
   # Create a red frame on the right
   main_frame = a.CTkFrame(window, width=400, height=600,fg_color="transparent",corner_radius = 20)
   main_frame.grid(row=0, column=2, padx=0, pady=0,sticky = "nsew")
   main_frame.grid_columnconfigure(0, weight=0)
   main_frame.grid_columnconfigure(1, weight=1)
   main_frame.grid_columnconfigure(2, weight=0)
   main_frame.grid_rowconfigure(0, weight=0)
   main_frame.grid_rowconfigure(1, weight=1)
   main_frame.grid_rowconfigure(2, weight=0)

   logimg1 = Image.open('assets/contour.jpeg')
   logimg2 = a.CTkImage(logimg1, size=(600,600))  # Resize to match frame size

   # Create a label with the image and place it in the frame
   label_pic1 = a.CTkLabel(main_frame, image=logimg2, text="")
   label_pic1.place(relx=0, rely=0, relwidth=1, relheight=1)
   
   # Create a yellow frame inside the red frame on the right
   input_vox = a.CTkFrame(main_frame, width=375, height=375, corner_radius=20, fg_color="whitesmoke")
   input_vox.grid(column=1,row=1, padx=16, pady=16)
   input_vox.grid_propagate(False)
   input_vox.grid_columnconfigure(0, weight=0)
   input_vox.grid_columnconfigure(1, weight=1)
   input_vox.grid_columnconfigure(2, weight=0)
   input_vox.grid_rowconfigure((1,3), weight=0)
   input_vox.grid_rowconfigure((0,2,4,5,6), weight=1)

   # Entry boxes
   loginbox = a.CTkFrame(input_vox, width=300, height=50, fg_color="transparent")
   loginbox.grid(row=0, column=1, padx=10, pady=10)
   loginbox.grid_columnconfigure(0, weight=0)
   loginbox.grid_rowconfigure((0,1), weight=1)
   log = a.CTkLabel(loginbox, text="Welcome Back!", font=("Arial", 32),fg_color= "transparent",text_color = "black")
   log.grid(column=1, row=0, padx=50, pady=6,sticky = "nsew")
   logmsg = a.CTkLabel(loginbox, text="Ready to continue your journey? \n  Log in now to book your next adventure!", font=("Arial", 10),fg_color= "transparent",text_color = "black")
   logmsg.grid(column=1, row=1, padx=50, pady=0,sticky = "nsew")
   log1 = a.CTkLabel(input_vox, text="Username:", font=("Arial", 12),fg_color= "transparent",text_color="black")
   log1.grid(column=1, row=1, padx=50, pady=5,sticky = "w")
   log2 = a.CTkLabel(input_vox, text="Password:", font=("Arial", 12),fg_color= "transparent",text_color="black")
   log2.grid(column=1, row=3, padx=50, pady=5,sticky = "w")

   username = b.Entry(input_vox)
   password = b.Entry(input_vox)

   username.insert(0, "Username")
   username.bind("<FocusIn>", on_entry_click)
   username.bind("<FocusOut>", on_focus_out)
   username.grid(column=1, row=2, padx=50, pady=0,sticky = "nsew")

   password.insert(0, "Password")
   password.bind("<FocusIn>", on_entry_click1)
   password.bind("<FocusOut>", on_focus_out1)
   password.grid(column=1, row=4, padx=50, pady=5,sticky = "nsew")

   vottonframe = a.CTkFrame(input_vox, width=300, height=30,fg_color= "transparent")
   vottonframe.grid(column=1, row=6, padx=20, pady=5)
   vottonframe.grid_columnconfigure((0,1), weight=1)
   vottonframe.grid_rowconfigure((0), weight=1)

   signlable = a.CTkLabel(vottonframe, text="Don't have an account?", font=("Arial", 12),fg_color = "transparent",text_color="black",width = 100,height = 20)
   signlable.grid(column=0, row=0, padx=0, pady=0)
   
   signup_button = a.CTkButton(vottonframe,text="SignUp",width = 5,height = 20,fg_color= "whitesmoke",hover_color= "whitesmoke",text_color = "blue",command = breakop)
   signup_button.grid(column=1,row=0,padx=0, pady=0)
   
   signin_button = a.CTkButton(input_vox,text="Log In",width = 250,height = 35,fg_color = "#02b875",hover_color = "#03eb95",corner_radius = 10,font=("Arial", 18),text_color = "white",command = transfer)

   signin_button.grid(column=1,row=5,padx=5, pady=8)
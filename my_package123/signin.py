from PIL import Image, ImageTk

def signop(a,b,window1):
   print("hwllo work")

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
   
   def on_entry_click2(event):
      if password1.get() == "Re-enter Password":
         password1.delete(0, a.END)
         password1.configure(foreground="black")

   def on_focus_out2(event):
      if password1.get() == "":
         password1.insert(0, "Re-enter Password")
         password1.configure(foreground="gray")

   
   # Main frame
   frame_width = 300
   frame_height = 300
   frame = a.CTkFrame(window1,width=frame_width,height=frame_height,fg_color="#F6F7F2",corner_radius=10,border_width=2,border_color="black")

   frame.place(relx=0.622, rely=0.5, anchor="center")
   frame.pack_propagate(False)

   # Entry boxes
   sign = a.CTkLabel(frame, text="Sign Up", font=("Arial", 24))
   sign.place(relx=0.5, rely=0.3, anchor="center")
   
   username = b.Entry(frame)
   password = b.Entry(frame)
   password1 = b.Entry(frame)

   username.insert(0, "Username")
   username.bind("<FocusIn>", on_entry_click)
   username.bind("<FocusOut>", on_focus_out)
   username.place(relx=0.5, rely=0.5, anchor="center")
   
   password.insert(0, "Password")
   password.bind("<FocusIn>", on_entry_click1)
   password.bind("<FocusOut>", on_focus_out1)
   password.place(relx=0.5, rely=0.62, anchor="center")

   password1.insert(0, "Re-enter Password")
   password1.bind("<FocusIn>", on_entry_click2)
   password1.bind("<FocusOut>", on_focus_out2)
   password1.place(relx=0.5, rely=0.74, anchor="center")



   #buttons
   wid = 20
   hei = 10
   signup_button = b.Button(frame,text="SignUp",bootstyle="primary")
   signup_button.place(relx=0.6, rely=0.85)



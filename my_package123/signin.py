from PIL import Image, ImageTk

from my_package123.authenticating import on_signup

def signop(a,b,window,return_callback,):
   print("hwllo work")

   def transfer():
      f = on_signup(username.get(),password.get(),password1.get())
      if f == True:
         return_callback("dashboard")
   
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

   
   #window
   window.geometry('900x600')
   window.title("SignUp")
   window.grid_columnconfigure(0, weight=0)
   window.grid_columnconfigure(1, weight=0)
   window.grid_columnconfigure(2, weight=1)
   window.grid_rowconfigure(0, weight=0)
   window.configure(fg_color='#fbf2e1')

   # Create a red frame on the left
   pic_frame = a.CTkFrame(window, width=300, height=600,fg_color="transparent")
   pic_frame.grid(row=0, column=0, padx=0, pady=0,sticky = "nsew")
   pic_frame.grid_columnconfigure(0, weight=0)
   pic_frame.grid_rowconfigure(0, weight=0)

   logimg = Image.open('assets/Fix.png')
   picop = ImageTk.PhotoImage(logimg.resize((300, 600)))
   lable_pic = a.CTkLabel(pic_frame, image=picop,text = "")
   lable_pic.grid(row=0, column=0,sticky= "nsew")

   
   # Create a red frame on the right
   main_frame = a.CTkFrame(window, width=400, height=600,fg_color="transparent")
   main_frame.grid(row=0, column=2, padx=20, pady=20,sticky = "nsew")
   main_frame.grid_columnconfigure(0, weight=0)
   main_frame.grid_columnconfigure(1, weight=1)
   main_frame.grid_columnconfigure(2, weight=0)
   main_frame.grid_rowconfigure(0, weight=0)
   main_frame.grid_rowconfigure(1, weight=1)
   main_frame.grid_rowconfigure(2, weight=0)



   # Create a yellow frame inside the red frame on the right
   input_vox = a.CTkFrame(main_frame, width=300, height=300, corner_radius=20, fg_color="white")
   input_vox.grid_propagate(False)
   input_vox.grid(column=1,row=1, padx=20, pady=20)
   input_vox.grid_columnconfigure(0, weight=0)
   input_vox.grid_columnconfigure(1, weight=1)
   input_vox.grid_columnconfigure(2, weight=0)
   input_vox.grid_rowconfigure(0, weight=1)
   input_vox.grid_rowconfigure(1, weight=1)
   input_vox.grid_rowconfigure(2, weight=1)
   input_vox.grid_rowconfigure(3, weight=1)
   input_vox.grid_rowconfigure(4, weight=1)


   # Entry boxes
   log = a.CTkLabel(input_vox, text="Sign In", font=("Arial", 24),fg_color = "transparent")
   log.grid(column=1, row=0, padx=20, pady=20,sticky = "nsew")

   username = b.Entry(input_vox)
   password = b.Entry(input_vox)
   password1 = b.Entry(input_vox)

   username.insert(0, "Username")
   username.bind("<FocusIn>", on_entry_click)
   username.bind("<FocusOut>", on_focus_out)
   username.grid(column=1, row=1, padx=20, pady=5,sticky = "nsew")

   password.insert(0, "Password")
   password.bind("<FocusIn>", on_entry_click1)
   password.bind("<FocusOut>", on_focus_out1)
   password.grid(column=1, row=2, padx=20, pady=5,sticky = "nsew")

   password1.insert(0, "Re-enter Password")
   password1.bind("<FocusIn>", on_entry_click2)
   password1.bind("<FocusOut>", on_focus_out2)
   password1.grid(column=1, row=3, padx=20, pady=5,sticky = "nsew")

   vottonframe = a.CTkFrame(input_vox, width=50, height=25,fg_color= "transparent")
   vottonframe.grid(column=1, row=4, padx=20, pady=20)
   vottonframe.grid_columnconfigure(0, weight=1)
   vottonframe.grid_rowconfigure(0, weight=0)

   signup_button = b.Button(vottonframe,text="SignUp",bootstyle="primary",command = transfer)

   signup_button.grid(column=0,row=0,padx=5, pady=0)



import customtkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

#window 
window = tk.CTk()
window.title("Testing")
window.geometry('600x400')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


# Left Frame
left_frame = tk.CTkFrame(window,width=300, height=400)
left_frame.pack(side="left")
left_frame.pack_propagate(False)
#image

logimg = Image.open('loginop.jpg')
image = ImageTk.PhotoImage(logimg.resize((300,400)))
label = ttk.Label(left_frame, image=image)
label.pack()

# Right Frame
right_frame = tk.CTkFrame(window, fg_color="white", width=300, height=400)
right_frame.pack(side="right")

# Centered Frame inside Right Frame
centered_frame = tk.CTkFrame(right_frame, fg_color="white",width = 250,height = 250,border_width = 1,border_color = "black",)
centered_frame.place(relx=0.5, rely=0.5, anchor="center")

# Entry boxes
username = ttk.Entry(centered_frame,text = "hello")
password = ttk.Entry(centered_frame)
username.pack(padx=10,pady=10)
password.pack(padx=10,pady=10)

#buttons 
signin = tk.CTkButton(centered_frame, text="Signin",width = 20,fg_color="transparent",hover_color="blue",text_color="black",border_width=1,border_color="black")
login = tk.CTkButton(centered_frame, text="Login",width = 20,fg_color="transparent",hover_color="blue",text_color="black",border_width=1,border_color="black")
signin.pack(padx=1, pady=10,side= 'right')
login.pack(padx=1,pady=10,side= 'right')


#run
window.mainloop()
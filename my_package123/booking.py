from tkinter.constants import ACTIVE, DISABLED
from typing import Text
from tkinter import messagebox
from ttkbootstrap.constants import PRIMARY

def book(a,b,c,d):
    from PIL import Image, ImageTk

    c.geometry("960x700")
    c.title("Dashboard")
    c.configure(fg_color='#5ca3ff')
    # Configure grid layout for the window
    c.grid_columnconfigure((0,2), weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure((0,2), weight=0)
    c.grid_rowconfigure(1, weight=1)

    bm = a.CTkFrame(c, fg_color="transparent",width = 960,height = 700,corner_radius = 10)
    bm.grid(row=1, column=1, sticky="nsew",padx = 10,pady=10)
    bm.grid_columnconfigure(0, weight=0)
    bm.grid_columnconfigure(1, weight=1)
    bm.grid_rowconfigure(0, weight=1)
    bm.grid_rowconfigure(1, weight=0)
    bm.grid_rowconfigure(2, weight=1)
    bm.grid_propagate(False)

    # Load the background image
    bg_image = Image.open("assets/14337.jpg")
    bg_photo = a.CTkImage(bg_image,size = (960, 700))

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(bm, image=bg_photo,text="")
    bg_label.place(relwidth=1, relheight=1)
    
    def on_button_click(a):
        print("booking is working")
    def search():
        q,w,e,r = drop1.get(),drop2.get(),dropdown3.get(),spinbox.get()
        if q == w : 
            messagebox.showerror("Error", "Departure and Arrival location cannot be same.")
            return
        elif q != "Form" and w != "To" and dropdown3 != "Class" and spinbox != "Passengers" :
            
            bottom_frame = a.CTkFrame(bm, width=600, height=400, corner_radius=20, fg_color="whitesmoke")
            bottom_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
            bottom_frame.grid_columnconfigure(0, weight=1)
            bottom_frame.grid_rowconfigure(0, weight=1)
            bottom_frame.grid_propagate(False)
            # Configure rows and columns for the grid in bottom_frame
            for i in range(6):
                bottom_frame.grid_rowconfigure(i, weight=1)
            for j in range(5):
                bottom_frame.grid_columnconfigure(j, weight=1)

            # Populate the grid with labels and buttons
            for row in range(6):
                for col in range(5):
                    if col == 4:  # Place button in the 5th column
                        if row == 0:
                            continue
                        button = b.Button(bottom_frame, text=f"Button {row}", style="primary.Outline.TButton", command=lambda r=row: on_button_click(r))
                        button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
                    elif row == 0:
                        if col == 0:
                            label = a.CTkLabel(bottom_frame, text="Sl No.")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 1:
                            label = a.CTkLabel(bottom_frame, text="Flight No")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 2:
                            label = a.CTkLabel(bottom_frame, text="Date")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 3:
                            label = label = a.CTkLabel(bottom_frame, text="Time")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
                    else:  # Place labels in other columns
                        label = a.CTkLabel(bottom_frame, text=f"Label {row},{col}")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    
    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm,
                                   width=106,
                                   height=700,
                                   corner_radius=0,
                                   fg_color="#5ca3ff")
        sidebar_frame.grid(row=0, column=0, rowspan=3, padx=0, pady=0, sticky="ns")
        sidebar_frame.grid_rowconfigure((0, 5), weight=1)  # Add empty rows for centering
        sidebar_frame.grid_rowconfigure((1, 2, 3, 4), weight=0)  # Rows for buttons

        def clk2():
            sidebar_frame.grid_forget()

        cross = a.CTkImage(Image.open('assets/close.png'), size=(18,18))
        buttoncross = a.CTkButton(sidebar_frame,text = "",image = cross,width = 18,height=18,fg_color = "transparent",command = clk2)
        buttoncross.grid(row=0,column=0,padx=5,pady=5,sticky = "ne")
        # Home button
        img1 = a.CTkImage(Image.open('assets/home.png'), size=(32, 32))
        button1 = a.CTkButton(sidebar_frame,
                              text="Home",
                              font=("Arial", 16),
                              text_color="black",
                              image=img1,
                              width=36,
                              height=36,
                              corner_radius=18,
                              fg_color="#5ca3ff",
                              hover_color="#A2CCFE",
                               command=lambda: d("Dash"))
        button1.grid(row=1, column=0, padx=2, pady=4)

        # Explore button
        img4 = a.CTkImage(Image.open('assets/map.png'), size=(30, 30))
        button4 = a.CTkButton(sidebar_frame,
                              text="Explore",
                              font=("Arial", 16),
                              text_color="black",
                              width=36,
                              height=36,
                              corner_radius=16,
                              fg_color="#5ca3ff",
                              image=img4,
                              hover_color="#A2CCFE",
                              command=lambda: d("Map"))
        button4.grid(row=2, column=0, padx=2, pady=4)

        # Book button
        img2 = a.CTkImage(Image.open('assets/plane.png'), size=(34, 34))
        button2 = a.CTkButton(sidebar_frame,
                              text="Book",
                              font=("Arial", 16),
                              text_color="black",
                              width=36,
                              height=36,
                              corner_radius=18,
                              fg_color="#A2CCFE",
                              image=img2,
                              hover="DISABLE")
        button2.grid(row=3, column=0, padx=2, pady=4)

        # Cust button
        img3 = a.CTkImage(Image.open('assets/cust.png'), size=(32, 32))
        button3 = a.CTkButton(sidebar_frame,
                              text="",
                              width=36,
                              height=36,
                              corner_radius=18,
                              fg_color="#5ca3ff",
                              image=img3,
                              hover_color="#A2CCFE",
                              command=lambda: d("Cust"))
        button3.grid(row=5, column=0, padx=2, pady=4)

    imgmen = a.CTkImage(Image.open('assets/menu.png'), size=(20,20))
    menu = a.CTkButton(bm,width = 20,height=20,corner_radius=18,fg_color="#5ca3ff",image = imgmen,text="",command = clk)
    menu.grid(row=0,column=0,padx=5,pady=0,sticky = "n")

    # Top Frame
    top_frame = a.CTkFrame(bm, width=750, height=150, corner_radius=20, fg_color="whitesmoke",border_color="black",border_width=1)
    top_frame.grid(row=0, column=1, padx=10, pady=10)
    top_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
    top_frame.grid_rowconfigure((0, 1), weight=1)
    top_frame.grid_propagate(False)
    
    cities = ['Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune']

    # Dropdown Boxes and Other Widgets in Top Frame
    drop1 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop1.grid(row=0, column=0, padx=10, pady=1, sticky="we")
    drop1.set("From")

    drop2 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop2.grid(row=0, column=1, padx=10, pady=1, sticky="we")
    drop2.set("To")

    spinbox = b.Spinbox(top_frame, from_=1, to=100, style='info.TSpinbox')
    spinbox.grid(row=0, column=2, padx=10, pady=1, sticky="ew")
    spinbox.set("Passengers")

    datepicker1 = b.DateEntry(top_frame, style='primary')
    datepicker1.grid(row=1, column=0, padx=10, pady=1, sticky="ew")

    datepicker2 = b.DateEntry(top_frame, bootstyle="danger", firstweekday=0)
    datepicker2.grid(row=1, column=1, padx=10, pady=1, sticky="ew")

    dropdown3 = b.Combobox(top_frame, style='primary.TCombobox', values=["Economic" , "Business", "First Class"])
    dropdown3.grid(row=1, column=2, padx=10, pady=1, sticky="ew")
    dropdown3.set("Class")

    button = b.Button(top_frame, text="Book", bootstyle="primary.outline",command = search)
    button.grid(row=1, column=3, padx=10, pady=1, sticky="ew")


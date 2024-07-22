from tkinter.constants import ACTIVE, DISABLED
from typing import Text
from tkinter import messagebox
from ttkbootstrap.constants import PRIMARY
from my_package123.authenticating import authenticate

def book(a, b, c, d, m,placename):
    import random
    from PIL import Image, ImageTk
    from datetime import datetime
    from .authenticating import searchfli
    from .form import formop

    c.geometry("960x700")
    c.title("Dashboard")
    c.configure(fg_color='#5ca3ff')
    # Configure grid layout for the window
    c.grid_columnconfigure((0, 2), weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure((0, 2), weight=0)
    c.grid_rowconfigure(1, weight=1)
    r = 1

    def flightb(x, r, m):
        formop(a, b, c, d, x, r, m)

    bm = a.CTkFrame(c, fg_color="transparent", width=960, height=700, corner_radius=10)
    bm.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    bm.grid_columnconfigure(0, weight=0)
    bm.grid_columnconfigure(1, weight=1)
    bm.grid_rowconfigure(1, weight=0)
    bm.grid_rowconfigure((0, 2), weight=1)
    bm.grid_propagate(False)

    # Load the background image
    bg_image = Image.open("assets/14337.jpg")
    bg_photo = a.CTkImage(bg_image, size=(960, 700))

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(bm, image=bg_photo, text="")
    bg_label.place(relwidth=1, relheight=1)

    def search():
        global r
        q, w, e, r, t, y = drop1.get(), drop2.get(), dropdown3.get(), spinbox.get(), datetime.strptime(datepicker1.entry.get(), "%d/%m/%Y"), datetime.strptime(datepicker2.entry.get(), "%d/%m/%Y")
        print("The selected date is: ", t)
        if q == "Form" or w == "To":
            messagebox.showerror("Error", "Select Departure and Arrival location properly.")
            return
        # elif q == w : 
        #     messagebox.showerror("Error", "Departure and Arrival location cannot be same.")
        #     return
        # elif dropdown3 == "Class":
        #     messagebox.showerror("Error", "Please select the class of ticket.")
        #     return
        # elif t == y:
        #     messagebox.showerror("Error", "Departure and Return date cannot be same.")
        #     return
        # elif t > y:
        #     messagebox.showerror("Error", "Time travel not allowed !")
        #     return
        elif q != "Form" and w != "To" and dropdown3 != "Class" and spinbox.get() != "Passengers":
            bottom_frame = a.CTkFrame(bm, width=600, height=400, corner_radius=20, fg_color="whitesmoke")
            bottom_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
            bottom_frame.grid_columnconfigure(0, weight=1)
            bottom_frame.grid_rowconfigure(0, weight=1)
            bottom_frame.grid_propagate(False)
            # Configure rows and columns for the grid in bottom_frame
            for i in range(6):
                bottom_frame.grid_rowconfigure(i, weight=1)
            for j in range(6):
                bottom_frame.grid_columnconfigure(j, weight=1)

            # Populate the grid with labels and buttons
            for row in range(6):
                for col in range(6):
                    if col == 5:  # Place button in the 5th column
                        if row == 0:
                            continue
                        button = b.Button(bottom_frame, text="Book Flight", style="primary.Outline.TButton", command=lambda x=row: flightb(x, r, m))
                        button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
                    elif row == 0:
                        if col == 0:
                            label = a.CTkLabel(bottom_frame, text="Sl No.", text_color="black")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 1:
                            label = a.CTkLabel(bottom_frame, text="Flight No", text_color="black")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 2:
                            label = a.CTkLabel(bottom_frame, text="Departure Date", text_color="black")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 3:
                            label = a.CTkLabel(bottom_frame, text="Return Date", text_color="black")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                        elif col == 4:
                            label = a.CTkLabel(bottom_frame, text="Time", text_color="black")
                            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif row != 0 and col == 1:
                        aaa = searchfli(w)
                        label = a.CTkLabel(bottom_frame, text=aaa[row-1], text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif col == 0:
                        label = a.CTkLabel(bottom_frame, text=row, text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif col == 2:  # Departure date
                        label = a.CTkLabel(bottom_frame, text=datepicker1.entry.get(), text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif col == 3:  # Return date
                        label = a.CTkLabel(bottom_frame, text=datepicker2.entry.get(), text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    else:
                        timeop = str(random.randint(1, 18)) + ":" + str(random.randint(0, 59))
                        label = a.CTkLabel(bottom_frame, text=timeop, text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm,
                                  width=106,
                                  height=700,
                                  corner_radius=0,
                                  fg_color="white")
        sidebar_frame.grid(row=0, column=0, rowspan=3, padx=0, pady=0, sticky="ns")
        sidebar_frame.grid_columnconfigure(0, weight=1)
        sidebar_frame.grid_rowconfigure((0, 5), weight=1)  # Add empty rows for centering
        sidebar_frame.grid_rowconfigure((1, 2, 3, 4), weight=0)  # Rows for buttons
        sidebar_frame.grid_propagate(False)

        def clk2():
            sidebar_frame.grid_forget()

        cross = a.CTkImage(Image.open('assets/close.png'), size=(18, 18))
        buttoncross = a.CTkButton(sidebar_frame, text="", image=cross, width=18, height=18, fg_color="transparent", command=clk2)
        buttoncross.grid(row=0, column=0, padx=5, pady=5, sticky="ne")
        # Home button
        img1 = a.CTkImage(Image.open('assets/home.png'), size=(32, 32))
        button1 = a.CTkButton(sidebar_frame,
                              text="Home",
                              font=("Arial", 16),
                              text_color="black",
                              image=img1,
                              width=36,
                              height=36,
                              corner_radius=0,
                              fg_color="white",
                              hover_color="#FFE4E4",
                              command=lambda: d("Dash"))
        button1.grid(row=1, column=0, padx=0, pady=4, sticky="we")

        # Explore button
        img4 = a.CTkImage(Image.open('assets/map.png'), size=(30, 30))
        button4 = a.CTkButton(sidebar_frame,
                              text="Explore",
                              font=("Arial", 16),
                              text_color="black",
                              width=36,
                              height=36,
                              corner_radius=0,
                              fg_color="white",
                              image=img4,
                              hover_color="#FFE4E4",
                              command=lambda: d("Map"))
        button4.grid(row=2, column=0, padx=0, pady=4, sticky="we")

        # Book button
        img2 = a.CTkImage(Image.open('assets/plane.png'), size=(34, 34))
        button2 = a.CTkButton(sidebar_frame,
                              text="Book",
                              font=("Arial", 16),
                              text_color="black",
                              width=36,
                              height=36,
                              corner_radius=0,
                              fg_color="#FFE4E4",
                              image=img2,
                              hover="DISABLE")
        button2.grid(row=3, column=0, padx=0, pady=4, sticky="we")

        # Cust button
        img3 = a.CTkImage(Image.open('assets/cust.png'), size=(32, 32))
        button3 = a.CTkButton(sidebar_frame,
                              text="",
                              width=36,
                              height=36,
                              corner_radius=18,
                              fg_color="white",
                              image=img3,
                              hover_color="#FFE4E4",
                              command=lambda: d("Cust"))
        button3.grid(row=5, column=0, padx=0, pady=4, sticky="we")

    imgmen = a.CTkImage(Image.open('assets/menu.png'), size=(20, 20))
    menu = a.CTkButton(bm, width=20, height=20, corner_radius=18, fg_color="#5ca3ff", image=imgmen, text="", command=clk)
    menu.grid(row=0, column=0, padx=5, pady=0, sticky="n")

    # Top Frame
    top_frame = a.CTkFrame(bm, width=750, height=150, corner_radius=20, fg_color="whitesmoke", border_color="black", border_width=1)
    top_frame.grid(row=0, column=1, padx=10, pady=10)
    top_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
    top_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    top_frame.grid_propagate(False)

    cities = ['Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune']

    # Dropdown Boxes and Other Widgets in Top Frame
    drop1 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop1.grid(row=1, column=1, padx=10, pady=1, sticky="we")
    drop1.set("From")

    drop2 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop2.grid(row=1, column=2, padx=10, pady=1, sticky="we")
    if placename != " ":
        for i in range(len(cities)):
            if placename == cities[i]:
                drop2.set(cities[i])
            else:
                drop2.set("To")
    
    spinbox = b.Spinbox(top_frame, from_=1, to=100, style='info.TSpinbox')
    spinbox.grid(row=1, column=3, padx=10, pady=1, sticky="ew")
    spinbox.set("Passengers")

    datepicker1 = b.DateEntry(top_frame, style='primary', startdate=None, dateformat="%d/%m/%Y")
    datepicker1.grid(row=3, column=1, padx=10, pady=1, sticky="ew")

    datepicker2 = b.DateEntry(top_frame, bootstyle="danger", firstweekday=0, startdate=None, dateformat="%d/%m/%Y")
    datepicker2.grid(row=3, column=2, padx=10, pady=1, sticky="ew")

    dropdown3 = b.Combobox(top_frame, style='primary.TCombobox', values=["Economic", "Business", "First Class"])
    dropdown3.grid(row=3, column=3, padx=10, pady=1, sticky="ew")
    dropdown3.set("Class")

    button = b.Button(top_frame, text="Book", bootstyle="primary.outline", command=search)
    button.grid(row=4, column=3, padx=10, pady=1, sticky="ew")

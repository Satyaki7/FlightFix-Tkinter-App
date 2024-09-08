def book(a, b, c, d, m, placename):
    import random
    from PIL import Image, ImageDraw, ImageTk, ImageSequence
    from datetime import datetime
    from .authenticating import searchfli
    from .authenticating import get_flight_times
    from tkinter import messagebox
    from .form import formop

    c.geometry("960x700")
    c.title("Booking")
    c.configure(fg_color='#1c82e3')
    c.grid_columnconfigure((0, 2), weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure((0, 2), weight=0)
    c.grid_rowconfigure(1, weight=1)
    r = 1
    q, w, e, r, t, y = "", "", "", "", "", ""

    def flightb(x, r, m, e):
        print("the row may be: ",x)
        global q, w, t, y
        formop(a, b, c, d, x, r, m, e, q, w, t)

    bm = a.CTkFrame(c, fg_color="transparent", width=960, height=700, corner_radius=10)
    bm.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
    bm.grid_columnconfigure(0, weight=0)
    bm.grid_columnconfigure(1, weight=1)
    bm.grid_rowconfigure(1, weight=0)
    bm.grid_rowconfigure((0, 2), weight=1)
    bm.grid_propagate(False)

    def btframe(w,r,t,y,e):
        bottom_frame = a.CTkScrollableFrame(bm, width=700, height=400, corner_radius=20, fg_color="white")
        bottom_frame.grid(row=2, column=1, padx=10, pady=10)
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_rowconfigure(0, weight=1)
        for i in range(11):
            bottom_frame.grid_rowconfigure(i, weight=1)
        for j in range(6):
            bottom_frame.grid_columnconfigure(j, weight=1)

        for row in range(11):
            for col in range(7):
                if col == 6:
                    if row == 0:
                        continue
                    button = b.Button(bottom_frame, text="Book Flight", style="primary.Outline.TButton", command=lambda x=row: flightb(x, r, m, e))
                    button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
                elif row == 0:
                    headers = ["Sl No.", "Flight No", "Departure Date", "Return Date", "Time", "Price"]
                    if col < len(headers):
                        label = a.CTkLabel(bottom_frame, text=headers[col], text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 1:
                    #flight search function
                    aaa = searchfli(w.lower())
                    if aaa is None:
                        messagebox.showerror("Error", "No flights found.")
                        return
                    if row - 1 < len(aaa):
                        label = a.CTkLabel(bottom_frame, text=aaa[row-1], text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 0:
                    label = a.CTkLabel(bottom_frame, text=row, text_color="black")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 2:
                    label = a.CTkLabel(bottom_frame, text=datepicker1.entry.get(), text_color="black")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 3:
                    if not retcheck_var.get():
                        label = a.CTkLabel(bottom_frame, text="N/A", text_color="black")
                    else:
                        label = a.CTkLabel(bottom_frame, text=datepicker2.entry.get(), text_color="black")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 4:
                    timelist = get_flight_times()
                    if row - 1 < len(timelist):
                        label = a.CTkLabel(bottom_frame, text=timelist[row-1], text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 5:
                    if e == "First Class":
                        price = f"₹{random.randint(20000, 30000)}"
                        label = a.CTkLabel(bottom_frame, text=price, text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif e == "Economic":
                        price = f"₹{random.randint(6000, 10000)}"
                        label = a.CTkLabel(bottom_frame, text=price, text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    elif e == "Business Class":
                        price = f"₹{random.randint(30000, 40000)}"
                        label = a.CTkLabel(bottom_frame, text=price, text_color="black")
                        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


    #searching for the flight
    def search():
        global q, w, e, r, t, y
        q, w, e, r, t, y = drop1.get(), drop2.get(), dropdown3.get(), spinbox.get(), datetime.strptime(datepicker1.entry.get(), "%d/%m/%Y"), datetime.strptime(datepicker2.entry.get(), "%d/%m/%Y")
        t = t.strftime("%d/%m/%Y")
        y = y.strftime("%d/%m/%Y")
        print("The selected date is: ", t)
        if q == "From" or w == "To":
            messagebox.showerror("Error", "Select Departure and Arrival location properly.")
            return
        elif e == "Class":
            messagebox.showerror("Error", "Please select ticket type.")
            return
        elif r == "Passengers":
            messagebox.showerror("Error", "Number of passengers cannot be zero")
            return
        elif q == w:
            messagebox.showerror("Error", "Departure and Arrival location cannot be same.")
            return
        elif dropdown3 == "Class":
            messagebox.showerror("Error", "Please select the class of ticket.")
            return
        elif retcheck_var.get():
            if t == y:
                messagebox.showerror("Error", "Departure and Return date cannot be same.")
                return
            elif t > y:
                messagebox.showerror("Error", "Time travel not allowed!")
                return
            elif q != "From" and w != "To" and dropdown3 != "Class" and spinbox.get() != "Passengers" and t != y:
                btframe(w,r,t,y,e)
        elif not retcheck_var.get():
            if q != "From" and w != "To" and dropdown3 != "Class" and spinbox.get() != "Passengers":
                btframe(w,r,t,y,e)

    #this is the side bar
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
    top_frame = a.CTkFrame(bm, width=750, height=150, corner_radius=20, fg_color="white", border_color="black", border_width=1)
    top_frame.grid(row=0, column=1, padx=10, pady=10)
    top_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
    top_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    top_frame.grid_propagate(False)

    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "London", "Paris", "Tokyo", "Sydney", "Dubai", "New York", "Srinagar", "Kochi", "Kyoto", "Jaipur"]



    # Dropdown Boxes and Other Widgets in Top Frame
    drop1 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop1.grid(row=1, column=1, padx=10, pady=1, sticky="we")
    drop1.set("From")

    drop2 = b.Combobox(top_frame, style='primary.TCombobox', values=cities)
    drop2.grid(row=1, column=2, padx=10, pady=1, sticky="we")
    if placename != "":
        for i in range(len(cities)):
            if placename != " ":
                if placename in cities:
                    drop2.set(placename)
                else:
                    drop2.set("To")
            else:
                drop2.set("To")
    
    spinbox = b.Spinbox(top_frame, from_=1, to=100, style='info.TSpinbox')
    spinbox.grid(row=1, column=3, padx=10, pady=1, sticky="ew")
    spinbox.set("Passengers")

    departure = a.CTkLabel(top_frame, text="Departure", text_color="black",font = ("Arial", 10))
    departure.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    
    datepicker1 = b.DateEntry(top_frame, style='primary', startdate=None, dateformat="%d/%m/%Y")
    datepicker1.grid(row=3, column=1, padx=10, pady=1, sticky="w")

    def toggle_datepicker():
        if retcheck_var.get():
            datepicker2.configure(state="normal")
        else:
            datepicker2.configure(state="disabled")
    
    returndate = a.CTkLabel(top_frame, text="Return", text_color="black",font = ("Arial", 10))
    returndate.grid(row=2, column=2, padx=10, pady=1, sticky = "ew")

    retcheck_var = b.BooleanVar()
    retcheck = b.Checkbutton(top_frame, style = "success",text="Return Ticket", variable=retcheck_var, command=toggle_datepicker)
    retcheck.grid(row=2, column=3, padx=10, pady=1, sticky="ew")

    datepicker2 = b.DateEntry(top_frame, bootstyle="danger", firstweekday=0, startdate=None, dateformat="%d/%m/%Y")
    datepicker2.grid(row=3, column=2, padx=10, pady=1, sticky="ew")
    datepicker2.configure(state="disabled")


    dropdown3 = b.Combobox(top_frame, style='primary.TCombobox', values=["Economic","First Class","Business Class"])
    dropdown3.grid(row=3, column=3, padx=10, pady=1, sticky="ew")
    dropdown3.set("Class")

    button = b.Button(top_frame, text="Book", bootstyle="primary.outline", command=search)
    button.grid(row=4, column=3, padx=10, pady=1, sticky="ew")

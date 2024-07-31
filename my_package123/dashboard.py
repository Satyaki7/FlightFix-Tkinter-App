from CTkTable import *

def dashboardop(a, b, c, d, m):
    import sqlite3
    from PIL import Image, ImageDraw, ImageTk
    from .explore import create_rounded_image
    from .authenticating import get_bookings_by_username
    import tkinter as tk
    import time
    c.geometry("1000x700")
    c.title("Dashboard")
    c.configure(fg_color='#b187e8')
    # Configure grid layout for the window
    c.grid_columnconfigure((0,2), weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure((0, 2), weight=0)
    c.grid_rowconfigure(1, weight=1)

    bm = a.CTkFrame(c, fg_color="transparent", width=960, height=700,corner_radius=10)
    bm.grid(row=1, column=1, sticky="nsew", padx=0, pady=0, rowspan=3, columnspan=3)

    bm.grid_columnconfigure((0,4), weight=0)
    bm.grid_columnconfigure((1,2,3), weight=1)
    bm.grid_rowconfigure((0), weight=0)
    bm.grid_rowconfigure((1, 2,3), weight=1)

    # Load the background image
    # bg_photo = a.CTkImage(Image.open("assets/14337.jpg"), size=(1100, 700))

    # # Create a Label to hold the background image
    # bg_label = a.CTkLabel(bm, image=bg_photo, text="")
    # bg_label.place(relwidth=1, relheight=1)
    
    def on_button_click(a):
        print("booking is working")

    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm, width=106, height=700, corner_radius=0, fg_color="white")
        sidebar_frame.grid(row=0, column=0, rowspan=2, padx=0, pady=0, sticky="ns")
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
                              fg_color="#FFE4E4",
                              hover="DISABLE")
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
                              fg_color="white",
                              image=img2,
                              hover_color="#FFE4E4",
                              command=lambda: d("Flight"))
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
    
    
    # User Info Frame
    user_info_frame = a.CTkFrame(bm, width=273, height=273, corner_radius=20, fg_color="white", border_color="black", border_width=1)
    user_info_frame.grid(row=1, column=1, padx=2, pady=5)
    user_info_frame.grid_columnconfigure(0, weight=1)
    user_info_frame.grid_rowconfigure((0, 1, 2, 3,4), weight=0)
    user_info_frame.grid_propagate(False)

    def cancelbooking():
        # Create a new top window
        top = a.CTkToplevel(c)
        top.title("Cancel a Booking")
        top.geometry("300x300")
        top.configure(fg_color='white')

        # Add a label
        label = b.Label(top, text="Cancel a Booking", font=("Arial", 14))
        label.pack(pady=10)

        # Add an input field for unique ID
        unique_id_var = a.StringVar()
        entry = b.Entry(top, textvariable=unique_id_var, font=("Arial", 12))
        entry.pack(pady=10)

        # Add a cancel booking button
        def search_and_delete():
            unique_id = unique_id_var.get()
            conn = sqlite3.connect('users.db')  # Replace with your actual database file
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM bookinghistory WHERE unique_id=?", (unique_id,))
            result = cursor.fetchone()

            if result:
                cursor.execute("DELETE FROM bookinghistory WHERE unique_id=?", (unique_id,))
                conn.commit()
                messagebox.showinfo("Success", "Booking has been cancelled.")
            else:
                messagebox.showerror("Error", "Booking not found.")

            conn.close()
            top.destroy()

        cancel_button = b.Button(top, text="Cancel Booking", command=search_and_delete, state="disabled", bootstyle="success")
        cancel_button.pack(pady=10)

        # Enable the button only when the unique ID is entered
        def on_unique_id_entry(*args):
            if unique_id_var.get().strip():
                cancel_button.config(state="normal")
            else:
                cancel_button.config(state="disabled")

        unique_id_var.trace_add("write", on_unique_id_entry)

        
    
    cancelbook = a.CTkButton(user_info_frame, text="Cancel a Booking", width=150, height=30,fg_color = "#02b875",hover_color = "#03eb95",corner_radius = 10,text_color = "white",font = ("Arial", 12),command = cancelbooking)
    cancelbook.grid(row=4, column=0, padx=5, pady=5, sticky="")

    bookingmanagement = a.CTkFrame(bm, width=273, height=273, corner_radius=10, fg_color="white", border_color="black", border_width=1)
    bookingmanagement.grid(row=1, column=2,padx=2, pady=5)
    bookingmanagement.grid_propagate(False)
    bookingmanagement.grid_columnconfigure(0, weight=1)
    bookingmanagement.grid_rowconfigure((0, 1, 2, 3), weight=1) 
    startop = a.CTkLabel(bookingmanagement, text="Start Your Journey", font=("Arial", 20), text_color="black")
    startop.grid(row=0, column=0, padx=2, pady=2, sticky="")
    start = a.CTkButton(bookingmanagement,width = 200,height = 40,fg_color = "#02b875",hover_color = "#03eb95",corner_radius = 10,text = "Book Flight",font=("Arial", 20),text_color = "white",command = lambda: d("Flight"))
    start.grid(row=1, column=0, padx=10, pady=2, sticky="ew")
    explore = a.CTkButton(bookingmanagement,width = 200,height = 40,fg_color = "#386de7",hover_color = "#8dabf1",corner_radius = 10,text = "Explore",font=("Arial", 20),text_color = "white",command = lambda: d("Map"))
    explore.grid(row=2, column=0, padx=10, pady=2, sticky="ew")
    
    
    # Load and process the image to be circular
    image_path = "assets/luffy.jpg"
    size = 50
    img = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS)

    # Create a circular mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the mask to the image
    circular_img = Image.new('RGBA', (size, size), (245, 245, 245, 255))  # Transparent background
    circular_img.paste(img, (0, 0), mask=mask)

    # Convert the circular image to PhotoImage
    photo = ImageTk.PhotoImage(circular_img)

    # Create a frame to hold the canvas
    frame = a.CTkFrame(user_info_frame, width=60, height=60, fg_color="transparent")
    frame.grid(row=0, column=0, pady=5)

    # Create a canvas to display the image
    canvas = a.CTkCanvas(frame, width=size, height=size, bg='white', highlightthickness=0)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.grid(row=0, column=0, padx=20, pady=20)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

    # Username
    userop = m
    usernamela = a.CTkLabel(user_info_frame, fg_color="white", text=userop, font=("Arial", 25), text_color="black")
    usernamela.grid(row=1, column=0, padx=5, pady=0)
    usertype = a.CTkLabel(user_info_frame, fg_color="white", text="Account Type:", font=("Arial", 15), text_color="black")
    usertype.grid(row=2, column=0, padx=5, pady=0)
    usertype = a.CTkLabel(user_info_frame, fg_color="white", text="Non-Premium", font=("Arial", 15), text_color="black")
    usertype.grid(row=3, column=0, padx=5, pady=0)


    # Premium Frame
    premium_frame = a.CTkFrame(bm, width=480, height=273, corner_radius=20, fg_color="white", border_color="black", border_width=1)
    premium_frame.grid(row=1, column=3, padx=2, pady=5)
    premium_frame.grid_propagate(False)
    premium_frame.grid_rowconfigure((0), weight=1)
    premium_frame.grid_columnconfigure((0), weight=1)
    premiumad = create_rounded_image("assets/Flat.jpg", (273,273), 10)
    premiumadop = a.CTkImage(premiumad, size=(480, 273))
    premiumadd = a.CTkLabel(premium_frame, image=premiumadop,text = " ")
    premiumadd.grid(row=0, column=0, padx=0, pady=0,sticky = "nsew")

    
    # Upcoming Flights Frame
    upcoming_flights_frame = a.CTkFrame(bm, width=480, height=273, corner_radius=10, fg_color="white", border_color="black", border_width=1)
    upcoming_flights_frame.grid(row=2, column=1,columnspan = 2, padx=5, pady=0,sticky = "nsew")
    # upcoming_flights_frame.grid_propagate(False)

    flighthistory = [
        ["From","To","Passengers","Seating","Date"," "]
    ]

    nv = get_bookings_by_username(m)
    for record in nv:
        flighthistory.append(record)
        print(record)
    
    table = CTkTable(master = upcoming_flights_frame, row=5, column=6, values=flighthistory,colors = ["white","whitesmoke"])
    table.pack(expand=True, fill="both", padx=2, pady=2)

    # # Configure rows and columns for the grid in upcoming_flights_frame
    # for i in range(6):
    #     upcoming_flights_frame.grid_rowconfigure(i, weight=1)
    # for j in range(5):
    #     upcoming_flights_frame.grid_columnconfigure(j, weight=1)

    # # Populate the grid with labels and buttons
    # for row in range(6):
    #     for col in range(5):
    #         if col == 4:  # Place button in the 5th column
    #             if row == 0:
    #                 continue
    #             button = b.Button(upcoming_flights_frame, text=f"Button {row}", bootstyle="primary.Outline.TButton", command=lambda r=row: on_button_click(r))
    #             button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
    #         elif row == 0:
    #             if col == 0:
    #                 label = a.CTkLabel(upcoming_flights_frame, text="Sl No.", text_color="black")
    #                 label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    #             elif col == 1:
    #                 label = a.CTkLabel(upcoming_flights_frame, text="Flight No", text_color="black")
    #                 label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    #             elif col == 2:
    #                 label = a.CTkLabel(upcoming_flights_frame, text="Date", text_color="black")
    #                 label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    #             elif col == 3:
    #                 label = a.CTkLabel(upcoming_flights_frame, text="Time", text_color="black")
    #                 label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    #         else:  # Place labels in other columns
    #             label = a.CTkLabel(upcoming_flights_frame, text=f"Label {row},{col}", text_color="black")
    #             label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

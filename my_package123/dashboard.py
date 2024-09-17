from CTkTable import *

def dashboardop(a, b, c, d, m):
    import sqlite3
    from .authenticating import search_and_delete
    from PIL import Image, ImageDraw, ImageTk, ImageSequence
    from .explore import create_rounded_image
    from .authenticating import get_bookings_by_username
    import tkinter as tk
    import time#b8dbef
    c.geometry("1000x700")
    c.title("Dashboard")
    c.configure(fg_color='#1c99ed')
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

    # the background image
    bg_photo = a.CTkImage(Image.open("assets/background.jpg"), size=(1100, 700))

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(bm, image=bg_photo, text="")
    bg_label.place(relwidth=1, relheight=1)
    
    def on_button_click(a):
        print("booking is working")

    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm, width=106, height=700, corner_radius=0, fg_color="white")
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

        def cancelop(unique_id_var):
            if search_and_delete(unique_id_var):
                for widget in upcoming_flights_frame.winfo_children():
                    widget.destroy()
                flighthistory = [
                    ["Booking ID","From","To","Passengers","Seating","Date"]
                ]
                nv = get_bookings_by_username(m)
                for record in nv:
                    flighthistory.append(record)
                    print(record)
                table = CTkTable(master = upcoming_flights_frame, row=5, column=6, values=flighthistory,colors = ["white","whitesmoke"])
                table.pack(expand=True, fill="both", padx=2, pady=2)
                top.destroy()
            else:
                pass
            
        
        # Add a cancel booking button
        cancel_button = b.Button(top, text="Cancel Booking", command=lambda:cancelop(unique_id_var), state="disabled", bootstyle="success")
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

    bookingmanagement = a.CTkFrame(bm, width=273, height=273, corner_radius=20, fg_color="white", border_color="black", border_width=1)
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
    frame.grid(row=0, column=0, pady=2)

    # Create a canvas to display the image
    canvas = a.CTkCanvas(frame, width=size, height=size, bg='white', highlightthickness=0)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.grid(row=0, column=0, padx=20, pady=20)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

    # Username
    userop = m
    usernamela = a.CTkLabel(user_info_frame, fg_color="white", text=userop, font=("Arial", 25), text_color="black")
    usernamela.grid(row=1, column=0, padx=5, pady=4)
    usertype = a.CTkLabel(user_info_frame, fg_color="white", text="Your next flight is on: ", font=("Arial", 15), text_color="black")
    usertype.grid(row=2, column=0, padx=5, pady=0)
    usertype = a.CTkLabel(user_info_frame, fg_color="white", text="xx/xx/xxxx at xx:xx", font=("Arial", 15), text_color="black")
    usertype.grid(row=3, column=0, padx=5, pady=2)


    # Premium Frame
    premium_frame = a.CTkFrame(bm, width=480, height=273, corner_radius=20, fg_color="white", border_color="black", border_width=1)
    premium_frame.grid(row=1, column=3, padx=10, pady=5)
    premium_frame.grid_propagate(False)
    premium_frame.grid_rowconfigure((0), weight=1)
    premium_frame.grid_columnconfigure((0), weight=1)

    # Load the GIF

    gif = Image.open("assets/ad.gif")

    # Extract frames and their durations
    frames = []
    durations = []

    for frame in ImageSequence.Iterator(gif):
        frame_ctk = a.CTkImage(light_image=frame.convert('RGBA'), size=(480, 273))
        frames.append(frame_ctk)
        durations.append(frame.info.get('duration', 100))  # Default to 100ms if no duration is found

    # Create a label to display GIF frames
    gif_label = a.CTkLabel(premium_frame, text="")
    gif_label.grid(row=0, column=0, sticky="nsew")

    def play_gif(frame_index=0):
        frame = frames[frame_index]
        gif_label.configure(image=frame)
        next_frame_index = (frame_index + 1) % len(frames)
        premium_frame.after(durations[frame_index], play_gif, next_frame_index)

    # Start playing the GIF
    play_gif()
    
    # Upcoming Flights Frame
    upcoming_flights_frame = a.CTkScrollableFrame(bm, width=480, height=273, corner_radius=10, fg_color="white", border_color="black", border_width=1,scrollbar_fg_color = "white",scrollbar_button_color = "black",scrollbar_button_hover_color = "blue")
    upcoming_flights_frame.grid(row=2, column=1,columnspan = 3, padx=10, pady=5,sticky = "nsew")
    # upcoming_flights_frame.grid_propagate(False)

    flighthistory = [
        ["Booking ID","Flight_ID","From","To","Passengers","Seating","Date","Time"]
    ]

    nv = get_bookings_by_username(m)
    for record in nv:
        flighthistory.append(record)
        print(record)
    
    table = CTkTable(master = upcoming_flights_frame, row=len(flighthistory), column=8, values=flighthistory,colors = ["white","whitesmoke"])
    table.pack(expand=True, fill="both", padx=2, pady=2)

   
def dashboardop(a, b, c, d,m):
    from PIL import Image, ImageDraw, ImageTk
    import tkinter as tk
    import time
    c.geometry("960x700")
    c.title("Dashboard")
    c.configure(fg_color='#5ca3ff')
    # Configure grid layout for the window
    c.grid_columnconfigure((0,2), weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure((0,2), weight=0)
    c.grid_rowconfigure(1, weight=1)

    bm = a.CTkFrame(c, fg_color="transparent",width = 960,height = 700,corner_radius = 10)
    bm.grid(row=1, column=1, sticky="nsew",padx = 10,pady=10,rowspan = 3,columnspan = 3)
    
    bm.grid_columnconfigure(0, weight=0)
    bm.grid_columnconfigure(1, weight=1)
    bm.grid_columnconfigure(2, weight=2)
    bm.grid_rowconfigure((0,1,2,3), weight=1)

    # Load the background image
    bg_photo = a.CTkImage(Image.open("assets/14337.jpg"),size = (1100,700))

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(bm, image=bg_photo,text="")
    bg_label.place(relwidth=1, relheight=1)  

    def on_button_click(a):
        print("booking is working")
    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm,
                                   width=106,
                                   height=700,
                                   corner_radius=10,
                                   fg_color="#FFFFFF")
        sidebar_frame.grid(row=0, column=0, rowspan=2, padx=0, pady=0, sticky="ns")
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
                              fg_color="#A2CCFE",
                              hover="DISABLED")
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
                              fg_color="#5ca3ff",
                              image=img2,
                              hover_color="#A2CCFE",
                              command=lambda: d("Flight"))
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
    
    # User Info Frame
    user_info_frame = a.CTkFrame(bm,
                                 width=273,
                                 height=273,
                                 corner_radius=20,
                                 fg_color="whitesmoke",
                                 border_color = "black",
                                 border_width = 1)
    user_info_frame.grid(row=0, column=1, padx=5, pady=5)
    user_info_frame.grid_columnconfigure(0, weight=1)
    user_info_frame.grid_rowconfigure((0,1,2,3), weight=0)
    user_info_frame.grid_propagate(False)
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
    frame = a.CTkFrame(user_info_frame, width=60, height=60,fg_color="transparent")
    frame.grid(row=0, column=0,pady = 5)

    # Create a canvas to display the image
    canvas = a.CTkCanvas(frame, width=size, height=size, bg='whitesmoke', highlightthickness=0)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.grid(row=0, column=0, padx=20, pady=20)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

    #username
    userop = m
    usernamela = a.CTkLabel(user_info_frame,
                            fg_color = "whitesmoke",
                            text = userop,
                           font=("Arial", 25))
    usernamela.grid(row=1, column=0, padx=5, pady=0)
    usertype = a.CTkLabel(user_info_frame,
        fg_color = "whitesmoke",
        text = "Account Type:",
       font=("Arial", 15))
    usertype.grid(row=2, column=0, padx=5, pady=0)
    usertype = a.CTkLabel(user_info_frame,
        fg_color = "whitesmoke",
        text = "Non-Premium",
       font=("Arial", 15))
    usertype.grid(row=3, column=0, padx=5, pady=0)

    # Flights Frame
    flights_frame = a.CTkFrame(bm,
                               width=437,
                               height=273,
                               corner_radius=10,
                               fg_color="transparent")
    flights_frame.grid(row=0, column=2,padx=5, pady=5)
    # Premium Frame
    premium_frame = a.CTkFrame(bm,
                               width=273,
                               height=273,
                               corner_radius=20,
                               fg_color="whitesmoke",
                               border_color = "black",
                               border_width = 1)
    premium_frame.grid(row=1, column=1, padx=5, pady=5)
    premium_frame.grid_propagate(False)
    # Upcoming Flights Frame
    upcoming_flights_frame = a.CTkFrame(bm,
                                        width=480,
                                        height=273,
                                        corner_radius=10,
                                        fg_color="whitesmoke",
                                        border_color = "black",
                                        border_width = 1)
    upcoming_flights_frame.grid(row=1,
                                column=2,
                                padx=5,
                                pady=5)
    upcoming_flights_frame.grid_propagate(False)
    # Configure rows and columns for the grid in upcoming_flights_frame
    for i in range(6):
        upcoming_flights_frame.grid_rowconfigure(i, weight=1)
    for j in range(5):
        upcoming_flights_frame.grid_columnconfigure(j, weight=1)

    # Populate the grid with labels and buttons
    for row in range(6):
        for col in range(5):
            if col == 4:  # Place button in the 5th column
                if row == 0:
                    continue
                button = b.Button(upcoming_flights_frame, text=f"Button {row}", bootstyle="primary.Outline.TButton", command=lambda r=row: on_button_click(r))
                button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            elif row == 0:
                if col == 0:
                    label = a.CTkLabel(upcoming_flights_frame, text="Sl No.")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 1:
                    label = a.CTkLabel(upcoming_flights_frame, text="Flight No")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 2:
                    label = a.CTkLabel(upcoming_flights_frame, text="Date")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                elif col == 3:
                    label = a.CTkLabel(upcoming_flights_frame, text="Time")
                    label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            else:  # Place labels in other columns
                label = a.CTkLabel(upcoming_flights_frame, text=f"Label {row},{col}")
                label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

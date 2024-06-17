def dashboardop(a, b, c, d,m):
    from PIL import Image, ImageDraw, ImageTk
    c.geometry("900x600")
    c.title("Dashboard")
    #c.configure(fg_color='transparent')
    # Configure grid layout for the window
    c.grid_columnconfigure(0, weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_columnconfigure(2, weight=2)
    c.grid_rowconfigure(0, weight=1)
    c.grid_rowconfigure(1, weight=1)
    c.grid_rowconfigure(2, weight=1)
    c.grid_rowconfigure(3, weight=1)

    # Load the background image
    bg_image = Image.open("assets/14337.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(c, image=bg_photo,text="")
    bg_label.place(relwidth=1, relheight=1)  
    
    def on_button_click(a):
        print("booking is working")

    # Left Sidebar Frame
    sidebar_frame = a.CTkFrame(c,
                               width=30,
                               height=500,
                               corner_radius=20,
                               fg_color="transparent")
    sidebar_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
    sidebar_frame.grid_rowconfigure((0, 4), weight=1)  # Add empty rows for centering
    sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)  # Rows for buttons

    #dash
    img1 = ImageTk.PhotoImage(
        Image.open('assets/home.png').resize((30, 30)))
    button1 = a.CTkButton(sidebar_frame,
                          image=img1,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="blue",
                          hover="DISABLED")
    button1.grid(row=1, column=0, padx=2, pady=10)
    #flight
    img2 = ImageTk.PhotoImage(
        Image.open('assets/plane.png').resize((30, 30)))
    button2 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="whitesmoke",
                          image=img2,
                          hover_color="blue",
                          command=lambda: d("Flight"))
    button2.grid(row=2, column=0, padx=2, pady=30)
    #cust
    img3 = ImageTk.PhotoImage(
        Image.open('assets/cust.png').resize((30, 30)))
    button3 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="whitesmoke",
                          image=img3,
                          hover_color="blue",
                          command=lambda: d("Cust"))
    button3.grid(row=3, column=0, padx=2, pady=10)

    # User Info Frame
    user_info_frame = a.CTkFrame(c,
                                 width=200,
                                 height=250,
                                 corner_radius=20,
                                 fg_color="whitesmoke",
                                 border_color = "black",
                                 border_width = 1)
    user_info_frame.grid(row=0, column=1, padx=5, pady=10,sticky="nsew")
    user_info_frame.grid_columnconfigure(0, weight=1)
    user_info_frame.grid_rowconfigure(0, weight=0)
    user_info_frame.grid_rowconfigure(1, weight=0)
    user_info_frame.grid_rowconfigure(2, weight=0)
    user_info_frame.grid_rowconfigure(3, weight=0)
    user_info_frame.grid_propagate(False)
    # User Image


    # Load and process the image to be circular
    image_path = "assets/luffy.jpg"
    size = 50
    img = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS)

    # Create a circular mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the mask to the image
    circular_img = Image.new('RGBA', (size, size), (255, 192, 203))  # Transparent background
    circular_img.paste(img, (0, 0), mask=mask)

    # Convert the circular image to PhotoImage
    photo = ImageTk.PhotoImage(circular_img)

    
    user_image_frame = a.CTkFrame(user_info_frame,
                                  width=60,
                                  height = 60,
                                  corner_radius=30,
                                  fg_color = "transparent")
    user_image_frame.grid(row=0, column=0, padx=5, pady=15)
    user_image_frame.grid_propagate(False)
    user_image_frame.grid_columnconfigure(0, weight=1)
    user_image_frame.grid_rowconfigure(0, weight=1)
    user = a.CTkLabel(user_image_frame,image = photo,text="")
    user.grid(row=0, column=0, padx=0, pady=0)

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
    flights_frame = a.CTkFrame(c,
                               width=450,
                               height=250,
                               corner_radius=20,
                               fg_color="transparent")
    flights_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
    # Premium Frame
    premium_frame = a.CTkFrame(c,
                               width=200,
                               height=250,
                               corner_radius=20,
                               fg_color="whitesmoke",
                               border_color = "black",
                               border_width = 1)
    premium_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

    # Upcoming Flights Frame
    upcoming_flights_frame = a.CTkFrame(c,
                                        width=450,
                                        height=250,
                                        corner_radius=20,
                                        fg_color="whitesmoke",
                                        border_color = "black",
                                        border_width = 1)
    upcoming_flights_frame.grid(row=1,
                                column=2,
                                sticky="nsew",
                                padx=10,
                                pady=10)

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

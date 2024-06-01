# safety
#def dashboardop(a,b,c,d,z):


def dashboardop(a, b, c, d, z):
        from PIL import Image, ImageTk
        # Configure grid layout for the window
        c.grid_columnconfigure(0, weight=0)
        c.grid_columnconfigure(1, weight=1)
        c.grid_columnconfigure(2, weight=2)
        c.grid_rowconfigure(0, weight=1)
        c.grid_rowconfigure(1, weight=1)
        c.grid_rowconfigure(2, weight=1)
        c.grid_rowconfigure(3, weight=1)

        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(c,
                                   width=30,
                                   height=500,
                                   corner_radius=20,
                                   fg_color="transparent")
        sidebar_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
        sidebar_frame.grid_rowconfigure(
            (0, 4), weight=1)  # Add empty rows for centering
        sidebar_frame.grid_rowconfigure((1, 2, 3),
                                        weight=0)  # Rows for buttons

        #dash
        img1 = ImageTk.PhotoImage(
            Image.open('assets/home.png').resize((30, 30)))
        button1 = a.CTkButton(sidebar_frame,
                              image=img1,
                              text="",
                              width=10,
                              height=10,
                              corner_radius=100,
                              fg_color="lightblue",
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
                              fg_color="transparent",
                              image=img2,
                              hover_color="cyan",
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
                              fg_color="transparent",
                              image=img3,
                              hover_color="cyan",
                              command=lambda: d("Cust"))
        button3.grid(row=3, column=0, padx=2, pady=10)

        # User Info Frame
        user_info_frame = a.CTkFrame(c,
                                     width=200,
                                     height=250,
                                     corner_radius=20,
                                     fg_color="cyan")
        user_info_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)

        # Flights Frame
        flights_frame = a.CTkFrame(c,
                                   width=450,
                                   height=250,
                                   corner_radius=20,
                                   fg_color="transparent")
        flights_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=10)
        # Premium Frame
        premium_frame = a.CTkFrame(c,
                                   width=200,
                                   height=250,
                                   corner_radius=20,
                                   fg_color="cyan")
        premium_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

        # Upcoming Flights Frame
        upcoming_flights_frame = a.CTkFrame(c,
                                            width=450,
                                            height=250,
                                            corner_radius=20,
                                            fg_color="cyan")
        upcoming_flights_frame.grid(row=1,
                                    column=2,
                                    sticky="nsew",
                                    padx=5,
                                    pady=10)
        flights = [["Sl.No", "Flight No", "Date", "Status"], [1, 2, 3, 4],
                   [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

        table2 = z.CTkTable(upcoming_flights_frame,
                            row=6,
                            column=4,
                            values=flights,
                            colors=["#F6F7F2", "#F6F7F2"])
        table2.pack(expand=True, fill="both", padx=10, pady=10)

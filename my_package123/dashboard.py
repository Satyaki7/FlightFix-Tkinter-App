


def dashboardop(a,b,c,d,z):
    # Configure grid layout
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure(0, weight=1)
    c.grid_rowconfigure(1, weight=1)

    # Left Frame (Red)
    left_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    left_frame.grid(row=0, column=0, rowspan=2, sticky="ns", padx=10, pady=10)

    # User Info Frame (Yellow)
    user_info_frame = a.CTkFrame(left_frame, width=200, height=150, corner_radius=20, fg_color="yellow")
    user_info_frame.pack(padx=20, pady=(20, 10))

    user_info_label = a.CTkLabel(user_info_frame, text="User Info")
    user_info_label.pack(pady=10)

    # Buttons (Yellow)
    button1 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    button1.pack(padx=20, pady=10)

    button2 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    button2.pack(padx=20, pady=10)

    button3 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    button3.pack(padx=20, pady=10)

    # Flights Frame (Red)
    flights_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    flights_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=(10, 5))
    preflights = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
    
    table = z.CTkTable(flights_frame, row=5, column=5, values=preflights)
    table.pack(expand=True, fill="both", padx=20, pady=20)

    # Upcoming Flights Frame (Red)
    upcoming_flights_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    upcoming_flights_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=(5, 10))

    flights = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

    table2 = z.CTkTable(upcoming_flights_frame, row=5, column=5, values=flights)
    table2.pack(expand=True, fill="both", padx=20, pady=20)


    # Run the application
    c.mainloop()


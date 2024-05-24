# safety 
#def dashboardop(a,b,c,d,z):

def dashboardop(a,b,c,d,z):
     # Configure grid layout for the window
         c.grid_columnconfigure(0, weight=1)
         c.grid_columnconfigure(1, weight=1)
         c.grid_columnconfigure(2, weight=2)
         c.grid_rowconfigure(0, weight=1)
         c.grid_rowconfigure(1, weight=1)
         c.grid_rowconfigure(2, weight=1)
         c.grid_rowconfigure(3, weight=1)

     # Left Sidebar Frame
         sidebar_frame = a.CTkFrame(c, width=70, height=500, corner_radius=20, fg_color="red")
         sidebar_frame.grid(row=0, column=0, rowspan=4,  padx=10, pady=10)
         sidebar_frame.grid_rowconfigure((0, 4), weight=1)  # Add empty rows for centering
         sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)  # Rows for buttons
     
         # Buttons in Sidebar
         button1 = a.CTkButton(sidebar_frame, text="", width=50, height=50, corner_radius=25, fg_color="yellow", hover=False)
         button1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
     
         button2 = a.CTkButton(sidebar_frame, text="", width=50, height=50, corner_radius=25, fg_color="yellow", hover=False)
         button2.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
     
         button3 = a.CTkButton(sidebar_frame, text="", width=50, height=50, corner_radius=25, fg_color="yellow", hover=False)
         button3.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        
     
     # User Info Frame
         user_info_frame = a.CTkFrame(c, width=200, height=250, corner_radius=20, fg_color="red")
         user_info_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

         # Flights Frame
         flights_frame = a.CTkFrame(c, width=450, height=250, corner_radius=20, fg_color="red")
         flights_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
         preflights = [["Sl.No","Flight No","Date","Status"],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]]


         table = z.CTkTable(flights_frame, row=6, column=4, values=preflights,colors=["#F6F7F2", "#F6F7F2"])
         table.pack(expand=True, fill="both", padx=10, pady=10)

         # Premium Frame
         premium_frame = a.CTkFrame(c, width=200, height=250, corner_radius=20, fg_color="red")
         premium_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

         # Upcoming Flights Frame
         upcoming_flights_frame = a.CTkFrame(c, width=450, height=250, corner_radius=20, fg_color="red")
         upcoming_flights_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)        
         flights = [["Sl.No","Flight No","Date","Status"],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]]


         table2 = z.CTkTable(upcoming_flights_frame, row=6, column=4, values=preflights,colors=["#F6F7F2", "#F6F7F2"])
         table2.pack(expand=True, fill="both", padx=10, pady=10)

     
    # # Configure grid layout
    # c.grid_columnconfigure(1, weight=1)
    # c.grid_rowconfigure(0, weight=1)
    # c.grid_rowconfigure(1, weight=1)

    # # Left Frame (Red)
    # left_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    # left_frame.grid(row=0, column=0, rowspan=2, sticky="ns", padx=10, pady=10)

    # # User Info Frame (Yellow)
    # user_info_frame = a.CTkFrame(left_frame, width=200, height=150, corner_radius=20, fg_color="yellow")
    # user_info_frame.pack(padx=20, pady=(20, 10))

    # user_info_label = a.CTkLabel(user_info_frame, text="User Info")
    # user_info_label.pack(pady=10)

    # # Buttons (Yellow)
    # button1 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    # button1.pack(padx=20, pady=10)

    # button2 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    # button2.pack(padx=20, pady=10)

    # button3 = a.CTkButton(left_frame, text="Button", corner_radius=20, fg_color="yellow")
    # button3.pack(padx=20, pady=10)

    # # Flights Frame (Red)
    # flights_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    # flights_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=(10, 5))
    # preflights = [["Sl.No","Flight No","Date","Status"],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4]]
    
    # table = z.CTkTable(flights_frame, row=6, column=4, values=preflights,colors=["#F6F7F2", "#F6F7F2"])
    # table.pack(expand=True, fill="both", padx=20, pady=20)

    # # Upcoming Flights Frame (Red)
    # upcoming_flights_frame = a.CTkFrame(c, corner_radius=20, fg_color="red")
    # upcoming_flights_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=(5, 10))

    # flights = [["Sl.No","Flight No","Date","Status"],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4]]

    # table2 = z.CTkTable(upcoming_flights_frame, row=6, column=4, values=flights)
    # table2.pack(expand=True, fill="both", padx=20, pady=20)


    # # Run the application
    # c.mainloop()


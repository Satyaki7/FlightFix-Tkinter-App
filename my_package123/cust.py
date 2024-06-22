def customer(a, b, c, d):
  from PIL import Image, ImageTk

  c.geometry("1100x700")
  c.title("Dashboard")
  c.configure(fg_color='#5ca3ff')
  # Configure grid layout for the window
  c.configure(bg='blue')
  c.grid_columnconfigure(0, weight=1)
  c.grid_rowconfigure(0, weight=1)

  bm = a.CTkFrame(c, fg_color="transparent",width = 1100,height = 700,corner_radius = 20)
  bm.grid(row=0, column=0, sticky="nsew",padx = 10,pady=10)
  bm.grid_propagate(False)

  bm.grid_columnconfigure(0, weight=0)
  bm.grid_columnconfigure(1, weight=1)
  bm.grid_rowconfigure(0, weight=1)
  bm.grid_rowconfigure(1, weight=1)

  # Load the background image
  bg_image = Image.open("assets/14337.jpg")
  bg_photo = ImageTk.PhotoImage(bg_image)

  # Create a Label to hold the background image
  bg_label = a.CTkLabel(bm, image=bg_photo,text="")
  bg_label.place(relwidth=1, relheight=1)

  # Left Sidebar Frame
  sidebar_frame = a.CTkFrame(bm,
                             width=0,
                             height=0,
                             corner_radius=20,
                             fg_color="transparent")
  sidebar_frame.grid(row=0, column=0, rowspan=2, padx=10)
  sidebar_frame.grid_rowconfigure((0, 4), weight=1)  # Add empty rows for centering
  sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)  # Rows for buttons

  # Dash button
  img1 = ImageTk.PhotoImage(Image.open('assets/home.png').resize((30, 30)))
  button1 = a.CTkButton(sidebar_frame,
                        image=img1,
                        text="",
                        width=10,
                        height=10,
                        corner_radius=100,
                        fg_color="transparent",
                        hover_color="cyan",
                        command=lambda: d("Dash"))
  button1.grid(row=1, column=0, padx=2, pady=10)

  # Flight button
  img2 = ImageTk.PhotoImage(Image.open('assets/plane.png').resize((30, 30)))
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

  # Customer button
  img3 = ImageTk.PhotoImage(Image.open('assets/cust.png').resize((30, 30)))
  button3 = a.CTkButton(sidebar_frame,
                        text="",
                        width=10,
                        height=10,
                        corner_radius=100,
                        fg_color="lightblue",
                        hover="DISABLED",
                        image=img3)
  button3.grid(row=3, column=0, padx=2, pady=10)
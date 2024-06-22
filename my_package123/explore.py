def exploreop(a, b, c, d,m):
  from PIL import Image, ImageDraw, ImageTk
  c.geometry("1100x700")
  c.title("Dashboard")
  #c.configure(fg_color='transparent')
  # Configure grid layout for the window
  c.configure(bg='blue')
  c.grid_columnconfigure(0, weight=1)
  c.grid_rowconfigure(0, weight=1)

  backmain = a.CTkFrame(c, fg_color="transparent",width = 1100,height = 700,corner_radius = 20)
  backmain.grid(row=0, column=0, sticky="nsew",padx = 10,pady=10)
  backmain.grid_propagate(False)

  backmain.grid_columnconfigure(0, weight=0)
  backmain.grid_columnconfigure(1, weight=1)
  backmain.grid_columnconfigure(2, weight=2)
  backmain.grid_rowconfigure(0, weight=1)
  backmain.grid_rowconfigure(1, weight=1)

  # Load the background image
  bg_image = Image.open("assets/14337.jpg")
  bg_photo = ImageTk.PhotoImage(bg_image)

  # Create a Label to hold the background image
  bg_label = a.CTkLabel(backmain, image=bg_photo,text="")
  bg_label.place(relwidth=1, relheight=1)  
    
  # Left Sidebar Frame
  sidebar_frame = a.CTkFrame(backmain,
                             width=30,
                             height=500,
                             corner_radius=20,
                             fg_color="whitesmoke",
                             border_color = "black",
                             border_width = 1)
  sidebar_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
  sidebar_frame.grid_rowconfigure((0, 5), weight=1)  # Add empty rows for centering
  sidebar_frame.grid_rowconfigure((1, 2, 3, 4), weight=0)  # Rows for buttons

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
  button2.grid(row=3, column=0, padx=2, pady=10)
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
  button3.grid(row=4, column=0, padx=2, pady=10)

  img4 = ImageTk.PhotoImage(
      Image.open('assets/map.png').resize((30, 30)))
  button4 = a.CTkButton(sidebar_frame,
                        text="",
                        width=10,
                        height=10,
                        corner_radius=100,
                        fg_color="whitesmoke",
                        image=img4,
                        hover_color="blue",
                        command=lambda: d("Map"))
  button4.grid(row=2, column=0, padx=2, pady=10)

  
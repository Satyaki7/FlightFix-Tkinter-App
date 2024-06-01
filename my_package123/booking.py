from tkinter.constants import ACTIVE, DISABLED


def book(a, b, c, d, e):
    from PIL import Image, ImageTk
    c.geometry("900x600")
    c.configure(bg='white')

    # Configure grid layout for the window
    c.grid_columnconfigure(0, weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_columnconfigure(2, weight=1)
    c.grid_columnconfigure(3, weight=1)
    c.grid_rowconfigure(0, weight=1)
    c.grid_rowconfigure(1, weight=1)
    c.grid_rowconfigure(2, weight=1)
    c.grid_rowconfigure(3, weight=1)

    # Left Sidebar Frame
    sidebar_frame = a.CTkFrame(c,
                               width=0,
                               height=0,
                               corner_radius=20,
                               fg_color="transparent")
    sidebar_frame.grid(row=0, column=0, rowspan=4,padx=10)
    sidebar_frame.grid_rowconfigure((0, 4),
                                    weight=1)  # Add empty rows for centering
    sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)  # Rows for buttons

    #dash
    img1 = ImageTk.PhotoImage(Image.open('assets/home.png').resize((30, 30)))
    button1 = a.CTkButton(sidebar_frame,
                          image=img1,
                          text="",
                          width=10,
                          height=10,
                          fg_color="transparent",
                          corner_radius=100,
                          hover_color="cyan",
                          command=lambda: d("Dash"))
    button1.grid(row=1, column=0, padx=2, pady=10)
    #flight
    img2 = ImageTk.PhotoImage(Image.open('assets/plane.png').resize((30, 30)))
    button2 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          image=img2,
                          fg_color="lightblue",
                          hover="DISABLED")
    button2.grid(row=2, column=0, padx=2, pady=30)
    #cust
    img3 = ImageTk.PhotoImage(Image.open('assets/cust.png').resize((30, 30)))
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

    # Top Frame (for smaller frames and button)
    top_frame = a.CTkFrame(c,
                           width=600,
                           height=100,
                           corner_radius=20,
                           fg_color="red")
    top_frame.grid(row=0,
                   column=1,
                   columnspan=3,
                   sticky="nsew",
                   padx=10,
                   pady=10)
    top_frame.grid_columnconfigure(0, weight=1)
    top_frame.grid_columnconfigure(1, weight=1)
    top_frame.grid_columnconfigure(2, weight=1)
    top_frame.grid_columnconfigure(3, weight=1)
    top_frame.grid_columnconfigure(4, weight=1)

    # Frames and button inside top frame
    frame1 = a.CTkFrame(top_frame,
                        width=100,
                        height=80,
                        corner_radius=20,
                        fg_color="yellow")
     
                    
    frame1.grid(row=0, column=0, padx=10, pady=10)

    frame2 = a.CTkFrame(top_frame,
                        width=100,
                        height=80,
                        corner_radius=20,
                        fg_color="yellow")
    frame2.grid(row=0, column=1, padx=10, pady=10)

    frame3 = a.CTkFrame(top_frame,
                        width=100,
                        height=80,
                        corner_radius=20,
                        fg_color="yellow")
    frame3.grid(row=0, column=2, padx=10, pady=10)

    frame4 = a.CTkFrame(top_frame,
                        width=100,
                        height=80,
                        corner_radius=20,
                        fg_color="yellow")
    frame4.grid(row=0, column=3, padx=10, pady=10)

    top_button = a.CTkButton(top_frame,
                             text="",
                             width=80,
                             height=50,
                             corner_radius=25,
                             fg_color="yellow",
                             hover=False)
    top_button.grid(row=0, column=4, padx=10, pady=10)

    # Middle Frame
    middle_frame = a.CTkFrame(c,
                              width=600,
                              height=200,
                              corner_radius=20,
                              fg_color="red")
    middle_frame.grid(row=1,
                      column=1,
                      columnspan=3,
                      sticky="nsew",
                      padx=10,
                      pady=10)

    # Bottom Frame
    bottom_frame = a.CTkFrame(c,
                              width=600,
                              height=200,
                              corner_radius=20,
                              fg_color="red")
    bottom_frame.grid(row=2,
                      column=1,
                      columnspan=3,
                      sticky="nsew",
                      padx=10,
                      pady=10)


# Example usage:
# c = a.CTk()
# create_layout(c)
# c.mainloop()

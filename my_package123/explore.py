import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk

def exploreop(a, b, c, d):
    c.geometry("960x700")
    c.title("Dashboard")
    c.configure(fg_color='#5ca3ff')
    c.grid_columnconfigure(0, weight=1)
    c.grid_rowconfigure(0, weight=1)

    bm = a.CTkFrame(c, fg_color="transparent", width=960, height=700, corner_radius=20)
    bm.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    bm.grid_propagate(False)
    bm.grid_columnconfigure(0, weight=0)
    bm.grid_columnconfigure((1, 2, 3), weight=1)
    bm.grid_rowconfigure((0, 1), weight=1)

    # Load the background image
    bg_image = Image.open("assets/14337.jpg")
    bg_photo = a.CTkImage(bg_image, size=(960, 700))

    # Create a Label to hold the background image
    bg_label = a.CTkLabel(bm, image=bg_photo, text="")
    bg_label.place(relwidth=1, relheight=1)
    # cards

    def create_rounded_image(image_path, size, radius):
        image = Image.open(image_path).resize(size).convert("RGBA")
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, size[0], size[1]), radius, fill=255)
        rounded_image = Image.new("RGBA", size)
        rounded_image.paste(image, (0, 0), mask)
        return rounded_image
    
    one = a.CTkFrame(bm, fg_color="transparent", width=180, height=271,corner_radius = 20)
    one.grid(row=0, column=1, padx=0, pady=0)
    one.grid_propagate(False)

    one_r = create_rounded_image("assets/delhi.jpg", (180, 271), 10)
    one_photo = a.CTkImage(one_r,size = (180,271))
    one_label = a.CTkLabel(one, image=one_photo, text="")
    one_label.place(relx = 0.5,rely=0.5,anchor="center")
    on_frame = a.CTkFrame(one, fg_color="white", width=160, height=100,corner_radius =10)
    on_frame.place(relx = 0.5,rely=0.8,anchor="center")


    two = a.CTkFrame(bm, fg_color="transparent", width=180, height=271)
    two.grid(row=0, column=2, padx=0, pady=0, sticky="")
    two.grid_propagate(False)

    two_r = create_rounded_image("assets/delhi.jpg", (180, 271), 10)
    twop = a.CTkImage(two_r,size = (180,271))
    twob = a.CTkLabel(two, image=twop,text="")
    twob.place(relx=0.5, rely=0.5, anchor="center")

    three = a.CTkFrame(bm, fg_color="transparent", width=180, height=271)
    three.grid(row=0, column=3, padx=0, pady=0, sticky="")
    three.grid_propagate(False)
    three_photo = a.CTkImage(Image.open("assets/delhi.jpg"), size=(180, 271))
    threeb = a.CTkButton(three, image=three_photo, fg_color='#5ca3ff', hover_color="wheat", corner_radius=10, text="")
    threeb.place(relwidth=1, relheight=1)

    four = a.CTkFrame(bm, fg_color="transparent", width=180, height=271)
    four.grid(row=1, column=1, padx=0, pady=5, sticky="")
    four.grid_propagate(False)
    four_photo = a.CTkImage(Image.open("assets/delhi.jpg"), size=(180, 271))
    fourb = a.CTkButton(four, image=four_photo, fg_color='#5ca3ff', hover_color="wheat", corner_radius=10, text="")
    fourb.place(relwidth=1, relheight=1)

    five = a.CTkFrame(bm, fg_color="transparent", width=180, height=271)
    five.grid(row=1, column=2, padx=0, pady=5, sticky="")
    five.grid_propagate(False)
    five_photo = a.CTkImage(Image.open("assets/rajasthan.jpg"), size=(180, 271))
    fiveb = a.CTkButton(five, image=five_photo, fg_color='#5ca3ff', hover_color="wheat", corner_radius=10, text="")
    fiveb.place(relwidth=1, relheight=1)

    six = a.CTkFrame(bm, fg_color="transparent", width=180, height=271)
    six.grid(row=1, column=3, padx=0, pady=5, sticky="")
    six.grid_propagate(False)
    six_photo = a.CTkImage(Image.open("assets/delhi.jpg"), size=(180, 271))
    sixb = a.CTkButton(six, image=six_photo, fg_color='#5ca3ff', hover_color="wheat", corner_radius=10, text="")
    sixb.place(relwidth=1, relheight=1)
    def clk():
        # Left Sidebar Frame
        sidebar_frame = a.CTkFrame(bm,
                                   width=106,
                                   height=700,
                                   corner_radius=0,
                                   fg_color="#5ca3ff")
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
                              fg_color="#5ca3ff",
                              hover_color="#A2CCFE",
                              command = lambda:d("Dash"))
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
                              fg_color="#A2CCFE",
                              image=img4,
                              hover="DISABLE")
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
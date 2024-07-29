from tkinter import COMMAND, StringVar, END
from typing import final
import ttkbootstrap as b
from tkinter import messagebox
import time

def formop(a, b, c, d, x, y,m,e,depart,to,dateop):
    from .authenticating import add_booking_record
    ct = a.CTkToplevel(c, fg_color="white")
    ct.geometry("600x600")
    ct.title("Dashboard")
    ct.configure(fg_color='white')

    # Configure grid layout for the window
    ct.grid_columnconfigure((0, 2), weight=0)
    ct.grid_columnconfigure(1, weight=1)
    ct.grid_rowconfigure((0, 2), weight=0)
    ct.grid_rowconfigure(1, weight=1)

    def on_entry_click(event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.configure(foreground="black")

    def on_focus_out(event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(foreground="grey")

    def on_radio_button_change():
        selected_value = radio_var.get()
        print("selected gender: ", selected_value)
        global gender
        gender = selected_value
        print(f"Selected option: {selected_value}")

    def makinghistory(m,y,passengernames,selected_seats,depart,to,dateop):
        if ph.get() == "Phone Number" or email.get() == "Email ID eg: user@gmail.com":
            messagebox.showerror("Error", "Enter proper contact details")
            return
        elif ph.get() != "Phone Number" and email.get() != "Email ID eg: user@gmail.com":
            seating = ""
            for i in selected_seats:
                seating += i + ","
            add_booking_record(m,y,passengernames,seating,depart,to,dateop)
        print(m,y,passengernames,selected_seats,depart,to,dateop)
        passengernames = ""
    
    radio_var = a.StringVar()
    global gender
    gender = "0"
    global passengernames
    passengernames = ""
    global passs
    passs = 1

    def passengerdetails(y):
        global passs
        global gender
        global passengernames
        if passs == int(y):
            fir,las = first.get(),last.get()
            passengernames = passengernames + "," + gender + fir + las
            print(gender,fir,las)
            print("Disabling button")  # Debug print
            passengerbut.configure(state = "disabled")
            booking.configure(state="normal")
        else:
            fir,las = first.get(),last.get()
            passengernames = passengernames + "," + gender + fir + las
            print(gender,fir,las)
            passs += 1
            button_text.set(f"Add Passenger {passs} of {y}")
            first.delete(0, END)  # Clear the entry before inserting new text
            first.insert(0, "First Name")
            last.delete(0, END)  # Clear the entry before inserting new text
            last.insert(0, "Last Name")

    bm = a.CTkFrame(ct, fg_color="white", width=580, height=580, border_color="black", border_width=1)
    bm.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    bm.grid_columnconfigure((0, 1, 2), weight=1)
    bm.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    global selected_seats
    selected_seats = []
    #booking panel 
    def seatbooking():
        global selected_seats, seating_frame
        def create_seat_selection(num_seats=70, max_selectable_seats=1):
            global selected_seats
            if e == "First Class":
                row = 6
                col = 5
                butsize = 30
                letters = "AB DE"
                num_seats = butsize
            elif e == "Business Class":
                row = 6
                col = 3
                butsize = 40
                letters = "A B"
                num_seats = 10
            else:
                row = 10
                col = 7
                butsize = 20
                letters = "ABC DEF"  # 7 columns, so using 7 letters
            selected_seats = []
            buttons = []  # List to store buttons and seat numbers

            frame = a.CTkFrame(seating_frame, width=180, height=288, fg_color="white")
            frame.grid(column=0, row=1, pady=2, padx=3, sticky="ns")

            rows = num_seats // 10 + (num_seats % 10 != 0)

            for i in range(row):  # 10 rows
                for j in range(col):  # 7 columns
                    seat_number = letters[j] + str(i + 1)
                    if seat_number in selected_seats:
                        btn = a.CTkButton(
                            frame, text=seat_number, 
                            width=butsize, height=butsize, fg_color="green", text_color="black", 
                            font=("Arial", 10), hover_color="#4582ec", corner_radius=4, 
                            border_color="black", border_width=1
                        )
                        btn.configure(command=lambda btn=btn, sn=seat_number: select_seat(btn, sn, selected_seats, max_selectable_seats, buttons))
                        btn.grid(row=i, column=j, padx=6, pady=4, sticky="nsew")
                        buttons.append((btn, seat_number))
                    elif j == (col//2):
                        seat_number = letters[j] + str(i + 1)
                        btnn = a.CTkButton(frame, text=" ", width=butsize, height=butsize, fg_color="white")
                        btnn.grid(row=i, column=j, padx=8, pady=4,sticky = "nsew")
                        btnn.configure(state="disabled")
                    elif len(selected_seats) >= num_seats:
                        break
                    elif j != (col//2):
                        btn = a.CTkButton(
                            frame, text=seat_number, 
                            width=butsize, height=butsize, fg_color="white", text_color="black", 
                            font=("Arial", 10), hover_color="#4582ec", corner_radius=4, 
                            border_color="black", border_width=1
                        )
                        btn.configure(command=lambda btn=btn, sn=seat_number: select_seat(btn, sn, selected_seats, max_selectable_seats, buttons))
                        btn.grid(row=i, column=j, padx=6, pady=4, sticky="nsew")
                        buttons.append((btn, seat_number))
            
        
        def select_seat(seat_button, seat_number, selected_seats, max_seats, buttons):
            if seat_number in selected_seats:
                selected_seats.remove(seat_number)
                seat_button.configure(fg_color="white")  # Deselect the seat
            elif len(selected_seats) < int(max_seats):
                selected_seats.append(seat_number)
                seat_button.configure(fg_color="#02b875")  # Select the seat

            if len(selected_seats) >= int(max_seats):
                for btn, num in buttons:
                    if num not in selected_seats:
                        btn.configure(state="disabled")  # Disable unselected seats
                        finalseat_but.configure(state="normal")
            else:
                for btn, num in buttons:
                    if num not in selected_seats:
                        btn.configure(state="normal")  # Enable unselected seats

        ct.geometry("890x600")

        
        seating_frame = a.CTkFrame(bm, fg_color="white", width=300, height=580, border_color="black", border_width=1, corner_radius=5)
        seating_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns", rowspan=6)
        seating_frame.grid_propagate(False)
        seating_frame.grid_columnconfigure(0, weight=1)
        seating_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        def finalseating():
            print("Selected seats are:", selected_seats)

        test = a.CTkLabel(seating_frame, text="Seating Plan", font=("Arial", 20))
        test.grid(column = 0,row=0,padx=4,pady=2)

        finalseat_but = b.Button(seating_frame, text="Finalise Seating",style = "success",command = finalseating)
        finalseat_but.grid(column = 0,row=2,padx=4,pady=2,sticky = "ew")
        finalseat_but.configure(state="disabled")
        create_seat_selection(num_seats=70, max_selectable_seats=y)

    # Function to create seats
    
            
    lab = a.CTkFrame(bm, fg_color="transparent")
    lab.grid(row=0, column=1, padx=5, pady=5, sticky="ew", columnspan=2)
    lab.grid_rowconfigure((0, 1, 2), weight=1)
    lab.grid_columnconfigure(0, weight=1)
    custd = a.CTkLabel(lab, text="Enter Passenger Details", text_color="black", font=("Arial", 14))
    custd.grid(row=0, column=0, padx=5, pady=0, sticky="w")
    cc = f"ADD ADULT {y}"
    custcount = a.CTkLabel(lab, text=cc, text_color="black", font=("Arial", 14))
    custcount.grid(row=1, column=0, padx=5, pady=2, sticky="w")
    nameframe = b.Labelframe(bm, text="Enter name as per Aadhaar card/ Passport or any Govt. ID")
    nameframe.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
    nameframe.grid_columnconfigure((0, 1), weight=1)
    nameframe.grid_rowconfigure((0, 1, 2, 3), weight=1)
    gensub = a.CTkFrame(nameframe, fg_color="transparent")
    gensub.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    gensub.grid_columnconfigure((0, 1, 3), weight=1)
    gensub.grid_rowconfigure(0, weight=1)
    gen1 = a.CTkRadioButton(gensub, text="Mr", text_color="black", value="Mr", variable=radio_var, command=on_radio_button_change)
    gen1.grid(row=0, column=0, padx=5, pady=5)
    gen2 = a.CTkRadioButton(gensub, text="Ms", text_color="black", value="Ms", variable=radio_var, command=on_radio_button_change)
    gen2.grid(row=0, column=1, padx=5, pady=5)
    gen3 = a.CTkRadioButton(gensub, text="Mrs", text_color="black", value="Mrs", variable=radio_var, command=on_radio_button_change)
    gen3.grid(row=0, column=2, padx=5, pady=5)
    first = b.Entry(nameframe, style="primary")
    first.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    first.insert(0, "First Name")
    first.bind("<FocusIn>", lambda event: on_entry_click(event, first, "First Name"))
    first.bind("<FocusOut>", lambda event: on_focus_out(event, first, "First Name"))
    last = b.Entry(nameframe, style="primary")
    last.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    last.insert(0, "Last Name")
    last.bind("<FocusIn>", lambda event: on_entry_click(event, last, "Last Name"))
    last.bind("<FocusOut>", lambda event: on_focus_out(event, last, "Last Name"))

    # Create the StringVar and Button
    button_text = StringVar()
    button_text.set(f"Add Passenger {passs} of {y}")
    passengerbut = b.Button(nameframe, textvariable=button_text, command=lambda: passengerdetails(y), style="primary")
    passengerbut.grid(row=2, column=1, padx=5, pady=5)

    contframe = b.Labelframe(bm, text="")
    contframe.grid(row=3, column=1, padx=5, pady=2, sticky="ew")
    contframe.grid_columnconfigure((1, 2), weight=1)
    contframe.grid_columnconfigure(0, weight=0)
    contframe.grid_rowconfigure((0,1,2), weight=1)
    cont = a.CTkLabel(contframe, text="Contact Details", text_color="black", font=("Arial", 14))
    cont.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    ph = b.Entry(contframe, style="primary")
    ph.grid(row=1, column=1, padx=2, pady=5, sticky="ew")
    ph.insert(0, "Phone Number")
    ph.bind("<FocusIn>", lambda event: on_entry_click(event, ph, "Phone Number"))
    ph.bind("<FocusOut>", lambda event: on_focus_out(event, ph, "Phone Number"))
    email = b.Entry(contframe, style="primary")
    email.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    email.insert(0, "Email ID eg: user@gmail.com")
    email.bind("<FocusIn>", lambda event: on_entry_click(event, email, "Email ID eg: user@gmail.com"))
    email.bind("<FocusOut>", lambda event: on_focus_out(event, email, "Email ID eg: user@gmail.com"))
    ph9 = a.CTkEntry(contframe, placeholder_text="+91", width=35, height=15, fg_color="white", text_color="black", border_width=1, border_color="blue")
    ph9.grid(row=1, column=0, padx=2, pady=5)#4582ec
    ph9.configure(state="readonly")
 
    seating_frame = a.CTkFrame(bm, fg_color="transparent")
    seating_frame.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    seating_frame.grid_columnconfigure((0, 1), weight=1)
    seating_frame.grid_rowconfigure((0), weight=1)
    seatlabel = a.CTkLabel(seating_frame, text="Select Seating Arrangement", text_color="black")
    seatlabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    seat = b.Button(seating_frame, text="Select Seating",style = "success.outline",command=seatbooking)
    seat.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    booking = b.Button(bm, text="Book Flight", command= lambda:makinghistory(m,y,passengernames,selected_seats,depart,to,dateop), style="success")
    booking.configure(state="disabled")
    booking.grid(row=5, column=1, padx=10, pady=5, sticky="ew")


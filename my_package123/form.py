from tkinter import StringVar, END
import ttkbootstrap as b
from tkinter import messagebox

def formop(a, b, c, d, x, y,m):
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

    def makinghistory(m,y,passengernames):
        if ph.get() == "Phone Number" or email.get() == "Email ID eg: user@gmail.com":
            messagebox.showerror("Error", "Enter proper contact details")
            return
        elif ph.get() != "Phone Number" and email.get() != "Email ID eg: user@gmail.com":
            add_booking_record(m,y,passengernames)
    
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
            passengernames = ""
        else:
            fir,las = first.get(),last.get()
            passengernames = passengernames + "," + gender + fir + las
            print(gender,fir,las)
            passs += 1
            button_text.set(f"Add Passenger {passs} of {y}")
            first.delete(0, END)  # Clear the entry before inserting new text
            first.insert(0, "First Name")

    bm = a.CTkFrame(ct, fg_color="white", width=580, height=580, border_color="black", border_width=1)
    bm.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    bm.grid_columnconfigure((0, 1, 2), weight=1)
    bm.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

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
    contframe.grid_rowconfigure((1, 2), weight=1)
    cont = a.CTkLabel(bm, text="Contact Details", text_color="black", font=("Arial", 14))
    cont.grid(row=2, column=1, padx=5, pady=5, sticky="w")
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
    ph9.grid(row=1, column=0, padx=2, pady=5)
    ph9.configure(state="readonly")
    booking = b.Button(bm, text="Book Flight", command= lambda: makinghistory(m,y,passengernames), style="success")
    booking.configure(state="disabled")
    booking.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Call your formop function with the necessary arguments
# This is just an example, you'll need to pass the correct parameters
# formop(a, b, c, d, x, y)

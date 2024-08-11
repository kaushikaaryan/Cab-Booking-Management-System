from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

user_names = ["Admin", ""]
passwords = {"Admin": "admin"}
options = [
    "None",
    "Phagwara to LPU",
    "Phagwara to Ramamandi",
    "Phagwara to Satnampura",
    "Phagwara to Ludhiana",
    "Phagwara to Phillaur",
    "Phagwara to Chandigarh",
    "Phagwara to Jalandhar",
    "Phagwara to Amritsar",
    "Phagwara to Deepnagar",
    "Phagwara to kirthinagar",
    "Phagwara to Law Gate",
    "Phagwara to Hargobindnagar"
]
rates = {
    "Phagwara to LPU": "100",
    "Phagwara to Ramamandi": "80",
    "Phagwara to Satnampura": "80",
    "Phagwara to Ludhiana": "150",
    "Phagwara to Phillaur": "120",
    "Phagwara to Chandigarh": "300",
    "Phagwara to Jalandhar": "200",
    "Phagwara to Amritsar": "300",
    "Phagwara to Deepnagar": "150",
    "Phagwara to kirthinagar": "80",
    "Phagwara to Law Gate": "120",
    "Phagwara to Hargobindnagar": "80",

}

root = Tk()
root.geometry("700x450+300+100")
root.title("Main Screen")

# for login
username1 = StringVar()
password1 = StringVar()

# for new user
gender_box = IntVar()
username2 = StringVar()
password2 = StringVar()
name = StringVar()
mobile_no = StringVar()
Email_id = StringVar()

# for options
options_var = StringVar()

mobile_no_entry_text = StringVar()
day_entry_text = StringVar()
time_entry_text = StringVar()


def show_rate(child1):
    a = str(options_var.get())
    rate = rates[a]
    lbl_fare_1 = Label(child1, text=rate, font='Times 18 bold')
    lbl_fare_1.place(relx=.6, rely=.45, anchor=CENTER)

#------------------------------------for booking-----------------------------------------------
def show_msg_booking():
    mob = str(mobile_no_entry_text.get())
    day = str(day_entry_text.get())
    time = str(time_entry_text.get())

    if mob != "" and day != "" and time != "":
        messagebox.showinfo("Booking Successful", "Booking Successful")
    else:
        messagebox.showerror("ERROR", "Mobile number or day or time is not filled")

#--------------------------------------create account---------------------------------------------
def create_new_user():
    user_new = username2.get()
    pass_new = password2.get()
    gender = gender_box.get()
    name_new = name.get()
    mob = mobile_no.get()
    email_new = Email_id.get()

    if user_new != "" and pass_new != "" and (gender != 1 or gender != 2) and name_new != "" and mob != "" \
            and email_new != "":
        user_names[1] = user_new
        new_user_created = {user_new: pass_new}
        passwords.update(new_user_created)
        messagebox.showinfo("Successful", "New User Created successfully")
    else:
        messagebox.showerror("ERROR", "One or more field is empty")


def new_user():
    root_child_1 = Toplevel(root)
    root_child_1.title("New User")
    root_child_1.geometry("700x450+300+100")

    lbl2 = Label(root_child_1, text="Register for New Account", font='Times 30 bold')
    lbl2.place(relx=.5, rely=.1, anchor=CENTER)

    lbl_username = Label(root_child_1, text='Username :', font='Times 18 bold')
    lbl_username.place(relx=.3, rely=.25, anchor=CENTER)
    username_entry = Entry(root_child_1, textvariable=username2, width=35)
    username_entry.place(relx=.6, rely=.25, anchor=CENTER)

    lbl_password = Label(root_child_1, text='Password :', font='Times 18 bold')
    lbl_password.place(relx=.3, rely=.35, anchor=CENTER)
    password_entry = Entry(root_child_1, show="*", textvariable=password2, width=35)
    password_entry.place(relx=.6, rely=.35, anchor=CENTER)

    lbl_name = Label(root_child_1, text='Name :', font='Times 18 bold')
    lbl_name.place(relx=.3, rely=.45, anchor=CENTER)
    name_entry = Entry(root_child_1, textvariable=name, width=35)
    name_entry.place(relx=.6, rely=.45, anchor=CENTER)

    lbl_gender = Label(root_child_1, text='Gender :', font='Times 18 bold')
    lbl_gender.place(relx=.3, rely=.55, anchor=CENTER)

    gender1 = Radiobutton(root_child_1, text='Male', variable=gender_box, value=1)
    gender1.place(relx=.5, rely=.55, anchor=CENTER)
    gender2 = Radiobutton(root_child_1, text='Female', variable=gender_box, value=2)
    gender2.place(relx=.6, rely=.55, anchor=CENTER)

    lbl_mobile = Label(root_child_1, text='Mobile no. :', font='Times 18 bold')
    lbl_mobile.place(relx=.3, rely=.65, anchor=CENTER)
    mobile_no_entry = Entry(root_child_1, textvariable=mobile_no, width=35)
    mobile_no_entry.place(relx=.6, rely=.65, anchor=CENTER)

    lbl_email = Label(root_child_1, text='Email ID :', font='Times 18 bold')
    lbl_email.place(relx=.3, rely=.75, anchor=CENTER)
    email_entry = Entry(root_child_1, textvariable=Email_id, width=35)
    email_entry.place(relx=.6, rely=.75, anchor=CENTER)

    submit_btn1 = Button(root_child_1, text='Create', command=lambda: [create_new_user()])
    submit_btn1.place(relx=.6, rely=.9, anchor=CENTER, height=40, width=70)

    exit_btn2 = Button(root_child_1, text='Exit', command=lambda: [root_child_1.destroy()])
    exit_btn2.place(relx=.7, rely=.9, anchor=CENTER, height=40, width=70)

    root_child_1.mainloop()

#---------------------------------------------login----------------------------------------
def login_button():
    user1 = username1.get()
    user1 = str(user1)
    pass1 = password1.get()
    pass1 = str(pass1)

    a = "1"
    for x in user_names:
        if user1 == x:
            a = x

    if a == user1 and passwords[a] == pass1:
        root_child_1 = Toplevel(root)
        root_child_1.title("Booking Request")
        root_child_1.geometry("700x450+300+100")

        lbl5 = Label(root_child_1, text="Book your ride", font='Times 30 bold')
        lbl5.place(relx=.5, rely=.1, anchor=CENTER)

        mobile_no_booking = Label(root_child_1, text='Mobile no :', font='Times 18 bold')
        mobile_no_booking.place(relx=.3, rely=.25, anchor=CENTER)
        mobile_no_booking_entry = Entry(root_child_1, textvariable=mobile_no_entry_text, width=35)
        mobile_no_booking_entry.place(relx=.6, rely=.25, anchor=CENTER)
        lbl_routes = Label(root_child_1, text='Select Route :', font='Times 18 bold')
        lbl_routes.place(relx=.3, rely=.35, anchor=CENTER)
        routes = OptionMenu(root_child_1, options_var, *options)
        routes.place(relx=.55, rely=.35, anchor=CENTER)
        rate_btn = Button(root_child_1, text="Check fare", command=lambda: [show_rate(root_child_1)])
        rate_btn.place(relx=.75, rely=.35, anchor=CENTER)
        fare = Label(root_child_1, text='Fare in Rs. :', font='Times 18 bold')
        fare.place(relx=.3, rely=.45, anchor=CENTER)
        day = Label(root_child_1, text='Day :', font="Times 18 bold")
        day.place(relx=.3, rely=.55, anchor=CENTER)
        day_entry = Entry(root_child_1, textvariable=day_entry_text, width=25)
        day_entry.place(relx=.55, rely=.55, anchor=CENTER)
        day_format = Label(root_child_1, text='Format dd/mm', font="Times 10 italic")
        day_format.place(relx=.8, rely=.55, anchor=CENTER)

        time = Label(root_child_1, text='Time :', font="Times 18 bold")
        time.place(relx=.3, rely=.65, anchor=CENTER)
        time_entry = Entry(root_child_1, textvariable=time_entry_text, width=25)
        time_entry.place(relx=.55, rely=.65, anchor=CENTER)
        time_format = Label(root_child_1, text='Format HH AM/PM', font="Times 10 italic")
        time_format.place(relx=.8, rely=.65, anchor=CENTER)

        submit_btn1 = Button(root_child_1, text='Book', command=lambda: [show_msg_booking()])
        submit_btn1.place(relx=.6, rely=.75, anchor=CENTER, height=40, width=70)

        exit_btn3 = Button(root_child_1, text='Exit', command=lambda: [root_child_1.destroy()])
        exit_btn3.place(relx=.7, rely=.75, anchor=CENTER, height=40, width=70)

        root_child_1.mainloop()
    else:
        messagebox.showerror("ERROR", "Wrong Username or Password")


def login():
    root_child_1 = Toplevel(root)
    root_child_1.title("Login")
    root_child_1.geometry("700x450+300+100")

    lbl3 = Label(root_child_1, text="Please login to book a cab", font='Times 30 bold')
    lbl3.place(relx=.5, rely=.25, anchor=CENTER)

    lbl_username = Label(root_child_1, text='Username :', font='Times 20 bold')
    lbl_username.place(relx=.3, rely=.45, anchor=CENTER)
    username_entry = Entry(root_child_1, textvariable=username1, width=35)
    username_entry.place(relx=.6, rely=.45, anchor=CENTER)

    lbl_password = Label(root_child_1, text='Password :', font='Times 20 bold')
    lbl_password.place(relx=.3, rely=.55, anchor=CENTER)
    password_entry = Entry(root_child_1, show="*", textvariable=password1, width=35)
    password_entry.place(relx=.6, rely=.55, anchor=CENTER)

    lbl_new_user = Label(root_child_1, text="Don't have account", font='Times 10 italic')
    lbl_new_user.place(relx=.3, rely=.65, anchor=CENTER)
    register_btn = Button(root_child_1, text='Register here', command=lambda: [new_user()])
    register_btn.place(relx=.3, rely=.7, anchor=CENTER, height=25, width=100)

    submit_btn1 = Button(root_child_1, text='Login', command=lambda: [login_button()])
    submit_btn1.place(relx=.6, rely=.7, anchor=CENTER, height=40, width=70)

    exit_btn3 = Button(root_child_1, text='Exit', command=lambda: [root_child_1.destroy()])
    exit_btn3.place(relx=.7, rely=.7, anchor=CENTER, height=40, width=70)

    root_child_1.mainloop()

#-------------------------------------------------available routes---------------------
def available_route():
    root_child_1 = Toplevel(root)
    root_child_1.title("Available Routes")
    root_child_1.geometry("700x600+300+50")

    lbl4 = Label(root_child_1, text='Available Routes', font='Times 30 bold underline')
    lbl4.place(relx=.5, rely=.05, anchor=CENTER)
    lbl_routes = Label(root_child_1, text='Routes', font='Times 25 bold')
    lbl_routes.place(relx=.25, rely=.13, anchor=CENTER)
    lbl_fare = Label(root_child_1, text='Fare in Rs.', font='Times 25 bold')
    lbl_fare.place(relx=.75, rely=.13, anchor=CENTER)

    ja_ph = Label(root_child_1, text='Phagwara to LPU', font='Times 19 bold')
    ja_ph.place(relx=.25, rely=.2, anchor=CENTER)
    ja_ph_rate = Label(root_child_1, text='100', font='Times 19 bold')
    ja_ph_rate.place(relx=.75, rely=.2, anchor=CENTER)

    ja_am = Label(root_child_1, text='Phagwara to Ramamandi', font='Times 19 bold')
    ja_am.place(relx=.25, rely=.25, anchor=CENTER)
    ja_am_rate = Label(root_child_1, text='80', font='Times 19 bold')
    ja_am_rate.place(relx=.75, rely=.25, anchor=CENTER)

    ja_lu = Label(root_child_1, text='Phagwara to Satnampura', font='Times 19 bold')
    ja_lu.place(relx=.25, rely=.3, anchor=CENTER)
    ja_lu_rate = Label(root_child_1, text='80', font='Times 19 bold')
    ja_lu_rate.place(relx=.75, rely=.3, anchor=CENTER)

    ph_ja = Label(root_child_1, text='Phagwara to Ludhiana', font='Times 19 bold')
    ph_ja.place(relx=.25, rely=.4, anchor=CENTER)
    ph_ja_rate = Label(root_child_1, text='150', font='Times 19 bold')
    ph_ja_rate.place(relx=.75, rely=.4, anchor=CENTER)

    ph_am = Label(root_child_1, text='Phagwara to Phillaur', font='Times 19 bold')
    ph_am.place(relx=.25, rely=.45, anchor=CENTER)
    ph_am_rate = Label(root_child_1, text='120', font='Times 19 bold')
    ph_am_rate.place(relx=.75, rely=.45, anchor=CENTER)

    ph_lu = Label(root_child_1, text='Phagwara to Chandigarh', font='Times 19 bold')
    ph_lu.place(relx=.25, rely=.5, anchor=CENTER)
    ph_lu_rate = Label(root_child_1, text='300', font='Times 19 bold')
    ph_lu_rate.place(relx=.75, rely=.5, anchor=CENTER)

    am_ja = Label(root_child_1, text='Phagwara to Jalandhar', font='Times 19 bold')
    am_ja.place(relx=.25, rely=.6, anchor=CENTER)
    am_ja_rate = Label(root_child_1, text='200', font='Times 19 bold')
    am_ja_rate.place(relx=.75, rely=.6, anchor=CENTER)

    am_ph = Label(root_child_1, text='Phagwara to Amritsar', font='Times 19 bold')
    am_ph.place(relx=.25, rely=.65, anchor=CENTER)
    am_ph_rate = Label(root_child_1, text='300', font='Times 19 bold')
    am_ph_rate.place(relx=.75, rely=.65, anchor=CENTER)

    am_lu = Label(root_child_1, text='Phagwara to Deepnagar', font='Times 19 bold')
    am_lu.place(relx=.25, rely=.7, anchor=CENTER)
    am_lu_rate = Label(root_child_1, text='150', font='Times 19 bold')
    am_lu_rate.place(relx=.75, rely=.7, anchor=CENTER)

    lu_ja = Label(root_child_1, text='Phagwara to kirthinagar', font='Times 19 bold')
    lu_ja.place(relx=.25, rely=.8, anchor=CENTER)
    lu_ja_rate = Label(root_child_1, text='80', font='Times 19 bold')
    lu_ja_rate.place(relx=.75, rely=.8, anchor=CENTER)

    lu_ph = Label(root_child_1, text='Phagwara to Law Gate', font='Times 19 bold')
    lu_ph.place(relx=.25, rely=.85, anchor=CENTER)
    lu_ph_rate = Label(root_child_1, text='120', font='Times 19 bold')
    lu_ph_rate.place(relx=.75, rely=.85, anchor=CENTER)

    lu_am = Label(root_child_1, text='Phagwara to Hargobindnagar', font='Times 19 bold')
    lu_am.place(relx=.25, rely=.9, anchor=CENTER)
    lu_am_rate = Label(root_child_1, text='80', font='Times 19 bold')
    lu_am_rate.place(relx=.75, rely=.9, anchor=CENTER)

    exit_btn4 = Button(root_child_1, text='Exit', command=lambda: [root_child_1.destroy()])
    exit_btn4.place(relx=.9, rely=.95, anchor=CENTER, height=40, width=70)

    root_child_1.mainloop()


lbl1 = Label(root, text="Welcome to Cab Booking System", font='Times 30 bold')
lbl1.place(relx=.5, rely=.25, anchor=CENTER)

login_btn = Button(root, text="Login", command=lambda: [login()])
login_btn.place(relx=.3, rely=.5, anchor=CENTER, height=40, width=70)
new_user_btn = Button(root, text='New User', command=lambda: [new_user()])
new_user_btn.place(relx=.5, rely=.5, anchor=CENTER, height=40, width=75)
avail_routes_btn = Button(root, text='Available Routes', command=lambda: [available_route()])
avail_routes_btn.place(relx=.7, rely=.5, anchor=CENTER, height=40, width=100)
exit_btn1 = Button(root, text='Exit', command=lambda: [root.destroy()])
exit_btn1.place(relx=.5, rely=.7, anchor=CENTER, height=40, width=70)

mainloop()
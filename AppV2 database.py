import tkinter as tk
import sqlite3
from PIL import ImageTk, Image
from tkinter import colorchooser
from tkcalendar import Calendar
import datetime
from tkinter import messagebox

# Create connection with database
connect = sqlite3.connect('Tickify.db')
cursor = connect.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS USER(
               user_id integer primary key autoincrement not null,
               user_name varchar not null,
               user_email varchar not null,
               user_password varchar not null)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS TASK(
               task_id integer primary key autoincrement not null,
               user_id integer not null references USER(user_id),
               task_title varchar not null,
               task_description varchar default null,
               task_status varchar default 'pending',
               task_duedate varchar default null,
               task_priority integer not null,
               task_color varchar not null,
               created_time varchar not null)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS REMINDER(
               reminder_id integer primary key autoincrement not null,
               task_id integer not null references TASK(task_id),
               reminder_date varchar default null,
               reminder_time varchar default null)''')


# Insert SignUp Data into USER (Database)
def database_signup():
    user_name = username2_entry.get()
    user_email = email2_entry.get()
    user_password = password2_entry.get()

    # Insert value into table USER
    cursor.execute('''INSERT INTO USER(user_name, user_email, user_password)
                   VALUES(?, ?, ?)''', (user_name, user_email, user_password))

    # Commit changes
    connect.commit()


########################################
# Event for Entry (Welcome Window)
def insert_username1():
    if username1_entry.cget('fg') == '#8D93AB':
        username1_entry.delete(0, tk.END)
        username1_entry.config(fg='#363636')


def leave_username1():
    username1_entry.get()
    if username1_entry.get() == '':
        username1_entry.insert(0, 'Username')
        username1_entry.config(fg='#8D93AB')


def insert_password1():
    if password1_entry.cget('fg') == '#8D93AB':
        password1_entry.delete(0, tk.END)
        password1_entry.config(fg='#363636')

        show_password1()


def leave_password1():
    password1_entry.get()
    if password1_entry.get() == '':
        password1_entry.insert(0, 'Password')
        password1_entry.config(fg='#8D93AB')

    show_password1()


def show_password1():
    if show_password1_var.get() == 1 or password1_entry.cget('fg') == '#8D93AB':
        password1_entry.config(show='')
    elif show_password1_var.get() == 0 and password1_entry.cget('fg') == '#363636':
        password1_entry.config(show='*')


def insert_username2():
    username2_entry.delete(0, tk.END)
    username2_entry.config(fg='#363636')


def leave_username2():
    username2_entry.get()
    if username2_entry.get() == '':
        username2_entry.insert(0, 'Username')
        username2_entry.config(fg='#8D93AB')


def insert_email2():
    email2_entry.delete(0, tk.END)
    email2_entry.config(fg='#363636')


def leave_email2():
    email2_entry.get()
    if email2_entry.get() == '':
        email2_entry.insert(0, 'Email')
        email2_entry.config(fg='#8D93AB')


def insert_password2():
    password2_entry.delete(0, tk.END)
    password2_entry.config(fg='#363636')

    show_password2()


def leave_password2():
    password2_entry.get()
    if password2_entry.get() == '':
        password2_entry.insert(0, 'Password')
        password2_entry.config(fg='#8D93AB')

    show_password2()


def insert_confirmed_password2():
    confirmed_password2_entry.delete(0, tk.END)
    confirmed_password2_entry.config(fg='#363636')

    show_password2()


def leave_confirmed_password2():
    confirmed_password2_entry.get()
    if confirmed_password2_entry.get() == '':
        confirmed_password2_entry.insert(0, 'Confirmed Password')
        confirmed_password2_entry.config(fg='#8D93AB')

    show_password2()


def show_password2():
    condition1 = password2_entry.cget('fg') == '#8D93AB' and confirmed_password2_entry.cget('fg') == '#8D93AB'
    condition2 = password2_entry.cget('fg') == '#363636' and confirmed_password2_entry.cget('fg') == '#363636'
    condition3 = password2_entry.cget('fg') == '#8D93AB' and confirmed_password2_entry.cget('fg') == '#363636'
    condition4 = password2_entry.cget('fg') == '#363636' and confirmed_password2_entry.cget('fg') == '#8D93AB'
    if show_password2_var.get() == 1 and (condition4 or condition2 or condition1 or condition3):
        password2_entry.config(show='')
        confirmed_password2_entry.config(show='')
    elif show_password2_var.get() == 0 and condition4:
        password2_entry.config(show='*')
        confirmed_password2_entry.config(show='')
    elif show_password2_var.get() == 0 and condition3:
        password2_entry.config(show='')
        confirmed_password2_entry.config(show='*')
    elif show_password2_var.get() == 0 and condition2:
        password2_entry.config(show='*')
        confirmed_password2_entry.config(show='*')
    elif show_password2_var.get() == 0 and condition1:
        password2_entry.config(show='')
        confirmed_password2_entry.config(show='')


########################################
# Switching
def clear_login1_frame():
    username1_entry.delete(0, tk.END)
    username1_entry.insert(0, 'Username')
    username1_entry.config(fg='#8D93AB')

    password1_entry.delete(0, tk.END)
    password1_entry.insert(0, 'Password')
    password1_entry.config(fg='#8D93AB', show='')

    show_password1_var.set(False)
    show_password1()

    error1_label.config(text='')


def clear_signup2_frame():
    username2_entry.delete(0, tk.END)
    username2_entry.insert(0, 'Username')
    username2_entry.config(fg='#8D93AB')

    email2_entry.delete(0, tk.END)
    email2_entry.insert(0, 'Email')
    email2_entry.config(fg='#8D93AB')

    password2_entry.delete(0, tk.END)
    password2_entry.insert(0, 'Password')
    password2_entry.config(fg='#8D93AB', show='')

    confirmed_password2_entry.delete(0, tk.END)
    confirmed_password2_entry.insert(0, 'Confirmed Password')
    confirmed_password2_entry.config(fg='#8D93AB', show='')

    show_password2_var.set(False)
    show_password2()

    error2_label.config(text='')


def switch_signup2_frame():
    clear_login1_frame()
    start0_frame.place_forget()
    login1_frame.place_forget()
    signup2_frame.place(relx=0.5, rely=0.5, anchor='center')
    signup2_frame.focus_set()


def switch_login1_frame():
    clear_signup2_frame()
    start0_frame.place_forget()
    signup2_frame.place_forget()
    login1_frame.place(relx=0.5, rely=0.5, anchor='center')
    login1_frame.focus_set()

    signup_success_window.withdraw()


def switch_main_window():
    user_name = username1_entry.get()
    user_password = password1_entry.get()
    cursor.execute('SELECT * FROM USER WHERE user_email=? AND user_password=?', (user_name, user_password))
    login_data = cursor.fetchone()
    if login_data:
        username4_label.config(text=user_name)
        welcome_window.withdraw()
        main_window.deiconify()
        show_tasks() 
        add_task4()    
    else:
        error1_label.config(text='Incorrect Username or Password')


def sign_out():
    clear_login1_frame()
    login1_frame.place_forget()
    start0_frame.place(relx=0.5, rely=0.5, anchor='center')
    welcome_window.deiconify()
    main_window.withdraw()


def successful_submit():
    cursor.execute('SELECT user_name FROM USER WHERE user_name = ?', (username2_entry.get(),))
    existing_username = cursor.fetchone()[0]
    c1 = password2_entry.get() == confirmed_password2_entry.get()
    c2 = password2_entry.cget('fg') == '#363636' and confirmed_password2_entry.cget('fg') == '#363636'
    c3 = username2_entry.cget('fg') == '#363636' and username2_entry.get() != ''
    c4 = email2_entry.cget('fg') == '#363636' and email2_entry.get() != ''
    c5 = existing_username
    if c1 and c2 and c3 and c4 and not c5:
        # Show SignUp Successfully Window
        signup_success_window.deiconify()
        error2_label.config(text='')
        database_signup()
    elif c4 and c3 and c2 and not c1:
        error2_label.config(text='Password does not match')
    elif c4 and c3 and c2 and c1 and c5:
        error2_label.config(text='Username exists, please try another one')
    else:
        error2_label.config(text='Please fill in all the details')


########################################
# Welcome Window
welcome_window = tk.Tk()
welcome_window.title('Tickify')
welcome_window.geometry('800x500')
welcome_window.configure(bg='#F5F5F5')
welcome_window.iconphoto(True, tk.PhotoImage(file='C:/Users/sheal/Downloads/ti/Tickify_Icon16.png'))

# 0 - Start Frame
start0_frame = tk.Frame(welcome_window, height=490, width=700, bg='#F5F5F5')
start0_frame.place(relx=0.5, rely=0.5, anchor='center')

# Tickify Logo (Start Frame)
logo0_image = Image.open('C:/Users/sheal/Downloads/ti/Tickify_Logo.png')
logo0_resize_image = logo0_image.resize((300, 300), Image.LANCZOS)
logo0_tk_image = ImageTk.PhotoImage(logo0_resize_image)

logo0_label = tk.Label(start0_frame, image=logo0_tk_image, width=300, height=300, bg='#F5F5F5')
logo0_label.place(x=50, y=80)

# Frame Right Hand Side Widgets (Start Frame)
right0_frame = tk.Frame(start0_frame, height=400, width=300, bg='#F5F5F5')
right0_frame.place(x=370, y=45)

# Start Text (Start Frame)
start0_label = tk.Label(right0_frame, text='Start Manage', font=('Arial', 24), bg='#F5F5F5', fg='#363636')
start0_label.place(x=52, y=50)

your0_label = tk.Label(right0_frame, text='Your Task With', font=('Arial', 24), bg='#F5F5F5', fg='#363636')
your0_label.place(x=38, y=90)

tickify0_label = tk.Label(right0_frame, text='Tickify', font=('Arial', 24), bg='#F5F5F5', fg='#9BA3EB')
tickify0_label.place(x=100, y=130)

# LogIn & SignUp Button (Start Frame)
login0_button = tk.Button(right0_frame, text='LOG IN', font=('Arial', 10), width=25, height=2,
                          fg='#FFFFFF', bg='#9BA3EB', command=switch_login1_frame)
login0_button.place(x=46, y=225)

signup0_button = tk.Button(right0_frame, text='SIGN UP', font=('Arial', 10), width=25, height=2,
                           fg='#FFFFFF', bg='#9BA3EB', command=switch_signup2_frame)
signup0_button.place(x=46, y=280)

# 1 - LogIn Frame
login1_frame = tk.Frame(welcome_window, height=490, width=700, bg='#F5F5F5', takefocus=True)
login1_frame.bind('<Return>', lambda event: switch_main_window())

# Tickify Logo (LogIn Frame)
logo1_image = Image.open('C:/Users/sheal/Downloads/ti/Tickify_Logo.png')
logo1_resize_image = logo1_image.resize((300, 300), Image.LANCZOS)
logo1_tk_image = ImageTk.PhotoImage(logo1_resize_image)

logo1_label = tk.Label(login1_frame, image=logo1_tk_image, width=300, height=300, bg='#F5F5F5')
logo1_label.place(x=50, y=80)

# Frame Right Hand Side Widgets (LogIn Frame)
right1_frame = tk.Frame(login1_frame, height=400, width=300, bg='#F5F5F5')
right1_frame.place(x=370, y=45)

# Hello & Welcome text (LogIn Frame)
hello1_label = tk.Label(right1_frame, text='Hello Again!', font=('Arial', 20), bg='#F5F5F5', fg='#363636')
hello1_label.place(x=68, y=30)

welcome1_label = tk.Label(right1_frame, text='Welcome Back', font=('Arial', 20), fg='#676F90', bg='#F5F5F5')
welcome1_label.place(x=50, y=70)

# Username (LogIn Frame)
username1_frame = tk.Frame(right1_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
username1_frame.place(x=33, y=140)

username1_entry = tk.Entry(right1_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
username1_entry.place(x=36, y=150)
username1_entry.insert(0, 'Username')
username1_entry.bind('<FocusIn>', lambda event: insert_username1())
username1_entry.bind('<FocusOut>', lambda event: leave_username1())
username1_entry.bind('<Return>', lambda event: switch_main_window())

# Password (LogIn Frame)
password1_frame = tk.Frame(right1_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
password1_frame.place(x=33, y=190)

password1_entry = tk.Entry(right1_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
password1_entry.place(x=36, y=200)
password1_entry.insert(0, 'Password')
password1_entry.bind('<FocusIn>', lambda event: insert_password1())
password1_entry.bind('<FocusOut>', lambda event: leave_password1())
password1_entry.bind('<Return>', lambda event: switch_main_window())


# Checkbox for Show Password (LogIn Frame)
show_password1_var = tk.BooleanVar()
show_password1_checkbox = tk.Checkbutton(right1_frame, text='Show Password', font=('Arial', 8),
                                         bg='#F5F5F5', fg='#8D93AB',
                                         variable=show_password1_var, command=show_password1)
show_password1_checkbox.place(x=28, y=235)

# Error due to Incorrect Username/Password (LogIn Frame)
error1_label = tk.Label(right1_frame, fg='red', font=('Arial', 8), bg='#F5F5F5')
error1_label.place(x=30, y=261)

# Button of LogIn & SignUp (LogIn Frame)
login1_button = tk.Button(right1_frame, text='LOG IN', font=('Arial', 10), width=25, height=2,
                          fg='#FFFFFF', bg='#646FD4',
                          command=switch_main_window)
login1_button.place(x=44, y=285)

signup1_button = tk.Button(right1_frame, text='SIGN UP NOW', font=('Arial', 8, 'bold underline'),
                           bg='#F5F5F5', fg='#646FD4',
                           border=0, width=20, height=1, command=switch_signup2_frame)
signup1_button.place(x=118, y=337)

# Not a member? Text (LogIn Frame)
not_member1_label = tk.Label(right1_frame, text='Not registered?', font=('Arial', 10), fg='#888888', bg='#F5F5F5')
not_member1_label.place(x=60, y=336)

# 2- SignUp Frame
signup2_frame = tk.Frame(welcome_window, height=490, width=700, bg='#F5F5F5', takefocus=True)
signup2_frame.bind('<Return>', lambda event: successful_submit())

# Tickify Logo (SignUp Frame)
logo2_image = Image.open('C:/Users/sheal/Downloads/ti/Tickify_Logo.png')
logo2_resize_image = logo2_image.resize((300, 300), Image.LANCZOS)
logo2_tk_image = ImageTk.PhotoImage(logo2_resize_image)

logo2_label = tk.Label(signup2_frame, image=logo2_tk_image, width=300, height=300, bg='#F5F5F5')
logo2_label.place(x=50, y=80)

# Frame Right Hand Side Widgets (SignUp Frame)
right2_frame = tk.Frame(signup2_frame, height=480, width=300, bg='#F5F5F5')
right2_frame.place(x=380, y=10)

# Hello & Welcome & SignUp Text (SignUp Frame)
hello2_label = tk.Label(right2_frame, text='Hello!', font=('Arial', 20), bg='#F5F5F5', fg='#363636')
hello2_label.place(x=110, y=10)

welcome2_label = tk.Label(right2_frame, text='Welcome to Tickify app', font=('Arial', 20), fg='#676F90', bg='#F5F5F5')
welcome2_label.place(x=5, y=45)

signup2_label = tk.Label(right2_frame, text='sign up to get started', font=('Arial', 20), fg='#676F90', bg='#F5F5F5')
signup2_label.place(x=18, y=80)

# Username (SignUp Frame)
username2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
username2_frame.place(x=34, y=140)

username2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
username2_entry.place(x=37, y=150)
username2_entry.insert(0, 'Username')
username2_entry.bind('<FocusIn>', lambda event: insert_username2())
username2_entry.bind('<FocusOut>', lambda event: leave_username2())
username2_entry.bind('<Return>', lambda event: successful_submit())

# Email (SignUp Frame)
email2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                        highlightbackground='#8D93AB', highlightthickness=1.25)
email2_frame.place(x=34, y=185)

email2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
email2_entry.place(x=37, y=195)
email2_entry.insert(0, 'Email')
email2_entry.bind('<FocusIn>', lambda event: insert_email2())
email2_entry.bind('<FocusOut>', lambda event: leave_email2())
email2_entry.bind('<Return>', lambda event: successful_submit())

# Password & Confirmed Password (SignUp Frame)
password2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
password2_frame.place(x=34, y=230)

password2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
password2_entry.place(x=37, y=240)
password2_entry.insert(0, 'Password')
password2_entry.bind('<FocusIn>', lambda event: insert_password2())
password2_entry.bind('<FocusOut>', lambda event: leave_password2())
password2_entry.bind('<Return>', lambda event: successful_submit())

confirmed_password2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                                     highlightbackground='#8D93AB', highlightthickness=1.25)
confirmed_password2_frame.place(x=34, y=275)

confirmed_password2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
confirmed_password2_entry.place(x=37, y=285)
confirmed_password2_entry.insert(0, 'Confirmed Password')
confirmed_password2_entry.bind('<FocusIn>', lambda event: insert_confirmed_password2())
confirmed_password2_entry.bind('<FocusOut>', lambda event: leave_confirmed_password2())
confirmed_password2_entry.bind('<Return>', lambda event: successful_submit())

# Checkbox for Show Password (SignUp Frame)
show_password2_var = tk.BooleanVar()
show_password2_checkbox = tk.Checkbutton(right2_frame, text='Show Password', font=('Arial', 8),
                                         bg='#F5F5F5', fg='#8D93AB',
                                         variable=show_password2_var, command=show_password2)
show_password2_checkbox.place(x=29, y=318)

# Error due to Incomplete details/Unmatch password (LogIn Frame)
error2_label = tk.Label(right2_frame, fg='red', font=('Arial', 8), bg='#F5F5F5')
error2_label.place(x=32, y=340)

# SignUp Button (SignUp Frame)
signup2_button = tk.Button(right2_frame, text='SIGN UP', font=('Arial', 10), width=25, height=2,
                           fg='#FFFFFF', bg='#646FD4', command=successful_submit)
signup2_button.place(x=45, y=360)

# LogIn Button (SignUp Frame)
login2_button = tk.Button(right2_frame, text='LOG IN', font=('Arial', 8, 'bold underline'),
                          bg='#F5F5F5', fg='#646FD4',
                          border=0, width=20, height=1, command=switch_login1_frame)
login2_button.place(x=153, y=408)

# Already have account Text (SignUp Frame)
have_account2_label = tk.Label(right2_frame, text='Already have an account?', font=('Arial', 10),
                               fg='#888888', bg='#F5F5F5')
have_account2_label.place(x=53, y=407)

# Agree Text (SignUp Frame)
agree2_label = tk.Label(right2_frame, text='by signing up you agree to our', font=('Arial', 7),
                        fg='#888888', bg='#F5F5F5')
agree2_label.place(x=40, y=451)

of_use2_label = tk.Label(right2_frame, text='of use and', font=('Arial', 7),
                         fg='#888888', bg='#F5F5F5')
of_use2_label.place(x=93, y=465)


# T&C & Privacy Text (SignUp Frame)
terms2_label = tk.Label(right2_frame, text='Terms & Conditions', font=('Arial', 7),
                        bg='#F5F5F5', fg='#646FD4')
terms2_label.place(x=172, y=451)

privacy2_label = tk.Label(right2_frame, text='Privacy Policy', font=('Arial', 7),
                          bg='#F5F5F5', fg='#646FD4')
privacy2_label.place(x=141, y=465)

########################################
# SignUp Successfully Window
signup_success_window = tk.Toplevel(welcome_window)
signup_success_window.title('Tickify')
signup_success_window.geometry('200x80')
signup_success_window.configure(bg='#F5F5F5')
signup_success_window.withdraw()
signup_success_window.bind('<Return>', lambda event: switch_login1_frame())
signup_success_window.protocol('WM_DELETE_WINDOW', switch_login1_frame)
signup_success_window.iconphoto(True,
                             tk.PhotoImage(file='C:/Users/sheal/Downloads/ti/Tickify_Icon16.png'))

# SignUp Successfully Text (SignUp Successfully Window)
signup_success3_label = tk.Label(signup_success_window, text='Sign Up Successful',
                                 font=('Arial', 10, 'bold'), fg='#363636')
signup_success3_label.pack(pady=10)

# Done Button (SignUp Successfully Window)
done3_button = tk.Button(signup_success_window, text='Done', font=('Arial', 8), width=10, fg='#FFFFFF', bg='#9BA3EB',
                         command=switch_login1_frame)
done3_button.pack()

########################################
# Main Window
main_window = tk.Toplevel(welcome_window)
main_window.title('Tickify')
main_window.geometry('800x500')
main_window.withdraw()
main_window.iconphoto(True, tk.PhotoImage(file='C:/Users/sheal/Downloads/ti/Tickify_Icon16.png'))

def show_tasks():

    def delete_task(task_id):        
        cursor.execute('''UPDATE TASK SET task_status = 'deleted' where task_id = ?''',
                    (task_id,))
        connect.commit()

    def color_choose4():
        color_for_frame = colorchooser.askcolor()[1]

        task_frame.config(bg=color_for_frame)
        delete_button.config(bg=color_for_frame)
        color_plate_button.config(bg=color_for_frame)
        checkbox.config(bg=color_for_frame)
        task_title_entry.config(bg=color_for_frame)
        priority_level_button.config(bg=color_for_frame)
        priority_level_label.config(bg=color_for_frame)
        due_date_button.config(bg=color_for_frame)
        due_date_label.config(bg=color_for_frame)
        reminder_button.config(bg=color_for_frame)
        reminder_date_label.config(bg=color_for_frame)
        reminder_time_label.config(bg=color_for_frame)
        description_frame.config(bg=color_for_frame)
        description_text.config(bg=color_for_frame)
        edit_done_button.config(bg=color_for_frame)

    def insert_task_title():        
        if task_title_entry.cget('fg') == '#8D93AB':
            task_title_entry.delete(0, tk.END)
            task_title_entry.config(fg='#363636')

    def leave_task_title():
        task_title_entry.get()
        if task_title_entry.get() == '':
            task_title_entry.insert(0, 'Title')
            task_title_entry.config(fg='#8D93AB')

    def show_priority_level_frame():
        priority_level4_frame.tkraise()
        priority_level4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def choose_red_flag():
        priority_level_button.config(image=red_flag4_tk_image)
        priority_level_label.config(text='1st Priority', fg='red')
        priority_level4_frame.place_forget()

    def choose_blue_flag():
        priority_level_button.config(image=blue_flag4_tk_image)
        priority_level_label.config(text='2nd Priority', fg='blue')
        priority_level4_frame.place_forget()

    def choose_green_flag():
        priority_level_button.config(image=green_flag4_tk_image)
        priority_level_label.config(text='3rd Priority', fg='green')
        priority_level4_frame.place_forget()

    def choose_grey_flag():
        priority_level_button.config(image=grey_flag4_tk_image)
        priority_level_label.config(text='No Priority', fg='grey')
        priority_level4_frame.place_forget()

    def show_due_date_frame():
        due_date4_frame.tkraise()
        due_date4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def choose_due_date():
        due_date_button.config(image=due_date_black4_tk_image)
        due_date_label.config(text=due_date4_calendar.get_date(), fg='black')
        due_date4_frame.place_forget()

    def cancel_select_due():
        due_date4_frame.place_forget()

    def remove_due_date():
        due_date_button.config(image=due_date_grey4_tk_image)
        due_date_label.config(text='Due Date', fg='grey')
        due_date4_frame.place_forget()

    def show_reminder_frame():
        reminder4_frame.tkraise()
        reminder4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def set_reminder():
        hour = hour4_spinbox.get()
        minutes = minutes4_spinbox.get()
        if hour.isdigit() and len(hour) == 2 and minutes.isdigit() and len(minutes) == 2:
            reminder_button.config(image=clock_black4_tk_image)
            reminder_date_label.config(text=reminder4_calendar.get_date(), fg='black')
            reminder_time_label.config(text=hour + ':' + minutes, fg='black')
            error_format4_label.config(text='')
            reminder4_frame.place_forget()

            reminder_date_str = reminder4_calendar.get_date()
            reminder_date = datetime.datetime.strptime(reminder_date_str, "%Y-%m-%d")
            int_hour = int(hour)
            int_minutes = int(minutes)
            if 0 <= int_hour <= 23 and 0 <= int_minutes <= 59:
                current_datetime = datetime.datetime.now()
                reminder_datetime = current_datetime.replace(year=reminder_date.year,
                                                            month=reminder_date.month,
                                                            day=reminder_date.day,
                                                            hour=int_hour, minute=int_minutes,
                                                            second=0, microsecond=0)
                if current_datetime > reminder_datetime:
                    reminder_window.deiconify()
                    reminder_window_label1.config(text='Incorrect Reminder')
                    reminder_window_label2.config(text='Time already passed')
                else:
                    time_difference = reminder_datetime - current_datetime
                    millisecond_delay = time_difference.total_seconds() * 1000

                    def show_reminder_window():
                        reminder_window.deiconify()
                        reminder_window_label1.config(text='!!  Reminder  !!')
                        reminder_window_label2.config(text=task_title_entry.get())
                    reminder_window.after(int(millisecond_delay), show_reminder_window)
        else:
            error_format4_label.config(text="Invalid hour or minutes")

    def close_reminder_window():
        reminder_window.withdraw()
        remove_reminder()

        created_time = task_created_time
        task_title = task_title_entry.get()
        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                    (user_name, user_password))
        user_id = cursor.fetchone()[0]

        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                    (task_title, user_id, created_time))
        task_row = cursor.fetchone()
        if task_row:
            task_id = task_row[0]
            cursor.execute('''UPDATE REMINDER SET reminder_date = NULL, reminder_time = NULL where task_id = ?''',
                        (task_id,))
            connect.commit()

    def cancel_set_reminder():
        reminder4_frame.place_forget()

    def remove_reminder():
        reminder_button.config(image=clock_grey4_tk_image)
        reminder_date_label.config(text='Date', fg='grey')
        reminder_time_label.config(text='Time', fg='grey')
        reminder4_frame.place_forget()

    def insert_description():
        if description_text.cget('fg') == '#8D93AB':
            description_text.delete('1.0', 'end')
            description_text.config(fg='#363636')

    def leave_description():
        describe = description_text.get('1.0', 'end')
        if describe.strip() == '':
            description_text.insert('1.0', 'Description')
            description_text.config(fg='#8D93AB')

    def complete_task():
        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                    (user_name, user_password))
        user_id = cursor.fetchone()[0]

        created_time = task_created_time
        task_title = task_title_entry.get()
        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                    (task_title, user_id, created_time))
        task_row = cursor.fetchone()

        if checkbox_var.get() == 1:
            task_frame.configure(bg='grey')
            task_title_entry.configure(bg='grey', disabledbackground='grey')
            delete_button.configure(bg='grey')
            checkbox.configure(bg='grey')
            color_plate_button.place_forget()
            edit_done_button.place_forget()
            task_frame.configure(height=35)
            if task_row:
                task_id = task_row[0]
                cursor.execute('''UPDATE TASK SET task_status = 'achieved' where task_id = ?''',
                            (task_id,))

        elif checkbox_var.get() == 0:
            task_frame.configure(bg=color_plate_button.cget('bg'))
            task_title_entry.configure(bg=color_plate_button.cget('bg'),
                                    disabledbackground=color_plate_button.cget('bg'))
            delete_button.configure(bg=color_plate_button.cget('bg'))
            checkbox.configure(bg=color_plate_button.cget('bg'))
            color_plate_button.place(x=210, y=10)
            edit_done_button.place(x=208, y=235)
            task_frame.configure(height=255)
            if task_row:
                task_id = task_row[0]
                cursor.execute('''UPDATE TASK SET task_status = 'pending' where task_id = ?''',
                            (task_id,))
        connect.commit()

    def disable_edit():
        color_plate_button.config(command='')
        task_title_entry.config(state='disabled', disabledbackground=task_title_entry.cget('bg'))
        priority_level_button.config(command='')
        due_date_button.config(command='')
        reminder_button.config(command='')
        description_text.config(state='disabled')
        description_text.unbind('<FocusIn>')

    def able_edit():
        color_plate_button.config(command=color_choose4)
        task_title_entry.config(state='normal')
        priority_level_button.config(command=show_priority_level_frame)
        due_date_button.config(command=show_due_date_frame)
        reminder_button.config(command=show_reminder_frame)
        description_text.config(state='normal')
        description_text.bind('<FocusIn>', lambda event: insert_description())

    def database_task():
        created_time = task_created_time
        task_title = task_title_entry.get()
        task_color = color_plate_button.cget('bg')

        task_duedate = None
        if due_date_label.cget('fg') == 'black':
            task_duedate = due_date_label.cget('text')

        task_description = None
        if description_text.cget('fg') == '#363636' and description_text.get('1.0', 'end').strip() != '':
            task_description = description_text.get('1.0', 'end').strip('\n')

        task_priority = None
        if priority_level_label.cget('fg') == 'red':
            task_priority = 1
        elif priority_level_label.cget('fg') == 'blue':
            task_priority = 2
        elif priority_level_label.cget('fg') == 'green':
            task_priority = 3
        elif priority_level_label.cget('fg') == 'grey':
            task_priority = 4

        reminder_date = None
        if reminder_date_label.cget('fg') == 'black':
            reminder_date = reminder_date_label.cget('text')

        reminder_time = None
        if reminder_time_label.cget('fg') == 'black':
            reminder_time = reminder_time_label.cget('text')

        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                    (user_name, user_password))
        user_id = cursor.fetchone()[0]

        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                    (task_title, user_id, created_time))
        task_row = cursor.fetchone()
        if task_row:
            task_id = task_row[0]
            cursor.execute('''UPDATE TASK SET
                        task_title = ?, task_description = ?, task_duedate = ?, 
                        task_priority = ?, task_color = ? where task_id = ?''',
                        (task_title, task_description, task_duedate, task_priority, task_color, task_id))

            cursor.execute('''UPDATE REMINDER SET reminder_date = ?, reminder_time = ? where task_id = ?''',
                        (reminder_date, reminder_time, task_id))
        else:
            cursor.execute('''INSERT INTO TASK(user_id, task_title, task_description, task_duedate, 
                        task_priority, task_color, created_time)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (user_id, task_title, task_description, task_duedate,
                            task_priority, task_color, created_time))

            task_id = cursor.lastrowid
            cursor.execute('''INSERT INTO REMINDER(task_id, reminder_date, reminder_time)
                        VALUES (?, ?, ?)''',
                        (task_id, reminder_date, reminder_time))

        connect.commit()

    def edit_done_task():
        if edit_done_button.cget('text') == 'Save':
            if task_title_entry.cget('fg') == '#363636' and task_title_entry.get() != '':
                priority_level4_frame.place_forget()
                reminder4_frame.place_forget()
                due_date4_frame.place_forget()
                disable_edit()
                edit_done_button.config(image=pencil4_tk_image, text=' Edit')
                database_task()
            else:
                messagebox.showwarning('Empty Task Title', 'Please enter a Task Title.')
        elif edit_done_button.cget('text') == ' Edit':
            able_edit()
            edit_done_button.config(image=done4_tk_image, text='Save')

    ########################################
    # Clear everything in container frame to avoid duplicates
    for widgets in task_container4_frame.winfo_children():
        widgets.destroy()

    ########################################
    # Display Tasks by User Id
    user_name = username1_entry.get()
    user_password = password1_entry.get()
    cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                    (user_name, user_password))
    user_id = cursor.fetchone()[0]
    cursor.execute('''SELECT * FROM TASK WHERE user_id = ? and task_status != ? Order by task_duedate, task_priority''',
                        (user_id, 'deleted'))

    tasks = cursor.fetchall()
    row_index = 0
    column_index = 1
    previous_task_date =  ''
    for task in tasks:   
        task_created_time = task[8]    
        ########################################
        # Task Frame
        task_frame = tk.Frame(task_container4_frame, bg=task[7], height=255, width=250)

        # sorting task by due date and priority
        if(task[5] == None):
            row_index +=1
            task_frame.grid(row=row_index, column=0)
            
        elif(task[5] != previous_task_date):
            column_index +=1
            row_index = 0
            task_frame.grid(row=row_index, column=column_index)               
        else:
            row_index +=1
            task_frame.grid(row=row_index, column=column_index)       

        # Delete
        delete_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=delete4_tk_image, text=task[0], command=lambda: delete_task(task[0]))
        delete_button.place(x=230, y=9)

        # Colour Plate
        color_plate_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=color_plate4_tk_image,
                                    command=color_choose4)
        color_plate_button.place(x=210, y=10)

        # Checkbox
        checkbox_var = tk.BooleanVar()
        match task[4]:
            case 'achieved':
                checkbox_var = tk.BooleanVar(1)
            case _:
                checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(task_frame, bg='#D9F6E8', variable=checkbox_var, command=complete_task)
        checkbox.place(x=5, y=5)

        # Title
        task_title_entry = tk.Entry(task_frame, bg='#D9F6E8', fg='#8D93AB', border=0, width=24,
                                    font=('Arial', 10, 'bold'))
        task_title_entry.place(x=30, y=8)
        task_title_entry.insert(0, task[2])
        task_title_entry.bind('<FocusIn>', lambda event: insert_task_title())
        task_title_entry.bind('<FocusOut>', lambda event: leave_task_title())

        # Priority Level
        priority_level_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=grey_flag4_tk_image,
                                        command=show_priority_level_frame)
        priority_level_button.place(x=9, y=35)
        match task[6]:
            case 1:
                priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='1st Priority',fg='red')
                priority_level_button.config(image=red_flag4_tk_image)
            case 2:
                priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='2nd Priority',fg='blue')
                priority_level_button.config(image=blue_flag4_tk_image)
            case 3:
                priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='3rd Priority',fg='green')
                priority_level_button.config(image=green_flag4_tk_image)
            case _:
                priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='No Priority',fg='grey')      
        priority_level_label.place(x=29, y=35)

        # Due Date
        due_date_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=due_date_grey4_tk_image,
                                    command=show_due_date_frame)
        due_date_button.place(x=9, y=55)

        due_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Due Date',
                                fg='grey')            
        due_date_label.place(x=29, y=55)

        due_date_button.config(image=due_date_black4_tk_image)

        if(task[5] != None):
            due_date_label.config(text=task[5], fg='black')      
        
        # Reminder
        reminder_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=clock_grey4_tk_image,
                                    command=show_reminder_frame)
        reminder_button.place(x=9, y=75)

        reminder_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Date',
                                    fg='grey')
        reminder_date_label.place(x=29, y=75)

        reminder_time_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Time',
                                    fg='grey')
        reminder_time_label.place(x=99, y=75)

        # Description
        description_frame = tk.Frame(task_frame, bg='#D9F6E8', width=231, height=140)
        description_frame.place(x=9, y=95)

        description_text = tk.Text(description_frame, bg='#D9F6E8', width=35, height=9, fg='#8D93AB', font=('Arial', 8))
        description_text.place(x=2, y=3)
        description_text.insert('1.0', task[3])
        description_text.bind('<FocusIn>', lambda event: insert_description())
        description_text.bind('<FocusOut>', lambda event: leave_description())

        description_scrollbar = tk.Scrollbar(description_frame)
        description_scrollbar.place(x=216, y=3, height=132)

        description_text.configure(yscrollcommand=description_scrollbar.set)
        description_scrollbar.configure(command=description_text.yview)

        # Edit & Done
        edit_done_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=done4_tk_image, text='Edit',
                                    font=('Arial', 7), command=edit_done_task, compound=tk.LEFT, fg='grey')
        edit_done_button.place(x=208, y=235)

        ########################################
        # Frame - Choose Priority Level
        priority_level4_frame = tk.Frame(list4_frame, width=150, height=160, bg='#F5F5F5',
                                        highlightbackground="#ADB0BC", highlightthickness=2)

        priority_level4_label = tk.Label(priority_level4_frame, text='Priority Level', bg='#F5F5F5',
                                        font=('Arial', 10, 'underline', 'bold'))
        priority_level4_label.place(x=28, y=0)

        red_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='red', width=100,
                                    text='1st Priority', font=('Arial', 8),
                                    image=red_flag4_tk_image, compound=tk.LEFT, command=choose_red_flag)
        red_flag4_button.place(x=19, y=35)

        blue_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='blue', width=100,
                                    text='2nd Priority', font=('Arial', 8),
                                    image=blue_flag4_tk_image, compound=tk.LEFT, command=choose_blue_flag)
        blue_flag4_button.place(x=19, y=65)

        green_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='green', width=100,
                                    text='3rd Priority', font=('Arial', 8),
                                    image=green_flag4_tk_image, compound=tk.LEFT, command=choose_green_flag)
        green_flag4_button.place(x=19, y=95)

        grey_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='grey', width=100,
                                    text='No Priority', font=('Arial', 8),
                                    image=grey_flag4_tk_image, compound=tk.LEFT, command=choose_grey_flag)
        grey_flag4_button.place(x=19, y=125)

        # Frame - Choose Due Date
        due_date4_frame = tk.Frame(list4_frame, width=255, height=260, bg='#F5F5F5',
                                highlightbackground="#ADB0BC", highlightthickness=2)

        due_date4_label = tk.Label(due_date4_frame, text='Assign Due Date', bg='#F5F5F5',
                                font=('Arial', 10, 'underline', 'bold'))
        due_date4_label.place(x=70, y=5)

        due_date4_calendar = Calendar(due_date4_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        due_date4_calendar.place(x=0, y=35)

        select_due_date4_button = tk.Button(due_date4_frame, text='Select', font=('Arial', 8), bg='#F5F5F5',
                                            command=choose_due_date, width=6)
        select_due_date4_button.place(x=171, y=226)

        cancel_select_due4_button = tk.Button(due_date4_frame, text='Cancel', font=('Arial', 8), bg='#F5F5F5',
                                            command=cancel_select_due, width=6)
        cancel_select_due4_button.place(x=31, y=226)

        remove_due_date4_button = tk.Button(due_date4_frame, text='Remove', font=('Arial', 8), bg='#F5F5F5',
                                            command=remove_due_date, width=6)
        remove_due_date4_button.place(x=101, y=226)

        # Frame - Set reminder
        reminder4_frame = tk.Frame(list4_frame, width=255, height=300, bg='#F5F5F5',
                                highlightbackground="#ADB0BC", highlightthickness=2)

        reminder4_label = tk.Label(reminder4_frame, text='Set Reminder', bg='#F5F5F5',
                                font=('Arial', 10, 'underline', 'bold'))
        reminder4_label.place(x=80, y=5)

        reminder4_calendar = Calendar(reminder4_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        reminder4_calendar.place(x=0, y=35)

        remind_time4_label = tk.Label(reminder4_frame, text='Time (24-hour format):', bg='#F5F5F5',
                                    font=('Arial', 10))
        remind_time4_label.place(x=3, y=225)

        hour4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=23, width=4, justify='center', format='%02.0f')
        hour4_spinbox.place(x=150, y=228)

        minutes4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=59, width=4, justify='center', format='%02.0f')
        minutes4_spinbox.place(x=200, y=228)

        error_format4_label = tk.Label(reminder4_frame, bg='#F5F5F5', fg='red', font=('Arial', 8))
        error_format4_label.place(x=68, y=245)

        select_reminder4_button = tk.Button(reminder4_frame, text='Select', font=('Arial', 8), bg='#F5F5F5',
                                            command=set_reminder, width=6)
        select_reminder4_button.place(x=171, y=265)

        cancel_set_reminder4_button = tk.Button(reminder4_frame, text='Cancel', font=('Arial', 8), bg='#F5F5F5',
                                                command=cancel_set_reminder, width=6)
        cancel_set_reminder4_button.place(x=31, y=265)

        remove_reminder_button = tk.Button(reminder4_frame, text='Remove', font=('Arial', 8), bg='#F5F5F5',
                                        command=remove_reminder, width=6)
        remove_reminder_button.place(x=101, y=265)

        ########################################
        # Reminder window
        reminder_window = tk.Toplevel(main_window)
        reminder_window.title('Tickify')
        reminder_window.geometry('220x90')
        reminder_window.configure(bg='#F5F5F5')
        reminder_window.withdraw()
        reminder_window.bind('<Return>', lambda event: close_reminder_window())
        reminder_window.protocol('WM_DELETE_WINDOW', close_reminder_window)
        reminder_window.iconphoto(True,
                                tk.PhotoImage(file='C:/Users/sheal/Downloads/Tickify_Icon16.png'))

        reminder_window_label1 = tk.Label(reminder_window, text='Title', font=('Arial', 12, 'bold'),
                                        bg='#F5F5F5', fg='#9BA3EB')
        reminder_window_label1.pack(pady=2)

        reminder_window_label2 = tk.Label(reminder_window, text='Content', font=('Arial', 10), bg='#F5F5F5')
        reminder_window_label2.pack()

        reminder_window_done = tk.Button(reminder_window, text='Done', font=('Arial', 8), width=10,
                                        fg='#FFFFFF', bg='#9BA3EB', command=close_reminder_window)
        reminder_window_done.pack(pady=8)

        ########################################
        task_container4_frame.update_idletasks()
        task4_canvas.configure(scrollregion=task4_canvas.bbox("all"))

        previous_task_date = task[5]
            
        print(task)

        add_task4()
       

def add_task4():
    def delete_list4():
        if task_title_entry.cget('fg') == '#8D93AB':
            task_frame.destroy()
        else:
            user_name = username1_entry.get()
            user_password = password1_entry.get()
            cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                           (user_name, user_password))
            user_id = cursor.fetchone()[0]

            created_time = task_created_time
            task_title = task_title_entry.get()
            cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                           (task_title, user_id, created_time))
            task_id = cursor.fetchone()[0]

            cursor.execute('''UPDATE TASK SET task_status = 'deleted' where task_id = ?''',
                           (task_id,))
            connect.commit()
            task_frame.destroy()

    def color_choose4():
        color_for_frame = colorchooser.askcolor()[1]

        task_frame.config(bg=color_for_frame)
        delete_button.config(bg=color_for_frame)
        color_plate_button.config(bg=color_for_frame)
        checkbox.config(bg=color_for_frame)
        task_title_entry.config(bg=color_for_frame)
        priority_level_button.config(bg=color_for_frame)
        priority_level_label.config(bg=color_for_frame)
        due_date_button.config(bg=color_for_frame)
        due_date_label.config(bg=color_for_frame)
        reminder_button.config(bg=color_for_frame)
        reminder_date_label.config(bg=color_for_frame)
        reminder_time_label.config(bg=color_for_frame)
        description_frame.config(bg=color_for_frame)
        description_text.config(bg=color_for_frame)
        edit_done_button.config(bg=color_for_frame)

    def insert_task_title():        
        if task_title_entry.cget('fg') == '#8D93AB':
            task_title_entry.delete(0, tk.END)
            task_title_entry.config(fg='#363636')

    def leave_task_title():
        task_title_entry.get()
        if task_title_entry.get() == '':
            task_title_entry.insert(0, 'Title')
            task_title_entry.config(fg='#8D93AB')

    def show_priority_level_frame():
        priority_level4_frame.tkraise()
        priority_level4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def choose_red_flag():
        priority_level_button.config(image=red_flag4_tk_image)
        priority_level_label.config(text='1st Priority', fg='red')
        priority_level4_frame.place_forget()

    def choose_blue_flag():
        priority_level_button.config(image=blue_flag4_tk_image)
        priority_level_label.config(text='2nd Priority', fg='blue')
        priority_level4_frame.place_forget()

    def choose_green_flag():
        priority_level_button.config(image=green_flag4_tk_image)
        priority_level_label.config(text='3rd Priority', fg='green')
        priority_level4_frame.place_forget()

    def choose_grey_flag():
        priority_level_button.config(image=grey_flag4_tk_image)
        priority_level_label.config(text='No Priority', fg='grey')
        priority_level4_frame.place_forget()

    def show_due_date_frame():
        due_date4_frame.tkraise()
        due_date4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def choose_due_date():
        due_date_button.config(image=due_date_black4_tk_image)
        due_date_label.config(text=due_date4_calendar.get_date(), fg='black')
        due_date4_frame.place_forget()

    def cancel_select_due():
        due_date4_frame.place_forget()

    def remove_due_date():
        due_date_button.config(image=due_date_grey4_tk_image)
        due_date_label.config(text='Due Date', fg='grey')
        due_date4_frame.place_forget()

    def show_reminder_frame():
        reminder4_frame.tkraise()
        reminder4_frame.place(relx=0.5, rely=0.5, anchor='center')

    def set_reminder():
        hour = hour4_spinbox.get()
        minutes = minutes4_spinbox.get()
        if hour.isdigit() and len(hour) == 2 and minutes.isdigit() and len(minutes) == 2:
            reminder_button.config(image=clock_black4_tk_image)
            reminder_date_label.config(text=reminder4_calendar.get_date(), fg='black')
            reminder_time_label.config(text=hour + ':' + minutes, fg='black')
            error_format4_label.config(text='')
            reminder4_frame.place_forget()

            reminder_date_str = reminder4_calendar.get_date()
            reminder_date = datetime.datetime.strptime(reminder_date_str, "%Y-%m-%d")
            int_hour = int(hour)
            int_minutes = int(minutes)
            if 0 <= int_hour <= 23 and 0 <= int_minutes <= 59:
                current_datetime = datetime.datetime.now()
                reminder_datetime = current_datetime.replace(year=reminder_date.year,
                                                             month=reminder_date.month,
                                                             day=reminder_date.day,
                                                             hour=int_hour, minute=int_minutes,
                                                             second=0, microsecond=0)
                if current_datetime > reminder_datetime:
                    reminder_window.deiconify()
                    reminder_window_label1.config(text='Incorrect Reminder')
                    reminder_window_label2.config(text='Time already passed')
                else:
                    time_difference = reminder_datetime - current_datetime
                    millisecond_delay = time_difference.total_seconds() * 1000

                    def show_reminder_window():
                        reminder_window.deiconify()
                        reminder_window_label1.config(text='!!  Reminder  !!')
                        reminder_window_label2.config(text=task_title_entry.get())
                    reminder_window.after(int(millisecond_delay), show_reminder_window)
        else:
            error_format4_label.config(text="Invalid hour or minutes")

    def close_reminder_window():
        reminder_window.withdraw()
        remove_reminder()

        created_time = task_created_time
        task_title = task_title_entry.get()
        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                       (user_name, user_password))
        user_id = cursor.fetchone()[0]

        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                       (task_title, user_id, created_time))
        task_row = cursor.fetchone()
        if task_row:
            task_id = task_row[0]
            cursor.execute('''UPDATE REMINDER SET reminder_date = NULL, reminder_time = NULL where task_id = ?''',
                           (task_id,))
            connect.commit()

    def cancel_set_reminder():
        reminder4_frame.place_forget()

    def remove_reminder():
        reminder_button.config(image=clock_grey4_tk_image)
        reminder_date_label.config(text='Date', fg='grey')
        reminder_time_label.config(text='Time', fg='grey')
        reminder4_frame.place_forget()

    def insert_description():
        if description_text.cget('fg') == '#8D93AB':
            description_text.delete('1.0', 'end')
            description_text.config(fg='#363636')

    def leave_description():
        describe = description_text.get('1.0', 'end')
        if describe.strip() == '':
            description_text.insert('1.0', 'Description')
            description_text.config(fg='#8D93AB')

    def complete_task():
        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                       (user_name, user_password))
        user_id = cursor.fetchone()[0]

        created_time = task_created_time
        task_title = task_title_entry.get()
        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                       (task_title, user_id, created_time))
        task_row = cursor.fetchone()

        if checkbox_var.get() == 1:
            task_frame.configure(bg='grey')
            task_title_entry.configure(bg='grey', disabledbackground='grey')
            delete_button.configure(bg='grey')
            checkbox.configure(bg='grey')
            color_plate_button.place_forget()
            edit_done_button.place_forget()
            task_frame.configure(height=35)
            if task_row:
                task_id = task_row[0]
                cursor.execute('''UPDATE TASK SET task_status = 'achieved' where task_id = ?''',
                               (task_id,))

        elif checkbox_var.get() == 0:
            task_frame.configure(bg=color_plate_button.cget('bg'))
            task_title_entry.configure(bg=color_plate_button.cget('bg'),
                                       disabledbackground=color_plate_button.cget('bg'))
            delete_button.configure(bg=color_plate_button.cget('bg'))
            checkbox.configure(bg=color_plate_button.cget('bg'))
            color_plate_button.place(x=210, y=10)
            edit_done_button.place(x=208, y=235)
            task_frame.configure(height=255)
            if task_row:
                task_id = task_row[0]
                cursor.execute('''UPDATE TASK SET task_status = 'pending' where task_id = ?''',
                               (task_id,))
        connect.commit()

    def disable_edit():
        color_plate_button.config(command='')
        task_title_entry.config(state='disabled', disabledbackground=task_title_entry.cget('bg'))
        priority_level_button.config(command='')
        due_date_button.config(command='')
        reminder_button.config(command='')
        description_text.config(state='disabled')
        description_text.unbind('<FocusIn>')

    def able_edit():
        color_plate_button.config(command=color_choose4)
        task_title_entry.config(state='normal')
        priority_level_button.config(command=show_priority_level_frame)
        due_date_button.config(command=show_due_date_frame)
        reminder_button.config(command=show_reminder_frame)
        description_text.config(state='normal')
        description_text.bind('<FocusIn>', lambda event: insert_description())

    def database_task():
        created_time = task_created_time
        task_title = task_title_entry.get()
        task_color = color_plate_button.cget('bg')

        task_duedate = None
        if due_date_label.cget('fg') == 'black':
            task_duedate = due_date_label.cget('text')

        task_description = None
        if description_text.cget('fg') == '#363636' and description_text.get('1.0', 'end').strip() != '':
            task_description = description_text.get('1.0', 'end').strip('\n')

        task_priority = None
        if priority_level_label.cget('fg') == 'red':
            task_priority = 1
        elif priority_level_label.cget('fg') == 'blue':
            task_priority = 2
        elif priority_level_label.cget('fg') == 'green':
            task_priority = 3
        elif priority_level_label.cget('fg') == 'grey':
            task_priority = 4

        reminder_date = None
        if reminder_date_label.cget('fg') == 'black':
            reminder_date = reminder_date_label.cget('text')

        reminder_time = None
        if reminder_time_label.cget('fg') == 'black':
            reminder_time = reminder_time_label.cget('text')

        user_name = username1_entry.get()
        user_password = password1_entry.get()
        cursor.execute('SELECT user_id FROM USER WHERE user_name = ? and user_password = ?',
                       (user_name, user_password))
        user_id = cursor.fetchone()[0]

        cursor.execute('''SELECT task_id FROM TASK WHERE task_title = ? and user_id = ? and created_time = ? ''',
                       (task_title, user_id, created_time))
        task_row = cursor.fetchone()
        if task_row:
            task_id = task_row[0]
            cursor.execute('''UPDATE TASK SET
                           task_title = ?, task_description = ?, task_duedate = ?, 
                           task_priority = ?, task_color = ? where task_id = ?''',
                           (task_title, task_description, task_duedate, task_priority, task_color, task_id))

            cursor.execute('''UPDATE REMINDER SET reminder_date = ?, reminder_time = ? where task_id = ?''',
                           (reminder_date, reminder_time, task_id))
        else:
            cursor.execute('''INSERT INTO TASK(user_id, task_title, task_description, task_duedate, 
                           task_priority, task_color, created_time)
                           VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (user_id, task_title, task_description, task_duedate,
                            task_priority, task_color, created_time))

            task_id = cursor.lastrowid
            cursor.execute('''INSERT INTO REMINDER(task_id, reminder_date, reminder_time)
                           VALUES (?, ?, ?)''',
                           (task_id, reminder_date, reminder_time))

        connect.commit()

    def edit_done_task():
        if edit_done_button.cget('text') == 'Save':
            if task_title_entry.cget('fg') == '#363636' and task_title_entry.get() != '':
                priority_level4_frame.place_forget()
                reminder4_frame.place_forget()
                due_date4_frame.place_forget()
                disable_edit()
                edit_done_button.config(image=pencil4_tk_image, text=' Edit')
                database_task()
                show_tasks()
            else:
                messagebox.showwarning('Empty Task Title', 'Please enter a Task Title.')
        elif edit_done_button.cget('text') == ' Edit':
            able_edit()
            edit_done_button.config(image=done4_tk_image, text='Save')
    
    ########################################
    # Task Frame
    task_frame = tk.Frame(task_container4_frame, bg='#D9F6E8', height=255, width=250) 
    # remove pack() and used grid instead due to sorting use case
    # never mix pack() and grid() together in same main window
    task_frame.grid(row=0, column=0)

    task_created_time = datetime.datetime.now()

    # Delete
    delete_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=delete4_tk_image,
                              command=delete_list4)
    delete_button.place(x=230, y=9)

    # Colour Plate
    color_plate_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=color_plate4_tk_image,
                                   command=color_choose4)
    color_plate_button.place(x=210, y=10)

    # Checkbox
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(task_frame, bg='#D9F6E8', variable=checkbox_var, command=complete_task)
    checkbox.place(x=5, y=5)

    # Title
    task_title_entry = tk.Entry(task_frame, bg='#D9F6E8', fg='#8D93AB', border=0, width=24,
                                font=('Arial', 10, 'bold'))
    task_title_entry.place(x=30, y=8)
    task_title_entry.insert(0, 'Title')
    task_title_entry.bind('<FocusIn>', lambda event: insert_task_title())
    task_title_entry.bind('<FocusOut>', lambda event: leave_task_title())

    # Priority Level
    priority_level_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=grey_flag4_tk_image,
                                      command=show_priority_level_frame)
    priority_level_button.place(x=9, y=35)

    priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='No Priority',
                                    fg='grey')
    priority_level_label.place(x=29, y=35)

    # Due Date
    due_date_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=due_date_grey4_tk_image,
                                command=show_due_date_frame)
    due_date_button.place(x=9, y=55)

    due_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Due Date',
                              fg='grey')
    due_date_label.place(x=29, y=55)

    # Reminder
    reminder_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=clock_grey4_tk_image,
                                command=show_reminder_frame)
    reminder_button.place(x=9, y=75)

    reminder_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Date',
                                   fg='grey')
    reminder_date_label.place(x=29, y=75)

    reminder_time_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Time',
                                   fg='grey')
    reminder_time_label.place(x=99, y=75)

    # Description
    description_frame = tk.Frame(task_frame, bg='#D9F6E8', width=231, height=140)
    description_frame.place(x=9, y=95)

    description_text = tk.Text(description_frame, bg='#D9F6E8', width=35, height=9, fg='#8D93AB', font=('Arial', 8))
    description_text.place(x=2, y=3)
    description_text.insert('1.0', 'Description')
    description_text.bind('<FocusIn>', lambda event: insert_description())
    description_text.bind('<FocusOut>', lambda event: leave_description())

    description_scrollbar = tk.Scrollbar(description_frame)
    description_scrollbar.place(x=216, y=3, height=132)

    description_text.configure(yscrollcommand=description_scrollbar.set)
    description_scrollbar.configure(command=description_text.yview)

    # Edit & Done
    edit_done_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=done4_tk_image, text='Save',
                                 font=('Arial', 7), command=edit_done_task, compound=tk.LEFT, fg='grey')
    edit_done_button.place(x=208, y=235)

    ########################################
    # Frame - Choose Priority Level
    priority_level4_frame = tk.Frame(list4_frame, width=150, height=160, bg='#F5F5F5',
                                     highlightbackground="#ADB0BC", highlightthickness=2)

    priority_level4_label = tk.Label(priority_level4_frame, text='Priority Level', bg='#F5F5F5',
                                     font=('Arial', 10, 'underline', 'bold'))
    priority_level4_label.place(x=28, y=0)

    red_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='red', width=100,
                                 text='1st Priority', font=('Arial', 8),
                                 image=red_flag4_tk_image, compound=tk.LEFT, command=choose_red_flag)
    red_flag4_button.place(x=19, y=35)

    blue_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='blue', width=100,
                                  text='2nd Priority', font=('Arial', 8),
                                  image=blue_flag4_tk_image, compound=tk.LEFT, command=choose_blue_flag)
    blue_flag4_button.place(x=19, y=65)

    green_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='green', width=100,
                                   text='3rd Priority', font=('Arial', 8),
                                   image=green_flag4_tk_image, compound=tk.LEFT, command=choose_green_flag)
    green_flag4_button.place(x=19, y=95)

    grey_flag4_button = tk.Button(priority_level4_frame, bg='#F5F5F5', fg='grey', width=100,
                                  text='No Priority', font=('Arial', 8),
                                  image=grey_flag4_tk_image, compound=tk.LEFT, command=choose_grey_flag)
    grey_flag4_button.place(x=19, y=125)

    # Frame - Choose Due Date
    due_date4_frame = tk.Frame(list4_frame, width=255, height=260, bg='#F5F5F5',
                               highlightbackground="#ADB0BC", highlightthickness=2)

    due_date4_label = tk.Label(due_date4_frame, text='Assign Due Date', bg='#F5F5F5',
                               font=('Arial', 10, 'underline', 'bold'))
    due_date4_label.place(x=70, y=5)

    due_date4_calendar = Calendar(due_date4_frame, selectmode='day', date_pattern='yyyy-mm-dd')
    due_date4_calendar.place(x=0, y=35)

    select_due_date4_button = tk.Button(due_date4_frame, text='Select', font=('Arial', 8), bg='#F5F5F5',
                                        command=choose_due_date, width=6)
    select_due_date4_button.place(x=171, y=226)

    cancel_select_due4_button = tk.Button(due_date4_frame, text='Cancel', font=('Arial', 8), bg='#F5F5F5',
                                          command=cancel_select_due, width=6)
    cancel_select_due4_button.place(x=31, y=226)

    remove_due_date4_button = tk.Button(due_date4_frame, text='Remove', font=('Arial', 8), bg='#F5F5F5',
                                        command=remove_due_date, width=6)
    remove_due_date4_button.place(x=101, y=226)

    # Frame - Set reminder
    reminder4_frame = tk.Frame(list4_frame, width=255, height=300, bg='#F5F5F5',
                               highlightbackground="#ADB0BC", highlightthickness=2)

    reminder4_label = tk.Label(reminder4_frame, text='Set Reminder', bg='#F5F5F5',
                               font=('Arial', 10, 'underline', 'bold'))
    reminder4_label.place(x=80, y=5)

    reminder4_calendar = Calendar(reminder4_frame, selectmode='day', date_pattern='yyyy-mm-dd')
    reminder4_calendar.place(x=0, y=35)

    remind_time4_label = tk.Label(reminder4_frame, text='Time (24-hour format):', bg='#F5F5F5',
                                  font=('Arial', 10))
    remind_time4_label.place(x=3, y=225)

    hour4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=23, width=4, justify='center', format='%02.0f')
    hour4_spinbox.place(x=150, y=228)

    minutes4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=59, width=4, justify='center', format='%02.0f')
    minutes4_spinbox.place(x=200, y=228)

    error_format4_label = tk.Label(reminder4_frame, bg='#F5F5F5', fg='red', font=('Arial', 8))
    error_format4_label.place(x=68, y=245)

    select_reminder4_button = tk.Button(reminder4_frame, text='Select', font=('Arial', 8), bg='#F5F5F5',
                                        command=set_reminder, width=6)
    select_reminder4_button.place(x=171, y=265)

    cancel_set_reminder4_button = tk.Button(reminder4_frame, text='Cancel', font=('Arial', 8), bg='#F5F5F5',
                                            command=cancel_set_reminder, width=6)
    cancel_set_reminder4_button.place(x=31, y=265)

    remove_reminder_button = tk.Button(reminder4_frame, text='Remove', font=('Arial', 8), bg='#F5F5F5',
                                       command=remove_reminder, width=6)
    remove_reminder_button.place(x=101, y=265)

    ########################################
    # Reminder window
    reminder_window = tk.Toplevel(main_window)
    reminder_window.title('Tickify')
    reminder_window.geometry('220x90')
    reminder_window.configure(bg='#F5F5F5')
    reminder_window.withdraw()
    reminder_window.bind('<Return>', lambda event: close_reminder_window())
    reminder_window.protocol('WM_DELETE_WINDOW', close_reminder_window)
    reminder_window.iconphoto(True,
                              tk.PhotoImage(file='C:/Users/sheal/Downloads/Tickify_Icon16.png'))

    reminder_window_label1 = tk.Label(reminder_window, text='Title', font=('Arial', 12, 'bold'),
                                      bg='#F5F5F5', fg='#9BA3EB')
    reminder_window_label1.pack(pady=2)

    reminder_window_label2 = tk.Label(reminder_window, text='Content', font=('Arial', 10), bg='#F5F5F5')
    reminder_window_label2.pack()

    reminder_window_done = tk.Button(reminder_window, text='Done', font=('Arial', 8), width=10,
                                     fg='#FFFFFF', bg='#9BA3EB', command=close_reminder_window)
    reminder_window_done.pack(pady=8)

    ########################################
    task_container4_frame.update_idletasks()
    task4_canvas.configure(scrollregion=task4_canvas.bbox("all"))


########################################
# Main Frame
main4_frame = tk.Frame(main_window, bg='#F5F5F5', width=800, height=500)
main4_frame.place(relx=0.5, rely=0.5, anchor='center')

########################################
# Upper Frame
heading4_frame = tk.Frame(main4_frame, bg='#EBFAF2', width=790, height=70)
heading4_frame.place(x=5, y=0)

# Label - Hi, Username
hi4_label = tk.Label(heading4_frame, text="Hi, ", font=("Arial", 12, 'bold'), bg='#EBFAF2', fg='#1C1D22')
hi4_label.place(x=15, y=25)

username4_label = tk.Label(heading4_frame, text='UserName', font=("Arial", 12, 'bold'), bg='#EBFAF2', fg='#1C1D22')
username4_label.place(x=45, y=25)

# Sign Out Button
sign_out4_image = Image.open("C:/Users/sheal/Downloads/ti/SignOut_Image.png")
sign_out4_resize_image = sign_out4_image.resize((16, 16), Image.LANCZOS)
sign_out4_tk_image = ImageTk.PhotoImage(sign_out4_resize_image)

sign_out4_button = tk.Button(heading4_frame, text="Sign Out", border=0, font=('Arial', 8),
                             bg='#EBFAF2', fg='#1C1D22', image=sign_out4_tk_image, compound=tk.LEFT,
                             command=sign_out)
sign_out4_button.place(x=720, y=28)

########################################
# Separate Line
separate4_frame = tk.Frame(main4_frame, width=790, height=1, bg='#ADB0BC')
separate4_frame.place(x=5, y=70)

########################################
# Lower Frame
list4_frame = tk.Frame(main4_frame, height=429, width=790,
                       highlightbackground="#ADB0BC", highlightthickness=1, bg='#F5F5F5')
list4_frame.place(x=5, y=70)

# Task
task4_canvas = tk.Canvas(list4_frame, bg='#F5F5F5', height=423, width=783)
task4_canvas.place(x=0, y=0)

# Scrollbar Y
scrollbar_y4 = tk.Scrollbar(list4_frame, orient='vertical')
scrollbar_y4.place(x=770, y=2, height=423)

# Create connection between task canvas and scrollbar_y
task4_canvas.configure(yscrollcommand=scrollbar_y4.set)
scrollbar_y4.configure(command=task4_canvas.yview)

# Scrollbar X
scrollbar_x4 = tk.Scrollbar(list4_frame, orient='horizontal')
scrollbar_x4.place(x=0, y=410, width=775)

# Create connection between task canvas and scrollbar_x
task4_canvas.configure(xscrollcommand=scrollbar_x4.set)
scrollbar_x4.configure(command=task4_canvas.xview)

# List container frame
task_container4_frame = tk.Frame(task4_canvas, bg='#F5F5F5')
task4_canvas.create_window((0, 0), window=task_container4_frame, anchor="nw")

# Add New Task
add_task4_button = tk.Button(list4_frame, text='+ Create Task', font=('Arial', 10), height=2,
                             bg='#EBFAF2', fg='#797C89', command=add_task4)
add_task4_button.place(x=660, y=355)

# # Show Tasks (For testing purpose)
# show_tasks_button = tk.Button(list4_frame, text='+ Show Task', font=('Arial', 10), height=2,
#                              bg='#EBFAF2', fg='#797C89', command=show_tasks)
# show_tasks_button.place(x=660, y=255)

# Delete Image
delete4_image = Image.open("C:/Users/sheal/Downloads/ti/delete_image.png")
delete4_resize_image = delete4_image.resize((13, 13), Image.LANCZOS)
delete4_tk_image = ImageTk.PhotoImage(delete4_resize_image)

# Colour Plate Image
color_plate4_image = Image.open("C:/Users/sheal/Downloads/ti/color_plate_image.png")
color_plate4_resize_image = color_plate4_image.resize((13, 13), Image.LANCZOS)
color_plate4_tk_image = ImageTk.PhotoImage(color_plate4_resize_image)

# Red Flag
red_flag4_image = Image.open("C:/Users/sheal/Downloads/ti/red_flag.png")
red_flag4_resize_image = red_flag4_image.resize((13, 13), Image.LANCZOS)
red_flag4_tk_image = ImageTk.PhotoImage(red_flag4_resize_image)

# Blue Flag
blue_flag4_image = Image.open("C:/Users/sheal/Downloads/ti/c.png")
blue_flag4_resize_image = blue_flag4_image.resize((13, 13), Image.LANCZOS)
blue_flag4_tk_image = ImageTk.PhotoImage(blue_flag4_resize_image)

# Green Flag
green_flag4_image = Image.open("C:/Users/sheal/Downloads/ti/green_flag.png")
green_flag4_resize_image = green_flag4_image.resize((13, 13), Image.LANCZOS)
green_flag4_tk_image = ImageTk.PhotoImage(green_flag4_resize_image)

# Grey Flag
grey_flag4_image = Image.open("C:/Users/sheal/Downloads/ti/grey_flag.png")
grey_flag4_resize_image = grey_flag4_image.resize((13, 13), Image.LANCZOS)
grey_flag4_tk_image = ImageTk.PhotoImage(grey_flag4_resize_image)

# Calendar - Due Date
due_date_grey4_image = Image.open("C:/Users/sheal/Downloads/ti/calendar_grey.png")
due_date_grey4_resize_image = due_date_grey4_image.resize((13, 13), Image.LANCZOS)
due_date_grey4_tk_image = ImageTk.PhotoImage(due_date_grey4_resize_image)

due_date_black4_image = Image.open("C:/Users/sheal/Downloads/ti/calendar_black.png")
due_date_black4_resize_image = due_date_black4_image.resize((13, 13), Image.LANCZOS)
due_date_black4_tk_image = ImageTk.PhotoImage(due_date_black4_resize_image)

# Clock - Reminder
clock_grey4_image = Image.open("C:/Users/sheal/Downloads/ti/clock_grey.png")
clock_grey4_resize_image = clock_grey4_image.resize((13, 13), Image.LANCZOS)
clock_grey4_tk_image = ImageTk.PhotoImage(clock_grey4_resize_image)

clock_black4_image = Image.open("C:/Users/sheal/Downloads/ti/clock_black.png")
clock_black4_resize_image = clock_black4_image.resize((13, 13), Image.LANCZOS)
clock_black4_tk_image = ImageTk.PhotoImage(clock_black4_resize_image)

# Pencil - Edit
pencil4_image = Image.open("C:/Users/sheal/Downloads/ti/edit_image.png")
pencil4_resize_image = pencil4_image.resize((13, 13), Image.LANCZOS)
pencil4_tk_image = ImageTk.PhotoImage(pencil4_resize_image)

# Done Image
done4_image = Image.open("C:/Users/sheal/Downloads/ti/done_image.png")
done4_resize_image = done4_image.resize((13, 13), Image.LANCZOS)
done4_tk_image = ImageTk.PhotoImage(done4_resize_image)

########################################
# Start the Window1 - Welcome Window
welcome_window.mainloop()


# Close connection with database
cursor.close()
connect.close()

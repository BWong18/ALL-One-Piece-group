import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# Create connection with database
connect = sqlite3.connect('Tickify.db')
cursor = connect.cursor()


# Insert SignUp Data into USER (Database)
def database_signup():
    user_name = username2_entry.get()
    user_email = email2_entry.get()
    user_password = password2_entry.get()

    # Create table USER
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER(
                   user_id integer primary key autoincrement not null,
                   user_name varchar(20) not null,
                   user_email varchar(50) not null,
                   user_password varchar(50) not null)''')

    # Insert value into table USER
    cursor.execute('''INSERT INTO USER(user_name, user_email, user_password)
                   VALUES(?, ?, ?)''', (user_name, user_email, user_password))

    # Commit changes
    connect.commit()


########################################
# Event for Entry (Welcome Window)
def insert_username1():
    username1_entry.delete(0, tk.END)
    username1_entry.config(fg='#363636')


def leave_username1():
    username1_entry.get()
    if username1_entry.get() == '':
        username1_entry.insert(0, 'Username')
        username1_entry.config(fg='#8D93AB')


def insert_password1():
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
        welcome_window.withdraw()
        main_window.deiconify()
        clear_login1_frame()
    else:
        error1_label.config(text='Incorrect Username or Password')


def successful_submit():
    cursor.execute('SELECT * FROM USER WHERE user_name = ?', (username2_entry.get(),))
    existing_username = cursor.fetchall()
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
welcome_window.iconphoto(True, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Icon16.png'))

# 0 - Start Frame
start0_frame = tk.Frame(welcome_window, height=490, width=700, bg='#F5F5F5')
start0_frame.place(relx=0.5, rely=0.5, anchor='center')

# Tickify Logo (Start Frame)
logo0_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Logo.png')
logo0_resize_image = logo0_image.resize((300, 300), Image.ANTIALIAS)
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
logo1_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Logo.png')
logo1_resize_image = logo1_image.resize((300, 300), Image.ANTIALIAS)
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

# Password (LogIn Frame)
password1_frame = tk.Frame(right1_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
password1_frame.place(x=33, y=190)

password1_entry = tk.Entry(right1_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
password1_entry.place(x=36, y=200)
password1_entry.insert(0, 'Password')
password1_entry.bind('<FocusIn>', lambda event: insert_password1())
password1_entry.bind('<FocusOut>', lambda event: leave_password1())


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
logo2_image = Image.open('C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Logo.png')
logo2_resize_image = logo2_image.resize((300, 300), Image.ANTIALIAS)
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

# Email (SignUp Frame)
email2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                        highlightbackground='#8D93AB', highlightthickness=1.25)
email2_frame.place(x=34, y=185)

email2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
email2_entry.place(x=37, y=195)
email2_entry.insert(0, 'Email')
email2_entry.bind('<FocusIn>', lambda event: insert_email2())
email2_entry.bind('<FocusOut>', lambda event: leave_email2())

# Password & Confirmed Password (SignUp Frame)
password2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                           highlightbackground='#8D93AB', highlightthickness=1.25)
password2_frame.place(x=34, y=230)

password2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
password2_entry.place(x=37, y=240)
password2_entry.insert(0, 'Password')
password2_entry.bind('<FocusIn>', lambda event: insert_password2())
password2_entry.bind('<FocusOut>', lambda event: leave_password2())

confirmed_password2_frame = tk.Frame(right2_frame, height=40, width=230, bg='#F5F5F5',
                                     highlightbackground='#8D93AB', highlightthickness=1.25)
confirmed_password2_frame.place(x=34, y=275)

confirmed_password2_entry = tk.Entry(right2_frame, font=('Arial', 12), width=24, border=0, fg='#8D93AB', bg='#F5F5F5')
confirmed_password2_entry.place(x=37, y=285)
confirmed_password2_entry.insert(0, 'Confirmed Password')
confirmed_password2_entry.bind('<FocusIn>', lambda event: insert_confirmed_password2())
confirmed_password2_entry.bind('<FocusOut>', lambda event: leave_confirmed_password2())

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
signup2_button.bind('<Return>', lambda event: successful_submit())
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
signup_success_window.bind('<Destroy>', lambda event: switch_login1_frame())
signup_success_window.iconphoto(True,
                                tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Icon16.png'))

# SignUp Successfully Text (SignUp Successfully Window)
signup_success3_label = tk.Label(signup_success_window, text='Sign Up Successful',
                                 font=('Arial', 10, 'bold'), fg='#363636')
signup_success3_label.pack(pady=10)

# Done Button (SignUp Successfully Window)
done3_button = tk.Button(signup_success_window, text='Done', font=('Arial', 8), width=10, fg='#FFFFFF', bg='#9BA3EB',
                         command=switch_login1_frame)
done3_button.bind('<Return>', lambda event: switch_login1_frame())
done3_button.pack()

########################################
# Main Window
main_window = tk.Toplevel(welcome_window)
main_window.title('Tickify')
main_window.geometry('800x500')
main_window.withdraw()

########################################
# Start the Window1 - Welcome Window
welcome_window.mainloop()

# Close connection with database
cursor.close()
connect.close()

import tkinter as tk
from tkinter import colorchooser
from PIL import ImageTk, Image
from tkcalendar import Calendar

########################################
main_window = tk.Tk()
main_window.geometry("800x500")
main_window.title("Tickify")
main_window.configure(bg='#F5F5F5')
main_window.iconphoto(True, tk.PhotoImage(file='C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/Tickify_Icon16.png'))


########################################
def add_task4():
    def delete_list4():
        task_frame.destroy()

    def color_choose4():
        color_for_frame = colorchooser.askcolor()[1]

        task_frame.configure(bg=color_for_frame)
        delete_button.configure(bg=color_for_frame)
        color_plate_button.configure(bg=color_for_frame)
        checkbox.configure(bg=color_for_frame)
        task_title_entry.configure(bg=color_for_frame)
        priority_level_button.configure(bg=color_for_frame)
        priority_level_label.configure(bg=color_for_frame)
        due_date_button.configure(bg=color_for_frame)
        due_date_label.configure(bg=color_for_frame)
        reminder_button.configure(bg=color_for_frame)
        reminder_date_label.configure(bg=color_for_frame)
        reminder_time_label.configure(bg=color_for_frame)

    def insert_task_title():
        if task_title_entry.cget('fg') == '#8D93AB':
            task_title_entry.delete(0, tk.END)
            task_title_entry.config(fg='#363636')

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
        if hour.isdigit() and minutes.isdigit():
            reminder_button.config(image=clock_black4_tk_image)
            reminder_date_label.config(text=reminder4_calendar.get_date(), fg='black')
            reminder_time_label.config(text=hour + ':' + minutes, fg='black')
            error_format4_label.config(text='')
            reminder4_frame.place_forget() 
        else:
            error_format4_label.config(text='Incorrect format, please try again')

    def cancel_set_reminder():
        reminder4_frame.place_forget()

    def remove_reminder():
        reminder_button.config(image=clock_grey4_tk_image)
        reminder_date_label.config(text='Date', fg='grey')
        reminder_time_label.config(text='Time', fg='grey')
        reminder4_frame.place_forget()

    ########################################
    # Task Frame
    task_frame = tk.Frame(task_container4_frame, bg='#D9F6E8', height=250, width=250)
    task_frame.pack(side=tk.TOP, padx=10, pady=5)

    # Delete
    delete_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=delete4_tk_image,
                              command=delete_list4)
    delete_button.place(x=230, y=9)

    # Colour Plate
    color_plate_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=color_plate4_tk_image,
                                   command=color_choose4)
    color_plate_button.place(x=210, y=10)

    # Checkbox
    checkbox = tk.Checkbutton(task_frame, bg='#D9F6E8')
    checkbox.place(x=5, y=5)

    # Title
    task_title_entry = tk.Entry(task_frame, bg='#D9F6E8', fg='#8D93AB', border=0,
                                font=('Arial', 10, 'bold'))
    task_title_entry.place(x=30, y=8)
    task_title_entry.insert(0, 'Title')
    task_title_entry.bind('<FocusIn>', lambda event: insert_task_title())

    # Priority Level
    priority_level_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=grey_flag4_tk_image,
                                      command=show_priority_level_frame)
    priority_level_button.place(x=9, y=30)

    priority_level_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='No Priority',
                                    fg='grey')
    priority_level_label.place(x=29, y=30)

    # Due Date
    due_date_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=due_date_grey4_tk_image,
                                command=show_due_date_frame)
    due_date_button.place(x=9, y=50)

    due_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Due Date',
                              fg='grey')
    due_date_label.place(x=29, y=50)

    # Reminder
    reminder_button = tk.Button(task_frame, border=0, bg='#D9F6E8', image=clock_grey4_tk_image,
                                command=show_reminder_frame)
    reminder_button.place(x=9, y=70)

    reminder_date_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Date',
                                   fg='grey')
    reminder_date_label.place(x=29, y=70)

    reminder_time_label = tk.Label(task_frame, bg='#D9F6E8', font=('Arial', 7), text='Time',
                                   fg='grey')
    reminder_time_label.place(x=99, y=70)

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

    due_date4_calendar = Calendar(due_date4_frame, selectmode='day', date_pattern='dd/mm/yyyy')
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

    reminder4_calendar = Calendar(reminder4_frame, selectmode='day', date_pattern='dd/mm/yyyy')
    reminder4_calendar.place(x=0, y=35)

    remind_time4_label = tk.Label(reminder4_frame, text='Time (24-hour format):', bg='#F5F5F5',
                                  font=('Arial', 10))
    remind_time4_label.place(x=3, y=225)

    hour4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=23, width=4, justify='center')
    hour4_spinbox.place(x=150, y=228)

    minutes4_spinbox = tk.Spinbox(reminder4_frame, from_=00, to=59, width=4, justify='center')
    minutes4_spinbox.place(x=200, y=228)

    error_format4_label = tk.Label(reminder4_frame, bg='#F5F5F5', fg='red', font=('Arial', 8))
    error_format4_label.place(x=40, y=245)

    select_reminder4_button = tk.Button(reminder4_frame, text='Select', font=('Arial', 8), bg='#F5F5F5',
                                        command=set_reminder, width=6)
    select_reminder4_button.place(x=171, y=265)

    cancel_set_reminder4_button = tk.Button(reminder4_frame, text='Cancel', font=('Arial', 8), bg='#F5F5F5',
                                            command=cancel_set_reminder, width=6)
    cancel_set_reminder4_button.place(x=31, y=265)

    remove_reminder_button = tk.Button(reminder4_frame, text='Remove', font=('Arial', 8), bg='#F5F5F5',
                                       command=remove_reminder, width=6)
    remove_reminder_button.place(x=101, y=265)

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

username4_label = tk.Label(heading4_frame, text="UserName", font=("Arial", 12, 'bold'), bg='#EBFAF2', fg='#1C1D22')
username4_label.place(x=45, y=25)

# Sign Out Button
sign_out4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/SignOut_Image.png")
sign_out4_resize_image = sign_out4_image.resize((16, 16), Image.ANTIALIAS)
sign_out4_tk_image = ImageTk.PhotoImage(sign_out4_resize_image)

sign_out4_button = tk.Button(heading4_frame, text="Sign Out", border=0, font=('Arial', 8),
                             bg='#EBFAF2', fg='#1C1D22', image=sign_out4_tk_image, compound=tk.LEFT)
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

# Scrollbar
scrollbar4 = tk.Scrollbar(list4_frame)
scrollbar4.place(x=770, y=2, height=423)

# Create connection between task canvas and scrollbar
task4_canvas.configure(yscrollcommand=scrollbar4.set)
scrollbar4.configure(command=task4_canvas.yview)

# List container frame
task_container4_frame = tk.Frame(task4_canvas, bg='#F5F5F5')
task4_canvas.create_window((0, 0), window=task_container4_frame, anchor="nw")

# Add New Task
add_task4_button = tk.Button(list4_frame, text='+ Create Task', font=('Arial', 10), height=2,
                             bg='#EBFAF2', fg='#797C89', command=add_task4)
add_task4_button.place(x=660, y=365)

# Delete Image
delete4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/delete_image.png")
delete4_resize_image = delete4_image.resize((13, 13), Image.ANTIALIAS)
delete4_tk_image = ImageTk.PhotoImage(delete4_resize_image)

# Colour Plate Image
color_plate4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/color_plate_image.png")
color_plate4_resize_image = color_plate4_image.resize((13, 13), Image.ANTIALIAS)
color_plate4_tk_image = ImageTk.PhotoImage(color_plate4_resize_image)

# Red Flag
red_flag4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/red_flag.png")
red_flag4_resize_image = red_flag4_image.resize((13, 13), Image.ANTIALIAS)
red_flag4_tk_image = ImageTk.PhotoImage(red_flag4_resize_image)

# Blue Flag
blue_flag4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/blue_flag.png")
blue_flag4_resize_image = blue_flag4_image.resize((13, 13), Image.ANTIALIAS)
blue_flag4_tk_image = ImageTk.PhotoImage(blue_flag4_resize_image)

# Green Flag
green_flag4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/green_flag.png")
green_flag4_resize_image = green_flag4_image.resize((13, 13), Image.ANTIALIAS)
green_flag4_tk_image = ImageTk.PhotoImage(green_flag4_resize_image)

# Grey Flag
grey_flag4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/grey_flag.png")
grey_flag4_resize_image = grey_flag4_image.resize((13, 13), Image.ANTIALIAS)
grey_flag4_tk_image = ImageTk.PhotoImage(grey_flag4_resize_image)

# Calendar - Due Date
due_date_grey4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/calendar_grey.png")
due_date_grey4_resize_image = due_date_grey4_image.resize((13, 13), Image.ANTIALIAS)
due_date_grey4_tk_image = ImageTk.PhotoImage(due_date_grey4_resize_image)

due_date_black4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/calendar_black.png")
due_date_black4_resize_image = due_date_black4_image.resize((13, 13), Image.ANTIALIAS)
due_date_black4_tk_image = ImageTk.PhotoImage(due_date_black4_resize_image)

# Clock - Reminder
clock_grey4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/clock_grey.png")
clock_grey4_resize_image = clock_grey4_image.resize((13, 13), Image.ANTIALIAS)
clock_grey4_tk_image = ImageTk.PhotoImage(clock_grey4_resize_image)

clock_black4_image = Image.open("C:/Users/xueer/OneDrive/Desktop/ALL1(4006CEM)/clock_black.png")
clock_black4_resize_image = clock_black4_image.resize((13, 13), Image.ANTIALIAS)
clock_black4_tk_image = ImageTk.PhotoImage(clock_black4_resize_image)

########################################
main_window.mainloop()

import time
from tkinter import *

import customtkinter
import ttkbootstrap as tb
from tkinter import messagebox

from App import OpenApp



def Auth_window():
    # Toplevel object which will
    # be treated as a new window

    username = "AG_insurance"
    password = "Aginsure123!"

    def log_user_in():
       if username == Username_textbox.get() and password == Password_textbox.get():
           OpenApp(AuthWindow)
           # AuthWindow.destroy()

       else:
           error_message.config(text=f"Incorrect Username or Password", bootstyle="danger")
           time.sleep(10)
           error_message.config(text=f"", bootstyle="danger")
           print("error")



    LightTheme = ["pulse", "default", "default", "white"]
    DarkTheme = ["cyborg", "dark", "default", "black"]
    Theme = LightTheme

    AuthWindow = tb.Window(themename=Theme[0])


    # sets the title of the
    # Toplevel widget
    AuthWindow.title("Authentication")
    AuthWindow.iconbitmap("./A&GICON.ico")
    AuthWindow.geometry('800x500')

    # User Interface GUI
    my_frame = customtkinter.CTkFrame(AuthWindow, fg_color=Theme[3], border_width=2, width=800, height=550)
    my_frame.pack(fill="both", expand=True, pady=70, padx=100)
    AuthWindow.rowconfigure(4, weight=1)

    my_label = tb.Label(my_frame, text="Sign Up", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=(50, 1), padx=(20, 20))

    Username = tb.Label(master=my_frame, text="Username", font=("Inter", 12))
    Username.pack(pady=10)
    global Username_textbox
    Username_textbox = tb.Entry(my_frame, width=50, )
    Username_textbox.pack()

    Password = tb.Label(master=my_frame, text="Password", font=("Inter", 12))
    Password.pack(pady=10)
    global Password_textbox
    Password_textbox = tb.Entry(my_frame, width=50, )
    Password_textbox.pack()

    Login = tb.Button(my_frame, bootstyle="danger", text="Login", width=30,
                      command=log_user_in)
    Login.pack(pady=20)

    error_message = tb.Label(my_frame, text="1111", bootstyle="danger", font=("Inter", 9))
    error_message.pack(pady=10, )

    AuthWindow.mainloop()



if __name__ == '__main__':
    Auth_window()

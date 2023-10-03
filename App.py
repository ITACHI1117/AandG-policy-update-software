import threading
from tkinter import *
import ttkbootstrap as tb
import customtkinter
from ttkbootstrap.toast import ToastNotification
from tkinter import messagebox

from Chassis_Update import correct_chassisNO
from Niid_Reg_Correction import correct_regNoNiid
from Niid_chassis_only import correct_chassisNo_Niid
from Reg_Update import correct_regNo

import multiprocessing

LightTheme = ["pulse", "default", "default", "white"]
DarkTheme = ["cyborg", "dark", "default", "black"]
Theme = DarkTheme

root = tb.Window(themename=Theme[0])
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('1240x600')

REG_POLICY_NUMBER = ""

# Functions
# Default Platform Scratch card Platform
email = 'mayowa_admin'
password = 'Gbohunmi17'
LINK = ["https://aginsuranceapplications.com/card/Index.aspx", email, password]
print(LINK)


# Change Platform to Scratch Card
def change_platform():
    global LINK
    email = 'mayowa_admin'
    password = 'Gbohunmi17'
    LINK = ["https://aginsuranceapplications.com/card/Index.aspx", email, password]

    top_frame_label.config(text="Scratch Card Platform")


# Change Platform to E_PIN
def change_platform_epin():
    global LINK
    email = 'mayowa1022'
    password = 'Gbohunmi17'
    LINK = ["https://aginsuranceapplications.com/", email, password]

    top_frame_label.config(text="E-PIN Platform")


Running_program = 0
# Update Reg Number Function


print(Running_program)


def run_program():

    #Reg number update function
    def update_reg_number():
        # Checking if enter is null
        if reg_policy_number_textbox.get() == "" or reg_number_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Input Reg and policy number")
            print("Input Reg and policy number")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")

            # get Entry data
            global REG_POLICY_NUMBER
            REG_POLICY_NUMBER = reg_policy_number_textbox.get()
            REG_NUMBER = reg_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER, RETURNED_POLICY_NUMBER, RETURNED_REGNUMBER = correct_regNo(REG_POLICY_NUMBER,
                                                                                                REG_NUMBER, LINK)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(f'Reg Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                                         f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print("Updating on NIID")
                    correct_regNoNiid(RETURNED_POLICY_NUMBER, RETURNED_POLICY_NUMBER, INCORRECT_REGNUMBER)
                    Running_program -= 1
                    messagebox.showinfo("Reg Number Correction Successful",
                                        f"The Policy {RETURNED_POLICY_NUMBER} has been updated ✅")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Reg Number Correction Error',
                                     f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]


    def update_chassis_update_only():
        global Running_program
        Running_program += 1
        runing_programs_button.config(text=Running_program, state="enabled")

        if Running_program == 5:
            Reg_update_button.config(state="disabled")

        # get Entry data

        CHASSIS_POLICY_NUMBER = chassis_policy_number_textbox.get()
        CHASSIS_NUMBER = chassis_number_textbox.get()

        RETURNED_POLICY_NUMBER = "Unknown"

        # Checking if enter is null
        if chassis_policy_number_textbox.get() == "" or chassis_number_textbox.get() == "":
            print("Input Reg and policy number")
        else:
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER,RETURNED_POLICY_NUMBER,RETURNED_CHASSIS_NUMBER = correct_chassisNO(CHASSIS_POLICY_NUMBER,CHASSIS_NUMBER,LINK)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(f'Reg Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]', f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print("Updating on NIID")
                    correct_chassisNo_Niid(RETURNED_POLICY_NUMBER, INCORRECT_REGNUMBER, RETURNED_CHASSIS_NUMBER)
                    Running_program -= 1
                    messagebox.showinfo("Reg Number Correction Successful", f"The Policy {RETURNED_POLICY_NUMBER} has been updated ✅")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Reg Number Correction Error',f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]

    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_reg_number)
        thread.start()

    def run_chassis_only_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_chassis_update_only)
        thread.start()

    # Reg frame
    root.columnconfigure(2, weight=1)
    # root.columnconfigure(1, weight=3)
    root.rowconfigure(2, weight=2)

    # Side bar
    my_frame = customtkinter.CTkFrame(root, fg_color=Theme[3], height=300)
    my_frame.grid(row=0, column=0, rowspan=4, sticky=NS)
    root.rowconfigure(4, weight=1)

    # Side bar Label

    # Scratch card button
    scratch_button = tb.Button(my_frame, text="Scratch Card", bootstyle="danger ", command=change_platform, width=20)
    scratch_button.grid(pady=10, padx=0)
    # E-PIN button
    epin_button = tb.Button(my_frame, text="E-PIN", command=change_platform_epin, bootstyle="danger ", width=20)
    epin_button.grid(pady=10, padx=0)
    # Side bar Label
    my_label = tb.Label(my_frame, text="Running Updates", bootstyle=Theme[2], font=("Helvetica", 15))
    my_label.grid(pady=30, padx=(20, 20))
    # Running Programs
    runing_programs_button = tb.Button(my_frame, text=Running_program, state="disabled", bootstyle="success ", width=20)
    runing_programs_button.grid(pady=10, padx=0)

    # if Theme == LightTheme:
    #     # THEME button
    #     epin_button = tb.Button(root, text="Dark", command=change_theme, bootstyle="danger ", width=20)
    #     epin_button.grid( row=3,pady=10, padx=10, sticky=SE)
    # else:
    #     # THEME button
    #     epin_button = tb.Button(my_frame, text="Light", command=change_theme, bootstyle="danger ", width=20)
    #     epin_button.grid(pady=10, padx=0)

    # TOP frame
    verify = customtkinter.CTkFrame(root, fg_color=Theme[3], border_width=2, height=30, )
    verify.grid(padx=5, pady=10, column=2, row=1, sticky=NSEW)
    global top_frame_label
    # top fram label
    top_frame_label = tb.Label(verify, text="Scratch Card Platform", bootstyle=Theme[2], font=("Poppins", 15))
    top_frame_label.pack(pady=5)

    Policy_frame = tb.Frame(root, )
    Policy_frame.grid(padx=(5, 0), column=1, columnspan=2, row=2, sticky=NSEW)
    Policy_frame.columnconfigure((0, 1), weight=2)

    # frme
    reg_frame = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    reg_frame.grid(padx=5, pady=5, column=0, row=0, sticky=NSEW)

    label_radio_group = tb.Label(master=reg_frame, text="Reg Corrections")
    label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

    # create textbox
    reg_policy_number = tb.Label(master=reg_frame, text="Policy Number")
    reg_policy_number.grid(row=2, column=2, padx=10, pady=10, sticky="")
    global reg_policy_number_textbox
    reg_policy_number_textbox = tb.Entry(reg_frame, width=30, )
    reg_policy_number_textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

    reg_policy_number = tb.Label(master=reg_frame, text="Reg Number")
    reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
    global reg_number_textbox
    reg_number_textbox = tb.Entry(reg_frame, width=30)
    reg_number_textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    Reg_update_button = tb.Button(reg_frame, bootstyle="danger", text="Update", width=30,
                                  command=run_function_in_background)
    Reg_update_button.grid(row=4, column=3, padx=0, pady=10, )

    # frme
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=5, pady=5, column=1, row=0, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Chassis Corrections")
    label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

    # create textbox
    chassis_policy_number = tb.Label(master=f2, text="Policy Number")
    chassis_policy_number.grid(row=2, column=2, padx=10, pady=10, sticky="")
    chassis_policy_number_textbox = tb.Entry(f2, width=30, )
    chassis_policy_number_textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

    chassis_number = tb.Label(master=f2, text="Chassis Number")
    chassis_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
    chassis_number_textbox = tb.Entry(f2, width=30)
    chassis_number_textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    Chassis_update_button = tb.Button(f2, text="Update", bootstyle="danger", width=30, command=run_chassis_only_function_in_background)
    Chassis_update_button.grid(row=5, column=3, padx=0, pady=10, )

    # frme
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=5, pady=5, column=0, row=1, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Reg and Chassis Corrections")
    label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

    # create textbox
    reg_policy_number = tb.Label(master=f2, text="Policy Number")
    reg_policy_number.grid(row=2, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30, )
    textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

    reg_policy_number = tb.Label(master=f2, text="Chassis Number")
    reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30)
    textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    reg_policy_number = tb.Label(master=f2, text="Chassis Number2")
    reg_policy_number.grid(row=4, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30)
    textbox.grid(row=4, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    sidebar_button_1 = tb.Button(f2, text="Update", bootstyle="danger", width=30)
    sidebar_button_1.grid(row=5, column=3, padx=0, pady=10, )

    # frme
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=5, pady=5, column=1, row=1, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Change Name")
    label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

    # create textbox
    reg_policy_number = tb.Label(master=f2, text="Policy Number")
    reg_policy_number.grid(row=2, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30, )
    textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

    reg_policy_number = tb.Label(master=f2, text="First Name")
    reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30)
    textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    reg_policy_number = tb.Label(master=f2, text="Last Name")
    reg_policy_number.grid(row=4, column=2, padx=10, pady=10, sticky="")
    textbox = tb.Entry(f2, width=30)
    textbox.grid(row=4, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

    sidebar_button_1 = tb.Button(f2, text="Update", bootstyle="danger", width=30)
    sidebar_button_1.grid(row=5, column=3, padx=0, pady=10, )

    # Verify Policy
    verify = customtkinter.CTkFrame(root, fg_color=Theme[3], height=30, border_width=1)
    verify.grid(padx=5, pady=5, column=2, row=3, sticky=EW)

    reg_policy_number = tb.Label(master=verify, text="Verify Policy")
    reg_policy_number.grid(row=0, column=0, padx=10, pady=10, sticky="")
    textbox = tb.Entry(verify, width=30)
    textbox.grid(row=0, column=2, padx=(10, 20), pady=(10, 10), sticky="nsew")

    sidebar_button_1 = tb.Button(verify, text="Update", bootstyle="danger", width=30)
    sidebar_button_1.grid(row=0, column=3, padx=0, pady=10, )

    # my_label = tb.Label(reg_frame, text="Reg Correction",  bootstyle="inverse-dark", font=("Helvetica", 10) )
    # my_label.grid(column=0, pady=20,padx=(20, 20))
    #
    # my_label = tb.Label(reg_frame, text="Policy Number",  bootstyle="inverse-dark", font=("Helvetica", 10) )
    # my_label.grid(column=0, pady=20,padx=(20, 20))
    #
    # policy_input = Entry(reg_frame, width=30,)
    # policy_input.grid(column=1, row=1, padx=30)
    #
    # my_label = tb.Label(reg_frame, text="Reg Number",  bootstyle="inverse-dark", font=("Helvetica", 10) )
    # my_label.grid(column=0, pady=20,padx=(20, 20))
    #
    # policy_input = Entry(reg_frame, width=30,)
    # policy_input.grid(column=1, row=2, padx=30)

    root.mainloop()


if __name__ == '__main__':
    run_program()

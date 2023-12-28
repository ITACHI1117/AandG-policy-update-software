import threading
import time
from tkinter import *
import ttkbootstrap as tb
import customtkinter
from ttkbootstrap.toast import ToastNotification
from tkinter import messagebox

from Change_Name import change_name
from Chassis_Update import correct_chassisNO
from Niid_Reg_Correction import correct_regNoNiid
from Niid_RegandChassis_correction import correct_reg_and_chassisNo_Niid
from Niid_chassis_only import correct_chassisNo_Niid
from Reg_Update import correct_regNo

import multiprocessing

from RegandChasis_correction import correct_reg_and_chassisNO
from VerifyPolicy import verify_policy
from fetch_Reg_number import fetch_regNo
from fetch_RegandChassis_number import fetch_reg_and_chassisNO
from fetch_chassis_number import fetch_wrong_chassis
from PIL import ImageTk, Image

from Check_driver import Check_and_install_Updated_driver
from verify_policy_results_window import openNewWindow

LightTheme = ["pulse", "default", "default", "white"]
DarkTheme = ["cyborg", "dark", "default", "black"]
Theme = LightTheme

root = tb.Window(themename=Theme[0])
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('1300x700')
root.state('zoomed')

REG_POLICY_NUMBER = ""

# Functions
# Default Platform Scratch card Platform
email = 'mayowa_admin'
password = 'Gbohunmi17'
LINK = ["https://aginsuranceapplications.com/card/Index.aspx", email, password]

#verify policy data
data=""

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


SHOW_WINDOW = "null"
def run_program():


    # def run_Status_check_in_background():
    #     # Create a thread to run the long_running_function
    #     thread = threading.Thread(target=Check_and_install_Updated_driver)
    #     thread.start()

    # Check the driver Status
    Status = Check_and_install_Updated_driver()
    messagebox.showinfo("Driver verification",
                        Status)

    #Detremine if the chrome window will run headless or not
    def window_satus_on():
        global  SHOW_WINDOW
        show_window_button.config(bootstyle="success",text="ON", command=window_satus_off)
        SHOW_WINDOW = "null"
    def window_satus_off():
        global SHOW_WINDOW
        show_window_button.config(bootstyle="secondary",text="OFF", command=window_satus_on)
        SHOW_WINDOW = "--headless=new"

    # Close policy details frame
    def close():
        w.destroy()

    def fetch_reg_number():
        if reg_policy_number_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Input Reg and policy number")
            print("Input policy number")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data
            global REG_POLICY_NUMBER
            REG_POLICY_NUMBER = reg_policy_number_textbox.get()
            REG_NUMBER = reg_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                global SHOW_WINDOW
                print("Updating on A&G")
                INCORRECT_REGNUMBER, RETURNED_POLICY_NUMBER, RETURNED_REGNUMBER = fetch_regNo(REG_POLICY_NUMBER,
                                                                                                REG_NUMBER, LINK,
                                                                                                SHOW_WINDOW)
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
                    print(f"{INCORRECT_REGNUMBER}")
                    wrong_reg_number_textbox.insert("1", f"{INCORRECT_REGNUMBER}")
                    Running_program -= 1
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
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]

        # Fetch Wrong chassis number
    def fetch_wrong_chassis_number():
        global SHOW_WINDOW
        # Checking if enter is null
        if chassis_policy_number_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Enter the required field")
            print("Input policy number")
        else:
            global Running_program
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data

            CHASSIS_POLICY_NUMBER = chassis_policy_number_textbox.get()
            CHASSIS_NUMBER = chassis_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER, RETURNED_POLICY_NUMBER, WRONG_CHASSIS_NUMBER = fetch_wrong_chassis(
                    CHASSIS_POLICY_NUMBER, CHASSIS_NUMBER, LINK, SHOW_WINDOW)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(
                        f'Chassis Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                        f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print(f"{WRONG_CHASSIS_NUMBER}")
                    wrong_chassis_number_textbox.insert("1", f"{WRONG_CHASSIS_NUMBER}")
                    Running_program -= 1
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Chassis Number Correction Error',
                                     f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]

    def fetch_wrong_reg_and_chassis_number():
        global SHOW_WINDOW
        # Checking if enter is null
        if regNchassis_policy_number_textbox.get() == "" :
            messagebox.showerror("Error",
                                 f"Enter the required fields")
            print("Enter the Policy Number")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")


            # get Entry data

            REGnCHASSIS_POLICY_NUMBER = regNchassis_policy_number_textbox.get()
            REGnCHASSIS_REG_NUMBER = regNchassis_reg_number_textbox.get()
            REGnCHASSIS_CHASSIS_NUMBER = regNchassis_chassis_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                WRONG_REGNUMBER_RandC, RETURNED_POLICY_NUMBER, WRONG_CHASSIS_NUMBER_RandC, RETURNED_REGNUMBER = fetch_reg_and_chassisNO(
                    REGnCHASSIS_POLICY_NUMBER,
                    REGnCHASSIS_REG_NUMBER, REGnCHASSIS_CHASSIS_NUMBER, LINK, SHOW_WINDOW)
                if WRONG_REGNUMBER_RandC == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(
                        f'Reg and Chassis Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                        f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print(f"{WRONG_CHASSIS_NUMBER_RandC}")
                    print(f"{WRONG_REGNUMBER_RandC}")
                    regNchassis_Wchassis_number_textbox.insert("1", f"{WRONG_CHASSIS_NUMBER_RandC}")
                    regNchassis_Wreg_number_textbox.insert("1", f"{WRONG_REGNUMBER_RandC}")
                    Running_program -= 1
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Reg and Chassis Number Correction Error',
                                     f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]

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
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data
            global REG_POLICY_NUMBER
            REG_POLICY_NUMBER = reg_policy_number_textbox.get()
            REG_NUMBER = reg_number_textbox.get()
            WRONG_REGNUMBER = wrong_reg_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                global SHOW_WINDOW
                print("Updating on A&G")

                INCORRECT_REGNUMBER, RETURNED_POLICY_NUMBER, RETURNED_REGNUMBER = correct_regNo(REG_POLICY_NUMBER,
                                                                                                REG_NUMBER, LINK,SHOW_WINDOW)
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
                    correct_regNoNiid(RETURNED_POLICY_NUMBER, RETURNED_REGNUMBER, INCORRECT_REGNUMBER,WRONG_REGNUMBER,SHOW_WINDOW)
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
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]




    #Chassis only correction function
    def update_chassis_update_only():
        global SHOW_WINDOW
        # Checking if enter is null
        if chassis_policy_number_textbox.get() == "" or chassis_number_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Enter the required field")
            print("Input Reg and policy number")
        else:
            global Running_program
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data

            CHASSIS_POLICY_NUMBER = chassis_policy_number_textbox.get()
            CHASSIS_NUMBER = chassis_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER, RETURNED_POLICY_NUMBER, RETURNED_CHASSIS_NUMBER = correct_chassisNO(
                    CHASSIS_POLICY_NUMBER, CHASSIS_NUMBER, LINK,SHOW_WINDOW)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(
                        f'Chassis Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                        f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print("Updating on NIID")
                    correct_chassisNo_Niid(RETURNED_POLICY_NUMBER, INCORRECT_REGNUMBER, RETURNED_CHASSIS_NUMBER,SHOW_WINDOW)
                    Running_program -= 1
                    messagebox.showinfo("Chassis Number Correction Successful",
                                        f"The Policy {RETURNED_POLICY_NUMBER} has been updated ✅")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Chassis Number Correction Error',
                                        f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]


    # Reg and chassis number correction function
    def update_reg_and_chassis_number():
        global SHOW_WINDOW
        # Checking if enter is null
        if regNchassis_policy_number_textbox.get() == "" or regNchassis_reg_number_textbox.get() == "" or regNchassis_chassis_number_textbox == "":
            messagebox.showerror("Error",
                                 f"Enter the required fields")
            print("Enter the required fields")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data

            REGnCHASSIS_POLICY_NUMBER = regNchassis_policy_number_textbox.get()
            REGnCHASSIS_REG_NUMBER = regNchassis_reg_number_textbox.get()
            REGnCHASSIS_CHASSIS_NUMBER = regNchassis_chassis_number_textbox.get()
            WRONG_REG_NUMBER_RandC = regNchassis_Wreg_number_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER,RETURNED_POLICY_NUMBER,RETURNED_CHASSIS_NUMBER,RETURNED_REGNUMBER = correct_reg_and_chassisNO(REGnCHASSIS_POLICY_NUMBER,
                                                                                                REGnCHASSIS_REG_NUMBER,REGnCHASSIS_CHASSIS_NUMBER,LINK,SHOW_WINDOW)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(f'Reg and Chassis Number Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                                         f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    print("Updating on NIID")
                    correct_reg_and_chassisNo_Niid(RETURNED_POLICY_NUMBER,RETURNED_REGNUMBER,INCORRECT_REGNUMBER,RETURNED_CHASSIS_NUMBER,WRONG_REG_NUMBER_RandC,SHOW_WINDOW)
                    Running_program -= 1
                    messagebox.showinfo("Reg and Chassis Number Correction Successful",
                                        f"The Policy {RETURNED_POLICY_NUMBER} has been updated ✅")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Reg and Chassis Number Correction Error',
                                     f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]

    def update_name_num():
        global  SHOW_WINDOW
        # Checking if enter is null
        if name_change_policy_number_textbox.get() == "" or first_name_textbox.get() == "" or last_name_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Enter the required fields")
            print("Enter the required fields")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data

            NAME_POLICY_NUMBER = name_change_policy_number_textbox.get()
            FIRST_NAME = first_name_textbox.get()
            LAST_NAME = last_name_textbox.get()

            RETURNED_POLICY_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                INCORRECT_REGNUMBER,RETURNED_POLICY_NUMBER = change_name(NAME_POLICY_NUMBER,FIRST_NAME,LAST_NAME,LINK,SHOW_WINDOW)
                if INCORRECT_REGNUMBER == "Sorry. The Policy Number you entered does not exist or may have expired and has not been renewed":
                    Running_program -= 1
                    print(
                        f"Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist or may have expired and has not been renewed")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(f'Name Correction [Invalid policy Number  {RETURNED_POLICY_NUMBER}]',
                                         f'Sorry. The Policy Number {RETURNED_POLICY_NUMBER} you entered does not exist \n or may have expired and has not been renewed')
                    # openNewWindow(root, f"")
                    return
                else:
                    Running_program -= 1
                    messagebox.showinfo("Name Correction Successful",
                                        f"The Policy {RETURNED_POLICY_NUMBER} has been updated ✅")
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
            except Exception as error:
                # print(error)
                messagebox.showerror(f'Name Correction Error',
                                     f'Policy Number {RETURNED_POLICY_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")

            if Running_program == 0:
                runing_programs_button.config(state="disabled")

            return [Running_program]



    def verify_policy_by_certi():
        global SHOW_WINDOW
        # Checking if enter is null
        if verify_reg_policy_number_textbox.get() == "":
            messagebox.showerror("Error",
                                 f"Enter the required fields")
            print("Enter the required fields")
        else:
            global Running_program
            print(Running_program)
            print("Starting")
            # Getting the errors if there are any
            Running_program += 1
            runing_programs_button.config(text=Running_program, state="enabled")

            if Running_program == 5:
                Reg_update_button.config(state="disabled")
                Chassis_update_button.config(state="disabled")
                Reg_and_Chassis_Update_button.config(state="disabled")
                Name_change_button.config(state="disabled")
                verify_button.config(state="disabled")
                Reg_fetch_button.config(state="disabled")
                Chassis_fetch_button.config(state="disabled")
                Reg_and_Chassis_Fetch_button.config(state="disabled")

            # get Entry data

            CERTI_NUMBER = verify_reg_policy_number_textbox.get()

            RETURNED_CERTI_NUMBER = "Unknown"

            try:
                print("Updating on A&G")
                DATA, RETURNED_CERTI_NUMBER = verify_policy(CERTI_NUMBER,SHOW_WINDOW)
                if DATA == "There is no Existing Policy Record for the Certificate Number you Typed":
                    Running_program -= 1
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    # print("There was an error")
                    messagebox.showerror(f'No Record for {RETURNED_CERTI_NUMBER}',
                                         f'There is no Existing Policy Record for the Certificate Number you Typed')
                    runing_programs_button.config(state="disabled")
                    # openNewWindow(root, f"")
                    return
                else:
                    Running_program -= 1
                    print(DATA)
                    delimiter = "\n"
                    data = delimiter.join(DATA)
                    # show verified policy
                    global w
                    w = Text(root, height=10, borderwidth=2, )
                    w.insert(1.0, f"{data}")

                    w.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW)
                    # h.config(command=w.xview)
                    # v.config(command=w.yview)
                    w.configure(state="disabled")
                    # openNewWindow(root, data)
                    runing_programs_button.config(text=Running_program)
                    Reg_update_button.config(state="enabled")
                    print(Running_program)
                    time.sleep(1)

            except Exception as error:
                print(error)
                messagebox.showerror(f'Verify Policy Error',
                                     f'Certificate Number {RETURNED_CERTI_NUMBER} \n {error}')
                Running_program -= 1
                runing_programs_button.config(text=Running_program)
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")
            finally:
                Reg_update_button.config(state="enabled")
                Chassis_update_button.config(state="enabled")
                Reg_and_Chassis_Update_button.config(state="enabled")
                Name_change_button.config(state="enabled")
                verify_button.config(state="enabled")
                Reg_fetch_button.config(state="enabled")
                Chassis_fetch_button.config(state="enabled")
                Reg_and_Chassis_Fetch_button.config(state="enabled")



            if Running_program == 0:
                runing_programs_button.config(state="disabled")


            return [Running_program]


    #REg update and fetch
    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_reg_number)
        thread.start()

    def run_fetch_reg_number_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=fetch_reg_number)
        thread.start()

    #Chassis only Update and fetch
    def run_chassis_only_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_chassis_update_only)
        thread.start()

    def run_fetch_chassis_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=fetch_wrong_chassis_number)
        thread.start()

    def run_reg_and_chassis_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_reg_and_chassis_number)
        thread.start()

    def run_fetch_reg_and_chassis_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=fetch_wrong_reg_and_chassis_number)
        thread.start()

    def run_name_change_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_name_num)
        thread.start()
    def run_verify_policy_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=verify_policy_by_certi)
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

    img = ImageTk.PhotoImage(Image.open("AandGlogo.jpeg"))

    label = Label(my_frame, image=img)
    label.grid()

    # Scratch card button
    scratch_button = tb.Button(my_frame, text="Scratch Card", bootstyle="danger ", command=change_platform, width=20)
    scratch_button.grid(pady=10, padx=0)
    # E-PIN button
    epin_button = tb.Button(my_frame, text="E-PIN", command=change_platform_epin, bootstyle="danger ", width=20)
    epin_button.grid(pady=10, padx=0)
    # Side bar Label
    my_label = tb.Label(my_frame, text="Running Updates", bootstyle=Theme[2], font=("Helvetica", 15))
    my_label.grid(pady=10, padx=(20, 20))
    # Running Programs
    runing_programs_button = tb.Button(my_frame, text=Running_program, state="disabled", bootstyle="success ", width=20)
    runing_programs_button.grid(pady=5, padx=0)

    my_label = tb.Label(my_frame, text="Show Chrome Window", bootstyle=Theme[2], font=("Helvetica", 12))
    my_label.grid(pady=10, padx=(20, 20))

    show_window_button = tb.Button(my_frame, text="ON", state="enabled", bootstyle="success", width=20, command=window_satus_off)
    show_window_button.grid(pady=0, padx=0)

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
    Policy_frame.columnconfigure((0,1), weight=2)

    # frme
    reg_frame = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    reg_frame.grid(padx=2, pady=2, column=0, row=0, sticky=NSEW)

    label_radio_group = tb.Label(master=reg_frame, text="Reg Corrections")
    label_radio_group.grid(row=0, column=3, padx=5, pady=5, )

    # create textbox
    reg_policy_number = tb.Label(master=reg_frame, text="Policy Number")
    reg_policy_number.grid(row=2, column=2, padx=2, pady=2, sticky="")
    global reg_policy_number_textbox
    reg_policy_number_textbox = tb.Entry(reg_frame, width=30, )
    reg_policy_number_textbox.grid(row=2, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    reg_policy_number = tb.Label(master=reg_frame, text="Reg Number")
    reg_policy_number.grid(row=3, column=2, padx=2, pady=2, sticky="")

    global reg_number_textbox
    reg_number_textbox = tb.Entry(reg_frame, width=30)
    reg_number_textbox.grid(row=3, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")


    wrong_reg_number = tb.Label(master=reg_frame, text="Wrong Reg Number")
    wrong_reg_number.grid(row=4, column=2, padx=2, pady=2, sticky="")

    global wrong_reg_number_textbox
    wrong_reg_number_textbox = tb.Entry(reg_frame, width=30,)
    wrong_reg_number_textbox.grid(row=4, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")





    Reg_update_button = tb.Button(reg_frame, bootstyle="danger", text="Update", width=20,
                                  command=run_function_in_background)
    Reg_update_button.grid(row=5, column=2, padx=20, pady=10, )

    Reg_fetch_button = tb.Button(reg_frame, bootstyle="success", text="Fetch", width=20,
                                  command=run_fetch_reg_number_function_in_background)
    Reg_fetch_button.grid(row=5, column=3, padx=0, pady=10, )

    # frme
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=2, pady=2, column=1, row=0, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Chassis Corrections")
    label_radio_group.grid(row=0, column=3, padx=5, pady=5, )

    # create textbox
    chassis_policy_number = tb.Label(master=f2, text="Policy Number")
    chassis_policy_number.grid(row=2, column=2, padx=2, pady=2, sticky="")
    chassis_policy_number_textbox = tb.Entry(f2, width=30, )
    chassis_policy_number_textbox.grid(row=2, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    chassis_number = tb.Label(master=f2, text="Chassis Number")
    chassis_number.grid(row=3, column=2, padx=2, pady=2, sticky="")
    chassis_number_textbox = tb.Entry(f2, width=30)
    chassis_number_textbox.grid(row=3, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    wrong_chassis_number = tb.Label(master=f2, text="Wrong Chassis Number")
    wrong_chassis_number.grid(row=4, column=2, padx=2, pady=2, sticky="")
    global wrong_chassis_number_textbox
    wrong_chassis_number_textbox = tb.Entry(f2, width=30)
    wrong_chassis_number_textbox.grid(row=4, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    Chassis_update_button = tb.Button(f2, text="Update", bootstyle="danger", width=20, command=run_chassis_only_function_in_background)
    Chassis_update_button.grid(row=5, column=2, padx=20, pady=10, )

    Chassis_fetch_button = tb.Button(f2, bootstyle="success", text="Fetch", width=20,
                                 command=run_fetch_chassis_in_background)
    Chassis_fetch_button.grid(row=5, column=3, padx=0, pady=10, )

    # frAme
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=2, pady=2, column=0, row=1, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Reg and Chassis Corrections")
    label_radio_group.grid(row=0, column=3, padx=2, pady=2, )

    # create textbox
    regNchassis_policy_number = tb.Label(master=f2, text="Policy Number")
    regNchassis_policy_number.grid(row=2, column=2, padx=2, pady=2, sticky="")
    regNchassis_policy_number_textbox = tb.Entry(f2, width=30, )
    regNchassis_policy_number_textbox.grid(row=2, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    regNchassis_reg_number = tb.Label(master=f2, text="Reg Number")
    regNchassis_reg_number.grid(row=3, column=2, padx=2, pady=2, sticky="")
    regNchassis_reg_number_textbox = tb.Entry(f2, width=30)
    regNchassis_reg_number_textbox.grid(row=3, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    regNchassis_Wreg_number = tb.Label(master=f2, text="Wrong Reg Number")
    regNchassis_Wreg_number.grid(row=4, column=2, padx=2, pady=2, sticky="")
    regNchassis_Wreg_number_textbox = tb.Entry(f2, width=30)
    regNchassis_Wreg_number_textbox.grid(row=4, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    regNchassis_chassis_number = tb.Label(master=f2, text="Chassis Number")
    regNchassis_chassis_number.grid(row=5, column=2, padx=2, pady=2, sticky="")
    regNchassis_chassis_number_textbox = tb.Entry(f2, width=30)
    regNchassis_chassis_number_textbox.grid(row=5, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    regNchassis_Wchassis_number = tb.Label(master=f2, text="Wrong Chassis Number")
    regNchassis_Wchassis_number.grid(row=6, column=2, padx=2, pady=2, sticky="")
    regNchassis_Wchassis_number_textbox = tb.Entry(f2, width=30)
    regNchassis_Wchassis_number_textbox.grid(row=6, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")



    Reg_and_Chassis_Update_button = tb.Button(f2, text="Update", bootstyle="danger", width=20, command=run_reg_and_chassis_function_in_background)
    Reg_and_Chassis_Update_button.grid(row=7, column=2, padx=10, pady=10, )

    Reg_and_Chassis_Fetch_button = tb.Button(f2, text="Fetch", bootstyle="success", width=20,
                                              command=run_fetch_reg_and_chassis_function_in_background)
    Reg_and_Chassis_Fetch_button.grid(row=7, column=3, padx=10, pady=10, )

    # change name frame
    f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    f2.grid(padx=5, pady=5, column=1, row=1, sticky=NSEW)

    label_radio_group = tb.Label(master=f2, text="Change Name")
    label_radio_group.grid(row=0, column=3, padx=10, pady=10, )

    # create textbox
    name_change_policy_number = tb.Label(master=f2, text="Policy Number")
    name_change_policy_number.grid(row=2, column=2, padx=10, pady=2, sticky="")
    name_change_policy_number_textbox = tb.Entry(f2, width=30, )
    name_change_policy_number_textbox.grid(row=2, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    first_name = tb.Label(master=f2, text="First Name")
    first_name.grid(row=3, column=2, padx=2, pady=2, sticky="")
    first_name_textbox = tb.Entry(f2, width=30)
    first_name_textbox.grid(row=3, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    last_name = tb.Label(master=f2, text="Last Name")
    last_name.grid(row=4, column=2, padx=2, pady=2, sticky="")
    last_name_textbox = tb.Entry(f2, width=30)
    last_name_textbox.grid(row=4, column=3, padx=(2, 2), pady=(2, 2), sticky="nsew")

    Name_change_button = tb.Button(f2, text="Update", bootstyle="danger", width=30, command=run_name_change_function_in_background)
    Name_change_button.grid(row=5, column=3, padx=0, pady=10, )


    # f2 = customtkinter.CTkFrame(Policy_frame, fg_color=Theme[3], border_width=2)
    # f2.grid(padx=5, pady=5, column=0, row=2, sticky=NSEW)
    #
    # label_radio_group = tb.Label(master=f2, text="Policy Result")
    # label_radio_group.grid(row=0, column=2, padx=5, pady=5, )
    #


    # Verify Policy
    verify = customtkinter.CTkFrame(root, fg_color=Theme[3], height=100, border_width=1)
    verify.grid(padx=5, pady=5, column=2, row=300, sticky=EW)

    verify_reg_policy_number = tb.Label(master=verify, text="Verify Policy")
    verify_reg_policy_number.grid(row=0, column=0, padx=10, pady=10, sticky="")
    verify_reg_policy_number_textbox = tb.Entry(verify, width=30)
    verify_reg_policy_number_textbox.grid(row=0, column=2, padx=(10, 20), pady=(10, 10), sticky="nsew")

    verify_button = tb.Button(verify, text="Verify", bootstyle="danger", width=30, command=run_verify_policy_function_in_background)
    verify_button.grid(row=0, column=3, padx=0, pady=10, )

    verify_close_button = tb.Button(verify, text="Close", bootstyle="warning", width=30,
                              command=close)
    verify_close_button.grid(row=0, column=4, padx=10, pady=10, )



    root.mainloop()


if __name__ == '__main__':
    run_program()

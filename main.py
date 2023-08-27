from tkinter import *
import ttkbootstrap as tb
import customtkinter
from ttkbootstrap.toast import ToastNotification

from Niid_Reg_Correction import correct_regNoNiid
from Reg_Update import correct_regNo

root = tb.Window(themename="cyborg")
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('1240x600')

REG_POLICY_NUMBER = ""



#Functions
# Default Platform Scratch card Platform
email = 'mayowa_admin'
password = 'Gbohunmi17'
LINK = ["https://aginsuranceapplications.com/card/Index.aspx",email,password]
print(LINK)

#Change Platform to Scratch Card
def change_platform():
    global LINK
    email = 'mayowa_admin'
    password = 'Gbohunmi17'
    LINK = ["https://aginsuranceapplications.com/card/Index.aspx",email,password]
    print(LINK)
    top_frame_label.config(text="Scratch Card Platform")

#Change Platform to E_PIN
def change_platform_epin():
    global LINK
    email = 'mayowa1022'
    password = 'Gbohunmi17'
    LINK = ["https://aginsuranceapplications.com/",email,password]
    print(LINK)
    top_frame_label.config(text="E-PIN Platform")

# Update Reg Number Function
def update_reg_number():
    # get Entry data
    global REG_POLICY_NUMBER
    REG_POLICY_NUMBER = reg_policy_number_textbox.get()
    REG_NUMBER = reg_number_textbox.get()

    # Checking if enter is null
    if reg_policy_number_textbox.get() == "" or reg_number_textbox.get() == "":
        print("Input Reg and policy number")
    else:
        print("startting")

        INCORRECT_REGNUMBER = correct_regNo(REG_POLICY_NUMBER, REG_NUMBER,LINK)
        RegUpdateToast = ToastNotification(
            title=f"Policy Updated!✅",
            message=f"Policy {REG_POLICY_NUMBER} has been Updated on A&G Platform",
            duration=9000,
            bootstyle="dark",

            alert=True

        )
        RegUpdateToast.show_toast()
        print("startting")
        correct_regNoNiid(REG_POLICY_NUMBER,REG_NUMBER,INCORRECT_REGNUMBER)
        RegUpdateToast2 = ToastNotification(
            title=f"Policy Updated!✅",
            message=f"Policy {REG_POLICY_NUMBER} has been Updated on NIID Platform",
            duration=9000,
            bootstyle="dark",

            alert=True

        )
        RegUpdateToast2.show_toast()
        print("Done")
        print(reg_policy_number_textbox.get())
        print(reg_number_textbox.get())


#Reg frame
root.columnconfigure(2, weight=1)
# root.columnconfigure(1, weight=3)
root.rowconfigure(2, weight=2)


#Side bar
my_frame = tb.Frame(root, bootstyle="dark" , height=300)
my_frame.grid(row=0, column=0, rowspan=4, sticky=NS)
my_frame.grid_rowconfigure(4, weight=2)


#Side bar Label
my_label = tb.Label(my_frame, text="A&G Policy\nUpdater", bootstyle="inverse-dark", font=("Helvetica", 18) )
my_label.grid(pady=30,padx=(20, 20))

# Scratch card button
scratch_button = tb.Button(my_frame, text="Scratch Card", bootstyle="danger ", command=change_platform, width=20)
scratch_button.grid(pady=10, padx=0)
#E-PIN button
epin_button = tb.Button(my_frame, text="E-PIN", command=change_platform_epin, bootstyle="danger ", width=20)
epin_button.grid(pady=10, padx=0)

#TOP frame
verify = tb.Frame(root, bootstyle="dark",  height=30,)
verify.grid(padx=5, pady=10,  column=2, row=1, sticky=NSEW)

#top fram label
top_frame_label = tb.Label(verify,text="Scratch Card Platform", bootstyle="dark inverse", font=("Poppins", 15))
top_frame_label.pack(pady=5)



Policy_frame = tb.Frame(root, )
Policy_frame.grid(padx=(5,0), column=1, columnspan=2, row=2, sticky=NSEW)
Policy_frame.columnconfigure((0,1), weight=2)



#frme
reg_frame = customtkinter.CTkFrame(Policy_frame, fg_color="black",  border_width=1)
reg_frame.grid(padx=5, pady=5, column=0, row=0, sticky=NSEW)

label_radio_group = tb.Label(master=reg_frame, text="Reg Corrections")
label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

# create textbox
reg_policy_number = tb.Label(master=reg_frame, text="Policy Number")
reg_policy_number.grid(row=2, column=2,  padx=10, pady=10, sticky="")
reg_policy_number_textbox = tb.Entry(reg_frame, width=30,)
reg_policy_number_textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

reg_policy_number = tb.Label(master=reg_frame, text="Reg Number")
reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
reg_number_textbox = tb.Entry(reg_frame, width=30)
reg_number_textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

sidebar_button_1 = tb.Button(reg_frame, bootstyle="danger", text="Update",width=30, command=update_reg_number)
sidebar_button_1.grid(row=4, column=3, padx=0, pady=10, )

#frme
f2 = customtkinter.CTkFrame(Policy_frame, fg_color="black" , border_width=2)
f2.grid(padx=5, pady=5, column=1, row=0, sticky=NSEW)

label_radio_group = tb.Label(master=f2, text="Chassis Corrections")
label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

# create textbox
reg_policy_number = tb.Label(master=f2, text="Policy Number")
reg_policy_number.grid(row=2, column=2,  padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30,)
textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

reg_policy_number = tb.Label(master=f2, text="Chassis Number")
reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30)
textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

sidebar_button_1 = tb.Button(f2, text="Update", bootstyle="danger",width=30)
sidebar_button_1.grid(row=5, column=3, padx=0, pady=10, )


#frme
f2 = customtkinter.CTkFrame(Policy_frame, fg_color="black" , border_width=2)
f2.grid(padx=5, pady=5, column=0, row=1, sticky=NSEW)

label_radio_group = tb.Label(master=f2, text="Reg and Chassis Corrections")
label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

# create textbox
reg_policy_number = tb.Label(master=f2, text="Policy Number")
reg_policy_number.grid(row=2, column=2,  padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30,)
textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

reg_policy_number = tb.Label(master=f2, text="Chassis Number")
reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30)
textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

reg_policy_number = tb.Label(master=f2, text="Chassis Number2")
reg_policy_number.grid(row=4, column=2, padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30)
textbox.grid(row=4, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

sidebar_button_1 = tb.Button(f2, text="Update", bootstyle="danger",width=30)
sidebar_button_1.grid(row=5, column=3, padx=0, pady=10, )

#frme
f2 = customtkinter.CTkFrame(Policy_frame, fg_color="black" , border_width=2)
f2.grid(padx=5, pady=5, column=1, row=1, sticky=NSEW)

label_radio_group = tb.Label(master=f2, text="Change Name")
label_radio_group.grid(row=0, column=2, padx=10, pady=10, )

# create textbox
reg_policy_number = tb.Label(master=f2, text="Policy Number")
reg_policy_number.grid(row=2, column=2,  padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30,)
textbox.grid(row=2, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

reg_policy_number = tb.Label(master=f2, text="First Name")
reg_policy_number.grid(row=3, column=2, padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30)
textbox.grid(row=3, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

reg_policy_number = tb.Label(master=f2, text="Last Name")
reg_policy_number.grid(row=4, column=2, padx=10, pady=10, sticky="")
textbox = tb.Entry(f2, width=30)
textbox.grid(row=4, column=3, padx=(10, 20), pady=(10, 10), sticky="nsew")

sidebar_button_1 = tb.Button(f2, text="Update", bootstyle="danger",width=30)
sidebar_button_1.grid(row=5, column=3, padx=0, pady=10, )


#Verify Policy
verify = customtkinter.CTkFrame(root, fg_color="black" , height=30, border_width=1)
verify.grid(padx=5, pady=5, column=2, row=3, sticky=EW)

reg_policy_number = tb.Label(master=verify, text="Verify Policy")
reg_policy_number.grid(row=0, column=0, padx=10, pady=10, sticky="")
textbox = tb.Entry(verify, width=30)
textbox.grid(row=0, column=2, padx=(10, 20), pady=(10, 10), sticky="nsew")

sidebar_button_1 = tb.Button(verify, text="Update", bootstyle="danger",width=30)
sidebar_button_1.grid(row=0, column=3, padx=0, pady=10,)


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
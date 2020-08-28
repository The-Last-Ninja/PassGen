import pyperclip
from random import choice, shuffle
from string import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *


# Function for generating password
def gen_pwd(new_pwd, passlen, pwdmtrs, lower, upper, numbers, specials, msg, msg_box, status_bar):

    length = passlen.get()

    lowercase = ascii_lowercase

    uppercase = ascii_uppercase

    specs = punctuation

    nums = digits

    msg1 = "Error!"

    msg2 = "Weak"

    msg3 = "Medium"

    msg4 = "Strong"

    msg5 = "Very Strong"

    new_passwd = ""

    pwd_type = 0

    status_bar.config(text="Done")

    # If checkbox(es) for lowercase, uppercase, numbers and special characters are checked
    if lower.get() == 1 and upper.get() == 0 and numbers.get() == 0 and specials.get() == 0:
        pwd_type = 1
    elif lower.get() == 1 and upper.get() == 1 and numbers.get() == 0 and specials.get() == 0:
        pwd_type = 2
    elif lower.get() == 1 and upper.get() == 1 and numbers.get() == 1 and specials.get() == 0:
        pwd_type = 3
    elif lower.get() == 1 and upper.get() == 1 and numbers.get() == 1 and specials.get() == 1:
        pwd_type = 4
    elif lower.get() == 0 and upper.get() == 0 and numbers.get() == 1 and specials.get() == 0:
        pwd_type = 5
    elif lower.get() == 1 and upper.get() == 1 and numbers.get() == 0 and specials.get() == 1:
        pwd_type = 6
    else:
        msg.set(msg1)

    # Generate a password with lowercase
    if pwd_type == 1:
        for i in range(0, length):
            new_passwd += choice(lowercase)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)

    # Generate a password with lowercase and uppercase
    elif pwd_type == 2:
        for x in range(0, length):
            new_passwd += choice(lowercase + uppercase)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)

    # Generate a password with lowercase, uppercase and numbers
    elif pwd_type == 3:
        for y in range(0, length):
            new_passwd += choice(lowercase + uppercase + nums)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)

    # Generate a password with lowercase, uppercase, numbers and special characters
    elif pwd_type == 4:
        for z in range(0, length):
            new_passwd += choice(lowercase + uppercase + nums + specs)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)

    # Generate a password with numbers for PIN number
    elif pwd_type == 5:
        for n in range(0, length):
            new_passwd += choice(nums)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)

    # Generate a password with lowercase, uppercase and special characters
    elif pwd_type == 6:
        for s in range(0, length):
            new_passwd += choice(lowercase + uppercase + specs)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        new_pwd.set(new_passwd)
    else:
        msg.set(msg1)

    # Warning message will appear if password length is less than 10
    # It will displays "Weak" if length is less than 10, "Medium" if length is less than or equals to 20,
    # "Strong" if length is less than or equals to 30 and "Very Strong" if length is more than 30.
    # Password meter will change depending on length
    if length < 10:
        messagebox.showwarning(title="Error Occurred", message="Password length cannot be less than 10")
        pwdmtrs.set(10)
        msg.set(msg2)
        msg_box.config(foreground="Red")
        msg_box.config(background="Gray")
    elif length < 10 and pwd_type == 0:
        messagebox.showwarning(title="Error Occurred", message="Please select a box")
        pwdmtrs.set(0)
        msg.set(msg1)
        msg_box.config(foreground="Yellow")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 0:
        messagebox.showwarning(title="Error Occurred", message="Please select a box")
        pwdmtrs.set(0)
        msg.set(msg1)
        msg_box.config(foreground="Yellow")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 1:
        pwdmtrs.set(20)
        msg.set(msg2)
        msg_box.config(foreground="Red")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 2:
        pwdmtrs.set(20)
        msg.set(msg2)
        msg_box.config(foreground="Red")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 2:
        pwdmtrs.set(20)
        msg.set(msg2)
        msg_box.config(foreground="Red")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 3:
        pwdmtrs.set(20)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 4:
        pwdmtrs.set(20)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 20 and pwd_type == 6:
        pwdmtrs.set(20)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 0:
        messagebox.showwarning(title="Error Occurred", message="Please select a box")
        pwdmtrs.set(0)
        msg.set(msg1)
        msg_box.config(foreground="Yellow")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 1:
        pwdmtrs.set(30)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 2:
        pwdmtrs.set(35)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 3:
        pwdmtrs.set(40)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 4:
        pwdmtrs.set(45)
        msg.set(msg4)
        msg_box.config(foreground="Green")
        msg_box.config(background="Gray")
    elif length <= 30 and pwd_type == 6:
        pwdmtrs.set(50)
        msg.set(msg3)
        msg_box.config(foreground="Blue")
        msg_box.config(background="Gray")
    elif length > 30 and pwd_type == 0:
        messagebox.showwarning(title="Error Occurred", message="Please select a box")
        pwdmtrs.set(0)
        msg.set(msg1)
        msg_box.config(background="Gray")
        msg_box.config(foreground="Yellow")
    elif length > 30 and pwd_type == 1:
        pwdmtrs.set(0)
        msg.set(msg1)
        msg_box.config(background="Gray")
        msg_box.config(foreground="Yellow")
    else:
        pwdmtrs.set(100)
        msg.set(msg5)
        msg_box.config(background="Gray")
        msg_box.config(foreground="Black")


# Function for saving a password into a text file
def save_file(pwd_entry, status_bar):
    
    # this will write password.txt file
    file_write = open("password.txt", "w")
    
    # Getting password from entry box
    save_write = pwd_entry.get()
    
    # Writing a file to save 
    file_write.write(save_write)
     
    file_write.close()

    status_bar.config(text="Saved")


# Function for asking where to save a password files
def save_as_file(pwd_entry, status_bar):
    
    # Options for files
    files = [('All Files', '*.*'),
             ('Password File', '*.pwd'),
             ('Text Document', '*.txt')]
    
    file_save = filedialog.asksaveasfile(mode="w", filetypes=files, defaultextension=files)

    save_pwd = pwd_entry.get()

    file_save.write(save_pwd)

    file_save.close()

    status_bar.config(text="Saved")


# Function for copying password into a clipboard
def copy_pwd(new_pwd, passwd_app, status_bar):

    pwd_entry = tk.Entry(passwd_app, textvariable=new_pwd, width=25, font='Arial 10',
                         background="Gray", foreground="Black")
    pwd_entry.grid(row=9, column=3)
    
    # Getting a value(Password) from pwd_entry
    cp_pwd = pwd_entry.get()
    
    # Copying password using pyperclip module
    pyperclip.copy(cp_pwd)
    
    # Deletes password in a pwd_entry
    pwd_entry.delete(0, END)
    
    # Entry box color will change into white
    pwd_entry.config(background="White")
    
    # Disables entry box
    pwd_entry.config(state=DISABLED)
    
    # Display "Copied" message in a status bar
    status_bar.config(text="Copied")


# Function for showing a password when "Show" button is pressed
def show_pwd(passwd_app, new_pwd):

    pwd_entry = tk.Entry(passwd_app, textvariable=new_pwd, state=DISABLED,
                         width=25, font='Arial 10', background="Gray", foreground="Black", relief=SUNKEN)
    pwd_entry.grid(row=9, column=3)


# Function for hiding a password when "Hide" button is pressed
def hide_pwd(passwd_app, new_pwd):

    pwd_entry = tk.Entry(passwd_app, textvariable=new_pwd, state=DISABLED, width=25, font='Arial 10',
                         show="*", background="Gray", foreground="Black", relief=SUNKEN)
    pwd_entry.grid(row=9, column=3)


# Function for exiting a program and save a password
def exit_prgm(passwd_app, pwd_entry, status_bar):

    exit_msg = tk.messagebox.askyesno(title="Exiting Program", message="Would you like to save before exiting?")
    
    # It will save a password file if "Yes" option is pressed
    if exit_msg == 1:
        save_as_file(pwd_entry, status_bar)
    else:
        passwd_app.quit()


# Entry point of this program and display an app
def main():

    passwd_app = tk.Tk()

    passlen = IntVar()

    pwdmtrs = IntVar()

    lower = IntVar()

    upper = IntVar()

    numbers = IntVar()

    specials = IntVar()

    new_pwd = StringVar()

    msg = StringVar()

    passwd_app.title("Password Generator")

    passwd_app.configure(bg='gray')

    passwd_app.geometry('750x350')
    
    # Set up a menubar to save, save as and exit
    menubar = Menu(passwd_app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save", command=lambda: save_file(pwd_entry, status_bar))
    filemenu.add_command(label="Save as", command=lambda: save_as_file(pwd_entry, status_bar))
    filemenu.add_command(label="Exit", command=lambda: exit_prgm(passwd_app, pwd_entry, status_bar))
    menubar.add_cascade(label="File", menu=filemenu)
    passwd_app.config(menu=menubar)
    
    # Set up a title label
    title_txt = Label(passwd_app, text="Password Generator", font='Arial 22 bold', background="Gray")
    title_txt.grid(row=0, column=3)
    
    # Set up checkbox options
    btn_box = tk.LabelFrame(passwd_app, text="Checkbox options", font='Arial 12', background="Gray")
    btn_box.grid(row=1, column=3, pady=5)
    lower_btn = tk.Checkbutton(btn_box, text="Lowercase", variable=lower, font='Arial 10', background="Gray")
    lower_btn.grid(row=2, column=3)
    upper_btn = tk.Checkbutton(btn_box, text="Uppercase", variable=upper, font='Arial 10', background="Gray")
    upper_btn.grid(row=2, column=4)
    num_btn = tk.Checkbutton(btn_box, text="Numbers", variable=numbers, font='Arial 10', background="Gray")
    num_btn.grid(row=2, column=5)
    special_btn = tk.Checkbutton(btn_box, text="Special Characters", variable=specials, font='Arial 10',
                                 background="Gray")
    special_btn.grid(row=2, column=6)
    
    # Set up a password length with spinbox widget
    pwd_len_txt = Label(passwd_app, text="Password Length", font='Arial 15 bold', anchor=W, background="Gray")
    pwd_len_txt.grid(row=3, column=2, pady=10)
    spinbox = tk.Spinbox(passwd_app, from_=5, to=100, textvariable=passlen, width=6)
    spinbox.grid(row=3, column=3)
    
    # Set up a strength meter with progress bar for password length
    pwd_len = Label(passwd_app, text="Strength Meter", font='Arial 15 bold', anchor=W, background="Gray")
    pwd_len.grid(row=7, column=2, pady=10)
    pwd_strength = Progressbar(passwd_app, variable=pwdmtrs, orient=HORIZONTAL, length=150)
    pwd_strength.grid(row=7, column=3)
    msg_box = Label(passwd_app, font='Arial 15 bold', width=12, state=DISABLED, textvariable=msg, background="Gray")
    msg_box.grid(row=7, column=4)
    
    # Set up an entry box for generated password
    pwd_txt = Label(passwd_app, text="New Password", font='Arial 15 bold', anchor=W, background="Gray")
    pwd_txt.grid(row=9, column=2, pady=10)
    pwd_entry = tk.Entry(passwd_app, textvariable=new_pwd, font='Arial 10', width=25, state=DISABLED, bd=5,
                         relief=SUNKEN, background="Gray", foreground="Black", show="*")
    pwd_entry.grid(row=9, column=3)
    
    # Set up a label for status bar
    status_bar = Label(passwd_app, text="Ready", anchor=E, background="Gray", foreground="Black", font='Helvetica 10')
    status_bar.grid(row=13, column=5, ipady=5)
    
    # Set up a buttons for generate, copy, hide and show password
    gen_btn = tk.Button(passwd_app, text="Generate", font='Helvetica 10', width=7, bd=5,
                        command=lambda: gen_pwd(new_pwd, passlen, pwdmtrs,
                                                lower, upper, numbers, specials, msg, msg_box, status_bar))
    gen_btn.grid(row=10, column=2)
    copy_btn = tk.Button(passwd_app, text="Copy", font='Helvetica 10', width=7, bd=5,
                         command=lambda: copy_pwd(new_pwd, passwd_app, status_bar))
    copy_btn.grid(row=11, column=2)
    show_btn = tk.Button(passwd_app, text="Show", font='Helvetica 10', width=7, bd=5,
                         command=lambda: show_pwd(passwd_app, new_pwd))
    show_btn.grid(row=9, column=4)
    hide_btn = tk.Button(passwd_app, text="Hide", font='Helvetica 10', width=7, bd=5,
                         command=lambda: hide_pwd(passwd_app, new_pwd))
    hide_btn.grid(row=10, column=4)
    
    # Display an app in a loop
    passwd_app.mainloop()


# The following if statement helps Python determine whether or not the main()
# function in this program is our entry point.
if __name__ == "__main__":
    main()

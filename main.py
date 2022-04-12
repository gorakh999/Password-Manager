from tkinter import *
from tkinter import messagebox
import pyperclip

from matplotlib.pyplot import text
import password_generator


window = Tk()
window.title("Password Manager")
# window.geometry("500x400")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# canv.pack()

def generate_password():
    pass_entry.delete(0, END)
    password = password_generator.generate_pass()
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    websiteNameEntry = website_entry.get()
    emailNameEntry = email_entry.get()
    passwordEntry = pass_entry.get()

    if (len(websiteNameEntry) > 0 and len(emailNameEntry) > 0 and len(passwordEntry) > 0):
        is_ok = messagebox.askyesno(title="Website", message=f"You have Entered these details :\n Website : {websiteNameEntry}\n Email : {emailNameEntry}\n Password : {passwordEntry}")
        if is_ok:
            text = websiteNameEntry + ' | ' + emailNameEntry + ' | ' + passwordEntry
            password_generator.save_password(text)
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Please Don't Leave any Field Empty")


website_name = Label(text="Website: ")
website_name.grid(row=1, column=0)

email_name = Label(text="Email/Username:")
email_name.grid(row=2, column=0)

pass_name = Label(text="Password:")
pass_name.grid(row=3, column=0)


website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "gorakhgupta343@gmail.com")

pass_entry = Entry(width=18)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)







mainloop()









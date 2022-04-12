from tkinter import *
from tkinter import messagebox
import pyperclip

import json
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


def search_password():
    websiteNameEntry = website_entry.get()

    if (len(websiteNameEntry)) > 0:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

                email_id = data[websiteNameEntry]["email"]
                password = data[websiteNameEntry]["password"]

                messagebox.showinfo(title=websiteNameEntry, message=f"Email : {email_id} \nPassword : {password}")

        except FileNotFoundError:
            messagebox.showinfo(title=websiteNameEntry, message=f"No Data File Found")

        except KeyError:
            messagebox.showinfo(title=websiteNameEntry, message=f"Details for {websiteNameEntry} Does Not Exists")

    else:
        messagebox.showerror(title="Error", message="Please Don't Leave any Field Empty")


def generate_password():
    pass_entry.delete(0, END)
    password = password_generator.generate_pass()
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    websiteNameEntry = website_entry.get()
    emailNameEntry = email_entry.get()
    passwordEntry = pass_entry.get()

    new_data = {
        websiteNameEntry : {
            "email" : emailNameEntry,
            "password" : passwordEntry
        }
    }

    if (len(websiteNameEntry) > 0 and len(emailNameEntry) > 0 and len(passwordEntry) > 0):
        
        try:
            # reading JSON File
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
            # writing updated JSON File
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        finally:
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


website_entry = Entry(width=29)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=29)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "gorakhgupta343@gmail.com")

pass_entry = Entry(width=29)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search Password", command=search_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)







mainloop()









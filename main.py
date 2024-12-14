from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD SEARCHER ------------------------------- #
def ser_pass():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No data file found.")
    else:
        if web_in.get() in data:
            email_entry = data[web_in.get()]["email"]
            pass_entry = data[web_in.get()]["password"]
            messagebox.showinfo(title=web_in.get(), message=f"Email: {email_entry}\nPassword: {pass_entry}")
        else:
            messagebox.showinfo(title="Error!", message=f"No details for {web_in.get()} exists.")
        web_in.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)

# password = ""
# for char in password_list:
#     password += char
password = "".join(password_list)   # string join method
def gen_pass():
    pass_in.delete(0, END)    #not needed--we don't need to delete the entry as inserting from 0 rewrites the password
    pass_in.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        web_in.get(): {
            "email": email_in.get(),
            "password": pass_in.get()
        }
    }
    if len(web_in.get()) == 0 or len(email_in.get()) == 0 or len(pass_in.get()) == 0:
        messagebox.showinfo(title='Oops!', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_in.get(), message=f"These are the details entered:\nEmail: {email_in.get()}\n Password: {pass_in.get()}\n Do you want to save?")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)           # Reading old data
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)                # Updating old data with new data
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)    # Saving updated data
            finally:
                web_in.delete(0, END)
                pass_in.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager!")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, )
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web = Label(text="Website:")
web.grid(row=1, column=0)

web_in = Entry(width=32)
web_in.grid(row=1, column=1)
web_in.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_in = Entry(width=50)
email_in.grid(row=2, column=1, columnspan=2)
email_in.insert(END, "sample@mail.com")

passw = Label(text="Password:")
passw.grid(row=3, column=0)

pass_in = Entry(width=32)
pass_in.grid(row=3, column=1)

pass_gen = Button(text="Generate Password", command=gen_pass)
pass_gen.grid(row=3, column=2)

add = Button(text="Add", width=43, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=13, command=ser_pass)
search.grid(row=1, column=2)

window.mainloop()

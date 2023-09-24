from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME= "Helvetica"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 4)

    password_letters = [ random.choice(letters) for _ in range(nr_letters) ]
    password_symbols = [ random.choice(symbols) for _ in range(nr_symbols) ]
    password_numbers = [ random.choice(numbers) for _ in range(nr_numbers) ]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    generated_password = "".join(password_list)
    entry_password.insert(0, string=generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as my_file:
                my_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                entry_website.focus()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=2, row=1)

# Labels
label_website = Label(text="Website:", font=(FONT_NAME, 10), )
label_website.grid(column=1, row=2)
label_email = Label(text="Email/Username:", font=(FONT_NAME, 10))
label_email.grid(column=1, row=3)
label_password = Label(text="Password:", font=(FONT_NAME, 10))
label_password.grid(column=1, row=4)

# Entries
entry_website = Entry(width=40)
entry_website.grid(column=2, row=2, columnspan=2)
entry_website.focus()
entry_email = Entry(width=40)
entry_email.insert(0, string="eda@gmail.com")
entry_email.grid(column=2, row=3, columnspan=2)
entry_password = Entry(width=22)
entry_password.grid(column=2, row=4)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=3, row=4)
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Courier", 8, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "g", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    special_char = ["!", "£", "$", ">", "*", "(", ")", "_", "-", "?"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    password_letters = [random.choice(letters) for _ in range(random.randint(10, 15))]
    password_letters_upper = [random.choice(letters).upper() for _ in range(random.randint(10, 15))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 6))]
    password_char = [random.choice(special_char) for _ in range(random.randint(2, 6))]

    password = password_letters + password_numbers + password_char + password_letters_upper

    random.shuffle(password)
    password = "".join(password)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    data = ""
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Input Error", message="You have not entered all the information")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"You entered \n Email: {user}"
                                                  f"\nPassword: {password}\n Is it ok to save")

    if not is_ok:
        return

    data = f"{website} | {user} | {password}\n"
    fd = open("data.txt", "a")
    fd.write(data)
    fd.close()

    website_input.delete(0, END)
    user_input.delete(0, END)
    user_input.insert(0, "test@gmail.com")
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(pady=20, padx=20)

background_Image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=background_Image)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=1, row=2)
website_input = Entry(width=42)
website_input.grid(column=2, row=2, columnspan=2)
website_input.focus()

user_label = Label(text="Email/Username:", font=FONT)
user_label.grid(column=1, row=3)
user_input = Entry(width=42)
user_input.grid(column=2, row=3, columnspan=2)
user_input.insert(0, "test@gmail.com")

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=1, row=4)
password_input = Entry(width=21)
password_input.grid(column=2, row=4)
password_button = Button(text="Generate Password", command=generate_password, font=FONT)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", command=save_password, font=FONT, width=36)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char


    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save():

    if website_entry.get() == '' or  password_entry.get() == '':
        messagebox.showerror(title='Error',message='Please fill out all fields') 
    else:


        is_ok=messagebox.askokcancel(title='website', message=f"These are the details you entered \n Email:{email_entry.get()} \n website: {website_entry.get()} \n password:{password_entry.get()}")


        if is_ok:
            with open('data.txt',W) as f:
                f.write(f'{website_entry.get()} |  {email_entry.get()} | {password_entry.get()} \n')
            website_entry.delete(0,END)
            password_entry.delete(0,END)




# Initialize the window
windows = Tk()
windows.minsize(height=450, width=400)
windows.title('Password Manager')


canvas = Canvas(windows, height=250, width=250, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(125, 125, image=image)
canvas.grid(row=0, column=0, columnspan=3, pady=20)


label_text = Label(text="Website:")
label_text.grid(row=1, column=0, padx=5, pady=5)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
website_entry.focus()

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0, padx=5, pady=5)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
email_entry.insert(0,'aqibhamid900@gmail.com')

password_text = Label(text="Password:")
password_text.grid(row=3, column=0, padx=0, pady=5)
password_entry = Entry(width=19)  
password_entry.grid(row=3, column=1, padx=0, pady=5)

generate_btn = Button(text='Generate Password',command=generate)
generate_btn.grid(row=3, column=2, padx=0, pady=5)


add_btn = Button(text='Add', width=36,command=save)
add_btn.grid(row=4, column=1, columnspan=2, padx=5, pady=5)









windows.mainloop()

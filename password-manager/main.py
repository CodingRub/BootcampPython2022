from tkinter import *
from decrypt import *
from encrypt import *
import os.path, json
from tkinter import messagebox
from genHashPwd import *
from passwordGen import pwdGen
import pyperclip

JSON_PATH = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/data.json"
LOGO_PATH = "C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/logo.png"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genPwd():
    password = pwdGen()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UPDATE EVENT ------------------------------- #

def update_text():
    info_label.config(text="")

# ---------------------------- CLOSING EVENT ------------------------------- #

def on_closing():
    is_quit = messagebox.askokcancel("Quit", "Do you want to quit?")
    if is_quit:
        if os.path.isfile(JSON_PATH):
            print("Encrypting data...")
            encrypt(pathkey)
        else:
            print("Fichier inexistant")
        window.destroy()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        try:
            with open(JSON_PATH, "r") as data_file:
                data = json.load(data_file)
                        
        except FileNotFoundError:
            with open(JSON_PATH, "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            if website in data:
                is_exist = messagebox.askokcancel("Remove", "Information about this website already exists. Do you want to replace it ?")
                if is_exist:
                    data.update(new_data)
                    print("Update")
                    with open(JSON_PATH, "w") as data_file:
                        json.dump(data, data_file, indent=4)
            else:
                data.update(new_data)
                print("Update")
                with open(JSON_PATH, "w") as data_file:
                    json.dump(data, data_file, indent=4)                
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            try:
                if is_exist:
                    info_label.config(text="Your password has been saved !", fg="green")
                    window.after(3000, update_text)
            except UnboundLocalError:
                    info_label.config(text="Your password has been saved !", fg="green")
                    window.after(3000, update_text)

    else:
        info_label.config(text="Error, missing information", fg="red")
        window.after(3000, update_text)
# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_pwd():
    website = website_entry.get()
    try:
        with open(JSON_PATH) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No Data File Found !")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            website_entry.delete(0, END)
        else:
            messagebox.showerror(title="Error", message=f"For {website}, there is no information available")
# ---------------------------- UI SETUP ------------------------------- #
pathkey = str(input("Enter the path of the key to unlock the file: "))
extension = os.path.splitext(pathkey)[1]
size = os.path.getsize(pathkey)
hashPwd = "8ae6ae71a75d3fb2e0225deeb004faf95d816a0a58093eb4cb5a3aa0f197050d7a4dc0a2d5c6fbae5fb5b0d536a0a9e6b686369fa57a027687c3630321547596"
if os.path.isfile(pathkey) and extension == ".key" and size == 44:
    main_pwd = str(input("Enter the password to unlock the file: "))
    verif_hash = gen_hash(main_pwd)
    if hashPwd == verif_hash:
        print("Decrypting data...")
        decrypting(pathkey)
        window = Tk()
        window.title("Password Manager")
        window.config(padx=50, pady=50)
        
        canvas = Canvas(width=200, height=200)
        logo_img = PhotoImage(file=LOGO_PATH)
        canvas.create_image(100, 100, image=logo_img)
        canvas.grid(column=1, row=0)
        
        website_label = Label(text="Website:")
        website_label.grid(column=0, row=1)
        
        website_entry = Entry(width=21)
        website_entry.grid(column=1, row=1, sticky="EW")
        website_entry.focus()
        
        search_button = Button(text="Search", width=13, command=find_pwd)
        search_button.grid(column=2, row=1)

        email_label = Label(text="Email/Username:")
        email_label.grid(column=0, row=2)
        
        email_entry = Entry(width=35)
        email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
        
        password_label = Label(text="Password:")
        password_label.grid(column=0, row=3)
        
        password_entry = Entry(width=21)
        password_entry.grid(column=1, row=3, sticky="W")
        

        password_button= Button(text="Generate Password", command=genPwd)
        password_button.grid(column=2, row=3, sticky="EW")
        
        add_button= Button(text="Add", width=36, command=save)
        add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

        info_label = Label(text="")
        info_label.grid(column=1, row=5)

        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.mainloop()
    else:
        print("Password wrong !")
else:
    print("Vous n'avez pas la cl?? :(")
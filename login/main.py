from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.title('Login Page')
root.geometry('500x500')
root.resizable('False', 'False')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='HOSPITAL',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

username_label = Label(root, text='Please enter your username:', width=25)
username_label.place(relx=0.1, rely=0.2)
username_entry = Entry(root, width=25)
username_entry.place(relx=0.53, rely=0.2)

password_label = Label(root, text='Please enter your password:', width=25)
password_label.place(relx=0.1, rely=0.3)
password_entry = Entry(root, width=25)
password_entry.place(relx=0.53, rely=0.3)


def verify():
    user = str(username_entry.get())
    passkey = str(password_entry.get())
    query = 'select * from Login'
    mycursor.execute(query)
    user_pass = mycursor.fetchall()
    print(user_pass)
    if user == '' and passkey == '':
        messagebox.showerror(message='Please fill in your details')
    if (user, passkey) in user_pass:
        messagebox.showinfo(message='You have successfully logged in.')
    else:
        user_found = False
        for item in user_pass:
            if user in item:
                user_found = True
        if user_found:
            messagebox.showerror(message='Incorrect password entered')
        else:
            messagebox.showerror(message='This user does not exist')


def register():
    user = username_entry.get()
    passkey = password_entry.get()
    query_users = 'SELECT user from Login'
    mycursor.execute(query_users)
    users = mycursor.fetchall()
    print(users)
    query_passwords = 'SELECT password from Login'
    mycursor.execute(query_passwords)
    passwords = mycursor.fetchall()
    try:
        if user == '' or passkey == '':
            messagebox.showerror(message='Please enter your user information')
        elif user in users:
            messagebox.showerror(message='This username is already taken')
        elif passkey in passwords:
            messagebox.showerror(message='This password is already taken')
        else:
            query_register = "INSERT INTO Login (user, password) VALUES ('{}', '{}')".format(user, passkey)
            mycursor.execute(query_register)
            messagebox.showinfo(message='You have been successfully registered')
    except mysql.connector.errors.IntegrityError:
        messagebox.showerror(message='Username and password must be unique')


login_button = Button(root, text='Login', command=verify)
login_button.place(relx=0.3, rely=0.5)

register_button = Button(root, text='Register new user', command=register)
register_button.place(relx=0.6, rely=0.5)

root.mainloop()
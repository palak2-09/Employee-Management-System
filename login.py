from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='palak' and passwordEntry.get()=='vansh02':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong credentials')

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image=CTkImage(Image.open('cover.png'), size=(930,478))
imageLabel=CTkLabel(root, image=image, text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#FAFAFA', font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=10,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=25,y=150)
passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180, show='*')
passwordEntry.place(x=25,y=200)
loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=40,y=250)
root.mainloop()

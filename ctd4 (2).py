import tkinter as tk

root = tk.Tk()

un = tk.StringVar()
pw = tk.StringVar()

def submit():
    username = un.get()
    password = pw.get()
    print("name is "+ username)
    print("password is "+ password)
    un.set("")
    pw.set("")
    
text1 = tk.Label(root, text = "username")
un_entry = tk.Entry(root , textvariable = un)

text2 = tk.Label(root, text = "password")
pw_entry = tk.Entry(root , textvariable = pw , show = '*')

button1 = tk.Button(root, text='Login' , command = submit)



text1.grid(row=0,column=0)
un_entry.grid(row=0, column=1)
text2.grid(row=1,column=0)
pw_entry.grid(row=1, column=1)
button1.grid(row = 2 , column = 1)

root.mainloop()
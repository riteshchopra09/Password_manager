from tkinter import *
from tkinter import messagebox


def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS",message="Please make sure you haven't left any place empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"There are the details entered:\n email:{email}"
                                                           f"\n password:{password} \n is it ok to save?")
        with open ("data.txt","a")as data_file:
            data_file.write(f"{website} | {email}| {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)


window=Tk()
window.title("password manager")
window.config(padx=40,pady=40)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#entries
website_entry=Entry(width=58)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=58)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"riteshchopra009@gmail.com")
password_entry=Entry(width=40)
password_entry.grid(row=3,column=1,)

#Buttons
generate_password_button=Button(text='Generate Password')
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=50,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()

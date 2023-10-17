# Importing Libraries
import smtplib
from tkinter import *
from tkinter import messagebox

# Application window witch Icon
root = Tk()
root.geometry("800x580")
root.resizable(False, False)
root.title("Mail Application")
icon_image = PhotoImage(file="Mail_Icon_App.png")
root.iconphoto(False, icon_image)


# Function to get the data from user and set their actions
def Send():
    try:
        username = username_str.get()
        password = password_str.get()
        receiver = receiver_str.get()
        subject = subject_str.get()
        body = body_str.get()

        if username == "" or password == "" or receiver == "" or subject == "" or body == "":
            # notif.config(text="All fields are required", fg="Red")
            messagebox.showwarning(title="Warning", message="All fields are required")
        else:
            finalMessage = 'Subject : {} \n\n {}'.format(subject, body)
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(username, password)
            smtp_server.sendmail(username, receiver, finalMessage)
            messagebox.showinfo(title="Mail Application", message="Mail Sent Successfully")

    except:
        messagebox.showerror("ERROR while sending the message to {}".format(receiver))


# Function to reset all the typed areas to null
def Reset():
    userEntry.delete(0, 'end')
    passEntry.delete(0, 'end')
    passEntry.delete(0, 'end')
    recEntry.delete(0, 'end')
    sub_Entry.delete(0, 'end')
    bodyEntry.delete(0, 'end')
    print("Data is cleared")

# Function to exit the application
def Exit():
    root.destroy()

# Main Logo
textlogo = PhotoImage(file="Logo application.png")
Logo_app = Label(root, image=textlogo, height=100, width=650)
Logo_app.grid(padx=75)

# Background for the application
background_img = PhotoImage(file="Background.png")
BG1 = Label(root, image=background_img).place(x=30, y=103, width=700, height=440)

# Set textbox for username
username_str = StringVar()
Label(root, text="Enter your Email Address ", font="Calibri", bg="#E5F8F9", fg="Black").grid(padx=35, row=1, sticky=W)
userEntry = Entry(root, textvariable=username_str, font="Calibri", fg="green", bg="#F2F5BF", width=23)
userEntry.grid(row=1, pady=10)

# Set textbox for password
password_str = StringVar()
Label(root, text="Enter your password ", font="Calibri", bg="#E5F8F9", fg="Black").grid(padx=35, row=2, sticky=W)
passEntry = Entry(root, textvariable=password_str, show="*", font="Calibri", fg="green", bg="#F2F5BF")
passEntry.grid(row=2)

# Set textbox for receiver mail id
receiver_str = StringVar()
Label(root, text="To ", font="Calibri", bg="#E5F8F9", fg="Black").grid(padx=35, row=3, sticky=W)
recEntry = Entry(root, textvariable=receiver_str, font="Calibri", fg="green", bg="#F2F5BF", width=23)
recEntry.grid(row=3, pady=10)

# Set textbox for Subject
subject_str = StringVar()
Label(root, text="Subject ", font="Calibri", bg="#E5F8F9", fg="Black").grid(padx=35, row=4, sticky=W)
sub_Entry = Entry(root, textvariable=subject_str, font="Calibri", fg="green", bg="#F2F5BF")
sub_Entry.grid(row=4, pady=5)

# Set textbox for Body
body_str = StringVar()
Label(root, text="Body of the message", font="Calibri", bg="#FDFDFD", fg="Black").grid(padx=35, row=5, sticky=W)
bodyEntry = Entry(root, textvariable=body_str, font="Calibri", fg="green", bg="#F2F5BF")
bodyEntry.grid(row=5, pady=5)

# Buttons
Button(root, text="Send Message", font="Algerian", bd=3, bg="#2FD615", fg="Black", command=Send).place(x=100, y=350)
Button(root, text="Exit APP", font="Algerian", bd=3, bg="#DC2846", fg="Yellow", command=Exit).place(x=300, y=350)
Button(root, text="RESET", font="Algerian", bd=3, bg="#0ADEDB", fg="#0F0AC3", command=Reset).place(x=450, y=350)

root.mainloop()

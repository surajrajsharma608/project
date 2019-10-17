from tkinter import *
from tkinter import messagebox
import  login
import db.db

class RegistrationWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Registration | Administration')

        canvas = Canvas(self.win,width=600,height=500,bg='skyblue')
        canvas.pack(expand=YES,fill= BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2 - 600/2)
        y = int(height/2 - 500/2)
        strl = "600x500+"+str(x)+"+"+str(y)
        self.win.geometry(strl)


    def add_frame(self):
        frame = Frame(self.win,width=500,height=450)
        frame.place(x=50,y=20)

        heading = Label(frame,text='Register Account',font = 'courier 25 bold underline')
        heading.place(x=75,y=70)

        #Labels
        username = Label(frame, text='UserName', font='courier 15 bold')
        username.place(x=10, y=150)
        email = Label(frame, text='Email', font='courier 15 bold')
        email.place(x=10, y=200)
        password = Label(frame, text='Password', font='courier 15 bold')
        password.place(x=10, y=250)

        #Entries
        self.user_entry = Entry(frame,font='courier 15')
        self.user_entry.place(x=150,y=150)
        self.email_entry = Entry(frame, font='courier 15')
        self.email_entry.place(x=150, y=200)
        self.password_entry = Entry(frame, font='courier 15')
        self.password_entry.place(x=150, y=250)

        #Buttons
        btn = Button(frame,text='Register', font='courier 15',bg='darkgreen',fg='white',command=self.insert_db)
        btn.place(x=275,y=300)

        back = Button(frame,text='Back',font='courier 15',bg='darkgreen',fg='white',command=self.backLogin)
        back.place(x=10,y=10)


        self.win.mainloop()

    def insert_db(self):
        data = (self.user_entry.get(),
                self.email_entry.get(),
                self.password_entry.get()
                )
        if self.user_entry.get()=='':
            messagebox.showinfo('Message','please enter username')
        elif self.email_entry.get()=='':
            messagebox.showinfo('Message','please enter email')
        elif self.password_entry.get()=='':
            messagebox.showinfo('Message','please enter password')
        else:
            res = db.db.insert_register_data(data)
            if res:
                messagebox.showinfo('Message','Account Register Successfully')



    def backLogin(self):
        self.win.destroy()
        x = login.LoginWindow()
        x.add_frame()

if __name__== "__main__":
    x = RegistrationWindow()
    x.add_frame()
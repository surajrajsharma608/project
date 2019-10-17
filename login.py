from tkinter import *
from tkinter import messagebox
import dashboard
import registration
import db.db


class LoginWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Login | Administrator')
        self.win.geometry('500x400')

        canvas = Canvas(self.win,height=500,width=600,bg='white')
        canvas.pack(expand=YES,fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        strl = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(strl)




    def add_frame(self):
        frame = Frame(self.win, height=430, width=550)
        frame.place(x=25, y=35)

        self.img = PhotoImage(file="images\\login.png")
        imgLabel = Label(frame, image=self.img)
        imgLabel.place(x=200, y=20)

        userloginLabel = Label(frame, text='User Login', font='courier 20 bold')
        userloginLabel.place(x=180, y=150)

        username = Label(frame, text='User Name', font='courier 15 bold')
        username.place(x=50, y=220)

        password = Label(frame, text='Password', font='courier 15 bold')
        password.place(x=50, y=250)
        #
        self.user_entry = Entry(frame, font='courier 15')
        self.user_entry.place(x=170, y=220)
        self.user_entry.focus()

        self.pass_entry = Entry(frame, font='courier 15')
        self.pass_entry.place(x=170, y=250)

        btn = Button(frame, text='login', font='courier 12', bg='dark green',fg='white', command=self.login,width=10)
        btn.place(x=170, y=290)


        btn = Button(frame, text='Register', font='courier 12', bg='dark green',fg='white',command=self.register,width=10)
        btn.place(x=300, y=290)
        #
        self.win.mainloop()

    def login(self):

        data = (self.user_entry.get(),
                self.pass_entry.get()
                )

        if self.user_entry.get()=='':
            messagebox.showinfo('Message','enter usrname')
        elif self.pass_entry.get()=='':
            messagebox.showinfo('Message','enter password')

        else:
            res = db.db.user_login(data)
            if res:
                messagebox.showinfo('Message','login success')
                self.win.destroy()
                x = dashboard.DashaboarWindow()
                x.add_frame()

            else:
                messagebox.showinfo('Message','incorrect  username/password')

    def register(self):
        self.win.destroy()
        x = registration.RegistrationWindow()
        x.add_frame()







if __name__=="__main__":
    x = LoginWindow()
    x.add_frame()
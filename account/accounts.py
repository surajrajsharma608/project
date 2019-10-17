from tkinter import *
from tkinter import messagebox
import account.bills
import  dashboard
import db.db

class AccountWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Account Management | Administration')
        self.win.resizable(width=False,height=False)

        canvas = Canvas(self.win,width=1050,height=500,bg='skyblue')
        canvas.pack(expand=YES,fill= BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2 - 1050/2)
        y = int(height/2 - 500/2)
        strl = "1050x500+"+str(x)+"+"+str(y)
        self.win.geometry(strl)



    def add_frame(self):
        frame = Frame(self.win,width=900,height=460)
        frame.place(x=70,y=20)

        headinglabel = Label(frame,text='Account Management',font='courier 24 bold underline')
        headinglabel.place(x=270,y=20)

        addstaffBtn = Button(frame,text='Billing',font='courier 20 ',bg='dark green',fg='white',width=13,height=5,command=self.move_to_bills)
        addstaffBtn.place(x=80,y=150)

        viewstaffBtn = Button(frame, text='View Account', font='courier 20 ', bg='dark green', fg='white', width=13,height=5)
        viewstaffBtn.place(x=320, y=150)

        searchstaffBtn = Button(frame, text='Search staff', font='courier 20 ', bg='dark green', fg='white', width=13,
                              height=5)
        searchstaffBtn.place(x=560, y=150)

        # backBtn = Button(frame,text='Back',font='courier 15',bg='dark green',fg='white',command=self.back_to_dashboard)
        # backBtn.place(x=5,y=5)

        self.win.mainloop()

    def move_to_bills(self):
        x = account.bills.AccountWindow()
        x.add_frame()
        x.qty_menu()
        x.type_menu()


    # def move_to_viewstaff(self):
    #     x = staffs.viewstaffs.TableWindow()
    #     x.add_frame()



if __name__ =="__main__":
    x = AccountWindow()
    x.add_frame()

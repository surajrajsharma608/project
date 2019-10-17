from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import  dashboard
import db.db

class AddStaffWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Add Staffs | Administration')
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

        headinglabel = Label(frame,text='Add New Staffs',font='courier 24 bold underline')
        headinglabel.place(x=290,y=20)

        #Buttons
        AddBtn = Button(frame,text='Add Staff',font='courier 15',bg='dark green',fg='white',width=25,command=self.insert_record)
        AddBtn.place(x=500,y=300)


        #Labels

        nameLebal = Label(frame,text='Name',font = 'courier 15')
        nameLebal.place(x=80,y=120)
        addressLebal = Label(frame, text='Address', font='courier 15')
        addressLebal.place(x=500, y=120)
        phoneLebal = Label(frame, text='Phone No', font='courier 15')
        phoneLebal.place(x=80, y=180)
        genderLebal = Label(frame, text='Gender', font='courier 15')
        genderLebal.place(x=500, y=180)
        positionLebal = Label(frame, text='Position', font='courier 15')
        positionLebal.place(x=500, y=240)
        salaryLebal = Label(frame, text='Salary', font='courier 15')
        salaryLebal.place(x=80, y=240)

        #Entries
        self.nameEntry = Entry(frame,font = 'courier 15',width=15)
        self.nameEntry.place(x=200,y=120)
        self.nameEntry.focus()
        self.addressEntry = Entry(frame, font='courier 15',width=15)
        self.addressEntry.place(x=620, y=120)
        self.phoneEntry = Entry(frame, font='courier 15',width=15)
        self.phoneEntry.place(x=200, y=180)
        self.salaryEntry = Entry(frame, font='courier 15', width=15)
        self.salaryEntry.place(x=200, y=240)


        #dropdown for gender
        self.genderValue = ['Male','Female']
        self.genderDropdown = ttk.Combobox(frame,font='courier 15',width=13,state='readonly',values=self.genderValue)
        self.genderDropdown.place(x=620,y=180)
        self.genderDropdown.set('Select')

        #dropdown for staff position
        self.positionValue = ['Manager','Cook','Waiter','Sweeper','Security Guard']
        self.positionDropdown = ttk.Combobox(frame,font='courier 15',width=13,state='readonly',values=self.positionValue)
        self.positionDropdown.place(x=620,y=240)
        self.positionDropdown.set('Select')


        self.win.mainloop()

    def insert_record(self):
        data = (self.nameEntry.get(),
                self.addressEntry.get(),
                self.phoneEntry.get(),
                self.genderDropdown.get(),
                self.salaryEntry.get(),
                self.positionDropdown.get()
                )
        if self.nameEntry.get()=='':
            print('please enter name')
        elif self.addressEntry.get()=='':
            print('please enter address')
        elif self.phoneEntry.get()=='':
            print('please enter phone number')
        elif self.genderDropdown.get()=='':
            print('please select gender')
        elif self.salaryEntry.get()=='':
            print('please enter salary')
        elif self.positionDropdown.get()=='':
            print('please select position')

        else:
            res = db.db.insert_staff(data)

            if res:
                messagebox.showinfo('Message','record insert successfully')




if __name__ =="__main__":
    x = AddStaffWindow()
    x.add_frame()
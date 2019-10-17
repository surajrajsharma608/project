from tkinter import *
from tkinter import ttk
import db.db

class TableWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('View Staffs | Administration')
        self.win.resizable(width=False, height=False)

        canvas = Canvas(self.win, width=1150, height=500, bg='skyblue')
        canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1050 / 2)
        y = int(height / 2 - 500 / 2)
        strl = "1050x500+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

    def add_frame(self):
        frame = Frame(self.win, width=1030, height=460)
        frame.place(x=10, y=20)

        headinglabel = Label(frame, text='Staffs Details', font='courier 24 bold underline')
        headinglabel.place(x=350, y=20)

        self.table = ttk.Treeview(frame,height=17,column=('id','name','address','phone','gender','salary'))
        self.table.place(x=10,y=80)
        self.table.heading('#0',text='Id')
        self.table.column('#0',width=100)
        self.table.heading('#1', text='Name')
        self.table.column('#1', width=150)
        self.table.heading('#2', text='Address')
        self.table.column('#2', width=150)
        self.table.heading('#3', text='Phone Number')
        self.table.column('#3', width=150)
        self.table.heading('#4', text='Gender')
        self.table.column('#4', width=150)
        self.table.heading('#5', text='Salary')
        self.table.column('#5', width=150)
        self.table.heading('#6', text='Position')
        self.table.column('#6', width=150)

        j = 0
        for i in db.db.view_table():
            self.table.insert('',index=j,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],i[6]))
            j+=1



        self.win.mainloop()
if __name__=="__main__":
    x = TableWindow()
    x.add_frame()

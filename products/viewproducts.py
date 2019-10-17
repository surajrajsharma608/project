from tkinter import *
from tkinter import ttk
import db.db

class ProductTableWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('View Products | Administration')
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

        headinglabel = Label(frame, text='Products Details', font='courier 24 bold underline')
        headinglabel.place(x=350, y=20)

        self.table = ttk.Treeview(frame,height=17,column=('id','name','price'))
        self.table.place(x=150,y=80)
        self.table.heading('#0',text='Id')
        self.table.column('#0',width=150)
        self.table.heading('#1', text='Item Name')
        self.table.column('#1', width=200)
        self.table.heading('#2', text='Price')
        self.table.column('#2', width=200)
        self.table.heading('#3', text='Type')
        self.table.column('#3', width=200)


        j = 0
        for i in db.db.view_products():
            self.table.insert('',index=j,text=i[0],values=(i[1],i[2],i[3]))
            j+=1



        self.win.mainloop()
if __name__=="__main__":
    x = ProductTableWindow()
    x.add_frame()

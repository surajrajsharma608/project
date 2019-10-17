from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import  dashboard
import db.db

class AddProductWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Add Products | Administration')
        self.win.resizable(width=False,height=False)

        canvas = Canvas(self.win,width=1050,height=350,bg='skyblue')
        canvas.pack(expand=YES,fill= BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2 - 1050/2)
        y = int(height/2 - 350/2)
        strl = "1050x350+"+str(x)+"+"+str(y)
        self.win.geometry(strl)



    def add_frame(self):
        frame = Frame(self.win,width=900,height=300)
        frame.place(x=70,y=20)

        headinglabel = Label(frame,text='Add New Products',font='courier 24 bold underline')
        headinglabel.place(x=290,y=20)

        #Buttons
        AddBtn = Button(frame,text='Add Products',font='courier 15',bg='dark green',fg='white',width=25,command=self.insert_product)
        AddBtn.place(x=500,y=180)


        #Labels

        itemLebal = Label(frame,text='Item Name',font = 'courier 15')
        itemLebal.place(x=80,y=120)
        priceLebal = Label(frame, text='Price', font='courier 15')
        priceLebal.place(x=500, y=120)

        typeLebal = Label(frame, text='Type', font='courier 15')
        typeLebal.place(x=80, y=180)


        #Entries
        self.itemEntry = Entry(frame,font = 'courier 15',width=15)
        self.itemEntry.place(x=200,y=120)
        self.itemEntry.focus()
        self.priceEntry = Entry(frame, font='courier 15',width=15)
        self.priceEntry.place(x=620, y=120)
        self.typeEntry = Entry(frame, font='courier 15', width=15)
        self.typeEntry.place(x=200, y=180)



        self.win.mainloop()

    def insert_product(self):
        data = (self.itemEntry.get(),
                self.priceEntry.get(),
                self.typeEntry.get()
                )
        if self.itemEntry.get()=='':
            print('please enter product name')
        elif self.priceEntry.get()=='':
            print('please enter product price')
        elif self.typeEntry.get()=='':
            print('please enter product type')
        else:
            result = db.db.insert_products(data)
            if result:
                print('product insert successfully')



if __name__ =="__main__":
    x = AddProductWindow()
    x.add_frame()
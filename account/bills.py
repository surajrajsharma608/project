from tkinter import *
import math,random
from tkinter import messagebox
import datetime
import staffs.addstaff
import staffs.viewstaffs
import  dashboard
import db.db

date = datetime.datetime.now().date()
datestr = date.strftime("%Y/%m/%d" )
time = datetime.datetime.now().time()
timestr = time.strftime("%H:%M:%S")

class AccountWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Account Management | Administration')
        self.win.resizable(width=False,height=False)

        canvas = Canvas(self.win,width=1050,height=600,bg='skyblue')
        canvas.pack(expand=YES,fill= BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2 - 1050/2)
        y = int(height/2 - 600/2)
        strl = "1050x600+"+str(x)+"+"+str(y)
        self.win.geometry(strl)
    def add_frame(self):

        self.frame_1 = Frame(self.win,width=400,height=555)
        self.frame_1.place(x=20,y=20)

        self.frame_2 = Frame(self.win,width=570,height=555)
        self.frame_2.place(x=450,y=20)

        #variable for random bill number generate
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))

        #working on frame_1
        heading_l = Label(self.frame_1,text='Products',font='courier 20 bold underline')
        heading_l.place(x=120,y=10)
        #Button
        AddBtn = Button(self.frame_1, text='Add', font='courier 12', bg='dark green', fg='ghost white',width=9)
        AddBtn.place(x=226, y=450)

        #frame_1 Labels
        self.rate = 2
        rat = Label(self.frame_1, text=self.rate, font='courier 15')
        rat.place(x=10, y=50)
        customername = Label(self.frame_1, text='Customer Name', font='courier 15')
        customername.place(x=10, y=100)
        customerphone = Label(self.frame_1, text='Phone Number', font='courier 15')
        customerphone.place(x=10, y=160)
        itemname = Label(self.frame_1, text='Item Name', font='courier 15')
        itemname.place(x=10, y=220)
        qty = Label(self.frame_1, text='Quantity', font='courier 15')
        qty.place(x=10, y=280)
        price = Label(self.frame_1, text='Price', font='courier 15')
        price.place(x=10, y=340)
        type = Label(self.frame_1, text='Type', font='courier 15')
        type.place(x=10, y=400)


        #frame_1 Entries
        self.customername_entry  = Entry(self.frame_1,font='courier 15',width=15)
        self.customername_entry.place(x=180, y=100)
        self.customername_entry.focus()
        self.customerphone_entry = Entry(self.frame_1, font='courier 15', width=15)
        self.customerphone_entry.place(x=180, y=160)
        self.qtyVar = IntVar()
        self.qty_entry = Entry(self.frame_1,font='courier 15',width=15,textvariable=self.qtyVar)
        self.qty_entry.place(x=180,y=280)
        self.qtyVar.set('0.00')
        self.priceVar = IntVar()
        self.priceVar.set("0.00")
        self.price_entry = Entry(self.frame_1, font='courier 15', width=15,textvariable=self.priceVar)
        self.price_entry.place(x=180, y=340)


        # working on frame_2
        self.bill_heading = Label(self.frame_2, text='Bills', font='courier 20 bold underline')
        self.bill_heading.place(x=250, y=10)
        self.texBox = Text(self.frame_2, width=65, height=28)
        self.scroll = Scrollbar(self.frame_2,orient=VERTICAL)
        self.scroll.place(x=550,y=60)
        self.texBox.place(x=20, y=60)
        self.welcome_bill()
        #Print Bill
        printBill = Button(self.frame_2,text='Print',font='courier 10',bg='dark green',fg='white')
        printBill.place(x=490,y=515)

    def welcome_bill(self):
        self.texBox.delete('1.0',END)
        self.texBox.insert(END, "\n\t\t\t Beautiful Party Palace")
        self.texBox.insert(END, "\n\t\t\t    Kohalpur,10 Banke")
        self.texBox.insert(END, f"\n\n\t\t\t\t\t Date:"+str(datestr))
        self.texBox.insert(END, f"\t\t\t\t\t\t\t\t\t time:" + str(timestr))

        self.texBox.insert(END, "\n\n Bill No:\t"+str(self.bill_no.get()))
        self.texBox.insert(END, "\n Customer Name:\t"+str(self.customername_entry.get()))
        self.texBox.insert(END,"\n Phone Number:\t"+str(self.customerphone_entry.get()))
        self.texBox.insert(END, "\n ===============================================================")
        self.texBox.insert(END, "\n Item")
        self.texBox.insert(END, "\t\t Quantity")
        self.texBox.insert(END, "\t\t Type")
        self.texBox.insert(END, "\t\t Price")
        self.texBox.insert(END, "\n ===============================================================")


    #for option menu
    def qty_menu(self):
        qty_options = []
        for i in db.db.insert_on_qty_optionmenu():
            qty_options.append(i[0])
        self.qty_variable = StringVar(self.frame_1)
        self.qty_variable.set(qty_options[1])
        self.qty_om = OptionMenu(self.frame_1,self.qty_variable,*qty_options)
        self.qty_om.place(x=180,y=220)
        self.qty_om.configure(font='courier 15',width=12)

    def type_menu(self):
        type_options = []
        for i in db.db.insert_on_type_menu():
            type_options.append(i[0])
        self.type_variable = StringVar(self.frame_1)
        self.type_variable.set(type_options[1])
        self.type_om = OptionMenu(self.frame_1,self.type_variable,*type_options)
        self.type_om.place(x=180,y=400)
        self.type_om.configure(font='courier 15',width=12)
        self.win.mainloop()





if __name__=="__main__":
    x = AccountWindow()
    x.add_frame()
    x.qty_menu()
    x.type_menu()

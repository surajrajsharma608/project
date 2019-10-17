from tkinter import *
import staffs.staff
import developer.developer_info
import login
import products.viewproducts
import products.product
import account.accounts


class DashaboarWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Dashboard | Administrator')
        self.win.resizable(width=False,height=False)


        canvas = Canvas(self.win,width=333,height=500,bg='white')
        canvas.pack(expand=YES,fill=BOTH)

        self.img = PhotoImage(file='images//dashboard.png')
        imgLabel = Label(self.win,image=self.img)
        imgLabel.place(x=0,y=0)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 500 / 2)
        strl = "1000x500+" + str(x) + "+" + str(y)
        self.win.geometry(strl)
    def add_frame(self):

            frame = Frame(self.win,height=480,width=210,bg='skyblue')
            frame.place(x=10,y=10)

            staffBtn = Button(frame, text='Staffs', font='courier 15 bold', fg='white', bg='dark green',height=2,width=15,command=self.staff)
            staffBtn.place(x=10, y=30)

            itemBtn = Button(frame, text='Products', font='courier 15 bold', fg='white', bg='dark green', height=2, width=15,command=self.products)
            itemBtn.place(x=10, y=120)

            accountBtn = Button(frame, text='Account', font='courier 15 bold', fg='white', bg='dark green', height=2,width=15,command=self.accounts)
            accountBtn.place(x=10, y=210)

            developerBtn = Button(frame, text='Developer', font='courier 15 bold', fg='white', bg='dark green', height=2,width=15,command=self.developer)
            developerBtn.place(x=10, y=300)

            logoutBtn = Button(frame, text='Logout', font='courier 15 bold', fg='white', bg='dark green', height=2,width=15, command=self.logout)
            logoutBtn.place(x=10, y=390)

            self.win.mainloop()





    def logout(self):
        self.win.destroy()
        x = login.LoginWindow()
        x.add_frame()
    def staff(self):
        x = staffs.staff.StaffWindow()
        x.add_frame()

    def developer(self):
        x = developer.developer_info.DeveloperWindow()
        x.add_frame()
    def products(self):
        x = products.product.ProductsWindow()
        x.add_frame()
    def accounts(self):
        x = account.accounts.AccountWindow()
        x.add_frame()


if __name__=='__main__':
    x = DashaboarWindow()
    x.add_frame()



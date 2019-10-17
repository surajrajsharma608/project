from tkinter import *
import  dashboard


class DeveloperWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('Developer | Administration')
        self.win.resizable(width=False,height=False)

        canvas = Canvas(self.win,width=1050,height=500,bg='skyblue')
        canvas.pack(expand=YES,fill= BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2 - 1050/2)
        y = int(height/2 - 500/2)
        strl = "1050x500+"+str(x)+"+"+str(y)
        self.win.geometry(strl)

        back = Button(self.win,text='Back',font='courier 12',command=self.back_to_dashboard)
        back.place(x=10,y=20)



    def add_frame(self):
        frame = Frame(self.win,width=900,height=460)
        frame.place(x=70,y=20)

        img = PhotoImage(file='C:\\Users\\Dada\\Desktop\\sooraj.png')
        canvas = Canvas(frame,height=150,width=200)
        canvas.place(x=660,y=100)
        canvas.create_image(0,0,image=img,anchor=NW)


        # f1 = Frame(frame,width=200,height=150,bg='blue')
        # f1.place(x=10,y=5)


        # l = Label(f1,image=img)
        # l.place(x=0,y=0)




        headinglabel = Label(frame,text='Developer Information',font='courier 24 bold underline')
        headinglabel.place(x=290,y=20)

        name = Label(frame,text='Name          :',font='courier 15 bold',fg='red')
        name.place(x=30,y=100)
        namel = Label(frame, text='Bamdev Sharma', font='courier 15',fg='dark green')
        namel.place(x=230, y=100)


        add = Label(frame, text='Address       :', font='courier 15 bold',fg='red')
        add.place(x=30, y=150)
        addl = Label(frame, text='Kohalpur, 10 Chatar,Banke', font='courier 15',fg='dark green')
        addl.place(x=230, y=150)

        cont = Label(frame, text='Contact       :', font='courier 15 bold',fg='red')
        cont.place(x=30, y=200)
        contl = Label(frame, text='9868290782', font='courier 15',fg='dark green')
        contl.place(x=230, y=200)

        email = Label(frame, text='Eamil         :', font='courier 15 bold',fg='red')
        email.place(x=30, y=250)
        emaill = Label(frame, text='Surajsharmas272@gmail.com', font='courier 15',fg='dark green')
        emaill.place(x=230, y=250)

        qualificaion = Label(frame, text='Qualification :', font='courier 15 bold',fg='red')
        qualificaion.place(x=30, y=300)
        qualificaionl = Label(frame, text='Bachelor in Computer Science And Information Technology \n(BSC.CSIT)', font='courier 15',fg='dark green')
        qualificaionl.place(x=230, y=300)




        self.win.mainloop()
    def back_to_dashboard(self):
        x = dashboard.DashaboarWindow()
        x.add_frame()

if __name__=="__main__":
    x = DeveloperWindow()
    x.add_frame()
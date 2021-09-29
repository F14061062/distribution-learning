import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import socket
from tkinter import Tk, RIGHT, BOTH, RAISED,Menu,DoubleVar,Scale,Entry,END,LabelFrame,TOP ,BOTTOM
from tkinter.constants import LEFT
from tkinter.ttk import Frame, Button, Style,Scale,Label
import time
from _thread import *
import threading
from matplotlib.pyplot import fill
a=[0,0,0] #change here,if you want increase client
b=[0,0,0] #change here,if you want increase client
his=[]
go=True
step=0
print("sdfsdf")
nametype=["pc1","pc2","pc3"] #change here,if you want increase client
nametxt=[]
temptime=[]
settime=0
def threaded(c):
    def get(x,his,step):
        try:
            print('here')
            data=his[int(x[1])-1]
            avg=(int(data[0])+int(data[1]))/2
            avg=str(avg)
            c.send(avg.encode('ascii'))
        except:
            print("ssss")

    temp=0
    global a
    global b
    global step
    global his
    global nametype
    while True:
        try:
            c.settimeout(1000)
            data = c.recv(1024)
        except:
            break
        if not data:
            break
        print(str(data))
        ndata=str(data)
        ndata=ndata[2:len(ndata)-1]
        print(ndata)
        x=ndata.split('_')
        print(x[0])
		# reverse the given string from client
        data = data[::-1]
        #print(test())
        print('data == 123',ndata == "123")

        for count,value in enumerate(nametype):
            if x[0] == value:
                c.settimeout(1)
                get(x,his,step)
                if int(x[1]) == (step+1):
                    a[count]=1
                    b[count]=x[2]
        for i,value in enumerate(nametype):
            if i ==x[0]:
                print("match the name type is",i)
        for i in range(len(a)):
            if a[i] == 1 :

                temp+=1             
        
        if temp == len(a):
            a=[0,0,0]  #change here,if you want increase client
            global temptime,settime
            temptime.append(time.time()-settime)
            settime=time.time()
            try:
                his[step]=b
            except:
                step+=1
                his.append(b)
        print(his)
        temp=0
    c.close()


def Main():
    global a
    global s
    host = "192.168.0.130" #server ip if muti-ip create list to store 

    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    while go:
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        start_new_thread(threaded, (c,))
    s.close()


class app(Frame):

    def __init__(self):
        super().__init__()
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu,tearoff=0)
        fileMenu.add_command(label="Seting IP")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="base   ", menu=fileMenu)

        editMenu = Menu(menu,tearoff=0)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="none", menu=editMenu,font=30)
        self.initUI()

    def testf(self,frame21,nametxt,nametype,frame221):
        global a,his,step
        try:
            temp=his[step]
            print("hello")
            for i in nametxt:
                pass
        except:
            temp=0
            for i,value in enumerate(nametxt):
                if a[i]==1:
                    value.config(background='green')
                else:
                    temp=1
                    value.config(background='red')
        self.after(100,lambda:self.testf(frame21,nametxt,nametype,frame221))
        

    def arra(self,nametxt,nametype,frame221):
        #nametxt=[]
        for i in range(len(nametype)):
            temp=LabelFrame(frame221,width=100,height=30)
            nametxt.append(Label(temp,text=nametype[i],font=("Helvetica",10),background='red'))
            
            temp.grid(row = int(i/3)*20, column = (i-int(i/3))*20, rowspan = 3, columnspan = 4)
            temp.pack_propagate(0)
            temp.grid_propagate(0)
            nametxt[i].pack(side=LEFT, padx=5, pady=5)
        
    def pbar(self,ax,f,canvas):
        global step,temptime
        print("i am here")
        print(temptime)
        ax.clear()
        ind = numpy.arange(step)
        ax.bar(ind, temptime, 0.5)
        canvas.draw()
        self.after(400,lambda:self.pbar(ax,f,canvas))
        pass
    
    def exitProgram(self):
        global s
        global t
        global go
        go=False
        s.close()
        exit()

    def initUI(self):
        def testr(self):
            if True:
                print("hello")
        self.master.title("zookeeper")
        self.style = Style()
        self.style.theme_use("default")

        frame1 = Frame(self, relief=RAISED, borderwidth=2)
        
        frame1.pack(fill=BOTH, expand=True)
        
        frame2 = Frame(frame1, relief=RAISED, borderwidth=0,width=700,height=300)
        frame21 = Frame(frame2, relief=RAISED, borderwidth=0,width=700,height=250)
        frame22 = Frame(frame2, relief=RAISED, borderwidth=2,width=700,height=350)
        frame3 = Frame(frame1, relief=RAISED, borderwidth=2,height=250)
        frame4 = Frame(frame1, relief=RAISED, borderwidth=2,height=310)
        w1=LabelFrame(frame4,width=100,height=22)
        frame2.pack(side=RIGHT,fill='y' )
        frame2.pack_propagate(0)
        frame21.pack(side=TOP)
        frame21.pack_propagate(0)
        frame22.pack(side=BOTTOM)
        frame22.pack_propagate(0)
        frame3.pack(side=TOP,fill='x' )
        frame3.pack_propagate(0)
        
        close1Button = Button(frame3, text="Close")
        frame4.pack(side=BOTTOM,fill='x' )
        frame4.pack_propagate(0)
        w1.pack(fill=BOTH,expand=True)
        w1.pack_propagate(0)
        textw1=Label(w1,text='test block',font=("Helvetica",8),background='white')
        textw1.pack()
        close1Button.pack()

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close",command=self.exitProgram)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="refresh connect")
        slider= Scale(self , from_=10, to=2000 ,orient='horizontal',length=200)
        o2kButton = Button(self, text="AUTO Adjust")
        o2kButton.pack(side=RIGHT, padx=5, pady=5)
        slider.pack(side=RIGHT, padx=5, pady=5)
        okButton.pack(side=RIGHT, padx=5, pady=5)
        txtp = Entry(self,width=6,selectborderwidth=10,font=("Helvetica",10))
        txtp.insert(END, '2112')
        txtp.pack(side=RIGHT, padx=5, pady=5)       
        port = Label(self,text='Port:',font=("Helvetica",10))
        port.pack(side=RIGHT, padx=5, pady=5)
        txt = Entry(self,width=13,selectborderwidth=10,font=("Helvetica",10))
        txt.insert(END, '192.168.0.1')
        txt.pack(side=RIGHT, padx=5, pady=5)
        ip=Label(self,text='IP:',font=("Helvetica",10))
        ip.pack(side=RIGHT, padx=5, pady=5)      

        w = LabelFrame(self,width=100,height=22)
        w.pack(side=RIGHT, padx=5, pady=5)
        w.pack_propagate(0)
        left = Label(w, text="     training      ",font=("Helvetica",10),background='green',width=100)
        left.pack()
        sta=Label(self,text='Statue :',font=("Helvetica",10))
        sta.pack(side=RIGHT, padx=5, pady=5)
        global nametxt , nametype,settime
        settime=time.time()
        frame221=Frame(frame21, relief=RAISED, borderwidth=2,width=700,height=250)
        frame221.pack(side=TOP)
        frame221.pack_propagate(0)
        frame221.grid_propagate(0)
        self.arra(nametxt,nametype,frame221)
        self.after(1,lambda:self.testf(frame21,nametxt,nametype,frame221))
        #########################################################################################################
        #self.after(1,lambda:sc())
        f = Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)
        #data = (20, 35, 30, 35, 27)
        #ind = numpy.arange(5)
        #width = .5
        #ax.bar(ind, data, width)
        canvas = FigureCanvasTkAgg(f, master=frame22)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.after(1,lambda:self.pbar(ax,f,canvas))

        
running = True




root = Tk()
root.geometry('900x600')
root.resizable(width=False, height=False)
app1 = app()
t = threading.Thread(target = Main)
t.start()
app1.mainloop()
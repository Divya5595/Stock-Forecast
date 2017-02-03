from Tkinter import *
 
class Application (Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.score=0
        self.res=0
        self.create_widgets()

    def create_widgets(self):
        self.label=Label(self,text="   **********LETS TEST YOUR GENERAL KNOWLEDGE**********")
        self.label.grid(row=0,column=0,sticky=W)
        self.que1()
        self.que2()
        self.que3()
        self.que4()


    def que1(self):    
        self.label1=Label(self,text="Which is the largest state of India in terms of Area ?")
        self.label1.grid(row=1,column=0,columnspan=2,sticky=W)

        self.op11=BooleanVar()
        Checkbutton(self,text="Maharashtra",variable=self.op11).grid(row=2,column=0,sticky=W)

        self.op21=BooleanVar()
        Checkbutton(self,text="Rajsthan",variable=self.op21).grid(row=3,column=0,sticky=W)
        
        self.op31=BooleanVar()
        Checkbutton(self,text="Gujrat",variable=self.op31).grid(row=4,column=0,sticky=W)

        self.op41=BooleanVar()
        Checkbutton(self,text="Andhra Pradesh",variable=self.op41).grid(row=5,column=0,sticky=W)

        self.button1=Button(self,text="Submit")
        self.button1["command"]=self.result_que1
        self.button1.grid()
        
        #output text box
        self.text1=Text(self,width=35,height=1,wrap=WORD)
        self.text1.grid(row=7,column=0,columnspan=3)

    def result_que1(self):
        res1= ""    
        if  self.op11.get():
            res1 ="You are Wrong"
        elif self.op21.get():
            res1 ="You are Right"
            self.score +=1
            self.update_result()
        elif self.op31.get():
            res1 ="You are Wrong"
        elif self.op41.get():
            res1 ="You are Wrong"
        self.text1.delete(0.0,END)
        self.text1.insert(0.0,res1)

    def que2(self):    
        self.label2=Label(self,text=" What is the name of India's new fastest train ?")
        self.label2.grid(row=8,column=0,columnspan=2,sticky=W)

        self.op12=BooleanVar()
        Checkbutton(self,text="Rajdhani Express",variable=self.op12).grid(row=9,column=0,sticky=W)

        self.op22=BooleanVar()
        Checkbutton(self,text="Shatabdi Express",variable=self.op22).grid(row=10,column=0,sticky=W)
        
        self.op32=BooleanVar()
        Checkbutton(self,text="Gatiman Express",variable=self.op32).grid(row=11,column=0,sticky=W)

        self.op42=BooleanVar()
        Checkbutton(self,text="Vivek Express",variable=self.op42).grid(row=12,column=0,sticky=W)

        self.button2=Button(self,text="Submit")
        self.button2["command"]=self.result_que2
        self.button2.grid()
        
        #output text box
        self.text2=Text(self,width=35,height=1,wrap=WORD)
        self.text2.grid(row=14,column=0,columnspan=3)

    def result_que2(self):
        res2= ""    
        if  self.op12.get():
            res2 ="You are Wrong"
        elif self.op22.get():
            res2 ="You are Wrong"
        elif self.op32.get():
            res2 ="You are Right"
            self.score +=1
            self.update_result()
        elif self.op42.get():
            res2 ="You are Wrong"
        self.text2.delete(0.0,END)
        self.text2.insert(0.0,res2)

    def que3(self):    
        self.label3=Label(self,text=" Which is the largest river in the World?")
        self.label3.grid(row=15,column=0,columnspan=2,sticky=W)

        self.op13=BooleanVar()
        Checkbutton(self,text="Amazon",variable=self.op13).grid(row=16,column=0,sticky=W)

        self.op23=BooleanVar()
        Checkbutton(self,text="Ganga",variable=self.op23).grid(row=17,column=0,sticky=W)
        
        self.op33=BooleanVar()
        Checkbutton(self,text="Yangtze",variable=self.op33).grid(row=18,column=0,sticky=W)

        self.op43=BooleanVar()
        Checkbutton(self,text="Nile",variable=self.op43).grid(row=19,column=0,sticky=W)

        self.button3=Button(self,text="Submit")
        self.button3["command"]=self.result_que3
        self.button3.grid()
        
        #output text box
        self.text3=Text(self,width=35,height=1,wrap=WORD)
        self.text3.grid(row=21,column=0,columnspan=3)

    def result_que3(self):
        res3= ""    
        if  self.op13.get():
            res3 ="You are Wrong"
        elif self.op23.get():
            res3 ="You are Wrong"
        elif self.op33.get():
            res3 ="You are Wrong"
        elif self.op43.get():
            res3 ="You are Right"
            self.score +=1
            self.update_result()
        self.text3.delete(0.0,END)
        self.text3.insert(0.0,res3)

    def que4(self):    
        self.label14=Label(self,text=" Who is the first Indian woman to win an Asian Games gold in 400m running?")
        self.label14.grid(row=22,column=0,columnspan=2,sticky=W)

        self.op14=BooleanVar()
        Checkbutton(self,text="Kamaljit Sandhu",variable=self.op14).grid(row=23,column=0,sticky=W)

        self.op24=BooleanVar()
        Checkbutton(self,text="K.Malleshwari",variable=self.op24).grid(row=24,column=0,sticky=W)
        
        self.op34=BooleanVar()
        Checkbutton(self,text="P.T.Usha",variable=self.op34).grid(row=25,column=0,sticky=W)

        self.op44=BooleanVar()
        Checkbutton(self,text="M.L.Valsamma",variable=self.op44).grid(row=26,column=0,sticky=W)

        self.button4=Button(self,text="Submit")
        self.button4["command"]=self.result_que4
        self.button4.grid()
        
        #output text box
        self.text4=Text(self,width=35,height=1,wrap=WORD)
        self.text4.grid(row=28,column=0,columnspan=3)
        
        
    def result_que4(self):
        res4= ""    
        if  self.op14.get():
            res4 ="You are Right"
            self.score +=1
            self.update_result()
        elif self.op24.get():
            res4 ="You are Wrong"
        elif self.op34.get():
            res4 ="You are Wrong"
        elif self.op44.get():
            res4 ="You are Wrong"
        self.text4.delete(0.0,END)
        self.text4.insert(0.0,res4)

    def update_result(self):
        self.res=self.score*25
        self.label=Label(self,text="Your Result is: "+ str(self.res)+" %")
        self.label.grid(row=29,column=0,columnspan=2,sticky=W)
        
     

#create window
root=Tk()

# modify the window
root.title("GUI Task")
root.geometry("400x400")

app=Application(root)
root.mainloop()

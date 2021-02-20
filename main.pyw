from tkinter import *
from tkinter.messagebox import *

root=Tk()#Creating GUI platform
root.title("CALCULATOR") #seting the Title of GUI 
root.config(bg="blue")#seting blue background
root.iconbitmap("E:\Saini\Python\project -1\Calculator\download.ico") #seting icon of GUI
root.geometry("400x580") #GUI size 
root.maxsize(width=400,height=580) # GUI Maxsize
root.minsize(width=400,height=580)# GUI Minsize

Label(root,text="Made by Prashant",fg= "red").pack() # Writing a Label (Made by Prashant)

entry=Entry(root,width=60,font=150,highlightcolor="red") #Creating a Entry box
entry.pack(padx=50,pady=40)# seting the position of Entry box
frame=Frame(root,width=300,height=300) #Creating a Frame
frame.config(bg="red")#seting a background of Frame
frame.pack()

''' Now Creating button and fuction of the
button of 1,2,3,4,5,6,7,8,9,0,-,+,=,*,**,/ '''

def bt1():# function of button '1'
    entry.insert(END,"1")# insert '1' at the end in Entry box
button1=Button(frame,width=8,text="1",height=3,command=bt1,font=2,bg="orange")#Configuring the the button
button1.grid(column=1,row=1)


def bt2():# function of butt
    entry.insert(END,"2")
button2=Button(frame,width=8,text="2",height=3,command=bt2,font=2,bg="orange")
button2.grid(column=2,row=1)


def bt3():
    entry.insert(END,"3")
button3=Button(frame,width=8,text="3",height=3,command=bt3,font=2,bg="orange")
button3.grid(column=3,row=1)


def bt4():
    entry.insert(END,"4")
button4=Button(frame,width=8,text="4",height=3,command=bt4,font=2,bg="orange")
button4.grid(column=1,row=2)

def bt5():
    entry.insert(END,"5")
button5=Button(frame,width=8,text="5",height=3,command=bt5,font=2,bg="orange")
button5.grid(column=2,row=2)

def bt6():
    entry.insert(END,"6")
button6=Button(frame,width=8,text="6",height=3,command=bt6,font=2,bg="orange")
button6.grid(column=3,row=2)

def bt7():
    entry.insert(END,"7")
button7=Button(frame,width=8,text="7",height=3,command=bt7,font=2,bg="orange")
button7.grid(column=1,row=3)

def bt8():
    entry.insert(END,"8")
button8=Button(frame,width=8,text="8",height=3,command=bt8,font=2,bg="orange")
button8.grid(column=2,row=3)

def bt9():
    entry.insert(END,"9")
button9=Button(frame,width=8,text="9",height=3,command=bt9,font=2,bg="orange")
button9.grid(column=3,row=3)

def bt0():
    entry.insert(END,"0")
button0=Button(frame,width=8,text="0",height=3,command=bt0,font=2,bg="orange")
button0.grid(column=1,row=4)

def btf():
    entry.insert(END,"+")
buttonf=Button(frame,width=8,text="+",height=3,command=btf,font=2,bg="orange")
buttonf.grid(column=2,row=4)

def btG():
    entry.insert(END,"-")
buttong=Button(frame,width=8,text="-",height=3,command=btG,font=2,bg="orange")
buttong.grid(column=3,row=4)

def btH():
    entry.insert(END,"*")
buttonh=Button(frame,width=8,text="×",height=3,command=btH,font=2,bg="orange")
buttonh.grid(column=5,row=4)

def btd():
    entry.insert(END,"/")
buttonh=Button(frame,width=8,text="÷",height=3,command=btd,font=3,bg="orange")
buttonh.grid(column=5,row=3)

def btclear():
    entry.delete(0,END)
buttonc=Button(frame,width=8,text="Clear",height=3,command=btclear,font=3,bg="orange")
buttonc.grid(column=5,row=1)

def btans():
    try:
        k=entry.get()
        h=eval(k) 
        entry.delete(0,END)
        entry.insert(0,h)
    except Exception as error:
        showinfo(title="ERROR",message=error)
button=Button(frame,width=8,text="=",height=3,command=btans,font=4,bg="orange")
button.grid(column=5,row=2)

def btpower():
    entry.insert(END,"**")
buttonp=Button(frame,text=" bⁿ",command=btpower,font=4,height=3,width=8,bg="orange")
buttonp.grid(column=1,row=5)

def btrb():
    entry.insert(END,"(")
buttonrb=Button(frame,text="(",command=btrb,font=4,height=3,width=8,bg="orange")
buttonrb.grid(column=2,row=5)

def btlb():
    entry.insert(END,")")
buttonlb=Button(frame,text=")",command=btlb,font=4,height=3,width=8,bg="orange")
buttonlb.grid(column=3,row=5)

def btnd():
    entry.insert(END,".")
buttonlb=Button(frame,text=".",command=btnd,font=4,height=3,width=8,bg="orange")
buttonlb.grid(column=5,row=5)

root.mainloop()
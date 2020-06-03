


import Process
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

root = tk.Tk()
root.minsize(640,400)


l1=Label(text="enter the arrival time  ")
l2=Label(text="  enter the burst time  ")
l3=Label(text="   enter the priority   ")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
arr1=StringVar()
arr2=StringVar()
arr3=StringVar()
e1=Entry(width=50,textvariable=arr1)
e2=Entry(width=50,textvariable=arr2)
e3=Entry(width=50,textvariable=arr3)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
final=Process.Proces()

def compare():
    a1=len(final.burst)
    a2=len(final.arrival)
    a3=len(final.priority)
    if a1==0 or a2==0 or a3==0 or a1!=a2 or a1!=a3 or a2!=a3:
        msg.showerror("data input","entered values are not correct, enter again!")
    final.tat=[]
    final.wt=[]
    final.control()
    f = Figure(figsize=(5, 4), dpi=100)
    ax = f.add_subplot(111)
    #data = [8.6, 6.2, 6.0, 6.8, 7.4, 9.0]
    #data1 = [5.4, 3.0, 2.8, 3.6, 4.2, 5.8]
    data = final.tat
    data1 = final.wt
    print(data)
    print(data1)
    ind = [1, 2, 3, 4, 5, 6]
    ind1 = [1.3, 2.3, 3.3, 4.3, 5.3, 6.3]
    ind2 = [1.15, 2.15, 3.15, 4.15, 5.15, 6.15]

    width = .3
    tlabel = ['FIFO', 'SNP', 'SP', 'PNP', 'PP','RR']
    rects = ax.bar(ind, data, width, label="Average TAT")
    rects1 = ax.bar(ind1, data1, width, label="Average WT")
    ax.set_xticks(ind1)
    ax.set_ylabel("Time in miliseconds")
    ax.set_xticklabels(tlabel)
    ax.legend()
    canvas = FigureCanvasTkAgg(f, master=root)
    # canvas.show()
    canvas.get_tk_widget().grid(row = 4,column =0, columnspan= 4,sticky = W+E+N+S, padx = 70)
    labels()
def callme(a):
    if a==1:
        temp = arr1.get()
    elif a==2:
        temp = arr2.get()
    else:
        temp = arr3.get()
    avj=temp.split()
    avj1=[]
    for i in avj:
        if i==" ":
            continue
        else:
            avj1.append(int(i))
    if a==1:
        final.arrival=avj1
        print("in 1",avj1)
    elif a==2:
        final.burst=avj1
        print("in 2", avj1)
    else:
        final.priority=avj1
        print("in 3",avj1)
b1=Button(text="submit",command= lambda : callme(1))
b2=Button(text="submit",command= lambda : callme(2))
b3=Button(text="submit",command= lambda : callme(3))
b4=Button(text="compare",command= lambda : compare())

b1.grid(row=0,column=2)
b2.grid(row=1,column=2)
b3.grid(row=2,column=2)
b4.grid(row=3,column=1)

def labels():
    l4=Label(text=" FIFO = First in first out ")
    l5=Label(text="  SNP = Sjf nonpremptive  ")
    l6=Label(text="   SP = Sjf Premptive   ")
    l7=Label(text="  PNP = Priority nonpremptive ")
    l8=Label(text="   PP = Priority premptive  ")
    l9=Label(text="   RR = Round Robin   ")
    l4.grid(row=5,column=1)
    l5.grid(row=6,column=1)
    l6.grid(row=7,column=1)
    l7.grid(row=8,column=1)
    l8.grid(row=9,column=1)
    l9.grid(row=10,column=1)




root.mainloop()

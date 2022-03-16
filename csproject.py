from tkinter import *
root=Tk()
root.configure(background="deep sky blue")
root.title("CURRENCY CONVERTER")
root.geometry("300x350")
l5=Label(root,text="Enter the amount",fg="red",bg="deep sky blue",font="bold 12")
l5.grid(column=11,row=1)
e=Entry(root,width=10)
e.grid(column=11,row=3)
l2=Label(root,text="how do you like to convert the currency:\nfrom indian rupees to other currency :enter a",fg="orange red",bg="deep sky blue",font="bold 10") 
l2.grid(column=11,row=4)
l7=Label(root,text="from other currencies to indian rupees:enter b",fg="orange red",bg="deep sky blue",font="bold 10")
l7.grid(column=11,row=5)

def a():
    with open('currencydata.txt') as r:
	           lines = r.readlines()

    currencyDict = {}
    for line in lines:
	    parsed = line.split("\t")
	    currencyDict[parsed[0].lower().strip().replace(" ","")] = parsed[1]
    e1 = Entry(root,width=30)
    e1.grid(column=11,row=6)
    e1.insert(0,"Enter the currency name")
    def submit():
       w=float(currencyDict[(e1.get()).strip().replace(" ","")])
       l4=Label(root,text=f"{int(e.get())} INR is equal to {int(e.get())*w} {e1.get()}",fg="black",bg="blue",font="bold 10")
       l4.grid(column=11,row=8)
    bt3=Button(root,text="Submit",command=submit)
    bt3.grid(column=11,row=7)
def b():
    with open('currency2.txt') as t:
             lines=t.readlines()
    currencyDict = {}
    for line in lines:
	    parsed = line.split("\t")
	    currencyDict[parsed[0].lower().strip().replace(" ","")] = parsed[2]

    e2=Entry(root,width=30)
    e2.grid(column=11,row=6)
    e2.insert(0,"Enter the currency name")
    def submit():
         g=float(currencyDict[(e2.get()).strip().replace(" ","")])
         l3=Label(root,text=f"{int(e.get())} {e2.get()} is equal to {int(e.get())*g}INR",fg="black",bg="blue",font="bold 10")
         l3.grid(column=11,row=8)
    bt4=Button(root,text="Submit",command=submit)
    bt4.grid(column=11,row=7)
bt1=Button(root,text="a",command=a)
bt1.grid(column=12,row=4)
bt2=Button(root,text="b",command=b)
bt2.grid(column=12,row=5)
root.mainloop()

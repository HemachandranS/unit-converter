from tkinter import *
from tkinter import ttk
cdict = {
    "temperature": {
        "kelvin": {
            "kelvin": lambda x: x,
            "fahrenheit": lambda x:(x - 273) * 9/5 + 32,
            "celcius": lambda x:(x-273),
            },
        "celcius": {
            "celcius": lambda x: x,
            "kelvin": lambda x:x+273,
            "fahrenheit": lambda x:(x*9/5) + 32,
            },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celcius": lambda x: ((x - 32.0) * (5.0/9.0)),
            "kelvin": lambda x: ((x - 32.0) * (5.0/9.0)) + 273,
            },
        }
    }
if __name__ == "__main__":

    try:

        print("{0:.4f}".format(cdict["temperature"]["celcius"]["fahrenheit"](2)))

    except KeyError:
            pass

    for k in cdict.keys():

        print(k.capitalize())

        print(tuple(cdict[k].keys()))

 

def setUnitCb(*args):

    cbUnitFrom['values'] = tuple(cdict[quantVar.get().lower()].keys())

    cbUnitTo['values'] = tuple(cdict[quantVar.get().lower()].keys())

 

 

def calculate(*args):

    result = "{0:.4f}".format(cdict[quantVar.get().lower()][fromVar.get()][toVar.get()](val.get()))

    result_string = val.get(), fromVar.get(), "=", result, toVar.get()

    resultVar.set(result_string)

 

 

root = Tk()

root.title("Temperature Conversion")

 

Label(root, text="Quantity : ").grid(row=0, column=0, columnspan=4, sticky=W)

 

quantVar = StringVar()

cbQuantity = ttk.Combobox(root, textvariable=quantVar, state="readonly",values=tuple([x.capitalize() for x in cdict.keys()]))

cbQuantity.bind("<<ComboboxSelected>>", setUnitCb)

cbQuantity.grid(row=0, column=1)

 

Label(root, text="Convert : ").grid(row=1, column=0)

 

val = DoubleVar()

Entry(root, textvariable=val, width=7).grid(row=1, column=1)

 

fromVar = StringVar()

cbUnitFrom = ttk.Combobox(root, textvariable=fromVar, state="readonly")

cbUnitFrom.grid(row=1, column=2)

 

Label(root, text="to").grid(row=1, column=3)

 

toVar = StringVar()

cbUnitTo = ttk.Combobox(root, textvariable=toVar, state="readonly")

cbUnitTo.grid(row=1, column=4)

 

Button(root, text="Calculate", command=calculate).grid(row=2, columnspan=5)

 

resultVar = StringVar()

resultLabel = Label(root, textvariable=resultVar).grid(row=3, column=0, columnspan=5, sticky=W)

 

for child in root.winfo_children():

    child.grid_configure(padx=5, pady=5)

 

root.mainloop()

            
            

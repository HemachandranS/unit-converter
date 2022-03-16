from tkinter import *
from tkinter import ttk

cdict = {
    "volume": {
        "cubic meter": {
            "cubic meter": lambda x: x,
            "liter": lambda x: 1000 * x,
            "millileter": lambda x: 1000000 * x,
            "imperial gallon": lambda x: 219.969 * x,
            "imperial cup": lambda x: x * 3519.51,
            "fluid ounce": lambda x: x * 35195.1,
            "imperial teaspoon": lambda x: x * 168936,
            "imperial tablespoon": lambda x: x * 56312.1,
            "cubic foot": lambda x: x * 35.3147,
            "cubic inch": lambda x: x *61023.7,
        },
        "liter": {
            "cubic meter": lambda x: x / 1000,
            "liter": lambda x: x,
            "millileter": lambda x: 1000 * x,
            "imperial gallon": lambda x: 0.219969 * x,
            "imperial cup": lambda x: x * 3.51951,
            "fluid ounce": lambda x: x * 35.1951,
            "imperial teaspoon": lambda x: x * 168.936,
            "imperial tablespoon": lambda x: x * 56.3121,
            "cubic foot": lambda x: x * 0.0353147,
            "cubic inch": lambda x: x * 61.0237,
        },
        "millileter": {
            "cubic meter": lambda x: x / 1000000,
            "liter": lambda x: x / 1000,
            "millileter": lambda x: x,
            "imperial gallon": lambda x: x * 0.000219969,
            "imperial cup": lambda x: x * 0.00351951,
            "fluid ounce": lambda x: x * 0.0351951,
            "imperial teaspoon": lambda x: x * 0.168936,
            "imperial tablespoon": lambda x: x * 0.0563121,
            "cubic foot": lambda x: x * 0.0000353147,
            "cubic inch": lambda x: x * 0.0610237,
        },
        "imperial gallon": {
            "cubic meter": lambda x: x / 220,
            "liter": lambda x: 4.54609 * x,
            "millileter": lambda x: 4646.09 * x,
            "imperial gallon": lambda x: x,
            "imperial cup": lambda x: x * 16,
            "fluid ounce": lambda x: x * 160,
            "imperial teaspoon": lambda x: x * 768,
            "imperial tablespoon": lambda x: x * 256,
            "cubic foot": lambda x: x / 6.229,
            "cubic inch": lambda x: x * 227.419,
        },
        "imperial cup": {
            "cubic meter": lambda x: x / 3520,
            "liter": lambda x: x / 3.52,
            "millileter": lambda x: x * 284.131,
            "imperial gallon": lambda x: x / 16,
            "imperial cup": lambda x: x,
            "fluid ounce": lambda x: x * 10,
            "imperial teaspoon": lambda x: x * 48,
            "imperial tablespoon": lambda x: x * 16,
            "cubic foot": lambda x: x / 99.661,
            "cubic inch": lambda x: x * 17.339,
        },
        "fluid ounce": {
            "cubic meter": lambda x: x / 35195,
            "liter": lambda x: x / 35.195,
            "millileter": lambda x: x * 28.4131,
            "imperial gallon": lambda x: x / 160,
            "imperial cup": lambda x: x / 10,
            "fluid ounce": lambda x: x,
            "imperial teaspoon": lambda x: x * 4.8,
            "imperial tablespoon": lambda x: x * 1.6,
            "cubic foot": lambda x: x / 996.61,
            "cubic inch": lambda x: x * 1.7339,
        },
        "imperial teaspoon": {
            "cubic meter": lambda x: x / 168936,
            "liter": lambda x: x / 168.936,
            "millileter": lambda x: x * 5.91939,
            "imperial gallon": lambda x: x / 768,
            "imperial cup": lambda x: x / 48,
            "fluid ounce": lambda x: x / 4.8, 
            "imperial teaspoon": lambda x: x,
            "imperial tablespoon": lambda x: x / 3,
            "cubic foot": lambda x: x / 4784,
            "cubic inch": lambda x: x / 2.768,
        },
        "imperial tablespoon": {
            "cubic meter": lambda x: x / 56312,
            "liter": lambda x: x / 56.312,
            "millileter": lambda x: x * 17.7582,
            "imperial gallon": lambda x: x / 256,
            "imperial cup": lambda x: x / 16,
            "fluid ounce": lambda x: x / 1.6,
            "imperial teaspoon": lambda x: x * 3,
            "imperial tablespoon": lambda x: x,
            "cubic foot": lambda x: x / 1595,
            "cubic inch": lambda x: x * 1.08367,
        },
        "cubic foot": {
            "cubic meter": lambda x: x / 35.315,
           "liter": lambda x: x / 0.035315,
            "millileter": lambda x: x * 28316.8,
            "imperial gallon": lambda x: x * 6.22884,
            "imperial cup": lambda x: x * 99.6614,
            "fluid ounce": lambda x: x * 996.614,
            "imperial teaspoon": lambda x: x * 4783.74,
            "imperial tablespoon": lambda x: x * 1594.58,
            "cubic foot": lambda x: x,
            "cubic inch": lambda x: x * 1728,
        },
        "cubic inch": {
            "cubic meter": lambda x: x / 61024,
            "liter": lambda x: x / 61.024,
            "millileter": lambda x: x * 16.3871,
            "imperial gallon": lambda x: x / 277,
            "imperial cup": lambda x: x / 17.339,
            "fluid ounce": lambda x: x / 1.7339,
            "imperial teaspoon": lambda x: x * 2.76837,
            "imperial tablespoon": lambda x: x / 1.084,
            "cubic foot": lambda x: x / 1728,
            "cubic inch": lambda x: x,
        },
    },
    
    "mass": {
        "gram": {
            "gram": lambda x: x,
            "kilogram": lambda x: x / 1000,
            "tonne": lambda x: x / 1000000,
            "milligram": lambda x: x * 1000,
            "stone": lambda x: x / 6350,
            "pound": lambda x: x / 454,
            "ounce": lambda x: x / 28.35,
        },
        "kilogram": {
            "kilogram": lambda x: x,
            "gram": lambda x: x * 1000,
            "tonne": lambda x: x / 1000,
            "milligram": lambda x: x * 1000000,
            "stone": lambda x: x / 6.35,
            "pound": lambda x: x * 2.205,
            "ounce": lambda x: x * 35.274,
        },
        "tonne": {
            "tonne": lambda x: x,
            "kilogram": lambda x: x * 100,
            "gram": lambda x: x * 1000000,
            "milligram": lambda x: x * 1000000000,
            "stone": lambda x: x * 157,
            "pound": lambda x: x * 2204.62,
           "ounce": lambda x: x * 35274,
        },
        "milligram": {
            "gram": lambda x: x / 1000,
            "kilogram": lambda x: x / 1000000,
            "tonne": lambda x: x / 1000000000,
            "milligram": lambda x: x,
            "stone": lambda x: x / 6350000,
            "pound": lambda x: x / 454000,
            "ounce": lambda x: x / 28350,
        },
        "stone": {
            "gram": lambda x: x * 6350,
            "kilogram": lambda x: x * 6.35029,
            "tonne": lambda x: x / 157,
            "milligram": lambda x: x * 6350290,
            "stone": lambda x: x,
            "pound": lambda x: x * 14,
            "ounce": lambda x: x * 224,
        },
        "pound": {
            "gram": lambda x: x / 453.592,
            "kilogram": lambda x: x * 2.205,
            "tonne": lambda x: x * 2205,
            "milligram": lambda x: x * 453592,
            "stone": lambda x: x / 14,
            "pound": lambda x: x,
            "ounce": lambda x: x * 16,
        },
        "ounce": {
            "gram": lambda x: x * 28.35,
            "kilogram": lambda x: x / 35.274,
            "tonne": lambda x: x / 35274,
            "milligram": lambda x: x * 28349.5,
            "stone": lambda x: x / 224,
            "pound": lambda x: x / 16,
            "ounce": lambda x: x,
        },
    }
}
def setUnitCb(*args):
    cbUnitFrom['values'] = tuple(cdict[quantVar.get().lower()].keys())
    cbUnitTo['values'] = tuple(cdict[quantVar.get().lower()].keys())


def calculate(*args):
    result = "{0:.4f}".format(cdict[quantVar.get().lower()][fromVar.get()][toVar.get()](val.get()))
    result_string = val.get(), fromVar.get(), "=", result, toVar.get()
    resultVar.set(result_string)


root = Tk()
root.title("Unit conversion calculator")

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

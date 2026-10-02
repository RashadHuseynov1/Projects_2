import tkinter as tk
from tkinter import ttk


#Currencies are fixed currencies for now, as I will make it floating currencies in the future
conversions = {
    "Currencies": {
        "USD": 1.0,
        "EUR": 1.13,
        "GBP": 1.32,
        "CNY": 0.15,
        "RUB": 0.012
    },

    "Weight": {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lbs": 0.453592,
        "tonnes": 1000.0,
        "ounce": 0.0283495
    },

    "Volume": {
        "litres": 1.0,
        "ml": 0.001,
        "cubicmetre": 1000.0
    },

    "Length": {
        "km": 1.0,
        "meters": 0.001,
        "centimetre": 0.00001,
        "miles": 1.60934,
        "foot": 0.0003048,
        "inch": 0.0000254,
        
    },

    "Area": {
        "sq_metre": 1.0,
        "acres": 4046.86,
        "sq_km": 1000000,
        "hectare": 10000
    }
}


def update(event=None):
    category = category_box.get()
    units = list(conversions[category].keys())
    
    combo_1['values'] = units
    combo_2['values'] = units
    
    combo_1.set(units[0])
    if len(units) > 1:
        combo_2.set(units[1])
    else:
        units[0]    


def convert():
    try:
        number = float(entry_1.get())
        category = category_box.get()
        unit_from = combo_1.get()
        unit_to = combo_2.get()

        unit_dict = conversions[category]

        final_result = number * (unit_dict[unit_from] / unit_dict[unit_to])

        label_1.config(text=f"{number} {unit_from} equals to {final_result:.6g} {unit_to}")

    except ValueError:
        label_1.config(text="Please, write correct number!")


root = tk.Tk()
root.title("Converter")
root.geometry("800x600")

entry_1 = tk.Entry(root, width=20)
entry_1.pack(pady=10)

categories = list(conversions.keys())
category_box = ttk.Combobox(root, values=categories)
category_box.pack(pady=10)
category_box.set(categories[0])
category_box.bind("<<ComboboxSelected>>", update)

combo_1 = ttk.Combobox(root, state="readonly")
combo_1.pack(pady=10)

combo_2 = ttk.Combobox(root, state="readonly")
combo_2.pack(pady=10)

label_1 = tk.Label(root, text="The result will be shown here", padx=10, pady=10, font=("Aptos", 15))
label_1.pack(pady=10)

button_1 = tk.Button(root, text="Convert", width=30, pady=5, padx=5, command=convert)
button_1.pack(pady=20)

button_2 = tk.Button(root, text="Stop", width=10, padx=5, pady=5, command=root.destroy)
button_2.pack(pady=20)


update()
root.mainloop()
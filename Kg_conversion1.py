import tkinter as tk
from tkinter import *

#define pound conversion function
def convert_to_pound():
    try:
        kg_value = float(kg.get()) #gets value from entry
        pounds = kg_value *2.20462 #conversion
        result_label.config(text=f"{pounds} pounds") #update the result label
    except ValueError:
        result_label.config(text="PLease enter a valid number.")

#define gram conversion function
def convert_to_gram():
    try:
        kg_value = float(kg.get()) #gets value from entry
        grams = kg_value *1000 #conversion
        result_label.config(text=f"{grams} grams") #update the result label
    except ValueError:
        result_label.config(text="PLease enter a valid number.")

#define ounce conversion function
def convert_to_ounce():
    try:
        kg_value = float(kg.get()) #gets value from entry
        ounces = kg_value *35.274 #conversion
        result_label.config(text=f"{ounces} ounces") #update the result label
    except ValueError:
        result_label.config(text="PLease enter a valid number.")

#Make the basic GUI for measurement conversion
window = tk.Tk() #creating a window
window.title("My Conversion") #title of window
window.geometry("500x500") #size of window

#create a label
Label (window,text="Weight Converter",font=("Arial", 20), bg="black", fg="yellow").pack()
Label(window,text="Enter weight in KGs",font=("Arial", 14)).pack()

#make entry feild
kg = StringVar() #variable to hold input value "kg"

#make entry field
Entry(window,textvariable=kg).pack()

#Label to display the result
result_label = Label(window, text="",font=("Arial", 14))
result_label.pack()

#making buttons
Button(window, text="Convert to Gram",bg="blue",command=convert_to_gram).pack()
Button(window, text="Convert to Ounce",bg="red",command=convert_to_ounce).pack()
Button(window, text="Convert to Pounds",bg="green",command=convert_to_pound).pack()

window.mainloop()
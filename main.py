from tkinter import *
from tkinter import messagebox

import tk as tk


window = Tk()
window.title('Temperature Convector')  # title of the window
window.minsize(width=500, height=500)  # size of the window
window["bg"] = "aqua"

celcius_var = IntVar
fahrenheit_var = IntVar
results_entry = IntVar

l1 = LabelFrame(window, text=' Celcius To Fahrenheit', padx=20, pady=20, bg="pink", borderwidth=5)  # window 1, text,
# size
l1.place(x=50, y=50)
E1 = Entry(l1, state='readonly')
E1.grid(row=4, column=0)

l2 = LabelFrame(window, text='Fahrenheit To Celcius', padx=20, pady=20, bg="pink", borderwidth=5)   # window 2, text,
# size
l2.place(x=250, y=50)
E2 = Entry(l2, state='readonly')
E2.grid(row=4, column=5)


def Cel_Active():  # defines the celcius activated
    E2.configure(state='readonly')
    E1.configure(state='normal')


def Far_Active():  # defines the fahrenheit activated
    E1.configure(state='readonly')
    E2.configure(state='normal')


def clear_fields():  # will clear all the inputs
    E1.configure(state='normal')
    E1.delete(0, END)
    E1.configure(state='readonly')

    E2.configure(state='normal')
    E2.delete(0, END)
    E2.configure(state='readonly')

    results_entry.config(state="normal")
    results_entry.delete(0, END)
    results_entry.config(state="readonly")


def temperature_conversion():  # temperature conversion
    try:
        if E1['state'] == "normal" and E1.get() != "":
            to_fahrenheit = float(E1.get()) * 9 / 5 + 32
            results_entry.config(state="normal")
            results_entry.delete(0, END)
            results_entry.insert(0, to_fahrenheit)
            results_entry.config(state="readonly")
        elif E2['state'] == "normal" and E2.get() != "":
            to_celsius = (float(E2.get()) - 32) * 5 / 9
            results_entry.config(state="normal")
            results_entry.delete(0, END)
            results_entry.insert(0, to_celsius)
            results_entry.config(state="readonly")
    except ValueError as ex:
        messagebox.showerror("Error", ex)  # Error message will show if you type a value incorrect


def exit_program():  # exiting message box
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                     icon='warning')
    if msg_box == "yes":  # if you type yes, you will return to program
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")  # You will return to the app


btn_active = Button(window, text='Activate Celcius to Fahrenheit', command=Cel_Active, bg="pink", borderwidth=5)
btn_active.place(x=20, y=150)  # button for activation

btn_active1 = Button(window, text='Activate Fahrenheit to Celcius', command=Far_Active, bg="pink", borderwidth=5)
btn_active1.place(x=250, y=150)  # button for activation

convert_button = Button(window, text="Convert", command=temperature_conversion, bg="pink", borderwidth=5)
convert_button.place(x=130, y=240)  # button for temperature conversion

results_entry = Entry(window, bg="pink", width=10, state="readonly", borderwidth=5)
results_entry.place(x=220, y=240, height=100)  # results entry window

clear_button = Button(window, text="Clear", command=clear_fields, bg="pink", borderwidth=5)
clear_button.place(x=340, y=240)  # button for clearing

exit_button = Button(window, text="Exit", command=exit_program, bg="pink", borderwidth=5)
exit_button.place(x=340, y=290)  # button for exiting

window.mainloop()  # close the loop or else it will not show

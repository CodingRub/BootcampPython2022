from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_res_label.config(text=f"{round(km, 2)}")

window = Tk()
window.title("Miles to Km Converter")
window.config(pady=30, padx=30)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_res_label = Label(text="0")
km_res_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calcul_btn = Button(text="Calculate", command=miles_to_km)
calcul_btn.grid(column=1, row=2)

window.mainloop()
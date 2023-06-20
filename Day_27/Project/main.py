from tkinter import *


def converter():
    result_label.config(text=round(int(input_box.get())*1.6))

window = Tk()
window.title('First gui')
window.minsize(width=200, height=150)
window.config(padx=10, pady=10)

# Miles label

miles_label = Label(text='Miles', font=('Arial', 15, "bold"))
miles_label.grid(column=2, row=0)

# is equal to label

equal_label = Label(text='is equal to', font=('Arial', 15, "bold"))
equal_label.grid(column=0, row=1)

# result label

result_label = Label(text='0', font=('Arial', 15, "bold"))
result_label.grid(column=1, row=1)

# KM label

km_label = Label(text='Km', font=('Arial', 15, "bold"))
km_label.grid(column=2, row=1)

# calculate button
button = Button(text="calculate", command=converter)
button.grid(column=1, row=2)

# entry

input_box = Entry()
input_box.config(width=10)
input_box.grid(column=1, row=0)






window.mainloop()
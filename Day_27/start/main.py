from tkinter import *


def button_clicked():
    my_label.config(text=input_box.get())

window = Tk()
window.title('First gui')
window.minsize(width=300, height=150)
window.config(padx=100, pady=100)

# label

my_label = Label(text='Label', font=('Arial', 24, "bold"))
my_label.grid(column=0, row=0)


# button
button = Button(text="click", command=button_clicked)
button.grid(column=0, row=2)

# button2
button2 = Button(text="click", command=button_clicked)
button2.grid(column=1, row=1)

# entry
input_box = Entry()
input_box.config(width=10)
input_box.grid(column=3, row=3)






window.mainloop()
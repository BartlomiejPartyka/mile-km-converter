from tkinter import *


def converter():
    d_mile = int(user_input.get())
    d_km = 1.609 * d_mile
    label_3.config(text=f'{d_km}')


window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=200, height=100)

user_input = Entry(width=10)
user_input.grid(row=0, column=1)

label_1 = Label(text="miles", font=('Arial', 18))
label_1.grid(row=0, column=2)

label_2 = Label(text='is', font=('Arial', 18))
label_2.grid(row=1, column=0)

label_3 = Label(text='', font=('Arial', 18))
label_3.grid(row=1, column=1)

label_4 = Label(text='kilometers.', font=('Arial', 18))
label_4.grid(row=1, column=2)

button = Button(text='Calculate', command=converter)
button.grid(row=2, column=1)

window.mainloop()

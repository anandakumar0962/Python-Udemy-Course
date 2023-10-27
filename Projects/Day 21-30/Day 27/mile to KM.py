from tkinter import *

window = Tk()
window.minsize(width=300, height=200)

def calculate():
    miles = int(input.get())
    kilometers = round(miles*1.609)
    result.config(text=f"{kilometers}")

#Labels
label1= Label(text='is equal to')
label1.grid(column=0, row=1)

label2 = Label(text='Miles')
label2.grid(column=2, row=0)

result = Label(text='0')
result.grid(column=1, row=1)
result.config(padx=5, pady=5)

label4 = Label(text='Kilometers')
label4.grid(column=2, row=1)

#Button
button = Button(text='Calculate', width=10, height=1, command=calculate)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)





window.mainloop()
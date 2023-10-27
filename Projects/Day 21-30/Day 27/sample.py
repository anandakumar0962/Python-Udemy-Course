from tkinter import *


window = Tk()
window.minsize(width=300, height=300)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#Label
my_label = Label(text='Demo', font=('Arial', 15, 'bold'))
my_label.config(text='New Label')
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Button
button = Button(text='Click me!', command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=3, row=4)

#Button2
button2 = Button(text="New Button")
button2.grid(column=2, row=0)










window.mainloop()
from Tkinter import *
#creates the GUI
root = Tk()
root.resizable(width=True, height=True)
root.geometry("400x150")
frame = Frame(root)

def retrieve_input():
 input = first_entry.get("1.0",'end-1c')

title_label = Label(frame, text="CHEERS", fg="black")
title_label.grid(row=0, column=1)

radius_label = Label(frame, text="Enter Radius", fg="black")
radius_label.grid(row=1, column=0, sticky=E)

first_entry = Entry(frame)
first_entry.grid(row=1, column=1)

length_label_radians = Label(frame, text="Output Length(alpha in radians)", fg="black")
length_label_radians.grid(row=2, column=0, sticky=E)

second_entry = Entry(frame)
second_entry.grid(row=2, column=1)

length_label_degrees = Label(frame, text="Output Length(alpha in degrees)", fg="black")
length_label_degrees.grid(row=3, column=0, sticky=E)

third_entry = Entry(frame)
third_entry.grid(row=3, column=1)

length_button = Button(frame, text="Calculate Length", fg="black", command= lambda: retrieve_input())
length_button.grid(row=5, column=0, sticky=E)

XML_button = Button(frame, text="Save to XML ", fg="black")
XML_button.grid(row=5, column=1, sticky=E)

frame.pack()
#frame.pack(fill=None, expand=False)
root.mainloop()


print(input)

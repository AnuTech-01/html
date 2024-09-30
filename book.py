# Import Module 
from tkinter import *

# Create Object 
root = Tk() 

# Set geometry 
root.geometry('400x500')
              

# Add Buttons, Label, ListBox 
Label(root, text="Name",font="arial 12 bold").grid(row=0)
Label(root, text="Phone No.",font="arial 12 bold").grid(row=1)
Label(root, text="Adders",font="arial 12 bold").grid(row=2)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e1.grid(row=0 ,column=1)
e2.grid(row=1 ,column=1)
e3.grid(row=2 ,column=1)



Button(root,text="Add",font="arial 12 bold").place(x= 10, y=270) 
Button(root,text="View",font="arial 12 bold").place(x= 10, y=310) 
Button(root,text="Delete",font="arial 12 bold").place(x= 10, y=350) 
Button(root,text="Reset",font="arial 12 bold").place(x= 10, y=390) 

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12) 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=100,y=260) 

# Execute Tkinter 
root.mainloop()

from Tkinter import *


root = Tk()

grp_lbl = Label(root,text="Group Name:")
grp_lbl.grid(row=0)
############################################
grp_entry = Entry(root)
grp_entry.grid(row=0,column=1)
###################
c = Checkbutton(root,text="Specify manually:")
c.grid(row=1,column=0)
################


mainloop()
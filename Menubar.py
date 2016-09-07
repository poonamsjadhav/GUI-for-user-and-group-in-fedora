from Tkinter import *
from tkFileDialog   import askopenfilename



#functions for file menu
def add_user():
    print ("New user adding function")
def add_group():
    print("New group functionality")
def refresh():
    print("refresh functionality")


    #functions for edit
def remove_group():
    Print("Functions to remove group")
def edit_group():
    print("Edit group functionality")
def edit_user():
    print ("Editing user functionality")
def usermod():
    print("changing the permission for the user")
def remove_user():
    print("removing  user")

#functions about help
def contact_us():
    print("Page regarding feedbacks")
def About():
    print "This is a simple example of a menu"


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu,tearoff=0)                 #try script without using tearoff to match the diff
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Add user", command=add_user)
filemenu.add_command(label="Create group", command=add_group)
filemenu.add_separator()
filemenu.add_command(label="Refresh",command=refresh)
filemenu.add_command(label="Exit", command=root.quit)

#End of file menu
#Edit menu starts from here
editmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Edit User",command=edit_user)
editmenu.add_command(label="Remove User",command=remove_user)
editmenu.add_command(label="Edit Group",command=edit_group)
editmenu.add_command(label="Change Permission",command=usermod)




#help menu starts from here
helpmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Contact us",command=contact_us)
helpmenu.add_command(label="About...", command=About)



#Creating the toolbar

toolbar = Frame(root)
tulbar_useradd= Button(toolbar,text="Add User",command=add_user)
tulbar_useradd.pack(side=LEFT,padx=2,pady=2)
tulbar_grpadd = Button(toolbar,text="Add Group",command=add_group)
tulbar_grpadd.pack(side=LEFT,padx=2,pady=2)
tulbar_dlt = Button(toolbar,text="Delete",command=remove_user)
tulbar_dlt.pack(side=LEFT,padx=2,pady=2)
tulbar_rfrsh = Button(toolbar,text="Refresh",command=refresh)

tulbar_rfrsh.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)


''''
Creating frames
one for search utility
another for the displaying the group and suser information
'''''


search_frame = Frame(root)
search_frame.pack(side=TOP)

search_label = Label(search_frame,text="Search Filter:")
entry_search  = Entry(search_frame)
#search_label.grid(row=0)
#entry_search.grid(row=0,column=1)
search_label.pack(side=LEFT)
entry_search.pack(side=LEFT)






mainloop()


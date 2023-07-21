from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
root.title("Notepad By BVK")
def New():
    print("The file new is created")
    with open("notepad.txt","w") as f:
        f.write(" ")
def Save():
    print("The file has saved")
def save_text():
    print("The file has been saved")
    text_file = open("test.txt", "w")
    text_file.write(y.get(1.0, END))
    text_file.close()
def Open():
    print("The file is opened")
def open_text():
    print("The file is opened")
    text_file = open("test.txt", "r")
    content = text_file.read()
    y.insert(END, content)
    text_file.close()
def time():
    import datetime as dt
    x=dt.datetime.today()
    print(x)
    with open("test.txt","r") as f:
        f.read()
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=New)
m1.add_command(label="Save",command=Save)
m1.add_command(label="Open",command=Open)
m1.add_command(label="Time/Date",command=time)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
def Undo():
    print("The file is undoned")
def Redo():
    print("The file is redoed")
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=Undo)
m2.add_command(label="Redo",command=Redo)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)
opentxt= Button(root, text="Open Text File", command=open_text)
opentxt.place(x=70,y=400)
save = Button(root, text="Save File", command=save_text)
save.place(x=10,y=400)
def Help():
    msg=messagebox.showinfo("Viewing Help","For contact:7207203676 \n mail:vinodkumarjntua@gmail.com \n for any queries you can contact us")
def About():
    msg=messagebox.showinfo("About this notepad","This Notepad is done by BVK group of industries and done with pycharm")
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="View Help",command=Help)
m3.add_command(label="About this notepad",command=About)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)
z=Scrollbar(root)
z.pack(side=RIGHT,fill=Y)
y=Text(root)
y.pack()
statusvar=StringVar()
statusvar.set("This notepad is done by B.Vinod Kumar")
x=Label(root,textvariable=statusvar,relief=SUNKEN).pack(side=BOTTOM,fill=X)
root.mainloop()
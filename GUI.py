from tkinter import *
from kivy.core.image import Image as CoreImage



root = Tk()
root.title("FindMyCamper")

var = StringVar()
label = Label( root, textvariable = var )

L = Label(root, text = "Copy camp website URL")
L.place(x = 0, y = 200)
root.geometry("500x500")

var.set("Upload image of Your Child")


label.pack()

B = Button(root, text = "Upload")
B.place(x = 220, y = 50)




campEntry = Entry(root, bd = 1)
campEntry.place(x = 310, y = 200)



L1 = Label(root, text = "User Name")
L1.place(x = 0, y = 250)

E1 = Entry(root, bd = 1)
E1.place(x = 310, y = 250)

L2 = Label(root, text = "Password")
L2.place(x = 0, y = 300)

E2 = Entry(root, bd = 1)
E2.place(x = 310, y = 300)


detect = Button(root, text = "Detect")
detect.place(x=220, y=400)

root.mainloop()
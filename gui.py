from tkinter import *
# from attendance import *
from test import *

root = Tk()
root.title('Facial Recognition Attendance Program (Alpha-Version V1.0)')
root.minsize(800, 600)
root.configure(background='darkgrey')
label = Label(root, text="Welcome to Automated Attendance System")
label.configure(font=("", 35))
label.pack(fill='x')
btn1 = Button(root, text="Add Image to Database", fg='brown', bg='pink').pack()
btn2 = Button(root, text="Open Attendance Sheet", fg='brown', bg='pink', command=openExcel).pack()
btn3 = Button(root, text="Start Program", fg='brown', bg='pink', width=18).pack()
btn4 = Button(root, text="Stop Program", fg='brown', bg='pink', width=18).pack()
root.mainloop()



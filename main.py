from Tkinter import *
import time

c=0

def timer():
	root.after(1,timer)
	global c
	c+=1
	if c%1==0: 
		label.configure(text=str(c))

root=Tk()
root.title("HelloWorld")
root.geometry("800x600")
root.resizable(width=False, height=False)

canvas=Canvas(root,width=800,height=600,bg='white')
#canvas.pack()

label=Label(root,text='0')
label.pack()
timer()

canvas.create_rectangle(10,10,50,50,fill='blue')

root.mainloop()

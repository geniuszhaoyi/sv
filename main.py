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

canvas=Canvas(root,width=770,height=588,bg='white') # 35*28
canvas.pack()

f=open('farm.map')
ls=f.readlines()
f.close()

for i in range(22):
	for j in range(21):
		if ls[j][i]=='0':
			canvas.create_rectangle(i*35+0,j*28+0,i*35+34,j*28+27,fill='grey',outline='grey')

'''label=Label(root,text='0')
label.pack()
timer()
'''

canvas.create_rectangle(10,10,50,50,fill='blue')

root.mainloop()

from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox


GUI = Tk() # หน้าโปรแกรม

GUI.title('โปรแกรมบันทึกข้อมูล')# ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมทดสอบ',font=('Ansana New',30),fg='green')
L1 .place(x=20,y=30)
################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 999 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = labelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='How many bath?',command=Buttom2)
B2.pack(ipadx=20,ipady=20)
################################

GUI.mainloop()

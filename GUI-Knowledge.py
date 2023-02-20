from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox # theme of tk


#การสร้าง interface แบบปุ่ม

GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400') #ขนาดโปรแกรม กว้าง*สูง

L1 = Label(GUI,text= 'โปรแกรมบันทึกความรู้', font=('Angsana New',30),fg='green')
L1.place(x=20,y=30)
#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')# ใช้ปุ่มจาก theme ttk
#B1.pack() #ปรับตำแหน่งให้ปุ่มอยู่ด้านบน
#B1.pack(ipadx=20,ipady=20) #ขยายปุ่มแนวแกน x 20 pixcel แนวแกน y 20 pixcel

#B2 = Button(GUI,text='เงินมีอยู่กี่บาท')
#B2.pack() #ปรับตำแหน่งให้ปุ่มอยู่ด้านบน

################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=100, y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)# ใช้ปุ่มจาก theme ttk
#B2.pack(ipadx=20,ipady=20) #ขยายปุ่มแนวแกน x 20 pixcel แนวแกน y 20 pixcel
B2.pack(ipadx=20,ipady=20) #กำหนดตำแหน่งพิกัด (x,y) (0,0) อยู่มุมบนซ้าย

################################
def Button3():
    text = 'Python 101 , Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB2.place(x=100, y=200)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนอะไร',command=Button3)# ใช้ปุ่มจาก theme ttk
#B2.pack(ipadx=20,ipady=20) #ขยายปุ่มแนวแกน x 20 pixcel แนวแกน y 20 pixcel
B3.pack(ipadx=20,ipady=20) #กำหนดตำแหน่งพิกัด (x,y) (0,0) อยู่มุมบนซ้าย

GUI.mainloop()

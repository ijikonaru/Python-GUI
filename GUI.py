'''
นี่คือ
โปรแกรม
'''
print('ยอนดีต้อนรับสู่โปรแกรม')

from tkinter import *
from tkinter import ttk, messagebox


GUI = Tk()
GUI.title('Programs By IJIKO v.0.0.1') # นี่คือชื่อโปรแกรม
GUI.geometry('500x300')   # ปรับขนาดหน้านจอ

def Show():
    messagebox.showinfo('Show Box','สวัสดีจ้าวววว เย้!')
    

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Show)
B1.pack(ipadx=50, ipady=30,pady=50) # แปะปุ่มไว้กับโปรแกรมหลัก


GUI.mainloop()

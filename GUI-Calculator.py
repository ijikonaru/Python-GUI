from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
# from calendar import calendar


########################CSV########################
import csv

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

###############GUI#########################
GUI = Tk()
GUI.title('โปรแกรม ขายเนื้อหมู')
GUI.geometry('300x500')

L1 = Label(GUI,text = 'กรอกจำนวนเนื้อหมู (กิโลกรัม)',bg='blue',fg='white', font = ('Angsana new',25))
L1.pack(pady=10)

v_kilo = StringVar() #ตัวแปรพิเศษเอาไว้เก็บค่า
# v_money = StringVar()

E1 = ttk.Entry(GUI,textvariable= v_kilo, width=10,justify='right',font=('impact',30))
E1.pack(pady=10)

# L2 = Label(GUI,text = 'กรอกจำนวนเงินที่ได้รับ (บาท)',bg='green',fg='white', font = ('Angsana new',25))
# L2.pack(pady=10)

# E2 = ttk.Entry(GUI,textvariable= v_money, width=10,justify='right',font=('impact',30))
# E2.pack(pady=10)

by_kilo = 199 #กำหนดราคาเนิ้อหมู
print(f'เนื้อหมูกิโลกรัมละ {by_kilo:.2f} บาท')

def Calc(event=None):
    print('กำลังคำนวณ...กรุณารอสักครู่')
    kilo = float(v_kilo.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar
    print(kilo * by_kilo)
    calc_result = kilo*by_kilo
    # BE=datetime.now().year+543
    # dtime = datetime.now().strftime('%d-%m-%Y+ %H:%M:%S')
    BE = datetime.now().year+543
    dtime = datetime.now().strftime('%d-%m-{} %H:%M:%S'.format(BE))
    data =['เนื้อหมู','{:,.2f}'.format(calc_result),dtime]
    writetocsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด', 'ลูกค้าต้องจ่ายเงินทั้งหมด: {:,.2f} บาท (กิโลกรัมละ 199 บาท)'.format(calc_result))

# def Calc_T(event=None):
#     print('กำลังคำนวณเงินทอน...กรุณารอสักครู่')
#     kilo = float(v_kilo.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar
#     money = float(v_money.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar
#     calc_result = kilo*by_kilo
#     print(money-calc_result)
#     calc_result_t = money-calc_result
#     messagebox.showinfo('เงินทอนลูกค้า', 'ต้องทอนเงินทั้งหมด: {:,.2f} บาท (กิโลกรัมละ 199 บาท)'.format(calc_result_t))

B1 = ttk.Button(GUI, text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30,pady=10)

# B2 = ttk.Button(GUI, text='คำนวณเงินทอน',command=Calc_T)
# B2.pack(ipadx=40,ipady=30,pady=10)

E1.bind('<Return>',Calc) # ต้องใส่คำว่า event=None ไว้ในฟังชั่นด้วย
# E2.bind('<Return>',Calc_T) # ต้องใส่คำว่า event=None ไว้ในฟังชั่นด้วย

GUI.mainloop()

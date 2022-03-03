from tkinter import *
from tkinter import ttk, messagebox
import webbrowser
import wikipedia
from datetime import datetime
# from calendar import calendar






########################CSV########################
import csv

def writetocsv(data,filename='data.csv'):
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

###############GUI#########################
GUI = Tk()
GUI.title('โปรแกรม ขายเนื้อหมู')
GUI.geometry('1200x600')


#################### TAB SETTING #####################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_linkB = PhotoImage(file='linkB.png')
icon_tab3 = PhotoImage(file='tab3.png')

Tab.add(T1, text='เนื้อหมู',image=icon_tab1,compound='left')
Tab.add(T2, text='wiki',image=icon_tab2,compound='left')
Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')



################### TAB 1 - หมู ########################

L1 = Label(T1,text = 'กรอกจำนวนเนื้อหมู (กิโลกรัม)',bg='blue',fg='white', font = ('Angsana new',25))
L1.pack(pady=10)

v_kilo = StringVar() #ตัวแปรพิเศษเอาไว้เก็บค่า
# v_money = StringVar()

E1 = ttk.Entry(T1,textvariable= v_kilo, width=10,justify='right',font=('impact',30))
E1.pack(pady=10)

E1.focus()

# L2 = Label(GUI,text = 'กรอกจำนวนเงินที่ได้รับ (บาท)',bg='green',fg='white', font = ('Angsana new',25))
# L2.pack(pady=10)

# E2 = ttk.Entry(GUI,textvariable= v_money, width=10,justify='right',font=('impact',30))
# E2.pack(pady=10)

by_kilo = 199 #กำหนดราคาเนิ้อหมู
#print(f'เนื้อหมูกิโลกรัมละ {by_kilo:.2f} บาท')

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

B1 = ttk.Button(T1, text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30,pady=10)

# B2 = ttk.Button(T1, text='คำนวณเงินทอน',command=Calc_T)
# B2.pack(ipadx=40,ipady=30,pady=10)

E1.bind('<Return>',Calc) # ต้องใส่คำว่า event=None ไว้ในฟังชั่นด้วย
# E2.bind('<Return>',Calc_T) # ต้องใส่คำว่า event=None ไว้ในฟังชั่นด้วย


################################### TAB 2 - Wiki #####################################

FONT1 = ('Angsana new',25)


L2 = Label(T2,text='ค้นหาข้อมูล wikipedia', font=('Angsana new',25))
L2.pack()

v_search = StringVar() # .get()= ดึงข้อมูล .set('hello') เซ็ตข้อความให้เป็นแบบนั้น

E2 = ttk.Entry(T2, textvariable=v_search,justify='right', font=FONT1)
E2.pack(pady=10)

wikipedia.set_lang('th') #ทำให้เป็นภาษาไทย
v_link = StringVar()

def Search():
    try:
        search = v_search.get() #ดึงข้อความจากช่องกรอกมา
        # text = wikipedia.summary(search)
        text = wikipedia.page(search)
        print(text)
        v_result.set(text.content[:500])
        v_link.set(text.url)
        # if len(text) > 500:
        #     B3 = ttk.Button(T2,text='Link',image=icon_linkB,compound='left',command=Link)
        #     B3.pack(pady=10)
    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้นหาใหม่')

    # เพิ่มฟังชั่นสำหรับเด้งไปอ่านบทความฉบับเต็มในเว็บบราวเซอร์

def Link():
    try:
        # page = v_search.get() #ดึงข้อความจากช่องกรอกมา
        # link = wikipedia.page(page)
        # print(link.url)
        webbrowser.open(v_link.get())
        #v_result.set(text[:1500])
        # v_result.set(link.url)

    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้นหาใหม่')

B2 = ttk.Button(T2,text='Search',image=icon_tab2,compound='left',command=Search)
B2.pack(pady=10)


v_result= StringVar()
v_result.set('----------Result----------')
result = Label(T2,textvariable=v_result,wraplength=550,relief=SUNKEN  , font=(None,15))
result.pack(pady=10)
B3 = ttk.Button(T2,text='อ่านต่อ',image=icon_linkB,compound='left',command=Link)
B3.pack(pady=10)

########################TAB 3################################

Bfont= ttk.Style()
Bfont.configure('TButton',font=('Angsana new',15))

CF1 = Frame(T3)
CF1.place(x=50,y=100)

# ROW0
# header = ['No.','title','quantity','price','total']

allmenu = {}

product ={'latte':{'name':'ลาเต้','price':30},
        'cappuccino':{'name':'คาปูชิโน่','price':35},
        'espresso':{'name':'เอสเพรสโซ่','price':40},
        'greentea':{'name':'ชาเขียว','price':40},
        'icetea':{'name':'ชาเย็น','price':35},
        'hottea':{'name':'ชาร้อน','price':30}}

def UpdateTable():
    table.delete(*table.get_children()) # เคลียร์ข้อมูลเก่าในตาราง
    for i,m in enumerate(allmenu.values(),start=1):
        # {'latte': ['ลาเต้', 30, 1, 30]}
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3]])




# def AddMenu(name='latte'):
def AddMenu(name):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]

    else:
        # {'latte': ['ลาเต้', 30, 1, 30]}
        quan = allmenu[name][2]+1
        total = quan*product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'],quan,total]

    print(allmenu)
    # ยอดรวม
    count = sum([m[3] for m in allmenu.values()])
    v_total.set('{:.2f}'.format(count))
    UpdateTable()



B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=lambda m='latte': AddMenu(m))
B.grid(row=0,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน่',image=icon_tab3,compound='top',command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเพรสโซ่',image=icon_tab3,compound='top',command=lambda m='espresso': AddMenu(m))
B.grid(row=0,column=2,ipadx=20,ipady=10)


# ROW1
B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top',command=lambda m='greentea': AddMenu(m))
B.grid(row=1,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top',command=lambda m='icetea': AddMenu(m))
B.grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top',command=lambda m='hottea': AddMenu(m))
B.grid(row=1,column=2,ipadx=20,ipady=10)

# # ROW2
# B = ttk.Button(CF1,text='อเมริกาโน่ ร้อน',image=icon_tab3,compound='top')
# B.grid(row=2,column=0,ipadx=20,ipady=10)
# B = ttk.Button(CF1,text='คาปูชิโน่ ร้อน',image=icon_tab3,compound='top')
# B.grid(row=2,column=1,ipadx=20,ipady=10)
# B = ttk.Button(CF1,text='เอสเพรสโซ่ ร้อน',image=icon_tab3,compound='top')
# B.grid(row=2,column=2,ipadx=20,ipady=10)

############TABLE################
CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['No.','title','price','quantity','total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(CF2,columns=header, show ='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):
    table.heading(hd,text=hd)
    table.column(hd,width=hw)

# for hd in header:
#     table.heading(hd,text=hd)

L = Label(T3,text='Total: ',font=(None,15))
L.place(x=500,y=450)

v_total = StringVar()
v_total.set(0.0)
LT = Label(T3,textvariable=v_total,font=(None,15))
LT.place(x=600,y=450)

def Reset():
    global allmenu
    allmenu={}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction ID
    v_transaction.set(trstamp)


B = ttk.Button(T3,text='Clear',command=Reset)
B.place(x=500,y=500)



# Transaction ID

v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction ID
v_transaction.set(trstamp)
LTR = Label(T3,textvariable=v_transaction,font=(None,10)).place(x=950,y=70)


# Save Button
FB = Frame(T3)
FB.place(x=890,y=450)

def AddTransaction():
    # Writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction =v_transaction.get()
    print(transaction,stamp,allmenu.values())
    for m in allmenu.values():
        # before: m = ['คาปูชิโน่', 35, 1, 35]
        # after: m=  ['12341234', '2022-02-17 21:09:31', 'คาปูชิโน่', 35, 1, 35]
        m.insert(0,transaction)
        m.insert(1,stamp)
        writetocsv(m,'transaction.csv')
    Reset() #clear data


B= ttk.Button(FB,text='บันทึก',command=AddTransaction)
B.pack(ipadx=30,ipady=20)


# History New Windows

def HistoryWindow(event):
    HIS = Toplevel() # คล้ายกับ GUI = Tk()
    HIS.geometry('800x500')

    L = Label(HIS,text='ประวัติการสั่งซื้อ',font=(None,15))
    L.pack()

    # History
    header = ['ts-id','datetime','title','price','quantity','total']
    hwidth = [100,150,200,100,100,100]

    table_history = ttk.Treeview(HIS,columns=header, show ='headings',height=15)
    table_history.pack()

    for hd,hw in zip(header,hwidth):
        table_history.heading(hd,text=hd)
        table_history.column(hd,width=hw)

    # Update from CSV
    with open('transaction.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        for row in fr:
            table_history.insert('',0,value=row)

    HIS.mainloop()

GUI.bind('<F1>',HistoryWindow)


GUI.mainloop()

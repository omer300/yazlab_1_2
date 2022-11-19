import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title('Yazlab 1 - 2')
window.geometry('500x500+450+100')
thread_sayisi=0
sutun_no=0
benzerlik=0
def veri_al():
    global thread_sayisi
    global sutun_no
    global benzerlik
    thread_sayisi=int(thread_giris.get())
    sutun_no=int(sutun_giris.get())
    benzerlik=int(benzerlik_giris.get())
    print("thread ",isinstance(thread_sayisi, int)," sutun ",isinstance(sutun_no, int)," benzerlik ",isinstance(benzerlik, int))
    pass

def senaryo_1_yap():
    senaryo1_deneme=tk.Toplevel()
    senaryo1_deneme.geometry('1095x810+250+100')
    print("thread ",thread_sayisi," sutun ",sutun_no," benzerlik ",benzerlik)

    columns=("Product 1", "Product 2","Benzerlik Orani")
    sonuc = ttk.Treeview(senaryo1_deneme,columns=columns, show="headings" )

    sonuc.heading('Product 1', text='Product 1')
    sonuc.column("Product 1" , width=120,minwidth=25)
    sonuc.heading('Product 2', text='Product 2')
    sonuc.column("Product 2" , width=120,minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani" , width=120,minwidth=25)    


    style=ttk.Style()
    style.theme_use("clam")
    
    style.configure("Treeview",
          background="silver",
          foreground="black",
          rowheight=25,
          fieldbackground="silver"          
    )
    sonuc.place(x=50,y=10,width=1000,height=500)

    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(senaryo1_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)

    thread_table.place(x=50,y=550,width=350,height=200)

def senaryo_2_yap():
    senaryo2_deneme=tk.Toplevel()
    senaryo2_deneme.geometry('1095x810+250+100')

    columns=("Product", "Issue 1","Issue 2","Benzerlik Orani","Company 1","Company 2")
    sonuc = ttk.Treeview(senaryo2_deneme,columns=columns, show="headings" )

    sonuc.heading('Product', text='Product')
    sonuc.column("Product" , width=120,minwidth=25)
    sonuc.heading('Issue 1', text='Issue 1')
    sonuc.column("Issue 1" , width=120,minwidth=25)
    sonuc.heading('Issue 2', text='Issue 2')
    sonuc.column("Issue 2" , width=120,minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani" , width=120,minwidth=25)
    sonuc.heading('Company 1', text='Company 1')
    sonuc.column("Company 1" , width=120,minwidth=25)
    sonuc.heading('Company 2', text='Company 2')
    sonuc.column("Company 2" , width=120,minwidth=25)    


    style=ttk.Style()
    style.theme_use("clam")
    
    style.configure("Treeview",
          background="silver",
          foreground="black",
          rowheight=25,
          fieldbackground="silver"          
    )
    sonuc.place(x=50,y=10,width=1000,height=500)

    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(senaryo2_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)

    thread_table.place(x=50,y=550,width=350,height=200)


def senaryo_3_yap():
    senaryo3_deneme=tk.Toplevel()
    senaryo3_deneme.geometry('1095x810+250+100')

    columns=("Product", "Issue", "Company", "State", "ZIP code","Complaint ID")
    sonuc = ttk.Treeview(senaryo3_deneme,columns=columns, show="headings" )

    sonuc.heading('Product', text='Product')
    sonuc.column("Product" , width=120,minwidth=25)
    sonuc.heading('Issue', text='Issue')
    sonuc.column("Issue" , width=120,minwidth=25)
    sonuc.heading('Company', text='Company')
    sonuc.column("Company" , width=120,minwidth=25)
    sonuc.heading('State', text='State')
    sonuc.column("State" , width=120,minwidth=25)
    sonuc.heading('ZIP code', text='ZIP code')
    sonuc.column("ZIP code" , width=120,minwidth=25)
    sonuc.heading('Complaint ID', text='Complaint ID')
    sonuc.column("Complaint ID" , width=120,minwidth=25)    


    style=ttk.Style()
    style.theme_use("clam")
    
    style.configure("Treeview",
          background="silver",
          foreground="black",
          rowheight=25,
          fieldbackground="silver"          
    )
    sonuc.place(x=50,y=10,width=1000,height=500)

    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(senaryo3_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)

    thread_table.place(x=50,y=550,width=350,height=200)

    pass
def senaryo_4_yap():
    senaryo4_deneme=tk.Toplevel()
    senaryo4_deneme.geometry('1095x810+250+100')

    columns=("Issue 1", "Issue 2","Benzerlik Orani")
    sonuc = ttk.Treeview(senaryo4_deneme,columns=columns, show="headings" )

    sonuc.heading('Issue 1', text='Issue 1')
    sonuc.column("Issue 1" , width=120,minwidth=25)
    sonuc.heading('Issue 2', text='Issue 2')
    sonuc.column("Issue 2" , width=120,minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani" , width=120,minwidth=25)    


    style=ttk.Style()
    style.theme_use("clam")
    
    style.configure("Treeview",
          background="silver",
          foreground="black",
          rowheight=25,
          fieldbackground="silver"          
    )
    sonuc.place(x=50,y=10,width=1000,height=500)

    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(senaryo4_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)

    thread_table.place(x=50,y=550,width=350,height=200)
def baslat_yap():
    baslat_deneme=tk.Toplevel()
    baslat_deneme.geometry('1095x810+250+100')

    columns=("Sutun 1", "Sutun 2","Benzerlik Orani")
    sonuc = ttk.Treeview(baslat_deneme,columns=columns, show="headings" )

    sonuc.heading('Sutun 1', text='Sutun 1')
    sonuc.column("Sutun 1" , width=120,minwidth=25)
    sonuc.heading('Sutun 2', text='Sutun 2')
    sonuc.column("Sutun 2" , width=120,minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani" , width=120,minwidth=25)    


    style=ttk.Style()
    style.theme_use("clam")
    
    style.configure("Treeview",
          background="silver",
          foreground="black",
          rowheight=25,
          fieldbackground="silver"          
    )
    sonuc.place(x=50,y=10,width=1000,height=500)

    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(baslat_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)

    thread_table.place(x=50,y=550,width=350,height=200)

senaryo1=tk.Button(window,text='Senaryo 1',command=senaryo_1_yap)
senaryo1.place(x=10,y=50,width=100,height=75)#relx=0.5,rely=0.5

senaryo2=tk.Button(window,text='Senaryo 2',command=senaryo_2_yap)
senaryo2.place(x=10,y=150,width=100,height=75)

senaryo3=tk.Button(window,text='Senaryo 3',command=senaryo_3_yap)
senaryo3.place(x=10,y=250,width=100,height=75)

senaryo4=tk.Button(window,text='Senaryo 4',command=senaryo_4_yap)
senaryo4.place(x=10,y=350,width=100,height=75)

baslat=tk.Button(window,text='Baslat',command=baslat_yap)
baslat.place(x=350,y=300,width=100,height=75)

veri_butonu=tk.Button(window,text='Verileri al',command=veri_al)
veri_butonu.place(x=375,y=100)

thread_giris=tk.Entry()
thread_giris.place(x=350,y=20)
sutun_giris=tk.Entry()
sutun_giris.place(x=350,y=50)
benzerlik_giris=tk.Entry()
benzerlik_giris.place(x=350,y=80)

etiket_thread=tk.Label(window,text = "Thread").place(x = 290,y = 20)
etiket_sutun=tk.Label(window,text = "Sutun").place(x = 290,y = 50) 
etiket_benzerlik=tk.Label(window,text = "Benzerlik").place(x = 290,y = 80) 



window.mainloop()
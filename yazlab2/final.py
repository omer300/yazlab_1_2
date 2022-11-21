import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import threading
import time

same_column = []
esit_sutun_same_column = []
data_final = []
data = pd.read_csv("data_son.csv", low_memory=False)
df = data.loc[:, ["Product", "Issue", "Company", "State", "ZIP code", "Complaint ID"]]
df = df.head(100)
v = np.float64(0).item()
yazdir = []
window = tk.Tk()
window.title('Yazlab 1 - 2')
window.geometry('500x500+450+100')
thread_sayisi = 0
sutun_no = []
benzerlik = 0


def veri_al():
    global thread_sayisi
    global sutun_no
    global benzerlik
    global yazdir
    global complaint
    global esit_sutun
    thread_sayisi = int(thread_giris.get())
    sutun_no = sutun_giris.get()
    esit_sutun = int(esit_sutun_giris.get())
    if (sutun_no == "0"):
        yazdir = "Product"
    elif (sutun_no == "1"):
        yazdir = "Issue"
    elif (sutun_no == "2"):
        yazdir = "Company"
    elif (sutun_no == "3"):
        yazdir = "State"
    elif (sutun_no == "4"):
        yazdir = "ZIP code"
    elif (sutun_no == "5"):
        yazdir = "Complaint ID"
    print(yazdir)
    benzerlik = int(benzerlik_giris.get())
    complaint = int(complaint_giris.get())
    # print("thread ",isinstance(thread_sayisi, int)," sutun ",isinstance(sutun_no, int)," benzerlik ",isinstance(benzerlik, int))


def senaryo_1_yap():
    senaryo1_deneme = tk.Toplevel()
    senaryo1_deneme.geometry('1095x810+250+100')
    print("thread ", thread_sayisi, " sutun ", sutun_no, " benzerlik ", benzerlik)

    columns = ("Product 1", "Product 2", "Benzerlik Orani")
    sonuc = ttk.Treeview(senaryo1_deneme, columns=columns, show="headings")

    sonuc.heading('Product 1', text='Product 1')
    sonuc.column("Product 1", width=120, minwidth=25)
    sonuc.heading('Product 2', text='Product 2')
    sonuc.column("Product 2", width=120, minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani", width=120, minwidth=25)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    columns2 = ("Thread No", "Calisma Suresi")
    thread_table = ttk.Treeview(senaryo1_deneme, columns=columns2, show="headings")

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No", width=120, minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi", width=120, minwidth=25)
    global same_column

    startTime = time.perf_counter()
    i = 0
    same_column += sutun_no
    threads = []

    def func(thread_no, thread_sayisi, same_column):
        print(thread_no, "girdi")
        count = 0
        c1 = ""
        c2 = ""
        startTime = time.perf_counter()
        for i in range(thread_sayisi - 1, len(df.loc[:]), thread_sayisi):
            print("section 1")
            for j in range(i + 1, len(df.loc[:])):
                print("section 2")
                value = df.loc[i]
                value2 = df.loc[j]
                for v in same_column:
                    c1 += str(value[int(v)])
                    c2 += str(value2[int(v)])
                lst = c1.lower().split()
                lst2 = c2.lower().split()
                len_1 = len(lst)
                len_2 = len(lst2)
                if (len_1 >= len_2):
                    for a in range(len_1):
                        if (lst[a] in lst2):
                            count += 1
                    if (count != 0):
                        similar = count / len_1 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(c1, c2,similar)
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                else:
                    for b in range(len_2):
                        if (lst2[b] in lst):
                            count += 1
                    if (count != 0):
                        similar = count / len_2 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                            # print(c1, c2,similar,"*********************************")
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                c1 = ""
                c2 = ""
                endTime = time.perf_counter()
                fark = (endTime - startTime) * 1000
                thread_table.insert("", "0", values=(thread_no, fark))

    for i in range(thread_sayisi):
        t = threading.Thread(target=func, args=(i, thread_sayisi, same_column))
        t.start()
        threads.append(t)
    # for t in threads:
    #    t.join()
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(1, "- ", f"{fark} ms'de tamamlandı.")



    sonuc.place(x=50, y=10, width=1000, height=500)
    thread_table.place(x=50, y=550, width=350, height=200)
    same_column = []


def senaryo_2_yap():
    senaryo2_deneme = tk.Toplevel()
    senaryo2_deneme.geometry('1095x810+250+100')

    columns = ("Product", "Issue 1", "Issue 2", "Benzerlik Orani", "Company 1", "Company 2")
    sonuc = ttk.Treeview(senaryo2_deneme, columns=columns, show="headings")

    sonuc.heading('Product', text='Product')
    sonuc.column("Product", width=120, minwidth=25)
    sonuc.heading('Issue 1', text='Issue 1')
    sonuc.column("Issue 1", width=120, minwidth=25)
    sonuc.heading('Issue 2', text='Issue 2')
    sonuc.column("Issue 2", width=120, minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani", width=120, minwidth=25)
    sonuc.heading('Company 1', text='Company 1')
    sonuc.column("Company 1", width=120, minwidth=25)
    sonuc.heading('Company 2', text='Company 2')
    sonuc.column("Company 2", width=120, minwidth=25)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    columns2 = ("Thread No", "Calisma Suresi")
    thread_table = ttk.Treeview(senaryo2_deneme, columns=columns2, show="headings")
    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No", width=120, minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi", width=120, minwidth=25)
    global same_column
    global esit_sutun_same_column

    startTime = time.perf_counter()
    i = 0
    same_column += sutun_no
    threads = []

    def func(thread_no, thread_sayisi, same_column):
        print(thread_no, "girdi")
        count = 0
        c1 = ""
        c2 = ""
        deger1 = ""
        deger2 = ""
        startTime = time.perf_counter()
        for i in range(thread_sayisi - 1, len(df.loc[:]), thread_sayisi):
            for j in range(i + 1, len(df.loc[:])):
                value = df.loc[i]
                value2 = df.loc[j]
                deger1 += str(value[int(esit_sutun)])
                deger2 += str(value2[int(esit_sutun)])
                if (deger1 == deger2):
                    for v in same_column:
                        c1 += str(value[int(v)])
                        c2 += str(value2[int(v)])
                    lst = c1.lower().split()
                    lst2 = c2.lower().split()
                    len_1 = len(lst)
                    len_2 = len(lst2)
                    if (len_1 >= len_2):
                        for a in range(len_1):
                            if (lst[a] in lst2):
                                count += 1
                        if (count != 0):
                            similar = count / len_1 * 100
                            if (similar >= benzerlik):
                                # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                                # print(c1, c2,similar)
                                sonuc.insert("", "end", values=(df.loc[i,"Product"],df.loc[i,"Issue"], df.loc[i,"Issue"], similar,df.loc[i,"Company"],df.loc[j,"Company"]))
                                print(df.loc[j])
                        count = 0
                    else:
                        for b in range(len_2):
                            if (lst2[b] in lst):
                                count += 1
                        if (count != 0):
                            similar = count / len_2 * 100
                            if (similar >= benzerlik):
                                # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                                # print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                                # print(c1, c2,similar,"*********************************")
                                sonuc.insert("", "end", values=(df.loc[i,"Product"],df.loc[i,"Issue"], df.loc[i,"Issue"], similar,df.loc[i,"Company"],df.loc[j,"Company"]))
                                print(df.loc[j])
                        count = 0
                    c1 = ""
                    c2 = ""
                    deger1 = ""
                    deger2 = ""
                    endTime = time.perf_counter()
                    fark = (endTime - startTime) * 1000
                    thread_table.insert("", "0", values=(thread_no, fark))

    for i in range(thread_sayisi):
        t = threading.Thread(target=func, args=(i, thread_sayisi, same_column))
        t.start()
        threads.append(t)
    # for t in threads:
    #    t.join()
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(1, "- ", f"{fark} ms'de tamamlandı.")

    sonuc.place(x=50, y=10, width=1000, height=500)
    thread_table.place(x=50, y=550, width=350, height=200)
    same_column = []


def senaryo_3_yap():
    senaryo3_deneme = tk.Toplevel()
    senaryo3_deneme.geometry('1095x810+250+100')

    columns = ("Product", "Issue", "Company", "State", "ZIP code", "Complaint ID", "Benzerlik")
    sonuc = ttk.Treeview(senaryo3_deneme, columns=columns, show="headings")

    sonuc.heading('Product', text='Product')
    sonuc.column("Product", width=120, minwidth=25)
    sonuc.heading('Issue', text='Issue')
    sonuc.column("Issue", width=120, minwidth=25)
    sonuc.heading('Company', text='Company')
    sonuc.column("Company", width=120, minwidth=25)
    sonuc.heading('State', text='State')
    sonuc.column("State", width=120, minwidth=25)
    sonuc.heading('ZIP code', text='ZIP code')
    sonuc.column("ZIP code", width=120, minwidth=25)
    sonuc.heading('Complaint ID', text='Complaint ID')
    sonuc.column("Complaint ID", width=120, minwidth=25)
    sonuc.heading('Benzerlik', text='Benzerlik')
    sonuc.column("Benzerlik", width=120, minwidth=25)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    columns2 = ("Thread No", "Calisma Suresi")
    thread_table = ttk.Treeview(senaryo3_deneme, columns=columns2, show="headings")

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No", width=120, minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi", width=120, minwidth=25)
    global same_column
    global complaint

    startTime = time.perf_counter()
    i = 0
    same_column += sutun_no
    threads = []

    def func(thread_no, thread_sayisi, same_column):
        print(thread_no, "girdi")
        count = 0
        c1 = ""
        c2 = ""
        startTime = time.perf_counter()
        for i in range(0,len(df.loc[:]),1):
            print(df.loc[i, "Complaint ID"], complaint)
            if(df.loc[i,"Complaint ID"] == complaint):

                esit = i
                print(esit)
        for i in range(thread_sayisi - 1, len(df.loc[:]), thread_sayisi):
                value = df.loc[esit]
                value2 = df.loc[i]
                for v in same_column:
                    c1 += str(value[int(v)])
                    c2 += str(value2[int(v)])
                lst = c1.lower().split()
                lst2 = c2.lower().split()
                len_1 = len(lst)
                len_2 = len(lst2)
                if (len_1 >= len_2):
                    for a in range(len_1):
                        if (lst[a] in lst2):
                            count += 1
                    if (count != 0):
                        similar = count / len_1 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(c1, c2,similar)
                            sonuc.insert("", "end", values=(df.loc[i,"Product"],df.loc[i,"Issue"],df.loc[i,"Company"],df.loc[i,"State"],df.loc[i,"ZIP code"],df.loc[i,"Complaint ID"],similar))
                            print(df.loc[i])
                    count = 0
                else:
                    for b in range(len_2):
                        if (lst2[b] in lst):
                            count += 1
                    if (count != 0):
                        similar = count / len_2 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                            # print(c1, c2,similar,"*********************************")
                            sonuc.insert("", "end", values=(df.loc[i,"Product"],df.loc[i,"Issue"],df.loc[i,"Company"],df.loc[i,"State"],df.loc[i,"ZIP code"],df.loc[i,"Complaint ID"],similar))
                            print(df.loc[i])
                    count = 0
                c1 = ""
                c2 = ""
                endTime = time.perf_counter()
                fark = (endTime - startTime) * 1000
                thread_table.insert("", "0", values=(thread_no, fark))


    for i in range(thread_sayisi):
        t = threading.Thread(target=func, args=(i, thread_sayisi, same_column))
        t.start()
        threads.append(t)
    # for t in threads:
    #    t.join()
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(1, "- ", f"{fark} ms'de tamamlandı.")


    sonuc.place(x=50, y=10, width=1000, height=500)
    thread_table.place(x=50, y=550, width=350, height=200)
    same_column = []




def senaryo_4_yap():
    senaryo4_deneme = tk.Toplevel()
    senaryo4_deneme.geometry('1095x810+250+100')

    columns = ("Issue 1", "Issue 2", "Benzerlik Orani")
    sonuc = ttk.Treeview(senaryo4_deneme, columns=columns, show="headings")

    sonuc.heading('Issue 1', text='Issue 1')
    sonuc.column("Issue 1", width=120, minwidth=25)
    sonuc.heading('Issue 2', text='Issue 2')
    sonuc.column("Issue 2", width=120, minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani", width=120, minwidth=25)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    columns2 = ("Thread No", "Calisma Suresi")
    thread_table = ttk.Treeview(senaryo4_deneme, columns=columns2, show="headings")

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No", width=120, minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi", width=120, minwidth=25)

    global same_column

    startTime = time.perf_counter()
    i = 0
    same_column += sutun_no
    threads = []

    def func(thread_no, thread_sayisi, same_column):
        print(thread_no, "girdi")
        count = 0
        c1 = ""
        c2 = ""
        startTime = time.perf_counter()
        for i in range(thread_sayisi - 1, len(df.loc[:]), thread_sayisi):
            print("section 1")
            for j in range(i + 1, len(df.loc[:])):
                print("section 2")
                value = df.loc[i]
                value2 = df.loc[j]
                for v in same_column:
                    c1 += str(value[int(v)])
                    c2 += str(value2[int(v)])
                lst = c1.lower().split()
                lst2 = c2.lower().split()
                len_1 = len(lst)
                len_2 = len(lst2)
                if (len_1 >= len_2):
                    for a in range(len_1):
                        if (lst[a] in lst2):
                            count += 1
                    if (count != 0):
                        similar = count / len_1 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(c1, c2,similar)
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                else:
                    for b in range(len_2):
                        if (lst2[b] in lst):
                            count += 1
                    if (count != 0):
                        similar = count / len_2 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                            # print(c1, c2,similar,"*********************************")
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                c1 = ""
                c2 = ""
                endTime = time.perf_counter()
                fark = (endTime - startTime) * 1000
                thread_table.insert("", "0", values=(thread_no, fark))

    for i in range(thread_sayisi):
        t = threading.Thread(target=func, args=(i, thread_sayisi, same_column))
        t.start()
        threads.append(t)
    # for t in threads:
    #    t.join()
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(1, "- ", f"{fark} ms'de tamamlandı.")

    sonuc.place(x=50, y=10, width=1000, height=500)
    thread_table.place(x=50, y=550, width=350, height=200)
    same_column = []


def baslat_yap():
    baslat_deneme = tk.Toplevel()
    baslat_deneme.geometry('1095x810+250+100')

    columns = ("Sutun 1", "Sutun 2", "Benzerlik Orani")
    sonuc = ttk.Treeview(baslat_deneme, columns=columns, show="headings")

    sonuc.heading('Sutun 1', text='Sutun 1')
    sonuc.column("Sutun 1", width=120, minwidth=25)
    sonuc.heading('Sutun 2', text='Sutun 2')
    sonuc.column("Sutun 2", width=120, minwidth=25)
    sonuc.heading('Benzerlik Orani', text='Benzerlik Orani')
    sonuc.column("Benzerlik Orani", width=120, minwidth=25)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    columns2 = ("Thread No", "Calisma Suresi")
    thread_table = ttk.Treeview(baslat_deneme, columns=columns2, show="headings")
    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No", width=120, minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi", width=120, minwidth=25)


    global same_column

    startTime = time.perf_counter()
    i = 0
    same_column += sutun_no
    threads = []
    def func(thread_no,thread_sayisi,same_column):
        print(thread_no,"girdi")
        count = 0
        c1 = ""
        c2 = ""
        startTime = time.perf_counter()
        for i in range(thread_sayisi-1,len(df.loc[:]),thread_sayisi):
            print("section 1")
            for j in range(i + 1, len(df.loc[:])):
                print("section 2")
                value = df.loc[i]
                value2 = df.loc[j]
                for v in same_column:
                    c1 += str(value[int(v)])
                    c2 += str(value2[int(v)])
                lst = c1.lower().split()
                lst2 = c2.lower().split()
                len_1 = len(lst)
                len_2 = len(lst2)
                if (len_1 >= len_2):
                    for a in range(len_1):
                        if (lst[a] in lst2):
                            count += 1
                    if (count != 0):
                        similar = count / len_1 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(c1, c2,similar)
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                else:
                    for b in range(len_2):
                        if (lst2[b] in lst):
                            count += 1
                    if (count != 0):
                        similar = count / len_2 * 100
                        if (similar >= benzerlik):
                            # data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                            # print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                            # print(c1, c2,similar,"*********************************")
                            sonuc.insert("", "end", values=(c1, c2, similar))
                            print(df.loc[j])
                    count = 0
                c1 = ""
                c2 = ""
                endTime = time.perf_counter()
                fark = (endTime - startTime) * 1000
                thread_table.insert("","0",values=(thread_no,fark))
    for i in range(thread_sayisi):
        t = threading.Thread(target=func, args=(i, thread_sayisi, same_column))
        t.start()
        threads.append(t)
    #for t in threads:
    #    t.join()
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(1, "- ", f"{fark} ms'de tamamlandı.")

    sonuc.place(x=50, y=10, width=1000, height=500)
    thread_table.place(x=50, y=550, width=350, height=200)
    same_column = []


senaryo1 = tk.Button(window, text='Senaryo 1', command=senaryo_1_yap)
senaryo1.place(x=10, y=50, width=100, height=75)  # relx=0.5,rely=0.5

senaryo2 = tk.Button(window, text='Senaryo 2', command=senaryo_2_yap)
senaryo2.place(x=10, y=150, width=100, height=75)

senaryo3 = tk.Button(window, text='Senaryo 3', command=senaryo_3_yap)
senaryo3.place(x=10, y=250, width=100, height=75)

senaryo4 = tk.Button(window, text='Senaryo 4', command=senaryo_4_yap)
senaryo4.place(x=10, y=350, width=100, height=75)

baslat = tk.Button(window, text='Baslat', command=baslat_yap)
baslat.place(x=350, y=300, width=100, height=75)

veri_butonu = tk.Button(window, text='Verileri al', command=veri_al)
veri_butonu.place(x=375, y=100)

thread_giris = tk.Entry()
thread_giris.place(x=350, y=20)
sutun_giris = tk.Entry()
sutun_giris.place(x=350, y=50)
benzerlik_giris = tk.Entry()
benzerlik_giris.place(x=350, y=80)
complaint_giris = tk.Entry()
complaint_giris.place(x=350, y=150)
esit_sutun_giris = tk.Entry()
esit_sutun_giris.place(x=350, y=180)


etiket_thread = tk.Label(window, text="Thread").place(x=290, y=20)
etiket_sutun = tk.Label(window, text="Sutun").place(x=290, y=50)
etiket_benzerlik = tk.Label(window, text="Benzerlik").place(x=290, y=80)
esit_sutun_benzerlik = tk.Label(window, text="Eşit sütun").place(x=290, y=180)
complaint_benzerlik = tk.Label(window, text="Complaint ID").place(x=270, y=150)

window.mainloop()

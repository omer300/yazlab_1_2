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
    
    columns2=("Thread No","Calisma Suresi")
    thread_table = ttk.Treeview(baslat_deneme,columns=columns2, show="headings" )

    thread_table.heading('Thread No', text='Thread No')
    thread_table.column("Thread No" , width=120,minwidth=25)
    thread_table.heading('Calisma Suresi', text='Calisma Suresi')
    thread_table.column("Calisma Suresi" , width=120,minwidth=25)
    
    global content
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  
    liste2_str = ""
    i=0
    content += sutun_no
    for i in range(len(df.loc[:])): 
        for j in range(i + 1, len(df.loc[:])):  
            value = df.loc[i]  
            value2 = df.loc[j] 
            for v in content:  
                liste_str += str(value[int(v)])
                liste2_str += str(value2[int(v)])
            liste = liste_str.lower().split()  
            liste2 = liste2_str.lower().split()
            len_1 = len(liste)
            len_2 = len(liste2)
            if (len_1 >= len_2):
                for a in range(len_1):
                    if (liste[a] in liste2):
                        count += 1
                if (count != 0):
                    similar = count / len_1 * 100
                    if(similar >= benzerlik):
                        #data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                        #print(liste_str, liste2_str,similar)
                        sonuc.insert("","end",values=(liste_str, liste2_str,similar))
                        # print(df.loc[i, 'Company'])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    if(similar >= benzerlik):
                        #data_final.append([similar, df.loc[i,"Product"],df.loc[j,"Product"]])
                        #print(similar,df.loc[i,"Product"],df.loc[j,"Product"])
                        #print(liste_str, liste2_str,similar,"*********************************")
                        sonuc.insert("","end",values=(liste_str, liste2_str,similar))
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000

    sonuc.place(x=50,y=10,width=1000,height=500)


    thread_table.place(x=50,y=550,width=350,height=200)
    content=[]

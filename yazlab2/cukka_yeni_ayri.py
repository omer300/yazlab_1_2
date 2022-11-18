import pandas as pd
import numpy as np

# longsent=0
count = 0
liste = ""  # istenilen sütundaki cümlelerin liste hali
liste2 = ""
liste_str = ""  # cümlelerin string hali tutulur
liste2_str = ""
content = []  # seçilecek sütun sayısı tutulur

data = pd.read_csv("data_son.csv", low_memory=False)
df = data.loc[:, ["Product", "Issue", "Company", "State", "ZIP code","Complaint ID"]] 
df = df.head(5)
v = np.float64(0).item()
i = 0
sayi = input("seçilecek satır sayısı: ")
sayi = int(sayi)  # sütunların belirlenmesi
while (sayi):
    sutun = input("sütun no: ")
    content += sutun
    sayi -= 1
for i in range(len(df.loc[:])):  # dosya başından
    for j in range(i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
        value = df.loc[i]  # ana satır
        value2 = df.loc[j]  # karşılaştırılacak satır
        for v in content:  # istenilen sütunların bilgisi alınır
            liste_str += str(value[int(v)])
            liste2_str += str(value2[int(v)])
        liste = liste_str.lower().split()  # küçük harf üzerinden karşılaştırma
        liste2 = liste2_str.lower().split()
        len_1 = len(liste)
        len_2 = len(liste2)
        if (len_1 >= len_2):
            for a in range(len_1):
                if (liste[a] in liste2):
                    count += 1
            if (count != 0):
                similar = count / len_1 * 100
                print(liste_str, liste2_str, "-->", similar)
                print(df.loc[i,'Company'])
            count = 0
        else:
            for b in range(len_2):
                if (liste2[b] in liste):
                    count += 1
            if (count != 0):
                similar = count / len_2 * 100
                print(liste_str, liste2_str, "-->", similar)
                print(df.loc[i,'Company'])
            count = 0
        liste = ""
        liste2 = ""
        liste_str = ""
        liste2_str = ""

        
#senaryo 1

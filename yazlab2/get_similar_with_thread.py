import threading

import pandas as pd
import numpy as np
import time

# longsent=0
content = []  # seçilecek sütun sayısı tutulur
data_final = []  # son tablo verisi
data = pd.read_csv("data_son.csv", low_memory=False)
df = data.loc[:, ["Product", "Issue", "Company", "State", "ZIP code", "Complaint ID"]]
df = df.head(500)
v = np.float64(0).item()

def compare(startValue, threadNumber,content):
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  # cümlelerin string hali tutulur
    liste2_str = ""
    i=0
    for i in range(startValue,len(df.loc[:]),threadNumber):  # dosya başından
        for j in range(startValue + i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
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
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar, df.loc[i]])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar,df.loc[i]])# belki j olur
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(startValue,"- ", f"{fark} ms'de tamamlandı.")


def senario1(startValue, threadNumber,content):
    similarity = input("lütfen taban benzerlik oranını giriniz :")
    similarity = int(similarity)
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  # cümlelerin string hali tutulur
    liste2_str = ""
    i=0
    for i in range(startValue,len(df.loc[:]),threadNumber):  # dosya başından
        for j in range(startValue + i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
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
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    if(similar>=similarity):
                        data_final.append([similar, df.loc[i]])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    if (similar >= similarity):
                        data_final.append([similar, df.loc[i]])# belki j olur
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(startValue,"- ", f"{fark} ms'de tamamlandı.")

def senario2(startValue, threadNumber,content):
    similarity = input("lütfen taban benzerlik oranını giriniz :")
    similarity = int(similarity)
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  # cümlelerin string hali tutulur
    liste2_str = ""
    i=0
    for i in range(startValue,len(df.loc[:]),threadNumber):  # dosya başından
        for j in range(startValue + i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
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
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar, df.loc[i]])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar,df.loc[i]])# belki j olur
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(startValue,"- ", f"{fark} ms'de tamamlandı.")

def senario3(startValue, threadNumber,content):
    complaint = input("lütfen complaint idini giriniz :")
    complaint = int(complaint)
    similarity = input("lütfen taban benzerlik oranını giriniz :")
    similarity = int(similarity)
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  # cümlelerin string hali tutulur
    liste2_str = ""
    i=0
    for i in range(startValue,len(df.loc[:]),threadNumber):  # dosya başından
        for j in range(startValue + i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
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
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    if(similar>=similarity):
                        data_final.append([similar, df.loc[i]])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    if (similar >= similarity):
                        data_final.append([similar, df.loc[i]])
                    # belki j olur
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(startValue,"- ", f"{fark} ms'de tamamlandı.")

def senario4(startValue, threadNumber,content):
    similarity = input("lütfen taban benzerlik oranını giriniz :")
    similarity = int(similarity)
    sutun = input("lütfen sutun no giriniz :")
    sutun = int(sutun)
    startTime = time.perf_counter()
    count = 0
    liste_str = ""  # cümlelerin string hali tutulur
    liste2_str = ""
    i=0
    for i in range(startValue,len(df.loc[:]),threadNumber):  # dosya başından
        for j in range(startValue + i + 1, len(df.loc[:])):  # sonraki elemandna itibaren sona
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
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar, df.loc[i]])
                count = 0
            else:
                for b in range(len_2):
                    if (liste2[b] in liste):
                        count += 1
                if (count != 0):
                    similar = count / len_2 * 100
                    # print(liste_str, liste2_str, "-->", similar)
                    # print(df.loc[i, 'Company'])
                    data_final.append([similar,df.loc[i]])# belki j olur
                count = 0
            liste_str = ""
            liste2_str = ""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print(startValue,"- ", f"{fark} ms'de tamamlandı.")

sayi = input("seçilecek satır sayısı: ")
sayi = int(sayi)  # sütunların belirlenmesi
while (sayi):
    sutun = input("sütun no: ")
    content += sutun
    sayi -= 1
thread = input("Thread sayısı giriniz: ")
thread = int(thread)
threads = []
startTime = time.perf_counter()
for i in range (1,thread+1):
    t = threading.Thread(target=compare,args=(i,thread,content))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
endTime = time.perf_counter()
fark = (endTime - startTime) * 1000
print("->",f"{fark} ms'de tamamlandı.")

print(data_final,len(data_final))

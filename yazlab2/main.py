import threading
import time
import csv

with open('data_son.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

length = len(data)
def read(startValue,threadNumber):
    startTime = time.perf_counter()
    counter = startValue
    for counter in range (startValue,length,threadNumber):
       """ print(startValue
              , "|", counter, data[counter])"""
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print( startValue," ",f"{fark} ms'de tamamlandı.")

def compare(startValue,threadNumber):
    startTime = time.perf_counter()
    firstValue = data[startValue][1]
    countSame = 0;
    for counter in range (startValue,length,threadNumber):
        if firstValue == data[counter][1]:
            countSame += 1
    endTime = time.perf_counter()
    fark = (endTime - startTime) * 1000
    print( startValue," -",firstValue,countSame,"- ",f"{fark} ms'de tamamlandı.")


numberOfThread = 100
startTime = time.perf_counter()
for i in range (1,numberOfThread+1):
    threading.Thread(target=compare,args=(i,numberOfThread)).start()
endTime = time.perf_counter()
fark = (endTime - startTime) * 1000
print("->",f"{fark} ms'de tamamlandı.")
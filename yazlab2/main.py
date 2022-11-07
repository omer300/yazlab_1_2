import csv
import nltk
from nltk.corpus import stopwords
import string

with open('bla.txt','r') as f:
    moby_raw = f.read()
    stop = set(stopwords.words('english'))
    moby_tokens = nltk.word_tokenize(moby_raw)
    text_no_stop_words_punct = [t for t in moby_tokens if t not in stop and t not in string.punctuation]

    print(text_no_stop_words_punct)




#CSV KISMI VERİ ALIYORUZ
rows = []
with open("rows.csv", 'r',encoding="utf8") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
#print(header)
#print(rows)



file.close()

import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
## stopword ve noktalama işretleri kaldırma testi 
example_sent = """This is a sample sentence,
                  showing off the stop words filtration."""
  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(example_sent)
tokenizer = RegexpTokenizer(r'\w+')
  
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

filtered_sentence=tokenizer.tokenize(filtered_sentence)  #filtered_sentence list tokenize object istediğinden noktalama işaretleri atılamıyor
print(word_tokens)
print(filtered_sentence)





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
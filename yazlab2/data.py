import pandas as pd
import re
from nltk.corpus import stopwords

csv_frame = pd.read_csv("test_fil.csv")

csv_frame["Complaint ID"] = csv_frame["Complaint ID"].astype(str)

csv_frame=csv_frame.dropna(how='any')

stop_words=stopwords.words("english")

for i in csv_frame.columns.tolist():
    csv_frame[i] = csv_frame[i].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))


for i in csv_frame.columns.tolist():
    csv_frame[i] = [re.sub('[^\w\s]+', '', s) for s in csv_frame[i].tolist()]

print(csv_frame)

csv_frame.to_csv('data_final.csv',index=False) 

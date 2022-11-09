import pandas as pd
from nltk.corpus import stopwords
import re

stopwords = stopwords.words('english')
columns = ['Product', 'Issue', 'Company', 'State', 'ZIP code', 'Complaint ID']
f = pd.read_csv("rows.csv", usecols=columns, dtype={'Product': 'string',
                                                    'Issue': 'string',
                                                    'Company': 'string',
                                                    'State': 'string',
                                                    'ZIP code': 'string',
                                                    'Complaint ID': 'int64',
                                                    })

dataset = f.to_string()
print(dataset)

for word in stopwords:
    print(word)
    dataset = dataset.replace(" "+word+" ", " ")


dataset = re.sub(r"[,.;@#?!&$/]+", ' ', dataset)
# dataset = re.sub(r"\s+", ' ', dataset)

print(dataset)
f = open("data.txt", "a")
f.write(dataset)
f.close()
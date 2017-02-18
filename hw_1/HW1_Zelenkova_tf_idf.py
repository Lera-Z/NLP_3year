import os
from pymystem3.mystem import Mystem
import copy
import pandas as pd
from math import log10

with open('HW1_Zelenkova_KeyWords.txt', 'r', encoding='UTF-8') as f:
    words = [word.rstrip() for word in f.readlines()]


m = Mystem()
df_hash = dict(zip(words, [0]*len(words))) # слово и док частота
tf_hash = dict(zip(words, [dict() for _ in range(len(words))]))
N = 0
def read_txt(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            open_name = os.path.join(root, filename)
            with open(open_name, 'r', encoding='utf-8') as f:
                text = f.read()
                yield text, open_name

for text, open_name in read_txt(path='10_texts'):
    N+=1
    lemmata = m.lemmatize(text)
    for word in words:
        # for df
        if word in lemmata:
            df_hash[word] += 1

        # for tf
        tf = lemmata.count(word) / len(lemmata)
        tf_hash[word][open_name] = tf


tf_idf_hash = copy.deepcopy(tf_hash)
for word in tf_idf_hash:
    for text in tf_idf_hash[word]:
        idf = log10(N/df_hash[word])
        tf_idf_hash[word][text] = tf_idf_hash[word][text]*idf

# print(tf_idf_hash)
docum = pd.DataFrame.from_dict(tf_idf_hash).transpose()
tf_idf_final = pd.DataFrame.to_csv(docum)
with open('table_tfidf.csv', 'w', encoding='UTF-8') as w:
    w.write(tf_idf_final)



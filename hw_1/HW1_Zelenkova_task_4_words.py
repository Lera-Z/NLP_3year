import os
from pymystem3.mystem import Mystem
import copy
import pandas as pd
from math import log10



def read_txt(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            open_name = os.path.join(root, filename)
            with open(open_name, 'r', encoding='utf-8') as f:
                text = f.read()
                yield text, open_name

with open('HW1_Zelenkova_4_words.txt', 'r', encoding='UTF-8') as f:
    words = [word.rstrip() for word in f.readlines()]


words_hash = dict(zip(words, [dict() for _ in range(len(words))]))
words_full_hash = dict(zip(words, [0]*len(words)))
m = Mystem()
for text, open_name in read_txt(path='10_texts'):
    lemmata = m.lemmatize(text)
    for word in words:
        k = lemmata.count(word)
        words_hash[word][open_name] = k
        words_full_hash[word] += k

for word in words_hash:
    for text in words_hash[word]:
        words_hash[word][text] = words_hash[word][text]/words_full_hash[word]




docum = pd.DataFrame.from_dict(words_hash)
words_fin = pd.DataFrame.to_csv(docum)
with open('table_3.csv', 'w', encoding='UTF-8') as w:
    w.write(words_fin)



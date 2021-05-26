import nltk
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f=open("target_words.txt","r")
s=f.read()
f.close()

target_adverbs = nltk.word_tokenize(s)
# print(target_adverbs)

filepath = sys.argv[1]

f=open(filepath,"r")
s=f.read()
f.close()

#分词
text=nltk.word_tokenize(s)

#标记并提取出副词
tags=nltk.pos_tag(text)
adverbs = [key for key,value in tags if value == "RB"]
freq = nltk.FreqDist(adverbs)
df_freq = pd.DataFrame(freq.items(), columns = ["Word","Frequency"])
df_freq = df_freq.sort_values(by="Frequency",ascending=False)
df_freq.to_csv("frequencies_adverbs.csv",index=0)

#目标词
target = [word for word in text if word in target_adverbs]
# print(target)
if len(target):
    freq = nltk.FreqDist(target)
    # print(len(target))
    df_freq = pd.DataFrame(freq.items(), columns = ["Word","Frequency"])
    df_freq = df_freq.sort_values(by="Frequency",ascending=False)
    df_freq.to_csv("frequencies_target.csv",index=0)
    # print(df_freq)

# plt.ion()
# freq = nltk.FreqDist(target)
# # freq_dict = {}
# # for item in freq:
# #     freq_dict[item] = freq[item]
# # print(freq_dict)
# freq.tabulate(100)
# plt.savefig('test.png')
# plt.ioff()
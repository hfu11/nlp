import nltk
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import sys

probability_adverbs = ["probably","possibly","perhaps","maybe","likely","certainly","surely",]

filepath = sys.argv[1]

f=open(filepath,"r")
s=f.read()
f.close()
# print(s)

#分词
text=nltk.word_tokenize(s)

#标记并提取出副词
tags=nltk.pos_tag(text)
adverbs = [key for key,value in tags if value == "RB"]
adverbs2 = [word for word in adverbs if word in probability_adverbs]
print(adverbs2)

# 去重
# adverbs=list(set(adverbs))
# print(adverbs)

plt.ion()
freq = nltk.FreqDist(adverbs)
# freq_dict = {}
# for item in freq:
#     freq_dict[item] = freq[item]
# print(freq_dict)
freq.plot(100)
plt.savefig('test.png')
plt.ioff()
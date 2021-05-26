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
# print(filepath)

f=open(filepath,"r")
s=f.read()
f.close()

#分词
text=nltk.word_tokenize(s)
# print(text)

#标记并提取出副词
tags=nltk.pos_tag(text)
adverbs = [key for key,value in tags if value == "RB"]

#目标词
target = [word for word in text if word in target_adverbs]

with open("analysis.md","w") as f:
    print("ok")
    for word in text:
        if word in target:
            str = " ** " + word + " **"
            f.write(str)
        elif word in adverbs:
            str = " *** " + word + " ***"
            f.write(str)
        elif word.isnumeric() or word.isalpha() or word == "(":
            str = " " + word
            f.write(str)
        else:
            f.write(word)

    f.close()
    



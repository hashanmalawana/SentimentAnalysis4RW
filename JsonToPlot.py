# Ok for Research works
import json
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer
from wordcloud import WordCloud

with open('D:/Research/ResearchModelNew/RWPreprocessing/PreProcess_CSE_Media2015.json') as f:
    data = json.load(f)
# print(data)

# Before Cleaned or pre-process
df = pd.read_json('D:/Research/ResearchModelNew/RWGetTweets/CSE_Media2015.json')
kaf = df['content']
# print(kaf)

Tweet = df["content"]
df['pre_clean_len'] = [len(t) for t in Tweet]
fig, ax = plt.subplots(figsize=(5, 5))
plt.boxplot(df.pre_clean_len)
plt.title("Tweets Before Pre-process")
plt.show()
# plt.savefig('Tweets Before Pre-process.jpeg')
# print(df.head())

# After the Pre-Process
df = pd.read_json('D:/Research/ResearchModelNew/RWPreprocessing/PreProcess_CSE_Media2015.json')
cleanedT = df['content']
# print(cleanedT)
df['pre_clean_len'] = [len(t) for t in cleanedT]
fig, ax = plt.subplots(figsize=(5, 5))
plt.boxplot(df.pre_clean_len)
plt.title("Tweets After Pre-process")
plt.show()
# plt.savefig('Tweets After Pre-process.jpeg')
# print(df.head())

# WordCloud before Pre-processing
wrd_string = []
for t in Tweet:
    wrd_string.append(t)
wrd_string = pd.Series(wrd_string).str.cat(sep=' ')

wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(wrd_string)
plt.figure(figsize=(12, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.title("WordCloud Before Pre-processing")
plt.axis("off")
plt.show()
# plt.savefig('WordCloud Before Pre-processing.jpeg')

# WordCloud before After-processing
wrd_string = []
for c in cleanedT:
    wrd_string.append(c)
wrd_string = pd.Series(wrd_string).str.cat(sep=' ')

wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(wrd_string)
plt.figure(figsize=(12, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.title("WordCloud After Pre-processing")
plt.axis("off")
plt.show()
# plt.savefig('WordCloud After Pre-processing.jpeg')

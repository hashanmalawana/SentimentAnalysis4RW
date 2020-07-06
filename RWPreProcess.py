import pandas as pd
import numpy as np
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import datetime
import json

tweets = pd.read_json('D:/Research/ResearchModelNew/RWGetTweets/CSE_Media2015.json', encoding='utf-8')
dataVal = {}
dataVal['Data'] = {}


def form_sentence(tweet):
    tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
    tweet = re.sub(r'http', '', tweet)
    tweet = re.sub(r'www', '', tweet)
    tweet = re.sub(r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", '', tweet)
    tweet = re.sub(r'<[^>]+>', '', tweet)
    tweet = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', tweet)
    tweet_blob = TextBlob(tweet)
    return ' '.join(tweet_blob.words)


def no_user_alpha(tweet):
    tweet_list = [ele for ele in tweet.split() if ele != 'user']
    clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
    clean_s = ' '.join(clean_tokens)
    clean_mess = [word for word in clean_s.split() if word.lower() not in stopwords.words('english')]
    return clean_mess


def normalization(tweet_list):
    lem = WordNetLemmatizer()
    normalized_tweet = []
    for word in tweet_list:
        normalized_text = lem.lemmatize(word, 'v')
        normalized_tweet.append(normalized_text)
    return normalized_tweet


Final_words = []
for data in tweets['content']:
    filtered = normalization(no_user_alpha(form_sentence(data)))
    word_Final = ' '.join(filtered)
    Final_words.append(word_Final)

f = open("D:/Research/ResearchModelNew/RWPreprocessing/PreProcess_CSE_Media2015.json", "w")
f.write('[')
i = 0
while i < len(tweets):
    dt = datetime.datetime.strptime(str(tweets['date'][i]), "%Y-%m-%d %H:%M:%S")
    new_date = "%Y-%m-%d"
    dataVal['Data'].update({
        'date': dt.strftime(new_date),
        'content': Final_words[i]
    })
    jsonVal = json.dumps(dataVal['Data'])
    f.write(jsonVal + ',')
    f.write('\n')
    print(jsonVal)
    i += 1

f.write(']')
f.close()

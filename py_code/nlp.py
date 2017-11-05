# coding: utf-8

# In[ ]:

import re
from nltk.corpus import stopwords


# In[16]:

import json


# In[26]:

import requests
import pandas as pd

url = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=b99UVkWzYTQ&key=AIzaSyCVBriWh5AKNqip3V1PqaRdnKKxs0RIuqI'
response = requests.get(url)
dict = response.json()
z=pd.d


# In[27]:

type(dict)


# In[32]:

from nltk.corpus import stopwords


# In[42]:

l=['This first video is the Series Intro. If you wanna know how the series is set up, start here. Else start with episode 2.', 'Awesome. Next Probability and Stats and I am all set for deep learning... :D', 'Thans for sharing. This talk is full of insights and best practices. But its word is very simple and concise.', 'Skynet or Ultron. Which one should I make first, hmm?', "I'm all for unsupervised learning. It a good thing that computers will be able to do this in the future because the bulk of the world's population doesn't do a very good job of unsupervised learning.  They still rely on leaders and other institutions to instruct them on what to say, do and think.", 'This gent is a good lecturer -- explained intuitively, covering the important aspects well.  Keep it up.', 'So far, I think this is the best intuitive intro to backprop I\'ve seen. This channel means a lot to me. Because of its teaching style, I managed to get back to learning and grok maths while I was studying machine learning last year, 13 years since doing my undergrad in CS. It\'s almost the end of 2017 and I still keep hearing from the people I talked to that they fear/hate maths because they think it\'s a tough subject to tame. May be this example tell us why our education system (internationally) is still broken? As an aside, David Perkins, in his book "Making Learning Whole" also touch about this widespread diseases of the educational system, namely "elementitis". I think we can do better. Grant is doing great work to lower the barrier and making math more accessible to everyone. This is not an easy feat. I think we need some sort of concerted effort for encouraging more people to teaching maths or any subject through intuition. Visualization is one way to improve the teaching methodology. We can also distill intuition from stories, feelings, situations, etc. More examples, see:\nhttps://distill.pub/\nhttp://colah.github.io/', "how DP is a Hinton's invention if he is not present in DP wikipedia article?", "The time on the slides doesn't forward :disappointed: Have to pause to update them."]


# In[51]:

l = l.lower()        # Convert to lower case
words = l.split()


# In[52]:

from nltk.corpus import stopwords


# In[53]:

from sklearn.feature_extraction.text import CountVectorizer


# In[69]:

letters_only = re.sub("[^a-zA-Z]", " ",l)

stops = set(stopwords.words("english"))

meaningful_words = [w for w in words if not w in stops]

print( meaningful_words )


# In[81]:

import nltk
nltk.download('all')


# In[79]:

nltk.download('maxent_treebank_pos_tagger')


# In[91]:

sentence=a


# In[97]:

sentence= ''.join(a)


# In[99]:

from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank

tokenizer = treebank.TreebankWordTokenizer()
pos_words = 0
neg_words = 0
tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

x = list(range(len(tokenized_sent))) # x axis for the plot
y = []

for word in tokenized_sent:
    if word in opinion_lexicon.positive():
        pos_words += 1
        y.append(1) # positive
    elif word in opinion_lexicon.negative():
        neg_words += 1
        y.append(-1) # negative
    else:
        y.append(0) # neutral

if pos_words > neg_words:
    print('Positive')
elif pos_words < neg_words:
    print('Negative')
elif pos_words == neg_words:
    print('Neutral')


# In[ ]:

import re, json, os, requests, string, sys
import nltk
nltk.download('all')
nltk.download('maxent_treebank_pos_tagger')
import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from sklearn.feature_extraction.text import CountVectorizer


YOUTUBE_COMMENT_BASE_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

filename = "/home/aniruddha/Downloads/output.txt"
youtube_urls = []
vid_id = []
final_urls = []

s1_comments = []
s2_comments = []
s3_comments = []
s4_comments = []

with open(filename) as f:
    for line in f:
        youtube_urls.append([n for n in line.strip().split(',')])

try:
    os.remove(filename)
except OSError:
    pass

max_urls = len(youtube_urls[0])
youtube_urls[0].pop()

for i in range(max_urls-1):
	temp = youtube_urls[0][i].split('=',1)
	vid_id.append(temp[1])

for i in range(max_urls-1):
	temp = YOUTUBE_COMMENT_BASE_URL + '?part=snippet' + '&videoId=' + vid_id[i] + '&key=AIzaSyCVBriWh5AKNqip3V1PqaRdnKKxs0RIuqI'
	final_urls.append(temp)

#i is the number of videos
for i1 in range(0,4):
	#j is the number of comments per video
	for j1 in range(0,9):
		resp1 = requests.get(final_urls[i1])
		k1 = resp1.text
		parsed_json1 = json.loads(k1)
		l1 = parsed_json1['items']
		s1_comments.append(l1[j1]['snippet']['topLevelComment']['snippet']['textOriginal'])
print(s1_comments)

s1_comments = s1_comments.lower()
words = s1_comments.split()

letters_only = re.sub("[^a-zA-Z]", " ",l)

stops = set(stopwords.words("english"))

meaningful_words = [w for w in words if not w in stops]

print( meaningful_words )

sentence=s1_comments
sentence= ''.join(s1_comments)
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

for i2 in range(5,9):
	#j is the number of comments per video
	for j2 in range(0,9):
		resp2 = requests.get(final_urls[i2])
		k2 = resp2.text
		parsed_json2 = json.loads(k2)
		l2 = parsed_json2['items']
		s2_comments.append(l2[j2]['snippet']['topLevelComment']['snippet']['textOriginal'])
print(s2_comments)

for i3 in range(10,14):
	#j is the number of comments per video
	for j3 in range(0,9):
		resp3 = requests.get(final_urls[i3])
		k3 = resp3.text
		parsed_json3 = json.loads(k3)
		l3 = parsed_json3['items']
		s3_comments.append(l3[j3]['snippet']['topLevelComment']['snippet']['textOriginal'])
print(s3_comments)

for i4 in range(15,19):
	#j is the number of comments per video
	for j4 in range(0,9):
		resp4 = requests.get(final_urls[i4])
		k4 = resp4.text
		parsed_json4 = json.loads(k4)
		l4 = parsed_json4['items']
		s4_comments.append(l4[j4]['snippet']['topLevelComment']['snippet']['textOriginal'])
print(s4_comments)

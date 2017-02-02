import sys
from textblob import TextBlob
import codecs
from collections import Counter


filedata = codecs.open(sys.argv[1], 'r', 'utf-8')
text = filedata.read()


blob = TextBlob(text)

# get all the words
blob.words

# get the noun phrases
phrases = blob.noun_phrases
for phrase in phrases:
    print phrase


# find the most common phrases
counter = Counter(phrases)
most_common = counter.most_common(10)
for item in most_common:
    print item



# find lines that contain the most common phrases...
most_common = [w[0] for w in most_common]
for line in text.split('\n'):
    for phrase in most_common:
        if phrase.lower() in line.lower():
            print line



# # get verbs
# verbs = [w[0] for w in blob.tags if w[1]=='VBZ']
# counter = Counter(verbs)
# for item in counter.most_common(100):
#     print item
#
#
# # replacer
# for line in text.split('\n'):
#     if 'Trump' in line:
#         line = line.replace('Trump', 'Stalin')
#         print line

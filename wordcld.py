#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np


# In[17]:


df = pd.read_csv('wordcloud.csv')
df.head()


# In[18]:


X = df2['Review']
y = df2['Label']


# In[21]:


X.isnull().values.any()


# In[22]:


df1=df.copy()


# In[23]:


df2 = df[pd.notnull(df['Review'])]


# In[24]:


df2['Review'] = df2['Review'].str.replace("[^a-zA-Z#]", " ")


# In[25]:


df2['Review'] = df2['Review'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))


# In[26]:


tokenized_review = df2['Review'].apply(lambda x: x.split())
tokenized_review.head()


# In[32]:


sent_str = ""
for sentence in tokenized_review:
  print(sentence)
  #for i in sentence:
    #sent_str += str(i) + "-"
    #sent_str = sent_str[:-1]
    #print (sent_str[5:6])


# In[34]:


blob=(' '.join([str(k) for k in df2['Review']]))
print(blob)


# In[36]:


tagged_sentence = nltk.tag.pos_tag(blob.split())
edited_sentence = [word for word,tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
bn=(' '.join(edited_sentence))


# In[38]:


bn=bn.lower()


# In[40]:


from collections import Counter 
split_it = bn.split() 
Counter = Counter(split_it)
most_occur = Counter.most_common(70) 
print(most_occur)


# In[43]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
stopwords = nltk.corpus.stopwords.words('english')
newStopWords = ['this','would','have','with','been','could','rather','that','will','from','accounting','about','week',
               'weeks','your','which','just','into']
stopwords.extend(newStopWords)


# In[44]:


word_tokens = word_tokenize(bn) 


# In[48]:


filtered_sentence = [w for w in word_tokens if not w in stopwords] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stopwords: 
        filtered_sentence.append(w) 
  
#print(word_tokens) 
print(filtered_sentence) 


# In[50]:


blob1=(' '.join([str(k) for k in filtered_sentence]))
print(blob1)


# In[ ]:





# In[54]:


from wordcloud import WordCloud


# In[62]:


kk=' '.join(df2['Review'])


# In[67]:


rawText = kk.lower()


# In[51]:


tokens = nltk.word_tokenize(blob1)
text = nltk.Text(tokens)


# In[52]:


import re
from operator import itemgetter
 
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
finder = BigramCollocationFinder.from_words(text)
bigram_measures = BigramAssocMeasures()
scored = finder.score_ngrams(bigram_measures.raw_freq)


# In[53]:



scoredList = sorted(scored, key=itemgetter(1), reverse=True)
 


# In[65]:


word_dict = {}
 
listLen = len(scoredList)
 
# Get the bigram and make a contiguous string for the dictionary key. 
# Set the key to the scored value. 
for i in range(listLen):
    word_dict['_'.join(scoredList[i][0])] = scoredList[i][1]
#freq = nltk.FreqDist(word_dict)
 
#for key,val in freq.items():
 
    #print (str(key) + ':' + str(val))
#freq.plot(10, cumulative=False)


# In[64]:


import matplotlib.pyplot as plt
WC_height = 1000
WC_width = 1000
WC_max_words = 70

wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width,min_font_size=6)
 
wordCloud.generate_from_frequencies(word_dict)

plt.figure(figsize=(11,11),edgecolor='blue')
plt.title('Most frequently occurring bigrams connected with an underscore_')
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[66]:


df2.ix[df2.Label>3,'Sentiment']="POSITIVE"
df2.ix[df2.Label<=3,'Sentiment']="NEGATIVE"


# In[69]:


import seaborn as sns
ax = plt.axes()
sns.countplot(df2.Sentiment,ax=ax)
ax.set_title('Sentiment Positive vs Negative Distribution')
plt.show()


# In[70]:





# In[6]:


a=[1,2,3,4]


# In[8]:


b=[1,3]


# In[22]:


def finder(arr1,arr2):
    result=0
    for num in arr1+arr2:
        result^=num
    return result


# In[20]:


def finder1(arr1,arr2):
    counter={}
    for num in arr2:
        if num in counter:
            counter[num]+=1
        else:
            counter[num]=1
    for num in arr1:
        if num in counter:
            counter[num]-=1
        else:
            counter[num]=1
    for k in counter:
        if counter[k]!=0:
            return k


# In[23]:


finder([1,2,3,4,5,6],[3,6,5,4,2])


# In[25]:


finder1([1,2,3,4,5,6],[3,6,5,4,1])


# In[27]:


def unique_char(str):
    str.replace(' ','').lower()
    counter={}
    l=[]
    for i in str:
        if i in counter:
            counter[i]+=1
        else:
            counter[i]=1
    for k in counter:
        if counter[k]==1:
            l.append(k)
    return l


# In[29]:


unique_char('dddddddddd')


# In[ ]:





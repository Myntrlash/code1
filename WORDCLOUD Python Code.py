#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import plotly.plotly as py
import cufflinks as cf
import plotly.tools as tls
import plotly.graph_objs as go


# In[2]:


tls.set_credentials_file(username='Myntrlash', api_key='lh6fN0e0tTaM08xsKjRp')


# In[3]:


df = pd.read_excel('Book1.xlsx')
comment_words = ' '
stopwords = set(STOPWORDS) 
for val in df.Review:  
    val = str(val)  
    tokens = val.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()       
    for words in tokens: 
        comment_words = comment_words + words + ' '


# In[22]:


from plotly.offline import init_notebook_mode, iplot

def plotly_wordcloud(text):
    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 200,
                   max_font_size = 100)
    wc.generate(text)
    
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)
        
    # get the positions
    x=[]
    y=[]
    for i in position_list:
        x.append(i[0])
        y.append(i[1])
            
    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i*100)
    new_freq_list
    
    trace = go.Scatter(x=x, 
                       y=y, 
                       textfont = dict(size=new_freq_list,
                                       color=color_list),
                       hoverinfo='text',
                       hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                       mode="text",  
                       text=word_list
                      )
    
    layout = go.Layout(
                       xaxis=dict(showgrid=True, 
                                  showticklabels=True,
                                  zeroline=False,
                                  automargin=True),
                       yaxis=dict(showgrid=True,
                                  showticklabels=True,
                                  zeroline=False,
                                  automargin=True)
                      )
    
    fig = go.Figure(data=[trace], layout=layout) 
    return fig


# In[23]:


init_notebook_mode(connected=True)
iplot(plotly_wordcloud(comment_words))


# In[ ]:





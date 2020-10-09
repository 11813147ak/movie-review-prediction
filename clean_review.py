#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


sample_text="""films adapted from comic books have had plenty of success , whether they're about superheroes ( batman , superman , spawn ) , or geared toward kids ( casper ) or the arthouse crowd ( ghost world ) , but there's never really been a comic book like from hell before ."""


# In[43]:


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


# In[44]:


tokenizer=RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words('english'))
ps=PorterStemmer()


# In[52]:


def getstemmedreview(review):
    review=review.lower()
    review=review.replace("("," ")
    review=review.replace(")"," ")
    
    tokens=tokenizer.tokenize(review)
    new_tokens=[token for token in tokens if token not in en_stopwords]
    stemmed_tokens=[ps.stem(token) for token in new_tokens]
    
    cleaned_review=' '.join(stemmed_tokens)
    
    return cleaned_review
    


# In[53]:


getstemmedreview(sample_text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





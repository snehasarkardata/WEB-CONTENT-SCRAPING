#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup

s= requests.get('https://www.w3schools.com/python/python_reference.asp')
soup= BeautifulSoup(s.content,'html.parser')

s = soup.find('div', class_='entry-content')
 
lines = soup.find_all('p')
for line in lines:
 print(line.text)


# In[8]:





# In[ ]:





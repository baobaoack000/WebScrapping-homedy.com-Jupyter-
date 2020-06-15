#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as Req 
#Bs4 allow u to find the html code


# In[8]:


def GetUrl(url):
    Uclient = Req(url)
    page_html = Uclient.read()
    Uclient.close()
    page_soup = Soup(page_html, "html.parser")
    return page_soup


# In[6]:


def Printing(get):
    info = get.find("div",{"class":"info"}).find("div").text
    name = get.find("div",{"class":"mobile-number-des mobile-counter"}).get("data-mobile")
    print(name)
    print(info)
    

url = 'https://homedy.com/sieu-hot-chi-135tr-so-huu-ngay-ch-bien-cao-cap-ho-tram-complex-thien-duong-nghi-duong-moi-brvt-es1286736' 
get = GetUrl(url)

Printing(get)


# In[21]:


def LoopUrls(CombineUrls,n2):
    for i in isis:
        print('-----------------------------'+str(n2)+'-----------------------------')
        CombineUrl = 'https://homedy.com/ban-nha-dat'
        selectUrl = i.get("href")
        print(CombineUrl+selectUrl)
        link = GetUrl(CombineUrl+selectUrl)
        n2 = n2+1
    


# In[26]:


#https://repl.it/@baobaoack000/WebscrapingDemoRequest#main2.py
#Varibles
selectUrl  = []
get2 = GetUrl('https://homedy.com/ban-nha-dat')
n= 0
n2=0
#insert and select link / *select page Urls
isis = get2.findAll("a",{"class":"title padding-hoz"})
for i in range(0,2):
#url pages combination
    CombineUrl = 'https://homedy.com/ban-nha-dat'
    print('-----------------------------'+str(i)+'-----------------------------')
    CombineUrl = CombineUrl+ '/p'+ str(i)
    print(CombineUrl)

#href Urls compination(default setting 0)
    LoopUrls('https://homedy.com/ban-nha-dat',0)
    
    


# In[ ]:





# In[ ]:


#https://repl.it/@baobaoack000/WebscrapingDemoRequest#main1.py
#Urlpage number (link placement)
url = str
req = []
for i in range(3):
  url  = 'https://www.bbc.com/news'+'/p'+str(i)
  print(url)
  req  = requests.get(url)
  print(req.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





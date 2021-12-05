# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:57:21 2021

@author: yazan
"""

from bs4 import BeautifulSoup
import requests
import re
import math
import pandas as pd



#Add: Number of critics review, No. of Users Reviews, Certificate
def get_movies(url,headers):
    movies_links = []
    data_headers = ['Title', 'Rating','Oscars','Total Nominations and Awards','Director','Gross','MPAA Rating','Users Reviews Count','Critics Reviews Count']
    movie_title=[]
    movie_rate=[]
    oscars_list=[]
    directors_list=[]
    gross_list =[]
    nomination_wins_total=[]
    MPAA_rating_lsit =[]
    user_rev_count_list = []
    crit_rev_count_list = []
    #Scrape the first page
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(soup.prettify(),'html.parser')
    # Number of pages you want to scrape 
    titles_number = soup.find('div',class_= 'desc lister-total-num-results').get_text().strip()
    #extract comma if any:
    titles_number=titles_number.replace(',','')
    #extract the numerical number
    titles_number =re.findall(r'\d+',titles_number)[0]
    pages_number =  math.ceil(int(titles_number)/100)
   

    for i in range(1,pages_number):
     
     master_urls = url + str(i)   
     page = requests.get(master_urls,headers=headers)
     soup = BeautifulSoup(page.content,'html.parser')
     soup = BeautifulSoup(soup.prettify(),'html.parser')
        #Local Links:
     b_href= soup.find_all('div',class_= 'lister-item mode-detail') 

     for i in range(len(b_href)):
      href= b_href[i].find('div').find('a')['href']  
      href= 'https://www.imdb.com'+ href
      movies_links.append(href)


    for i in movies_links[:]:

        sub_page= requests.get(i,headers=headers)
        sub_soup = BeautifulSoup(sub_page.content,'html.parser')
        sub_soup = BeautifulSoup(sub_soup.prettify(),'html.parser')

        title = sub_soup.find('title').get_text()
        title=title.strip()
        title=title[0:-len( ' - imdb')]

        try:
         rating = sub_soup.find('div',class_= 'AggregateRatingButton__ContentWrap-sc-1ll29m0-0 hmJkIS').find('span').get_text().strip()
         oscars = sub_soup.find('ul',class_= 'ipc-metadata-list ipc-metadata-list--dividers-none Awards__Content-sc-1qdt65t-2 pWPhK ipc-metadata-list--base').find('a').get_text().strip()
         nom_wins =sub_soup.find('span',class_= 'ipc-metadata-list-item__list-content-item').get_text().strip()
         director =sub_soup.find('a',class_= 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text().strip()
         MPAA_rating= sub_soup.find_all('span',class_= 'TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex')[1].get_text().strip()
         user_rev_count  =  sub_soup.find('span',class_= 'score').get_text().strip()
         crit_rev_count =sub_soup.find_all('span',class_= 'score')[1].get_text().strip()
         gross = sub_soup.find_all('span',class_=  'ipc-metadata-list-item__list-content-item')[-2].get_text().strip()

        except:
         print('Error at i=',i)
       


        oscars_list.append(oscars)  
        movie_title.append(title)
        movie_rate.append(rating)
        nomination_wins_total.append(nom_wins)
        directors_list.append(director)
        gross_list.append(gross)
        MPAA_rating_lsit.append(MPAA_rating)
        user_rev_count_list.append(user_rev_count)
        crit_rev_count_list.append(crit_rev_count)

        myvalues =[movie_title,movie_rate,oscars_list,nomination_wins_total,directors_list,gross_list,MPAA_rating_lsit,user_rev_count_list,crit_rev_count_list]
        data_dict =dict(zip(data_headers,myvalues))
        
    return pd.DataFrame(data_dict)
  
 
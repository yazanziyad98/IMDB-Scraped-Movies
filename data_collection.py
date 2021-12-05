# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:02:10 2021

@author: yazan
"""
import IMDB_SCRAPER as IM
import pandas as pd 

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",}
url_a= 'https://www.imdb.com/list/ls091294718/?sort=list_order,asc&st_dt=&mode=detail&page='
url_b= 'https://www.imdb.com/list/ls009796553/?st_dt=&mode=detail&page='
url_c='https://www.imdb.com/list/ls071457904/?sort=list_order,asc&st_dt=&mode=detail&page='
url_d= 'https://www.imdb.com/list/ls051421138/?sort=list_order,asc&st_dt=&mode=detail&page='

df_a = IM.get_movies(url_a,headers)
df_b = IM.get_movies(url_b,headers)
df_c = IM.get_movies(url_c,headers)
df_d = IM.get_movies(url_d,headers)


df=pd.concat([df_a, df_b,df_c,df_d], ignore_index=True)
df.to_csv(r'C:\Users\yazan\OneDrive\Desktop\Data Science\Web Scraping\IMDB_scraping.csv',index=False)


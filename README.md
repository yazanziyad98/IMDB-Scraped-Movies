# Movies Rating Prediction: Project Overview

* Created a tool that estimates movies rating (MAE ~ 0.66)4


* Scraped over 3000 movies from several IMDB movies list using Beautifulsoup python scraper
* Optimized Linear, Lasso, and Random Forest Regressors and used GridsearchCV to reach the best model.

* Built a client facing API using flask

# Resources 
 Python Version: 3.8
 
 Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
 
 Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
 
 Movies List: 
1. https://www.imdb.com/list/ls091294718/?sort=list_order,asc&st_dt=&mode=detail&page=
2. https://www.imdb.com/list/ls009796553/?st_dt=&mode=detail&page=
3. https://www.imdb.com/list/ls071457904/?sort=list_order,asc&st_dt=&mode=detail&page=
4. https://www.imdb.com/list/ls051421138/?sort=list_order,asc&st_dt=&mode=detail&pag

# Web Scraping
Used the web scraper to scrape 3000 movies from IMDB, With each movie, i got the following features:
* Title 
*  Rating
*  Oscars
*  Total Nominations and Awards
*  Director
*  Gross 
*  MPAA Rating
*  Users Reviews Count
*  Critics Reviews Count
*  Ratings Number


# Data Cleaning


After scraping the data, I needed cleaned it up I made the following changes and created the following variables:
* Extracted the year of the movie out of the movie title
* Parser the oscar awards coloumn to create a coloum with numerical number of oscars won by each movie
* Created two columns from the total wins and awards column for the total wins and total awards numbers
* removed numeric letters and symbols from Gross, Users Reviews Count, Critics Reviews Count, and Ratings Number columns.
* Removed date from Gross column
* Removed duplicated rows
* Created a new boolean coloum for movies that are made after 2002
* Renamed the MPAA ratings to their correct names


# EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights 

![alt text](https://github.com/yazanziyad98/IMDB-Web-Scraping/blob/main/correlation%20heatmap.PNG)


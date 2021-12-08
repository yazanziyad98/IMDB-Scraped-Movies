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

<img src="https://github.com/yazanziyad98/IMDB-Web-Scraping/blob/main/correlation%20heatmap.PNG" width="450">  <img src="https://github.com/yazanziyad98/IMDB-Web-Scraping/blob/main/Oscars%20Average.PNG" width="400">

<img src="https://github.com/yazanziyad98/IMDB-Web-Scraping/blob/main/Directors%20Oscars.PNG" width="450">


# Model Building


After transforming the MPAA Rating categorical variables into dummy variables. I split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Root Mean Squared Error.

I tried three different models:

* Multiple Linear Regression 
* Lasso Regression 
* Random Forest 

# Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

* Random Forest : RMSE = 0.67
* Linear Regression: RMSE = 0.748
* Lasso Regression: RMSE = 0.75

# Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the tutorial in the reference section above. The API endpoint takes in a request with a list of values from a movie listing and returns an estimated rating.

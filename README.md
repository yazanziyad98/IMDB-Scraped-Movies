# Movies Rating Prediction: Project Overview

* Created a tool that estimates movies rating (MAE ~ 0.66)4


* Scraped over 3000 movies from several IMDB movies list using Beautifulsoup python scraper
* Optimized Linear, Lasso, and Random Forest Regressors and used GridsearchCV to reach the best model.

* Built a client facing API using flask

# Resources 
_ Python Version: 3.8
_ Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
_ Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
_ Movies List: 

1.  https://www.imdb.com/list/ls091294718/?sort=list_order,asc&st_dt=&mode=detail&page=
2. https://www.imdb.com/list/ls009796553/?st_dt=&mode=detail&page=
3. https://www.imdb.com/list/ls071457904/?sort=list_order,asc&st_dt=&mode=detail&page=
4. https://www.imdb.com/list/ls051421138/?sort=list_order,asc&st_dt=&mode=detail&page=


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
* 




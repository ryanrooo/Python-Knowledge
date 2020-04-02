#Plotting and visualization of data with Python

import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv("C:/Users/Ryann/Documents/movie_metadata.csv")

bmovies = table.groupby("director_name").imdb_score.mean().sort_values().head().plot(kind= "bar")
plt.show(bmovies)

gmovies =  table.groupby("director_name").gross.sum().head().sort_values().plot()
plt.show(gmovies)

ggenre = table.groupby("genres").gross.sum().head().sort_values().plot(kind = "bar")
plt.show(ggenre)


arating = table.groupby("actor_1_name").imdb_score.mean().sort_values().head().plot(kind= "pie")
plt.show(arating)

mgross = table.groupby("movie_title").gross.max().sort_values().head(5).plot(kind= "barh")
plt.show(mgross)





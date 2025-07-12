# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading all CSV files into separate dataframes for handling
df1=pd.read_csv('hotstar.csv')
df2=pd.read_csv('netflix.csv')
df3=pd.read_csv('prime.csv')

# removing naming inconsistencies across content types as required
df1["type"] = df1["type"].replace({"movie" : "Movie", "tv" : "TV Show"})
df2["type"] = df2["type"].replace({"TVSeries" : "TV Show"})

#Comparison of Movies by the Genre in Each Platform
movies_hotstar = df1[df1['type'] == 'Movie'].copy()
movies_netflix = df2[df2['type'] == 'Movie'].copy()
movies_prime = df3[df3['type'] == 'Movie'].copy()

genre_movies_hotstar=movies_hotstar["genre"].value_counts()
genre_movies_netflix=movies_netflix["genre"].value_counts()
movies_prime['genre_list'] = movies_prime['genre'].str.split(';')
movies_prime_new = movies_prime.explode('genre_list')
genre_movies_prime = movies_prime_new['genre_list'].value_counts()

others_hotstar = genre_movies_hotstar.iloc[5:].sum()
others_netflix = genre_movies_netflix.iloc[5:].sum()
others_prime = genre_movies_prime.iloc[5:].sum()

top5_genre_movies_hotstar=genre_movies_hotstar.head(5)
top5_genre_movies_hotstar['Others']=others_hotstar
top5_genre_movies_netflix=genre_movies_netflix.head(5)
top5_genre_movies_netflix['Others']=others_netflix
top5_genre_movies_prime=genre_movies_prime.head(5)
top5_genre_movies_prime['Others']=others_prime

# plotting the pie charts using subplot() function of Matplotlib
plt.figure(figsize=(15, 5.5))

plt.subplot(1, 3, 1)
plt.pie(top5_genre_movies_netflix, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':8})
plt.legend(labels = top5_genre_movies_netflix.index, loc = "upper right", bbox_to_anchor = (1.33, 1))
plt.title("Netflix", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 2)
plt.pie(top5_genre_movies_hotstar, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':8})
plt.legend(labels = top5_genre_movies_hotstar.index, loc = "upper right", bbox_to_anchor = (1.30, 1),fontsize=11)
plt.title("Hotstar", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 3)
plt.pie(top5_genre_movies_prime, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':8})
plt.legend(labels = top5_genre_movies_prime.index, loc = "upper right", bbox_to_anchor = (1.33, 1),fontsize=11)
plt.title("Prime Video", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.suptitle("Comparison of Movies by Genre in Each Platform", fontname = "serif", fontweight = "bold", fontsize = 22)

# saving the figure as an image
plt.savefig("movie_type.png")
plt.show()

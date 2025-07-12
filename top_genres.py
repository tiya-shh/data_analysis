# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading all CSV files into separate dataframes for handling
df1 = pd.read_csv("hotstar.csv")
df2 = pd.read_csv("netflix.csv")
df3 = pd.read_csv("prime.csv")

# counting number of items for each genre (the Prime Video dataset had merged genres, so had to split them first before counting)
genre_hotstar = df1["genre"].value_counts()
genre_netflix = df2["genre"].value_counts()
df3['genre_list'] = df3['genre'].str.split(';')
df3_new = df3.explode('genre_list')
genre_prime = df3_new['genre_list'].value_counts()

# plotting the bar graphs using subplot() function of Matplotlib
plt.figure(figsize = (13, 10))

plt.subplot(3, 1, 1)

top10_netflix = genre_netflix.head(10)
plt.bar(top10_netflix.index, top10_netflix.values)
plt.title("Netflix", loc = "left", fontname = "sans-serif", fontweight = "bold", fontsize = 14)
plt.xlabel("Genre", fontweight = "bold")
plt.ylabel("Number of Items", fontweight = "bold")

plt.subplot(3, 1, 2)

top10_hotstar = genre_hotstar.head(10)
plt.bar(top10_hotstar.index, top10_hotstar.values)
plt.title("Hotstar", loc = "left", fontname = "sans-serif", fontweight = "bold", fontsize = 14)
plt.xlabel("Genre", fontweight = "bold")
plt.ylabel("Number of Items", fontweight = "bold")

plt.subplot(3, 1, 3)
top10_prime = genre_prime.head(10)
plt.bar(top10_prime.index, top10_prime.values)
plt.title("Prime Video", loc = "left", fontname = "sans-serif", fontweight = "bold", fontsize = 14)
plt.xlabel("Genre", fontweight = "bold")
plt.ylabel("Number of Items", fontweight = "bold")

plt.suptitle("Comparison of Top 10 Genres", fontname = "serif", fontweight = "bold", fontsize = 22)

plt.subplots_adjust(hspace = 0.5)

# saving the figure as an image
plt.savefig("genre.png")
plt.show()

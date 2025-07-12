# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading all CSV files into separate dataframes for handling
df1 = pd.read_csv("hotstar.csv")
df2 = pd.read_csv("netflix.csv")
df3 = pd.read_csv("prime.csv")

# removing naming inconsistencies across content types as required
df1["type"] = df1["type"].replace({"movie" : "Movie", "tv" : "TV Show"})
df2["type"] = df2["type"].replace({"TVSeries" : "TV Show"})

# counting the number of movies & TV shows for each platform
type_hotstar = df1["type"].value_counts()
type_netflix = df2["type"].value_counts()
type_prime = df3["type"].value_counts()

# plotting the pie charts using subplot() function of Matplotlib
plt.figure(figsize=(15, 5.5))

plt.subplot(1, 3, 1)
plt.pie(type_netflix, labels=None, autopct = "%.2f%%", colors = ['skyblue', 'lightsalmon'])
plt.legend(labels = type_netflix.index, loc = "upper right")
plt.title("Netflix", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 2)
plt.pie(type_hotstar, labels=None, autopct = "%.2f%%", colors = ['skyblue', 'lightsalmon'])
plt.legend(labels = type_hotstar.index, loc = "upper right")
plt.title("Hotstar", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 3)
plt.pie(type_prime, labels=None, autopct = "%.2f%%", colors = ['skyblue', 'lightsalmon'])
plt.legend(labels = type_prime.index, loc = "upper right")
plt.title("Prime Video", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.suptitle("Proportion of Movies vs TV Shows", fontname = "serif", fontweight = "bold", fontsize = 22)

# saving the figure as an image
plt.savefig("content_type.png")
plt.show()

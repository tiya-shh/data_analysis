# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading all CSV files into separate dataframes for handling
df1 = pd.read_csv("hotstar.csv")
df2 = pd.read_csv("netflix.csv")
df3 = pd.read_csv("prime.csv")

# removing the NR (non-rated) rows
df3 = df3[df3.rating != 'NR']

# removing naming inconsistencies, making adjustments as required
df1["age_rating"] = df1["age_rating"].replace({"PG" : "U/A 13+"})
df3["rating"] = df3["rating"].replace({"18+" : "A", "16+" : "U/A 16+", "13+" : "U/A 13+", "7+" : "U/A 7+"})

# counting the number of movies/shows for each age rating (U, U/A 7+, U/A 13+, U/A 16+, A)
age_rating_hotstar = df1["age_rating"].value_counts()
age_rating_netflix = df2["rating"].value_counts()
age_rating_prime = df3["rating"].value_counts()

# plotting the pie charts using subplot() function of Matplotlib
plt.figure(figsize=(15, 5.5))

plt.subplot(1, 3, 1)
plt.pie(age_rating_netflix, labels=None, autopct = "%.2f%%", colors = ['#c6e0f5', '#74befa', '#229cff', '#016ac5', '#014f9b'])
plt.legend(labels = age_rating_netflix.index, loc = "upper right", bbox_to_anchor = (1.25, 1))
plt.title("Netflix", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 2)
plt.pie(age_rating_hotstar, labels=None, autopct = "%.2f%%", colors = ['skyblue', 'lightsalmon', 'plum', 'gold', 'mediumspringgreen'])
plt.legend(labels = age_rating_hotstar.index, loc = "upper right", bbox_to_anchor = (1.25, 1))
plt.title("Hotstar", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 3)
plt.pie(age_rating_prime, labels=None, autopct = "%.2f%%", colors = ['skyblue', 'lightsalmon', 'plum', 'gold', 'mediumspringgreen'])
plt.legend(labels = age_rating_prime.index, loc = "upper right", bbox_to_anchor = (1.25, 1))
plt.title("Prime Video", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.suptitle("Distribution of Content Age Rating", fontname = "serif", fontweight = "bold", fontsize = 22)

# saving the figure as an image
plt.savefig("rating_type.png")
plt.show()

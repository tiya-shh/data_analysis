#Comparison of TV Shows by the Genre in Each Platform
tv_hotstar = df1[df1['type'] == 'TV Show'].copy()
tv_netflix = df2[df2['type'] == 'TV Show'].copy()
tv_prime = df3[df3['type'] == 'TV Show'].copy()

genre_tv_hotstar=tv_hotstar["genre"].value_counts()
genre_tv_netflix=tv_netflix["genre"].value_counts()
tv_prime['genre_list'] = tv_prime['genre'].str.split(';')
tv_prime_new = tv_prime.explode('genre_list')
genre_tv_prime = tv_prime_new['genre_list'].value_counts()

others_hotstar = genre_tv_hotstar.iloc[5:].sum()
others_netflix = genre_tv_netflix.iloc[5:].sum()
others_prime = genre_tv_prime.iloc[5:].sum()

top5_genre_tv_hotstar=genre_tv_hotstar.head(5)
top5_genre_tv_hotstar['Others']=others_hotstar
top5_genre_tv_netflix=genre_tv_netflix.head(5)
top5_genre_tv_netflix['Others']=others_netflix
top5_genre_tv_prime=genre_tv_prime.head(5)
top5_genre_tv_prime['Others']=others_prime

# plotting the pie charts using subplot() function of Matplotlib
plt.figure(figsize=(15, 5.5))

plt.subplot(1, 3, 1)
plt.pie(top5_genre_tv_netflix, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':9})
plt.legend(labels = top5_genre_tv_netflix.index, loc = "upper right", bbox_to_anchor = (1.32, 1))
plt.title("Netflix", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 2)
plt.pie(top5_genre_tv_hotstar, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':9})
plt.legend(labels = top5_genre_tv_hotstar.index, loc = "upper right", bbox_to_anchor = (1.25, 1))
plt.title("Hotstar", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.subplot(1, 3, 3)
plt.pie(top5_genre_tv_prime, labels=None, autopct = "%.2f%%", colors = ['#628ECB', '#8AAEE0', '#B1C9EF', '#d7e3fc','#D5DEEF', '#F0F3FA'],textprops={'fontsize':9})
plt.legend(labels = top5_genre_tv_prime.index, loc = "upper right", bbox_to_anchor = (1.25, 1))
plt.title("Prime Video", fontname = "sans-serif", fontweight = "bold", fontsize = 14)

plt.suptitle("Comparison of TV Shows by the Genre in Each Platform", fontname = "serif", fontweight = "bold", fontsize = 22)

# saving the figure as an image
plt.savefig("tv_type.png")
plt.show()

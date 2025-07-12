# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading all CSV files into separate dataframes for handling
df1=pd.read_csv('hotstar.csv')
df2=pd.read_csv('netflix.csv')
df3=pd.read_csv('prime.csv')

#Cleaning the dataset
df1["type"] = df1["type"].replace({"movie" : "Movie", "tv" : "TV Show"})
df2["type"] = df2["type"].replace({"TVSeries" : "TV Show"})

df3['genre_list'] = df3['genre'].str.split(';')
df3_new = df3.explode('genre_list')

movie_netflix=df2[df2['type']== 'Movie'].copy()
movie_netflix['duration'] = movie_netflix['duration'].astype(float)

tv_netflix=df2[df2['type']== 'TV Show'].copy()
tv_netflix=tv_netflix.rename(columns={'duration':'seasons'})
tv_netflix['seasons'] = tv_netflix['seasons'].str.replace(' Season', '', regex=False)
tv_netflix['seasons'] = tv_netflix['seasons'].str.replace('s', '', regex=False).astype(float)

movie_hotstar=df1[df1['type']== 'Movie'].copy()
movie_hotstar['duration'] = movie_hotstar['running_time'] / 60

tv_hotstar=df1[df1['type']== 'TV Show'].copy()

movie_prime=df3[df3['type']== 'Movie'].copy()
movie_prime=movie_prime.rename(columns={'runtime':'duration'})

tv_prime=df3[df3['type']== 'TV Show'].copy()
tv_prime=tv_prime.rename(columns={'season':'seasons'})
tv_prime['seasons'] = tv_prime['seasons'].str.replace('Season ', '', regex=False).astype(float)

avg_netflix = pd.DataFrame({'Content Type':['Movie', 'TV Show'],'Average Duration':[movie_netflix['duration'].mean(),tv_netflix['seasons'].mean()]})

avg_hotstar = pd.DataFrame({'Content Type':['Movie', 'TV Show'],'Average Duration':[movie_hotstar['duration'].mean(),tv_hotstar['seasons'].mean()]})

avg_prime = pd.DataFrame({'Content Type':['Movie', 'TV Show'],'Average Duration':[movie_prime['duration'].mean(),tv_prime['seasons'].mean()]})

#Merging the dataframes

avg=pd.merge(avg_netflix,avg_hotstar, on='Content Type',suffixes=('_Netflix','_Hotstar'))
avg=pd.merge(avg,avg_prime,on='Content Type')
avg=avg.rename(columns={'Average Duration':'Average Duration_Prime'})

#Plotting the bar plot using matplotlib
colors = ['#628ECB', '#8AAEE0', '#B1C9EF']
ax=avg.plot(kind='bar',x='Content Type',color=colors)
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', label_type='edge', fontsize=10)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Average Duration of Movies/TV Shows in Each Platform')
plt.ylabel('Movie(Hours)/TV Shows(Seasons)')
plt.savefig('duration_type.jpg')
plt.show()

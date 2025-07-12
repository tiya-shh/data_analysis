#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading all CSV files into separate DataFrames
df=pd.read_csv("netflix.csv")
df2=pd.read_csv("prime.csv")
df3=pd.read_csv("hotstar.csv")

#cleaning the dataframe as required and grouping data on the basis of Movies Or TV Shows and transposing the datasets
df = df[df['release_year'] != 2024]
df2 = df2[df2['release_year'] != 2024]

data=(df.groupby('type')['release_year'].value_counts().unstack())
data=data.fillna(0)
data_T = data.T.tail(48)

data2=(df2.groupby('type')['release_year'].value_counts().unstack())
data2=data2.fillna(0)
data2_T=data2.T.tail(50)

data3=(df3.groupby('type')['year'].value_counts().unstack())
data3=data3.fillna(0)
data3_T=data3.T.tail(50)

#ploting Bar Graphs for Each using Subplots() in Matplotlib
fig, axs = plt.subplots(3, 1, figsize=(12, 12))

#1 Netflix
axs[0].bar(data_T.index.astype(int),data_T['Movie'],label='Movies',width=0.5,color="red")
axs[0].bar(data_T.index.astype(int),data_T['TVSeries'],bottom=data_T['Movie'],label='TV Shows',width=0.5,color="grey")
axs[0].set_ylim(0,1000)
axs[0].set_xlabel('Year', fontweight='bold')
axs[0].set_ylabel('Number of Movies \n and TV Shows', fontweight='bold')
axs[0].set_title('NETFLIX',loc='right',fontname='sans-serif',fontweight='bold',fontsize='12')
axs[0].legend()

#2 Prime Video
axs[1].bar(data2_T.index.astype(int),data2_T['Movie'],label='Movies',width=0.5,color="teal")
axs[1].bar(data2_T.index.astype(int),data2_T['TV Show'],bottom=data2_T['Movie'],label='TV Shows',width=0.5,color="coral")
axs[1].set_ylim(0,1000)
axs[1].set_xlabel('Year', fontweight='bold')
axs[1].set_ylabel('Number of Movies \n and TV Shows', fontweight='bold')
axs[1].set_title('AMAZON PRIME VIDEO',loc='right',fontname='sans-serif',fontweight='bold',fontsize='12')
axs[1].legend(loc='upper left')

#3 Hotstar
axs[2].bar(data3_T.index.astype(int),data3_T['movie'],label='Movies',width=0.5,color="slateblue")
axs[2].bar(data3_T.index.astype(int),data3_T['tv'],bottom=data3_T['movie'],label='TV Shows',width=0.5,color="turquoise")
axs[2].set_ylim(0,1000)
axs[2].set_xlabel('Year', fontweight='bold')
axs[2].set_ylabel('Number of Movies \n and TV Shows', fontweight='bold')
axs[2].set_title('HOTSTAR',loc='right',fontname='sans-serif',fontweight='bold',fontsize='12')
axs[2].legend(loc='upper left')

plt.suptitle('Comparison Of The Total Movies and TV Shows Released\n(Top 50)',fontname='sans-serif',fontweight='bold',fontsize='18')
plt.tight_layout()

#saving the figure as Image(.jpg format)
plt.savefig('Released_year.jpg')
plt.show()

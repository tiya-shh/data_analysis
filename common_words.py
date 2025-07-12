# importing libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# concatenating all the descriptions for all items on every platform into a single string
text_hotstar = " ".join(df1["description"].fillna(" "))
text_netflix = " ".join(df2["description"].fillna(" "))
text_prime = " ".join(df3["synopsis"].fillna(" "))

# forming the wordclouds for each platform
wordcloud_hotstar = WordCloud(width = 800, height = 400, background_color = "white", colormap = "viridis").generate(text_hotstar)
wordcloud_netflix = WordCloud(width = 800, height = 400, background_color = "white", colormap = "viridis").generate(text_netflix)
wordcloud_prime = WordCloud(width = 800, height = 400, background_color = "white", colormap = "viridis").generate(text_prime)

# plotting the wordclouds using subplot() function of Aatplotlib
plt.figure(figsize = (10, 18))

plt.subplot(3, 1, 1)
plt.imshow(wordcloud_netflix, interpolation = "bilinear")
plt.axis("off")
plt.title("Netflix", fontname = "sans-serif", fontweight = "bold", fontsize = 14, loc = "left")

plt.subplot(3, 1, 2)
plt.imshow(wordcloud_hotstar, interpolation = "bilinear")
plt.axis("off")
plt.title("Hotstar", fontname = "sans-serif", fontweight = "bold", fontsize = 14, loc = "left")

plt.subplot(3, 1, 3)
plt.imshow(wordcloud_prime, interpolation = "bilinear")
plt.axis("off")
plt.title("Prime Video", fontname = "sans-serif", fontweight = "bold", fontsize = 14, loc = "left")

plt.suptitle("Most Common Words in Movie & TV Show Descriptions", fontname = "serif", fontweight = "bold", fontsize = 22)
plt.subplots_adjust(hspace = 0.3)

# saving the figure as an image
plt.savefig("wordcloud.png")
plt.show()

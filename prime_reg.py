from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df_movie_df3 = df3[(df3["type"] == "Movie") & df3["runtime"].notna() & df3["release_year"].notna()].copy()
df_movie_df3["running_time"] = (df_movie_df3["runtime"] * 60).round()  # Converting to minutes
df_tv_df3 = df3[(df3["type"] == "TV Show") & df3["season"].notna() & df3["release_year"].notna()].copy()

# Extracting only the season number from strings like "Season 1"
df_tv_df3["seasons"] = df_tv_df3["season"].str.extract(r"(\d+)").astype("Int64")
df_tv_df3 = df_tv_df3[df_tv_df3["seasons"].notna()]

# Making regression model objects for Prime Video movies and TV shows
reg_movie_df3 = LinearRegression().fit(df_movie_df3[["release_year"]], df_movie_df3["running_time"])
reg_tv_df3 = LinearRegression().fit(df_tv_df3[["release_year"]], df_tv_df3["seasons"])

plt.figure(figsize=(12, 5))

# Movie plot
plt.subplot(1, 2, 1)
plt.scatter(df_movie_df3["release_year"], df_movie_df3["running_time"], color="blue", alpha=0.4, marker=".")
plt.plot(df_movie_df3["release_year"], reg_movie_df3.predict(df_movie_df3[["release_year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Running Time (minutes)", fontweight="bold")
plt.title("Movies: Year vs Runtime", loc="left")

# TV Show plot
plt.subplot(1, 2, 2)
plt.scatter(df_tv_df3["release_year"], df_tv_df3["seasons"], color="blue", alpha=0.4, marker=".")
plt.plot(df_tv_df3["release_year"], reg_tv_df3.predict(df_tv_df3[["release_year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Number of Seasons", fontweight="bold")
plt.title("TV Shows: Year vs No. of Seasons", loc="left")

plt.suptitle("Prime Video", fontname="serif", fontweight="bold", fontsize=22)
plt.subplots_adjust(top = 0.8)

plt.show()

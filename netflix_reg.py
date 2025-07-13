from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df2_movies = df2[(df2["type"] == "Movie") & df2["duration"].notna() & df2["release_year"].notna()].copy()
df2_movies["running_time"] = pd.to_numeric(df2_movies["duration"], errors="coerce")
df2_movies["running_time"] = (df2_movies["running_time"] * 60).round()  # converting to minutes

df2_tv = df2[(df2["type"] == "TV Show") & df2["duration"].notna() & df2["release_year"].notna()].copy()
tv_durations = df2_tv["duration"].astype(str).str.strip().str.lower()
df2_tv["seasons"] = tv_durations.str.extract(r"(\d+)").astype("Int64")

df2_tv = df2_tv[df2_tv["seasons"].notna()]

# Making regression objects for Netflix movies & TV shows
reg_movie_df2 = LinearRegression().fit(df2_movies[["release_year"]], df2_movies["running_time"])
reg_tv_df2 = LinearRegression().fit(df2_tv[["release_year"]], df2_tv["seasons"])

plt.figure(figsize=(12, 5))

# Movie plot
plt.subplot(1, 2, 1)
plt.scatter(df2_movies["release_year"], df2_movies["running_time"], color="blue", alpha=0.4, marker=".")
plt.plot(df2_movies["release_year"], reg_movie_df2.predict(df2_movies[["release_year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Running Time (minutes)", fontweight="bold")
plt.title("Movies: Year vs Runtime", loc="left")

# TV Show plot
plt.subplot(1, 2, 2)
plt.scatter(df2_tv["release_year"], df2_tv["seasons"], color="blue", alpha=0.4, marker=".")
plt.plot(df2_tv["release_year"], reg_tv_df2.predict(df2_tv[["release_year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Number of Seasons", fontweight="bold")
plt.title("TV Shows: Year vs No. of Seasons", loc="left")

plt.suptitle("Netflix", fontname="serif", fontweight="bold", fontsize=22)
plt.subplots_adjust(top = 0.8)

plt.show()

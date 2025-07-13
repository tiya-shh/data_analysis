from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df1_movie = df1[(df1["type"] == "Movie") & (df1["running_time"].notna()) & (df1["year"].notna())]
df1_tv = df1[(df1["type"] == "TV Show") & (df1["seasons"].notna()) & (df1["year"].notna())]

# Making regression objects for Hotstar movies & TV shows
reg_movie_df1 = LinearRegression().fit(df1_movie[["year"]], df1_movie["running_time"])
reg_tv_df1 = LinearRegression().fit(df1_tv[["year"]], df1_tv["seasons"])

plt.figure(figsize=(12, 5))

# Movies plot
plt.subplot(1, 2, 1)
plt.scatter(df1_movie["year"], df1_movie["running_time"], color="blue", alpha=0.4, marker=".")
plt.plot(df1_movie["year"], reg_movie_df1.predict(df1_movie[["year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Running Time (minutes)", fontweight="bold")
plt.title("Movies: Year vs Runtime", loc="left")

# TV Shows plot
plt.subplot(1, 2, 2)
plt.scatter(df1_tv["year"], df1_tv["seasons"], color="blue", alpha=0.4, marker=".")
plt.plot(df1_tv["year"], reg_tv_df1.predict(df1_tv[["year"]]), color="red")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Number of Seasons", fontweight="bold")
plt.title("TV Shows: Year vs No. of Seasons", loc="left")

plt.suptitle("Hotstar", fontname="serif", fontweight="bold", fontsize=22)
plt.subplots_adjust(top = 0.8)

plt.savefig("hotstar_reg.png")
plt.show()

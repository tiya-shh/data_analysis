title_hotstar = hotstar_df['year'].value_counts().sort_index()
title_hotstar_df = title_hotstar.reset_index()
title_hotstar_df.columns = ['year', 'count']

X1 = title_hotstar_df[['year']]
y1 = title_hotstar_df['count']

# Count titles per year for Netflix
title_netflix = netflix_df['release_year'].value_counts().sort_index()
title_netflix_df = title_netflix.reset_index()
title_netflix_df.columns = ['year', 'count']

X2 = title_netflix_df[['year']]
y2 = title_netflix_df['count']

# Count titles per year for Prime
title_prime = prime_df['release_year'].value_counts().sort_index()
title_prime_df = title_prime.reset_index()
title_prime_df.columns = ['year', 'count']

X3 = title_prime_df[['year']]
y3 = title_prime_df['count']

model1 = LinearRegression()
model1.fit(X1, y1)
X1_range = np.linspace(X1['year'].min(), X1['year'].max(), 300).reshape(-1, 1)
y1_pred = model1.predict(X1_range)

model2 = LinearRegression()
model2.fit(X2, y2)
X2_range = np.linspace(X2['year'].min(), X2['year'].max(), 300).reshape(-1, 1)
y2_pred = model2.predict(X2_range)

model3 = LinearRegression()
model3.fit(X3, y3)
X3_range = np.linspace(X3['year'].min(), X3['year'].max(), 300).reshape(-1, 1)
y3_pred = model3.predict(X3_range)


plt.figure(figsize=(12, 6))
plt.scatter(X1, y1, color='blue', label='Hotstar')
plt.plot(X1_range, y1_pred, color='blue', linewidth=2, label='Hotstar')
plt.title('Titles vs Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X2, y2, color='red', label='Netflix')
plt.plot(X2_range, y2_pred, color='red', linewidth=2, label='Netflix')
plt.title('Titles vs Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X3, y3, color='green', label='Prime')
plt.plot(X3_range, y3_pred, color='green', linewidth=2, label='Prime')
plt.title('Titles vs Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend()
plt.grid(True)
plt.show()

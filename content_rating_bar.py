import pandas as pd
import matplotlib.pyplot as plt

# Load all 3 datasets
hotstar = pd.read_csv("hotstar.csv")
prime = pd.read_csv("primevideo_india_movies_and_shows.csv")
netflix = pd.read_csv("netflix_india_shows_and_movies.csv")

# Clean Hotstar ratings
hotstar_df = hotstar[['title', 'age_rating']].dropna()
hotstar_df['Platform'] = 'Hotstar'
hotstar_df.rename(columns={'age_rating': 'Age Rating'}, inplace=True)

# Clean Prime Video ratings
prime_df = prime[['name', 'rating']].dropna()
prime_df['Platform'] = 'Prime Video'
prime_df.rename(columns={'rating': 'Age Rating', 'name': 'title'}, inplace=True)

# Clean Netflix ratings
netflix_df = netflix[['name', 'rating']].dropna()
netflix_df['Platform'] = 'Netflix'
netflix_df.rename(columns={'rating': 'Age Rating', 'name': 'title'}, inplace=True)

# Combine all
df = pd.concat([hotstar_df, prime_df, netflix_df], ignore_index=True)

# Standardize ratings
df['Age Rating'] = df['Age Rating'].str.strip().str.upper()
replace_map = {
    '13+': 'U/A 13+', '16+': 'U/A 16+', '18+': 'A',
    '7+': 'U/A 7+', 'NR': 'Unrated', 'TV-G': 'U',
    'TV-Y7': 'U/A 7+', 'TV-14': 'U/A 13+', 'TV-MA': 'A',
    'TV-Y': 'U', 'PG-13': 'U/A 13+', 'R': 'A', 'G': 'U',
    'PG': 'U/A 13+', 'NC-17': 'A'
}
df['Age Rating'] = df['Age Rating'].replace(replace_map)

# Keep only allowed ratings in desired order
allowed_order = ['U', 'U/A 7+', 'U/A 13+', 'U/A 16+', 'A']
df = df[df['Age Rating'].isin(allowed_order)]

# Count and reorder
rating_counts = df.groupby(['Platform', 'Age Rating']).size().unstack(fill_value=0)
rating_counts = rating_counts[allowed_order]  # Reorder columns as requested

# Plot
rating_counts.T.plot(kind='bar', figsize=(12, 6), colormap='tab20', edgecolor='black')
plt.title('Content Age Ratings per Platform')
plt.xlabel('Age Rating')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Platform')
plt.tight_layout()
plt.show()

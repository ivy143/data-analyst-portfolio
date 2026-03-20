import pandas as pd

df = pd.read_csv("netflix_dataset.csv")
df.info()
df.head()
df.isnull().sum()
df.describe()
df.shape
df.duplicated().sum()

# Check missing values clearly
print(df.isnull().sum())

# Fill missing values
df['director'] = df['director'].fillna("Not Available")
df['cast'] = df['cast'].fillna("Not Available")

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'])

# Create new column for year added
df['year_added'] = df['date_added'].dt.year

# Check again
df.info()

#PHASE 4- DURATION ANALYSIS (moved early so output isn't blocked by plots)
# EXTRACT NUMERIC DURATION and display a sample immediately
extracted = df['duration'].str.extract(r'(\d+)')[0]
df['duration_num'] = pd.to_numeric(extracted, errors='coerce').astype('Int64')
print("duration sample:\n", df[['duration','duration_num']].head())

# compute a few simple stats while we're here
movies = df[df['type'] == 'Movie']
shows = df[df['type'] == 'TV Show']
print("Average Movie Duration:", movies['duration_num'].mean())
print("Average Seasons:", shows['duration_num'].mean())
print(movies.sort_values(by='duration_num', ascending=False)[['title','duration_num']].head(1))

# Now continue with EDA

# Check value counts for type column


#PHASE 2- EXPLORATORY ANALYSIS(EDA)
#step1- MOVIE VS TV SHOWS DISTRIBUTION
print(df['type'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows Distribution")
plt.show()


# step2- CONTENT GROWTH OVER TIME
df['year_added'].value_counts().sort_index()
df['year_added'].value_counts().sort_index().plot(kind='line')
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()


#step3- TOP COUNTRIES
print(df['country'].value_counts())
df['country'].value_counts().plot(kind='bar')
plt.title("Content by Country")
plt.show()

#step4-  RATING DISTRIBUTION
df['rating'].value_counts()
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title("Rating Distribution")
plt.show()


#PHASE 3- GENRE ANALYSIS
df['listed_in'] = df['listed_in'].str.split(', ')
genre_df = df.explode('listed_in')

print(genre_df['listed_in'].value_counts())
genre_df['listed_in'].value_counts().plot(kind='bar')
plt.title("Top Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

#PHASE 4- DURATION ANALYSIS (runs before any plots)
extracted = df['duration'].str.extract(r'(\d+)')[0]
df['duration_num'] = pd.to_numeric(extracted, errors='coerce').astype('Int64')
print("duration sample:\n", df[['duration','duration_num']].head())


movies = df[df['type'] == 'Movie']
shows  = df[df['type'] == 'TV Show']
print("Average Movie Duration:", movies['duration_num'].mean())
print("Average Seasons:", shows['duration_num'].mean())
print(movies.sort_values(by='duration_num', ascending=False)[['title','duration_num']].head(1))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data/top-250-movie-ratings.csv")

# --- Data cleaning ---
# Remove commas and convert 'Rating Count' to integer
df['Rating Count'] = df['Rating Count'].str.replace(',', '').astype(int)

# --- Basic info ---
print("Dataset Info:")
print(df.info(), "\n")
print("First 5 rows:")
print(df.head(), "\n")

# --- General statistics ---
print("Average rating:", df["Rating"].mean())
print("Median rating:", df["Rating"].median())
print("Rating standard deviation:", df["Rating"].std())
print("Average number of votes:", df["Rating Count"].mean(), "\n")

# --- Top/Bottom movies ---
top_movie = df.loc[df["Rating"].idxmax()]
low_movie = df.loc[df["Rating"].idxmin()]
print(f"Highest rated movie: {top_movie['Title']} ({top_movie['Rating']})")
print(f"Lowest rated movie: {low_movie['Title']} ({low_movie['Rating']})\n")

# --- Ratings by decade ---
df['Decade'] = (df['Year'] // 10) * 10
decade_stats = df.groupby('Decade')['Rating'].mean()
print("Average rating by decade:")
print(decade_stats, "\n")

# --- Most voted movies ---
most_votes = df.sort_values(by='Rating Count', ascending=False).head(5)
print("Top 5 most voted movies:")
print(most_votes[['Title', 'Rating Count']], "\n")

# --- Visualizations ---
# Histogram of ratings
plt.figure(figsize=(8,5))
plt.hist(df["Rating"], bins=20, edgecolor='black', color='skyblue')
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.show()

# Average rating by decade bar chart
plt.figure(figsize=(8,5))
decade_stats.plot(kind='bar', color='orange')
plt.title("Average Movie Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.show()

# Scatter plot: Rating vs Rating Count
plt.figure(figsize=(8,5))
plt.scatter(df["Rating Count"], df["Rating"], alpha=0.5, color='green')
plt.xscale('log')  # Log scale because counts vary a lot
plt.title("Rating vs Number of Votes")
plt.xlabel("Number of Votes (log scale)")
plt.ylabel("Rating")
plt.show()

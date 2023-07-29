#top reviewers 

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("anime_reviews.csv")

# Step 2: Group data by reviewers and count their reviews
reviewer_review_count = df.groupby("Reviewer").size().reset_index(name="ReviewCount")

# Step 3: Identify unique anime titles reviewed by each reviewer
reviewer_anime_titles = df.groupby("Reviewer")["AnimeTitle"].apply(lambda x: x.unique().tolist()).reset_index(name="AnimeTitles")

# Step 4: Merge reviewer_review_count and reviewer_anime_titles
reviewer_stats = pd.merge(reviewer_review_count, reviewer_anime_titles, on="Reviewer")

# Step 5: Sort the reviewers based on the number of reviews
top_reviewers_by_reviews = reviewer_stats.sort_values(by="ReviewCount", ascending=False)

# Display the top reviewers and their statistics
print("Top Reviewers by Number of Reviews:")
print(top_reviewers_by_reviews.head(10))

# Step 6: Visualize the top reviewers and the number of reviews they have contributed
plt.figure(figsize=(10, 6))
plt.bar(top_reviewers_by_reviews["Reviewer"][:10], top_reviewers_by_reviews["ReviewCount"][:10])
plt.title("Top Reviewers by Number of Reviews")
plt.xlabel("Reviewer")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

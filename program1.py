# Simple Social Media Suggestion Algorithm
# Finds similar posts from a fake "database" based on word similarity

# Fake database of posts
database_posts = [
    "I love learning Python programming",
    "Python is great for beginners",
    "Having a great day at the park",
    "Programming is fun when you understand the basics",
    "Today I learned about algorithms",
    "Great weather to go outside",
]

# User's post
user_post = input("Enter your post: ").lower()

# Convert user post into words
user_words = user_post.split()

similar_posts = []

# Compare each database post
for post in database_posts:
    score = 0
    post_words = post.lower().split()

    # Count matching words
    for w in user_words:
        if w in post_words:
            score += 1

    # Store posts with a similarity score
    if score > 0:
        similar_posts.append((post, score))

# Sort by similarity score (highest first)
similar_posts.sort(key=lambda x: x[1], reverse=True)

# Show results
print("\n--- Suggested Posts ---")
if not similar_posts:
    print("No similar posts found.")
else:
    for post, score in similar_posts:
        print(f"- {post} (Similarity score: {score})")

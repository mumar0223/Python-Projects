# -----------------------------
# 3. SOCIAL MEDIA BAD WORD FILTER
# -----------------------------

bad_words = ["bad", "hate", "ugly", "stupid"]

post = input("Enter your post: ")
words = post.split()
filtered = []

for w in words:
    if w.lower() in bad_words:
        filtered.append("***")
    else:
        filtered.append(w)

filtered_post = " ".join(filtered)
print("Filtered post:", filtered_post)

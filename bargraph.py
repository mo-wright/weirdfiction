import matplotlib.pyplot as plt
import collections
import re


def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()  # Convert to lowercase
        text = re.sub(r"[^a-z\s]", "", text)
        words = text.split()
    return words

# Load both texts
file1_words = read_text("corpora/lovecraftSentences.txt")  # First text
file2_words = read_text("corpora/poeSentences.txt")  # Second text

# Count word frequency
file1_freq = collections.Counter(file1_words)
file2_freq = collections.Counter(file2_words)

# Find common words
common_words = set(file1_freq.keys()).intersection(set(file2_freq.keys()))

# Prepare for plotting
words_to_plot = list(common_words)[:10]  # 10 words
file1_counts = [file1_freq[word] for word in words_to_plot]
file2_counts = [file2_freq[word] for word in words_to_plot]

# Plot comparison
plt.figure(figsize=(10, 5))
plt.bar(words_to_plot, file1_counts, alpha=0.6, label="Colour Out of Space")
plt.bar(words_to_plot, file2_counts, alpha=0.6, label="Another Text", color="purple")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Comparison")
plt.legend()
plt.show()

# Save plot to a file
plt.savefig("docs/images/plot.png")






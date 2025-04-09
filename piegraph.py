import plotly.graph_objects as go
from collections import Counter
import re

# read text files
def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    # Remove non-alphabet characters and lowercase
    text = re.sub(r'[^A-Za-z\s]', '', text.lower())
    return text

# count unique words
def get_unique_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts

# File paths
file1_path = 'corpora/lovecraftSentences.txt'
file2_path = 'corpora/poeSentences.txt'

# Read texts
text1 = read_text(file1_path)
text2 = read_text(file2_path)

# Get word counts
word_counts1 = get_unique_words(text1)
word_counts2 = get_unique_words(text2)

# Find unique words
unique_words1 = {word: count for word, count in word_counts1.items() if word not in word_counts2}
unique_words2 = {word: count for word, count in word_counts2.items() if word not in word_counts1}

#  top 5 unique words from each text
top_unique_words1 = dict(sorted(unique_words1.items(), key=lambda item: item[1], reverse=True)[:5])
top_unique_words2 = dict(sorted(unique_words2.items(), key=lambda item: item[1], reverse=True)[:5])

# Combine data for visualization
labels = list(top_unique_words1.keys()) + list(top_unique_words2.keys())
sizes = list(top_unique_words1.values()) + list(top_unique_words2.values())

# Assign colors
colors = ['red', 'yellow', 'green', 'lightskyblue', 'purple', 'orange', 'blue', 'pink', 'cyan', 'brown']

# Highlight the most frequent word
pull = [0.1 if i == sizes.index(max(sizes)) else 0 for i in range(len(sizes))]

#  pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=pull, marker=dict(colors=colors))])

# Update layout and title
fig.update_layout(
    title="Top 5 Unique Word Frequency Comparison Between Two Texts",
    title_x=0.5,
    showlegend=True
)

# Show the plot
fig.show()

# Save  as an image
fig.write_image("docs/images/piegraph.png")

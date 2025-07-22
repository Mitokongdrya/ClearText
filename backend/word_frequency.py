import os
import re

# CONFIGURATION
COMMON_WORDS_PATH = os.path.join(os.path.dirname(__file__), "Common Words/common_words.txt")

# print(f"Loading common words from: {COMMON_WORDS_PATH}")

# Load common words into a set
def load_common_words():
    with open(COMMON_WORDS_PATH, "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f if word.strip())

# Tokenize and clean input text
def tokenize(text):
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())

# Calculate percentage of words in common list
def compute_common_word_percentage(text):
    common_words = load_common_words()
    words = tokenize(text)

    if not words:
        return 0.0

    match_count = sum(1 for word in words if word in common_words)
    percentage = (match_count / len(words)) * 100
    return round(percentage, 2)

# if __name__ == "__main__":
#     sample = "This is a sample sentence to test common word frequency."
#     print(f"Common word percentage: {compute_common_word_percentage(sample)}%")

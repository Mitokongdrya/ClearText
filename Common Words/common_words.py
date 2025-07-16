import os
import re
from collections import defaultdict

# CONFIGURATION
INPUT_DIR = "."  # Folder containing your .txt files
OUTPUT_FILE = "word_frequencies_grouped.txt"

# Clean and tokenize text
def tokenize(text):
    text = text.lower()
    return set(re.findall(r'\b[a-z]+\b', text))  # unique words per file

# Process all files to count file-level frequency of each word
def compute_word_file_frequencies(input_dir):
    word_file_counts = defaultdict(int)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                words_in_file = tokenize(f.read())
                for word in words_in_file:
                    word_file_counts[word] += 1

    return word_file_counts

# Categorize words by how many files they appear in
def categorize_frequencies(word_counts, total_files):
    categories = {
        f"Words in ALL {total_files} Files": [],
        f"Words in MOST Files ({total_files-1})": [],
        "Words in SOME Files (2+)": [],
        "Unique Words (1 file only)": []
    }

    for word, count in word_counts.items():
        if count == total_files:
            categories[f"Words in ALL {total_files} Files"].append((word, count))
        elif count == total_files - 1:
            categories[f"Words in MOST Files ({total_files-1})"].append((word, count))
        elif count >= 2:
            categories["Words in SOME Files (2+)"].append((word, count))
        else:
            categories["Unique Words (1 file only)"].append((word, count))

    return categories

# Write categorized results to file
def write_output(categories, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for category, words in categories.items():
            f.write(f"=== {category} ===\n")
            for word, count in sorted(words, key=lambda x: (-x[1], x[0])):
                f.write(f"{word}: {count}\n")
            f.write("\n")

def main():
    total_files = len([f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")])
    if total_files == 0:
        print("No .txt files found.")
        return

    word_counts = compute_word_file_frequencies(INPUT_DIR)
    categories = categorize_frequencies(word_counts, total_files)
    write_output(categories, OUTPUT_FILE)
    print(f"Categorized word report saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

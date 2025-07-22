import re
import sys

# Common forms of "to be"
TO_BE_VERBS = ["is", "am", "are", "was", "were", "be", "been", "being"]

# Basic list of past participle endings (can be improved with a lexicon)
PARTICIPLE_ENDINGS = ["ed", "en", "d", "t", "n"]

# Regex to match patterns like "was completed", "is managed", etc.
PASSIVE_PATTERN = re.compile(rf"\b({'|'.join(TO_BE_VERBS)})\b\s+(\w+ed|\w+en|\w+t|\w+n|\w+d)(\s+by\b.*)?", re.IGNORECASE)

def detect_passive_voice(text):
    passive_phrases = []
    lines = text.splitlines()
    
    for idx, line in enumerate(lines, 1):
        for match in PASSIVE_PATTERN.finditer(line):
            passive_phrases.append({
                "line": idx,
                "phrase": match.group(0).strip()
            })
    return passive_phrases

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python passive_voice.py input.txt")
        sys.exit(1)

    input_path = sys.argv[1]

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {input_path}")
        sys.exit(1)

    results = detect_passive_voice(content)
    if results:
        print("Passive voice phrases found:")
        for r in results:
            print(f"Line {r['line']}: {r['phrase']}")
    else:
        print("No passive voice phrases detected.")

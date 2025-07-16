import re
import textstat

# ------------------------------------------------------------
# 1. Cleaning utilities
# ------------------------------------------------------------
def clean_text(raw_text: str) -> str:
    """Normalise line‑breaks, spacing, bullets."""
    text = raw_text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'\n{2,}', '\n\n', text)           # collapse multiple blank lines
    text = re.sub(r'[ \t]+', ' ', text)              # collapse internal whitespace
    text = re.sub(r'(?<!\n)\n(?![\n•\-–\d])', ' ', text)  # join broken sentences
    text = re.sub(r'[\u2022\u25AA\u25CF\-–—]', '-', text) # normalise bullets
    return text.strip()

# ------------------------------------------------------------
# 2. Manual Flesch‑Reading‑Ease calculation
# ------------------------------------------------------------
def get_grade_level(flesch_score: float) -> str:
    score = max(0, flesch_score)           # floor at 0 to avoid negatives
    if score >= 90:   return "≈5th grade"
    if score >= 80:   return "≈6th grade"
    if score >= 70:   return "≈7th grade"
    if score >= 60:   return "≈8th‑9th grade"
    if score >= 50:   return "≈10th‑12th grade"
    if score >= 30:   return "College"
    return "College graduate"

def calculate_flesch_score(text: str):
    """Return (score, avg_words, avg_syllables, n_sent, n_words, grade_label)."""
    # retain sentence‑ending punctuation only
    text_clean = re.sub(r'[^\w\s\.\!\?]', '', text)

    sentences = textstat.sentence_count(text_clean)
    words      = textstat.lexicon_count(text_clean)
    syllables  = textstat.syllable_count(text_clean)

    avg_wps  = words / sentences if sentences else 0
    avg_spw  = syllables / words  if words else 0

    score = 206.835 - 1.015 * avg_wps - 84.6 * avg_spw
    score = max(0, score)     # floor at 0

    grade_label = get_grade_level(score)
    return score, avg_wps, avg_spw, sentences, words, grade_label

# ------------------------------------------------------------
# 3. Main driver
# ------------------------------------------------------------
def main():
    file_path = "pamphlet.txt"          # <- change if needed
    with open(file_path, encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_text(raw_text)

    # ------------------------- Method 1: textstat
    fk_grade = textstat.flesch_kincaid_grade(cleaned)
    fk_score = textstat.flesch_reading_ease(cleaned)

    # ------------------------- Method 2: manual
    (score, avg_wps, avg_spw,
     n_sent, n_words, grade_lbl) = calculate_flesch_score(cleaned)

    # ------------------------- Display
    print("=== Cleaned text preview (first 400 chars) ===")
    print(cleaned[:400] + ("…" if len(cleaned) > 400 else ""))
    print("\n\n=== Readability results ===")
    print("Method 1 – textstat")
    print(f"  Flesch Reading Ease : {fk_score:.2f}")
    print(f"  Flesch‑Kincaid Grade: {fk_grade:.2f}\n")

    print("Method 2 – manual formula")
    print(f"  Flesch Reading Ease : {score:.2f}")
    print(f"  Avg words / sentence: {avg_wps:.2f}")
    print(f"  Avg syllables / word: {avg_spw:.2f}")
    print(f"  Sentences            : {n_sent}")
    print(f"  Words                : {n_words}")
    print(f"  Estimated grade level: {grade_lbl}")

if __name__ == "__main__":
    main()

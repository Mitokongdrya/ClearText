from flask import Flask, request, jsonify, send_from_directory
import spacy
from flask_cors import CORS
import os

from extract_text import extract_text_from_pdf 
from readability_tool import clean_text, calculate_flesch_score
import textstat

app = Flask(__name__, static_folder='.')
CORS(app)

nlp = spacy.load("en_core_web_sm")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)  
    return jsonify({"text": extracted_text})

@app.route("/highlight", methods=["POST"])
def highlight_pos():
    data = request.json
    text = data.get("text", "")

    # Expanded POS color map
    pos_colors = {
        "ADJ": "yellow",         # Adjective
        "ADP": "#d3d3d3",        # Adposition (prepositions/subordinating conjunctions)
        "ADV": "lightpink",      # Adverb
        # "AUX": "#e0ffff",        # Auxiliary verbs
        "CONJ": "#f0e68c",       # Conjunction (coordinating)
        # "CCONJ": "#f0e68c",      # Coordinating conjunction
        # "DET": "#fffacd",        # Determiner
        "INTJ": "#dda0dd",       # Interjection
        "NOUN": "lightblue",     # Noun
        # "NUM": "#b0e0e6",        # Numeral
        # "PART": "#ffdab9",       # Particle
        "PRON": "orange",        # Pronoun
        "PROPN": "#bf2e5a",      # Proper noun
        # "PUNCT": "#ffffff",      # Punctuation (usually leave uncolored)
        # "SCONJ": "#f5deb3",      # Subordinating conjunction
        # "SYM": "#c0c0c0",        # Symbol
        "VERB": "lightgreen",    # Verb
        # "X": "#ffc0cb",          # Other, unknown
        # "SPACE": None            # Skip spaces
    }

    result = ""
    for token in nlp(text):
        color = pos_colors.get(token.pos_)
        if color:
            result += f'<span style="background-color: {color}">{token.text}</span>'
        else:
            result += token.text
        result += token.whitespace_

# Readability scoring
    cleaned_text = clean_text(text)

    # Method 1 – textstat
    score1 = textstat.flesch_reading_ease(cleaned_text)
    grade1 = textstat.flesch_kincaid_grade(cleaned_text)

    # Method 2 – manual
    score2, avg_wps, avg_spw, n_sent, n_words, grade_lbl = calculate_flesch_score(cleaned_text)

    return jsonify({
        "highlighted": result,
        "readability": {
            "method1": {
                "score": round(score1, 2),
                "grade_level": round(grade1, 2)
            },
            "method2": {
                "score": round(score2, 2),
                "avg_words_per_sentence": round(avg_wps, 2),
                "avg_syllables_per_word": round(avg_spw, 2),
                "sentences": n_sent,
                "words": n_words,
                "grade_level": grade_lbl
            }
        }
    })

if __name__ == "__main__":
    app.run(debug=True)

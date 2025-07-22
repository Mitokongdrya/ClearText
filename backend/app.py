from flask import Flask, request, jsonify
import spacy
from flask_cors import CORS

from extract_text import extract_text_from_pdf 
from readability_tool import clean_text, calculate_flesch_score
import textstat
from word_frequency import compute_common_word_percentage
from passive_voice import detect_passive_voice  # <-- NEW

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def serve_index():
    return app.send_static_file('index.html')

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    extracted_text = extract_text_from_pdf(file.stream)
    return jsonify({"text": extracted_text})

@app.route("/highlight", methods=["POST"])
def highlight_pos():
    data = request.json
    text = data.get("text", "")

    pos_colors = {
        "ADJ": "yellow",
        "ADP": "#d3d3d3",
        "ADV": "lightpink",
        "CONJ": "#f0e68c",
        "INTJ": "#dda0dd",
        "NOUN": "lightblue",
        "PRON": "orange",
        "PROPN": "#bf2e5a",
        "VERB": "lightgreen"
    }

    result = ""
    for token in nlp(text):
        color = pos_colors.get(token.pos_)
        if color:
            result += f'<span style="background-color: {color}">{token.text}</span>'
        else:
            result += token.text
        result += token.whitespace_

    # Readability calculations
    cleaned_text = clean_text(text)

    score1 = textstat.flesch_reading_ease(cleaned_text)
    grade1 = textstat.flesch_kincaid_grade(cleaned_text)

    score2, avg_wps, avg_spw, n_sent, n_words, grade_lbl = calculate_flesch_score(cleaned_text)

    common_pct = compute_common_word_percentage(text)

    # ✅ Detect passive voice
    passive_sentences = detect_passive_voice(text)

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
        },
        "common_word_percentage": common_pct,
        "passive_sentences": passive_sentences  # <-- NEW
    })

if __name__ == "__main__":
    app.run(debug=True)
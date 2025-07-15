from flask import Flask, request, jsonify, send_from_directory
import spacy
from flask_cors import CORS
import os

from extract_text import extract_text_from_pdf 

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

    pos_colors = {
        "ADJ": "yellow",
        "NOUN": "lightblue",
        "VERB": "lightgreen",
        "ADV": "lightpink",
        "PRON": "orange"
    }

    result = ""
    for token in nlp(text):
        color = pos_colors.get(token.pos_)
        if color:
            result += f'<span style="background-color: {color}">{token.text}</span>'
        else:
            result += token.text
        result += token.whitespace_

    return jsonify({"highlighted": result})

if __name__ == "__main__":
    app.run(debug=True)

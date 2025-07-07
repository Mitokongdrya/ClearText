from flask import Flask, request, jsonify, send_from_directory
import spacy
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)  # Allow all origins for development

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route("/highlight", methods=["POST"])
def highlight_pos():
    data = request.json
    text = data.get("text", "")
    print("Received text:", text)  # Debugging

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

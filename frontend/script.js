async function uploadPDF() {
  const fileInput = document.getElementById('pdfInput');
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a PDF file.");
    return;
  }

  const formData = new FormData();
  formData.append('pdf', file);

  try {
    const uploadRes = await fetch('/upload', {
      method: 'POST',
      body: formData
    });

    if (!uploadRes.ok) throw new Error("PDF upload failed");

    const uploadData = await uploadRes.json();
    const text = uploadData.text;
    highlightText(text);
  } catch (err) {
    alert("Error uploading PDF: " + err.message);
  }
}

async function highlightManualText() {
  const text = document.getElementById('manualText').value;
  if (!text.trim()) {
    alert("Please enter some text.");
    return;
  }
  highlightText(text);
}

async function highlightText(text) {
  try {
    const highlightRes = await fetch('/highlight', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    });

    if (!highlightRes.ok) throw new Error("Highlighting failed");

    const data = await highlightRes.json();

    // Show highlighted text
    document.getElementById('highlightedText').innerHTML = data.highlighted;

    // Readability info
    // const r1 = data.readability.method1;
    const r2 = data.readability.method2;

    let readabilityHTML = `
    <h3>Readability Analysis</h3>
      <ul>
        <li><strong>Flesch Reading Ease:</strong> ${r2.score}</li>
        <li><strong>Grade Level:</strong> ${r2.grade_level}</li>
        <li><strong>Avg words / sentence:</strong> ${r2.avg_words_per_sentence}</li>
        <li><strong>Avg syllables / word:</strong> ${r2.avg_syllables_per_word}</li>
        <li><strong>Total Sentences:</strong> ${r2.sentences}</li>
        <li><strong>Total Words:</strong> ${r2.words}</li>
      </ul>

      <h3>Common Word Usage</h3>
      <ul>
        <li><strong>% of words from common list:</strong> ${data.common_word_percentage}%</li>
      </ul>
    `;

    document.getElementById('readabilityInfo').innerHTML = readabilityHTML;

    const passiveInfo = data.passive_sentences;
    let passiveHTML = `
    <h3>Passive Voice Detection</h3>
    <ul>
      <li><strong>Passive constructions found:</strong> ${passiveInfo.length}</li>
    </ul>
  `;

    if (passiveInfo.length > 0) {
      passiveHTML += `<p><strong>Examples:</strong></p><ul>`;
      passiveInfo.forEach(item => {
        passiveHTML += `<li>Line ${item.line}: ${item.phrase}</li>`;
      });
      passiveHTML += `</ul>`;
    }

    document.getElementById('passiveVoiceInfo').innerHTML = passiveHTML;


  } catch (err) {
    alert("Error highlighting text: " + err.message);
  }
}

//DEFINITION POPUP
async function showDefinitionPopup(word) {
  try {
    const res = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
    if (!res.ok) throw new Error("Not found");

    const data = await res.json();
    const definition = data[0].meanings[0].definitions[0].definition;

    displayPopup(word, definition);
  } catch (err) {
    displayPopup(word, "Definition not found.");
  }
}

function displayPopup(word, definition) {
  // Remove existing popup
  const oldPopup = document.getElementById("definitionPopup");
  if (oldPopup) oldPopup.remove();

  const popup = document.createElement("div");
  popup.id = "definitionPopup";
  popup.innerHTML = `<strong>${word}</strong>: ${definition}`;
  popup.style.position = "absolute";
  popup.style.backgroundColor = "#fffffa";
  popup.style.border = "1px solid #ccc";
  popup.style.padding = "8px 12px";
  popup.style.borderRadius = "8px";
  popup.style.boxShadow = "0 2px 12px rgba(0,0,0,0.2)";
  popup.style.fontSize = "14px";
  popup.style.maxWidth = "300px";
  popup.style.zIndex = "1000";

  const selection = window.getSelection();
  if (selection.rangeCount === 0) return;

  const range = selection.getRangeAt(0);
  const rect = range.getBoundingClientRect();

  popup.style.top = `${window.scrollY + rect.top - 50}px`;
  popup.style.left = `${window.scrollX + rect.left}px`;

  document.body.appendChild(popup);

  // Remove after 5 seconds or if clicked
  setTimeout(() => popup.remove(), 5000);
  popup.addEventListener("click", () => popup.remove());
}

document.addEventListener('mouseup', async function () {
  const selectedText = window.getSelection().toString().trim();
  if (selectedText && selectedText.split(" ").length === 1) {
    showDefinitionPopup(selectedText.toLowerCase());
  }
});
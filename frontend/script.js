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
  
      document.getElementById('highlightedText').innerHTML = data.highlighted;
  
      const r1 = data.readability.method1;
      const r2 = data.readability.method2;
  
      document.getElementById('readabilityInfo').innerHTML = `
        <h3>Readability Scores</h3>
        <h4>Method 1: textstat</h4>
        <ul>
          <li><strong>Flesch Reading Ease:</strong> ${r1.score}</li>
          <li><strong>Flesch-Kincaid Grade:</strong> ${r1.grade_level}</li>
        </ul>
  
        <h4>Method 2: Manual Formula</h4>
        <ul>
          <li><strong>Flesch Reading Ease:</strong> ${r2.score}</li>
          <li><strong>Grade Level:</strong> ${r2.grade_level}</li>
          <li><strong>Avg words / sentence:</strong> ${r2.avg_words_per_sentence}</li>
          <li><strong>Avg syllables / word:</strong> ${r2.avg_syllables_per_word}</li>
          <li><strong>Total Sentences:</strong> ${r2.sentences}</li>
          <li><strong>Total Words:</strong> ${r2.words}</li>
        </ul>
      `;
    } catch (err) {
      alert("Error highlighting text: " + err.message);
    }
  }
  
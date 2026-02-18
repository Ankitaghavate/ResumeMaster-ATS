# ResumeMaster — AI Resume Screening & Job Role Recommendation System

An AI-powered web application that **analyzes resumes**, predicts suitable job roles, performs **skill gap analysis**, detects experience level, identifies spelling mistakes, provides resume improvement suggestions, and includes a **chatbot assistant** for guidance.

---

## 🎯 Objective

Design and develop an end-to-end AI-based Resume Screening System with a Chatbot Assistant that:

- Automatically analyzes resumes and predicts suitable job roles
- Provides actionable insights for resume improvement
- Assists users interactively through an AI-powered chatbot

---

## ❗ Problem Statement

Manual resume screening and candidate guidance are:

- Time-consuming and inconsistent
- Error-prone for recruiters
- Lacking in actionable feedback for applicants, such as:
  - Skill gaps
  - Role alignment
  - Resume quality issues
  - Experience level detection
  - Guidance through questions via chatbot

---

## 💡 Proposed Solution

**ResumeMaster** provides an intelligent platform that:

- Accepts resumes in PDF, DOCX, and TXT formats
- Extracts and cleans resume text using NLP
- Predicts the most suitable job role using TF-IDF + Logistic Regression
- Shows **Top 3 role recommendations** with confidence scores
- Matches candidate skills with job requirements and highlights missing skills
- Detects spelling mistakes and suggests corrections
- Identifies experience level (Fresher / Junior / Mid / Senior)
- Provides a **chatbot assistant** for resume and career guidance

---

## 🔄 System Workflow

1. **Resume Screening:**
   - Upload resume → Extract text → Preprocess → Convert to TF-IDF → Predict job role → Generate:
     - Predicted job role
     - Top 3 role recommendations
     - Matched & missing skills
     - Spelling mistakes and suggestions
     - Experience level classification
     - Resume improvement suggestions

2. **Chatbot Assistance:**
   - User interacts with chatbot
   - Chatbot answers questions on resume improvement, skill building, career guidance
   - Powered by AI with NLP and retrieval-augmented knowledge

---

## 🧠 Machine Learning & NLP Techniques

**Resume Screening:**
- Text preprocessing (regex cleaning, normalization)
- TF-IDF Vectorization
- Logistic Regression classifier
- Skill extraction via keyword matching
- Spelling correction using TextBlob or SymSpell
- Optional NLP improvements using NLTK or spaCy

**Chatbot:**
- Large Language Model (LLM) / GPT-style
- Retrieval-Augmented Generation (RAG) for real-time guidance
- Vector embeddings stored in FAISS or similar for semantic search
- Context-aware responses and multi-turn conversations

---

## 🛠️ Tech Stack

**Backend:**
- Python
- Flask (web app)
- scikit-learn
- NLTK / TextBlob / spaCy
- PDFMiner / pdfplumber (PDF parsing)
- python-docx (DOCX parsing)
- Pandas & NumPy

**Frontend:**
- HTML, CSS, JavaScript
- Bootstrap or TailwindCSS for styling

**Chatbot:**
- Python (Flask API)
- FAISS vector database
- OpenAI GPT / LLM integration for query responses

**Other Tools:**
- Git & GitHub for version control
- Optional: pdfkit for generating downloadable PDF reports

---

## ⭐ Key Features

- Multi-format resume upload (PDF, DOCX, TXT)
- Automated resume text extraction & cleaning
- Job role prediction (Logistic Regression)
- Top 3 role recommendations with confidence scores
- Matched & missing skills (skill gap analysis)
- Experience level detection
- Spelling mistake detection & suggestions
- Resume improvement tips
- **Chatbot assistant for guidance and Q&A**
- Downloadable resume analysis report (PDF)

---

## 📊 Expected Output

- Predicted job role
- Top 3 role recommendations with confidence
- Matched & missing skills
- Experience level classification
- Spelling mistakes and suggestions
- Resume improvement insights
- Interactive chatbot assistance

---

## 🚀 Quick Start — Clone & Run

1. Clone the repository:
```bash
git clone https://github.com/Ankitaghavate/ResumeMaster-ATS.git
cd ResumeMaster-ATS


2. Create a virtual environment (recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the Flask application
```bash
python app.py
```

5. Open in your browser
```
http://127.0.0.1:5000/
```

---

## 🌐 Live Demo

A demo may be available at: https://resume-master--ank26.replit.app

---

## 📦 Files of Interest

- `app.py` — Flask application entrypoint
- `best_model.pkl` — Trained Logistic Regression model
- `tfidf.pkl` — TF-IDF vectorizer used for feature extraction
- `label_encoder.pkl` — Label encoder for job roles
- `AI_Resume_Screening.ipynb` — Notebook used for data exploration and model training
- `UpdatedResumeDataSet.csv` — Dataset used for training

---

## 📝 Notes & Recommendations

- Ensure the pretrained model and vectorizer files (`best_model.pkl`, `tfidf.pkl`, `label_encoder.pkl`) are present in the repo root.
- For production deployment, consider:
  - Using a proper WSGI server (Gunicorn / uWSGI)
  - Packaging models or loading them from secure storage
  - Adding rate-limiting and authentication for the API
  - Improving parsing for complex resume formats (tables, images)
  - Using a more advanced spell-checker or contextual model for suggestions

---

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, improvements, or feature requests.

Suggested workflow:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-change`
3. Commit changes: `git commit -m "Add my feature"`
4. Push and open a PR

---

## 📄 License

Specify your license here (e.g., MIT). Add a LICENSE file to the repository.

---

## 📫 Contact

For questions, feature requests, or help, open an issue or contact the repository owner: [Ankitaghavate](https://github.com/Ankitaghavate)

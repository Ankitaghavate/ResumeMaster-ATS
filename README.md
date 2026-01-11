# ResumeMaster — AI Resume Screening & Job Role Recommendation System

An AI-powered web application that analyzes resumes and predicts the most suitable job role using Logistic Regression, performs skill gap analysis, detects experience level, identifies spelling mistakes, and provides resume improvement suggestions.

---

## 🎯 Objective

Design and develop an end-to-end AI-based Resume Screening System that automatically analyzes resumes and predicts suitable job roles using Natural Language Processing (NLP) and Logistic Regression, while providing actionable insights for resume improvement.

---

## ❗ Problem Statement

Manual resume screening is time-consuming, inconsistent, and error-prone. Recruiters struggle to shortlist candidates efficiently, and applicants often lack clear feedback on:

- Skill gaps
- Role alignment
- Resume quality issues
- Spelling errors

---

## 💡 Proposed Solution

ResumeMaster provides an intelligent resume analysis platform that:

- Accepts resumes in PDF, DOCX, and TXT formats
- Extracts and cleans resume text using NLP
- Predicts the most suitable job role using TF-IDF + Logistic Regression
- Shows Top 3 role recommendations with confidence scores
- Matches candidate skills with job requirements and highlights missing skills
- Detects spelling mistakes and suggests corrections
- Identifies experience level (Fresher / Junior / Mid / Senior)

---

## 🔄 System Workflow

1. Upload resume
2. Extract text from document
3. Clean and preprocess text
4. Convert text to numerical form using TF-IDF
5. Predict job role using Logistic Regression
6. Generate:
   - Predicted job role
   - Top 3 role recommendations with confidence
   - Matched & missing skills
   - Spelling error highlights
   - Experience level classification
   - Resume improvement suggestions

---

## 🧠 Machine Learning & NLP Techniques

- Text preprocessing (regex cleaning, normalization)
- TF-IDF Vectorization
- Logistic Regression classifier
- Skill extraction via keyword matching
- Spelling correction using TextBlob
- (Optional) Additional NLP improvements using NLTK or spaCy

---

## 🛠️ Tech Stack

- Python
- Flask (web app)
- scikit-learn
- NLTK / TextBlob
- PDFMiner (or pdfplumber) for PDF text extraction
- python-docx for DOCX parsing
- Pandas & NumPy
- HTML, CSS (frontend)

---

## ⭐ Key Features

- Multi-format resume upload (PDF, DOCX, TXT)
- Automated resume text extraction & cleaning
- Job role prediction (Logistic Regression)
- Top 3 role recommendations with confidence scores
- Matched & missing skills list (skill gap analysis)
- Experience level detection
- Spelling mistake detection & suggestions
- Resume improvement tips
- Web-based interface

---

## 📊 Expected Output

- Predicted job role
- Top 3 role recommendations with confidence
- Matched & missing skills
- Experience level classification
- Spelling mistakes and suggestions
- Resume improvement insights

---

## 📁 Project Folder Structure

ResumeMaster-AI/
│
├── app.py
├── requirements.txt
├── best_model.pkl
├── tfidf.pkl
├── label_encoder.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── AI_Resume_Screening.ipynb
└── UpdatedResumeDataSet.csv

---

## 🚀 Quick Start — Clone & Run

1. Clone the repository
```bash
git clone https://github.com/Ankitaghavate/ResumeMaster-ATS.git
cd ResumeMaster-ATS
```

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

A demo may be available at: https://resumemaster-ai.onrender.com  
(Free hosting — may sleep after inactivity)

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

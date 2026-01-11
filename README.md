📄 ResumeMaster – AI Resume Screening & Job Role Recommendation System

An AI-powered web application that analyzes resumes, predicts the most suitable job role using Logistic Regression, performs skill gap analysis, detects experience level, identifies spelling mistakes, and provides resume improvement suggestions.

🎯 Objective

To design and develop an end-to-end AI-based Resume Screening System that automatically analyzes resumes and predicts suitable job roles using Natural Language Processing (NLP) and Logistic Regression, while providing actionable insights for resume improvement.

❗ Problem Statement

Manual resume screening is time-consuming, inconsistent, and error-prone.
Recruiters struggle to shortlist candidates efficiently, and applicants lack clear feedback on:

Skill gaps

Role alignment

Resume quality issues

Spelling errors

💡 Proposed Solution

The system provides an intelligent resume analysis platform that:

Accepts resumes in PDF, DOCX, and TXT formats

Extracts and cleans resume text using NLP

Predicts the most suitable job role using:

TF-IDF + Logistic Regression

Displays Top 3 role recommendations with confidence scores

Matches candidate skills with job requirements

Highlights missing skills

Detects spelling mistakes

Identifies experience level (Fresher / Junior / Mid / Senior)

🔄 System Workflow

Upload resume

Extract text from document

Clean and preprocess text

Convert text to numerical form using TF-IDF

Predict job role using Logistic Regression

Generate:

Predicted job role

Top 3 role recommendations

Matched skills

Missing skills

Spelling errors

Experience level

🧠 Machine Learning & NLP Techniques

Text preprocessing (regex cleaning, normalization)

TF-IDF Vectorization

Logistic Regression classification

Skill extraction using keyword matching

Spelling correction using TextBlob

🛠️ Tech Stack

Python

Flask

Scikit-learn

NLTK / TextBlob

PDFMiner

python-docx

Pandas & NumPy

HTML, CSS

⭐ Key Features

Multi-format resume upload

Automated resume text extraction

Job role prediction (Logistic Regression)

Top 3 role recommendations

Skill gap analysis

Experience detection

Spelling mistake detection

Web-based interface

📊 Expected Output

Predicted job role

Top 3 role recommendations with confidence

Matched & missing skills list

Resume improvement insights

Experience level classification

📁 Project Folder Structure
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

🚀 How to Clone and Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/ResumeMaster-AI.git
cd ResumeMaster-AI

2️⃣ Create Virtual Environment (Recommended)
python -m venv myenv
myenv\Scripts\activate     # Windows
# source myenv/bin/activate  # Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

🌐 Live Demo

🔗 https://resumemaster-ai.onrender.com

(Free hosting – may sleep after inactivity)

🎓 Project Outcome

A production-ready AI Resume Screening System that:

Improves recruitment efficiency

Helps candidates optimize resumes

Provides data-driven career insights

Uses a reliable and interpretable ML model

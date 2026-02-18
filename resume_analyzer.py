import re
import pickle
import numpy as np
import nltk
from pdfminer.high_level import extract_text
import docx

nltk.download('punkt', quiet=True)

# ---------------- Load Models ----------------
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# ---------------- Safety Check ----------------
EXPECTED_FEATURES = model.coef_.shape[1]
TFIDF_FEATURES = len(tfidf.vocabulary_)

if EXPECTED_FEATURES != TFIDF_FEATURES:
    raise ValueError(
        f"TF-IDF features ({TFIDF_FEATURES}) != Model expects ({EXPECTED_FEATURES})"
    )

# Fix NotFittedError
if not hasattr(tfidf, 'idf_'):
    tfidf._tfidf.idf_ = np.ones(len(tfidf.vocabulary_))

# ---------------- Text Cleaning ----------------


def clean_text(text):
    text = re.sub('http\S+', ' ', str(text))
    text = re.sub('@\S+', ' ', text)
    text = re.sub('[^a-zA-Z ]', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text.lower().strip()

# ---------------- Experience Detection ----------------


def detect_experience(text):
    text = text.lower()
    if "intern" in text or "fresher" in text:
        return "Fresher"
    match = re.search(r'(\d+)\+?\s*(years|yrs)', text)
    if match:
        y = int(match.group(1))
        if y <= 2:
            return "Junior"
        elif y <= 5:
            return "Mid-Level"
        else:
            return "Senior"
    return "Not Mentioned"


# ---------------- Skill Analysis ----------------

# ---------------- Role → Skills ----------------
ROLE_SKILLS = {
    "Java Developer": ["Java", "Spring", "Spring Boot", "Hibernate", "JPA", "REST API", "Microservices", "SQL", "Git", "Maven"],
    "Testing": ["Manual Testing", "Test Cases", "SDLC", "STLC", "Bug Tracking", "JIRA", "Regression Testing"],
    "Automation Testing": ["Selenium", "Java", "Python", "TestNG", "JUnit", "Postman", "API Testing", "JIRA"],
    "DevOps Engineer": ["AWS", "Docker", "Kubernetes", "Jenkins", "CI/CD", "Linux", "Ansible", "Terraform"],
    "Python Developer": ["Python", "Django", "Flask", "REST API", "SQL", "Git", "OOPs"],
    "Web Designing": ["HTML", "CSS", "JavaScript", "Bootstrap", "UI Design", "Responsive Design", "Figma"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Express", "MongoDB", "Git"],
    "HR": ["Recruitment", "Onboarding", "Payroll", "HR Policies", "Employee Engagement", "Performance Management"],
    "Hadoop": ["Hadoop", "HDFS", "MapReduce", "Hive", "Pig", "Spark", "YARN"],
    "Sales": ["Sales Strategy", "Lead Generation", "CRM", "Negotiation", "Customer Handling", "Market Analysis"],
    "Data Science": ["Python", "Machine Learning", "Deep Learning", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Tableau"],
    "Mechanical Engineer": ["AutoCAD", "SolidWorks", "Manufacturing", "Maintenance", "Thermodynamics", "Production Planning"],
    "ETL Developer": ["ETL", "Informatica", "Data Warehousing", "SQL", "Data Mapping", "Data Validation"],
    "Blockchain": ["Blockchain", "Ethereum", "Solidity", "Smart Contracts", "Web3", "Cryptography"],
    "Operations Manager": ["Operations Management", "Process Improvement", "Supply Chain", "Inventory Management", "Project Management"],
    "Arts": ["Creative Writing", "Content Creation", "Visual Arts", "Design", "Communication"],
    "Database": ["SQL", "MySQL", "PostgreSQL", "Oracle", "Database Design", "Query Optimization"],
    "Health and fitness": ["Fitness Training", "Nutrition", "Workout Planning", "Health Assessment", "Personal Training"],
    "PMO": ["Project Management", "MS Project", "Risk Management", "Documentation", "Stakeholder Management"],
    "Electrical Engineering": ["Power Systems", "PLC", "SCADA", "Electrical Machines", "Circuit Design", "Wiring"],
    "Business Analyst": ["Requirement Analysis", "SQL", "Power BI", "Excel", "Data Analysis", "Documentation"],
    "DotNet Developer": [".NET", "C#", "ASP.NET", "MVC", "Entity Framework", "SQL Server"],
    "Network Security Engineer": ["Network Security", "Firewalls", "IDS/IPS", "Cyber Security", "VPN", "Ethical Hacking"],
    "Civil Engineer": ["AutoCAD", "Revit", "Construction Planning", "Estimation", "Site Engineering", "Building Design"],
    "SAP Developer": ["SAP ABAP", "SAP HANA", "SAP FICO", "SAP MM", "SAP SD"],
    "Advocate": ["Legal Research", "Drafting", "Court Proceedings", "Contracts", "Litigation", "Legal Compliance"]
}


def get_insights(text, skills):
    matched = [s for s in skills if s.lower() in text.lower()]
    missing = [s for s in skills if s.lower() not in text.lower()]
    return matched, missing

# ---------------- ML Prediction ----------------


def predict_role(resume_text):
    cleaned = clean_text(resume_text)
    vector = tfidf.transform([cleaned])
    probs = model.predict_proba(vector)[0]
    top3_idx = probs.argsort()[-3:][::-1]
    top_roles = [(le.inverse_transform([i])[0], round(
        float(probs[i]*100), 2)) for i in top3_idx]
    predicted_role = top_roles[0][0]
    target_skills = ROLE_SKILLS.get(predicted_role, [])
    matched, missing = get_insights(resume_text, target_skills)
    experience = detect_experience(resume_text)
    return {
        "predicted_role": predicted_role,
        "top_roles": top_roles,
        "matched": matched,
        "missing": missing,
        "experience": experience
    }

# ---------------- Resume Text Extraction ----------------


def extract_text_from_file(file, ext):
    if ext == "txt":
        return file.read().decode("utf-8", errors="ignore")
    elif ext == "docx":
        doc = docx.Document(file.stream)
        return "\n".join(p.text for p in doc.paragraphs)
    elif ext == "pdf":
        from io import BytesIO
        return extract_text(BytesIO(file.read()))
    else:
        raise ValueError("Unsupported file type")

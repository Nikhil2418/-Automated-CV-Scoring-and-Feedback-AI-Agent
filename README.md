# 🤖 Automated CV Scoring and Feedback AI Agent

This project automates the process of **evaluating resumes (CVs)** against **job descriptions (JDs)** using NLP techniques and machine learning. The system scores how well a CV matches a JD and optionally generates feedback, helping recruiters filter candidates faster.

---

## 🚀 Features

- 📄 Extracts key details from resumes (skills, experience, education, etc.)
- 📝 Compares CVs against job descriptions using semantic similarity
- 📊 Generates a score representing match level
- 📬 Optional email feedback system for candidates
- 🔄 Supports both **batch mode** and **interactive app mode**
- 💾 Logs scoring and feedback results

---

## 📁 Project Structure

Automated-CV-Scoring-and-Feedback-AI-Agent/
│
├── app.py # Main application script (Flask or CLI-based)
├── batch_runner.py # Script to run batch CV scoring
├── config.py # Configuration settings (paths, thresholds)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Files/folders excluded from Git
│
├── Utils/ # Helper functions (e.g., parsing, NLP)
├── emailer/ # Email automation module
├── logs/ # Stores logs for audit and debugging
├── samples/ # Sample CVs and job descriptions
├── scoring/ # Core logic for scoring and feedback generation


---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Natural Language Processing (NLP)** with spaCy / NLTK / transformers
- **Similarity models**: TF-IDF, BERT (optional)
- **Flask** (if running as a web app)
- **SMTP** for email integration

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikhil2418/automated-cv-scoring.git
   cd automated-cv-scoring

---

Would you like a downloadable `.md` file or help generating a `requirements.txt` file based on your current environment? 😊

# FakeBankAppScan

| Day   | Focus Area              | Key Deliverables                        |
|-------|-------------------------|------------------------------------------|
| Day 1 | Research & Architecture | System design, data collection strategy  |
| Day 2 | Data Collection & Setup | Legitimate/fake APK samples, basic framework |
| Day 3 | Static Analysis Engine  | APK parsing, metadata extraction         |
| Day 4 | Detection Algorithm     | ML model, rule-based detection           |
| Day 5 | Integration & Testing   | Working prototype, accuracy testing      |
| Day 6 | UI/Demo & Validation    | User interface, final testing            |
| Day 7 | PPT & Documentation     | Presentation, submission preparation     |


# 📂 Suggested Project Structure for APK Malware Detection

Based on the **7-day project plan**, here’s the recommended directory structure for the GitHub repository.  
This setup organizes the project logically around key focus areas (e.g., data collection, analysis, detection, and documentation) while following standard Python project conventions.

---

## 🌳 Project Structure (Tree View)


---

## 🏗 Root Directory
- **README.md** → Project overview, setup instructions, summary of 7-day plan.  
- **requirements.txt** → Dependencies (e.g., scikit-learn, androguard).  
- **.gitignore** → Ignore temp files, datasets, venv.  
- **LICENSE** → Open-source license (MIT, etc.).  

---

## 📁 Main Folders

### `src/` → Core Source Code
- **data_collection/** → Scripts for APK sample gathering (Day 2).  
- **static_analysis/** → APK parsing & metadata extraction (Day 3).  
- **detection/** → ML models & detection logic (Day 4).  
- **integration/** → Tie everything into a prototype (Day 5).  
- **ui/** → User interface (CLI/app demo) (Day 6).  
- **main.py** → Entry point.  

### `data/` → Dataset Storage
- **samples/** → APK files (legit + fake).  
- **processed/** → Extracted metadata/features.  
- **models/** → ML-related files.  
  - **trained_models/** → Saved ML models (.pkl).  

### `notebooks/` → Jupyter notebooks for prototyping.  

### `tests/` → Unit & Integration Tests
- **test_static_analysis.py**  
- **test_detection.py**  
- **test_integration.py**  

### `docs/` → Documentation & Reports
- **architecture.md** → System design notes (Day 1).  
- **presentation.pptx** → Final presentation (Day 7).  
- **report.md** → Project report & results (Day 5–6).  

---

## 🚀 Getting Started on GitHub

1. **Create a new repository** on GitHub.  
2. Initialize your local project:
   ```bash
   git init

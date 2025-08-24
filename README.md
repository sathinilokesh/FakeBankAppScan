# 🔒 FakeBankAppScan

FakeBankAppScan is a comprehensive cybersecurity tool designed to detect **fake banking APKs** using advanced static analysis and machine learning. Developed to support **law enforcement agencies** in cybercrime investigations, it delivers fast, reliable, and **court-admissible results**.

---

## ✨ Key Features

- 🛡️ **Certificate Validation** – Verifies app signing certificates against legitimate banking signatures  
- 🔍 **App Name Similarity Detection** – Flags typo-squatting and impersonation using string matching algorithms  
- ⚠️ **Permission Pattern Analysis** – Detects dangerous permission combinations commonly abused by malicious apps  
- 📦 **Package Name Verification** – Cross-checks against databases of trusted banking applications  
- 🤖 **Machine Learning Classification** – Trained models detect fake apps with high accuracy  
- ⚡ **Batch Processing** – Analyze multiple APKs in one go  
- 📋 **Evidence Management** – Tracks chain of custody for digital evidence  
- 📊 **Detailed Reporting** – Court-admissible investigation reports  
- 🌐 **Threat Intelligence Correlation** – Maps detections to known malware families and campaigns  

---

## 🏗️ Project Structure

```
FakeBankAppScan/
├── docs/                     # Documentation and presentations
├── LICENSE                   # Project license
├── README.md                 # Project overview and instructions
├── requirements.txt          # Python dependencies
├── src/
│   ├── app.py                # Main Streamlit entry point
│   ├── core/                 # APK analysis engine
│   │   ├── apk_analyzer.py
│   │   ├── certificate_validator.py
│   │   ├── permission_analyzer.py
│   │   ├── similarity_checker.py
│   │   ├── ml_detector.py
│   │   └── risk_calculator.py
│   ├── interface/            # Frontend + system integration
│   │   ├── streamlit_app.py
│   │   ├── database_manager.py
│   │   ├── report_generator.py
│   │   ├── batch_processor.py
│   │   └── api_endpoints.py
│   ├── data/
│   │   ├── legitimate_apps/
│   │   ├── test_samples/
│   │   ├── databases/
│   │   └── models/
│   ├── reports/              # Templates + output
│   ├── utils/                # Helpers and configs
│   └── scripts/              # Setup and maintenance scripts
└── tests/                    # Unit and integration tests
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip`
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sathinilokesh/FakeBankAppScan.git
   cd FakeBankAppScan
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up folders and databases:**
   ```bash
   mkdir -p src/data/legitimate_apps src/data/test_samples src/data/databases src/data/models
   mkdir -p src/reports/templates src/reports/generated

   python src/scripts/setup_database.py
   ```

5. **Add APKs:**

   Download legitimate banking APKs from trusted sources (e.g., APKMirror, APKPure).  
   Place them in:

   ```
   src/data/legitimate_apps/
   ```

6. **Launch the application:**
   ```bash
   streamlit run src/app.py
   ```

   Access it at [http://localhost:8501](http://localhost:8501)

---

## 📊 Technical Specifications

| Metric                    | Value                            |
|--------------------------|----------------------------------|
| ⏱️ Analysis Speed        | <30s per APK                     |
| 🎯 Detection Accuracy     | >90% on validated datasets       |
| ❌ False Positive Rate    | <5% for legit banking apps       |
| 🔄 Concurrent Processing  | 10+ APKs at once supported       |

### ⚙️ Tech Stack

- **Backend**: Python, Androguard, scikit-learn  
- **Frontend**: Streamlit, HTML/CSS  
- **Database**: SQLite (dev), PostgreSQL (prod)  
- **ML**: scikit-learn, pandas, numpy  
- **Reports**: ReportLab, Jinja2  

### 🔐 Security

- Sandboxed APK analysis  
- No dynamic code execution  
- Secure evidence storage with audit trails  
- Chain-of-custody documentation  
- GDPR-compliant data handling  

---

## 🎯 Use Cases

- 👮 **Law Enforcement**: Investigate fake banking apps from victims’ devices  
- 🏦 **Banking Security Teams**: Proactively monitor for brand abuse  
- 🧠 **Cybersecurity Researchers**: Analyze malware trends  
- 📱 **App Stores**: Auto-screen submitted APKs  

---

## 📋 Requirements

See `requirements.txt` for full list. Key dependencies:

- `streamlit` – Web interface  
- `androguard` – APK analysis  
- `scikit-learn` – ML classifiers  
- `pandas`, `numpy` – Data wrangling  
- `pillow` – Image/icon analysis  
- `python-levenshtein` – String similarity  

---

## 🤝 Contributing

1. Fork the repo  
2. Create a branch: `git checkout -b feature/your-feature`  
3. Commit: `git commit -am "Add your feature"`  
4. Push: `git push origin feature/your-feature`  
5. Open a Pull Request  

---

## 📄 License

Licensed under the [MIT License](LICENSE)

---

## 🏆 Acknowledgments

Developed for **National CyberShield Hackathon 2025** – Problem Statement 06: Detecting Fake Banking APKs

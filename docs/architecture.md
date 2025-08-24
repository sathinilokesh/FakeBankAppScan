# 1. High-Level Component Diagram (Mermaid)

┌────────────┐        ┌─────────────────┐        ┌────────────────┐
│  Data Src  │ ──►    │ Ingestion &     │ ──►    │  Raw Storage   │
│  (APKs)    │        │ Pre-processing  │        │   (Object DB)  │
└────────────┘        └─────────────────┘        └────────────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │ Feature Store  │
                     └────────────────┘
                             │
    ┌────────────┐           ▼            ┌──────────────┐
    │ Static     │──feature──┬──────────► │ ML Service / │
    │ Analysis   │           │            │ Rule Engine  │
    └────────────┘           │            └──────────────┘
                             ▼
                     ┌────────────────┐
                     │ Results API    │
                     └────────────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │ UI / CLI Tool  │
                     └────────────────┘




---

# 2. Core Building Blocks

| Layer                  | Purpose                                   | Key Tech Choices (Fast-track)                                                                 | Notes                                                                 |
|-------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **1. Data Sources**     | Acquire benign & malicious APKs.          | - Public datasets: AndroZoo, VirusShare<br>- Your in-house apps                                | Use dataset metadata (e.g., SHA-256, VT labels) for ground truth.     |
| **2. Ingestion & Pre-processing** | Download, verify hash, tag with label, push to storage. | Python scripts + requests + tqdm                                                               | Keep a manifest JSON/CSV for traceability.                           |
| **3. Raw Storage**      | Persist original APKs & metadata.         | S3 bucket or local MinIO; fallback: filesystem                                                 | Folder structure: `/raw/{benign...}`                                 |
| **4. Static Analysis Engine** | Extract features without executing code. | Androguard; apktool (shell); custom Python                                                     | Pull: Manifest permissions, API call strings, byte-code n-grams, cert info. |
| **5. Feature Store**    | Persist compact, queryable feature vectors. | SQLite (quick) or Parquet files; use pandas for I/O                                            | Schema: `sha256 TEXT PRIMARY KEY, label INT, features BLOB/JSON`.    |
| **6. Detection Service**| Classify APK as benign/malicious.         | - ML: scikit-learn RandomForest, XGBoost<br>- Rule engine: simple heuristics                   | Start with ML pipeline in Jupyter; export pickled model behind REST service (Flask/FastAPI). |
| **7. Results API**      | Expose prediction & confidence.           | FastAPI (auto Swagger docs)                                                                    | Endpoint: `POST /scan` with APK file or sha256.                      |
| **8. UI / CLI**         | Human-friendly interface & demo.          | - CLI: Click library<br>- Web: React or minimal Flask-Jinja template                           | Show scan logs, verdict, feature importance chart.                   |

# 🛡️ If Insurance: Risk-Intelligence Engine
**End-to-End Automated Fraud Detection Pipeline**

## 🚀 Project Overview
This project delivers a high-impact solution for automating insurance claim audits. By leveraging machine learning, it identifies high-risk claims with a focus on maximizing ROI and reducing manual overhead for insurance providers.

### 📈 Key Impact (Simulated on 5,000 cases)
- **Total Recovery Potential:** 7,151,977 SEK
- **Model Precision:** 97% (Fraud Class)
- **Model Recall:** 78% (Fraud Class)
- **Processing Time:** < 5 seconds per 1k records

## 🛠 Tech Stack
- **Data Engineering:** Python, Pandas, Faker (Synthetic Data Gen)
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Automation:** Python SMTP-Lib, .env Security
- **Reporting:** FPDF (Executive Summary Automation)

## 📁 Repository Structure
- `data_generation.py`: Custom synthetic data engine mimicking insurance fraud patterns.
- `model_training.py`: ML pipeline for anomaly detection.
- `final_report.py`: Automated PDF generator and email dispatcher.
- `run_pipeline.bat`: One-click execution for the entire workflow.

## ⚙️ Setup & Execution
1. Clone the repo.
2. Create a `.venv` and run `pip install -r requirements.txt`.
3. Configure your `.env` file with credentials.
4. Run `run_pipeline.bat` to execute the full data-to-inbox pipeline.

---
*Created by Lily - The Data Translator*

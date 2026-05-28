# 🔍 Fraud Detection App

![PYTHON](https://img.shields.io/badge/PYTHON-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![STREAMLIT](https://img.shields.io/badge/STREAMLIT-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SCIKIT--LEARN](https://img.shields.io/badge/SCIKIT--LEARN-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![PANDAS](https://img.shields.io/badge/PANDAS-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![ML MODEL](https://img.shields.io/badge/ML-MODEL-green?style=for-the-badge)

> A machine learning web application built with Streamlit that predicts whether a financial transaction is **fraudulent or legitimate** — powered by a trained ML model on 6M+ real transaction records.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Author](#-author)

---

## ✨ Features

- 🔎 Predicts fraud in real-time based on transaction details
- 💳 Supports 5 transaction types: `PAYMENT`, `TRANSFER`, `CASH_OUT`, `CASH_IN`, `DEPOSIT`
- 📊 Takes sender & receiver balance into account
- ✅ Clean and simple Streamlit UI
- ⚡ Instant prediction with a single click

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Streamlit | Web UI framework |
| Scikit-learn | ML model training & prediction |
| Pandas | Data processing |
| Joblib | Model serialization |

---

## 📂 Dataset

- **Source:** [PaySim Financial Fraud Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)
- **Size:** 6.3 Million+ transactions
- **Features used:**
  - `type` — Transaction type
  - `amount` — Transaction amount
  - `oldbalanceOrg` / `newbalanceOrig` — Sender's balance before/after
  - `oldbalanceDest` / `newbalanceDest` — Receiver's balance before/after
  - `isFraud` — Target label

> ⚠️ The dataset CSV is not included in this repo due to GitHub's 100MB file size limit.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/satyanandpandey71-byte/fraud-detection-app.git
cd fraud-detection-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run fraud_detection.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 🗂 Project Structure

```
fraud-detection-app/
├── fraud_detection.py          # Main Streamlit app
├── fraud_detection_model.pkl   # Trained ML model
├── analysis_model.ipynb        # Model training notebook
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 📸 Screenshots

> _Add screenshots of the app here after running locally._

---

## 👤 Author

**Satyanand Pandey**
- GitHub: [@satyanandpandey71-byte](https://github.com/satyanandpandey71-byte)

---

⭐ **If you found this project useful, please give it a star!**

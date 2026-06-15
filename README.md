# 💰 AI Financial Risk Analyzer

> A production-style Machine Learning web application that predicts financial loan risk using AI and provides an interactive analytics dashboard built with Streamlit.

---

## 🚀 Overview

The **AI Financial Risk Analyzer** is a smart financial decision-support system that evaluates loan applicants based on their financial history and predicts whether they are **Low Risk or High Risk**.

It simulates a real-world banking risk assessment system used in fintech and credit institutions.

---

## 🎯 Key Features

- 📂 Upload any CSV financial dataset
- 🧠 Machine Learning model (Random Forest Classifier)
- ⚙️ Automatic data cleaning & preprocessing
- 🔄 Intelligent column mapping for different datasets
- 📊 Interactive analytics dashboard
- 📉 Loan risk classification (High / Low Risk)
- 🔮 Real-time prediction system
- 📈 Data visualization using Plotly
- 🧩 Fully dynamic dataset support (no fixed format required)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| Streamlit | Web app framework |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Plotly | Data visualization |

---

## 🧠 How It Works

1. Upload a financial dataset (CSV format)
2. System automatically:
   - Detects dataset structure
   - Maps required financial features
   - Handles missing values
3. Machine Learning model is trained dynamically
4. User enters loan applicant details
5. Model predicts:
   - ✅ Low Risk Loan
   - ⚠ High Risk Loan

---

## 📊 Dataset Requirements

The system supports multiple dataset formats. It automatically maps common financial features such as:

- Age / Person Age
- Income / Annual Income
- Loan Amount
- Employment Length
- Credit History Length

👉 No fixed dataset structure required

---

## 📂 Project Structure

```

AI-Financial-Risk-Analyzer/
│
├── app.py               # Main Streamlit application (ML + UI)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https:https://github.com/vijaydevverse/AI-Financial-Risk-Analyzer
````

### 2️⃣ Move into project folder

```bash
cd AI-Financial-Risk-Analyzer
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📊 Project Workflow

```
Dataset Upload → Data Cleaning → Feature Mapping → Model Training → Prediction → Visualization Dashboard
```

---

## 📈 Dashboard Highlights

* Loan risk distribution visualization
* Income vs Loan amount analysis
* Real-time prediction panel
* Model accuracy metrics
* Interactive UI with sidebar controls

---

## 🧠 Machine Learning Approach

* Algorithm: Random Forest Classifier
* Training: Supervised learning on financial datasets
* Output: Binary classification (0 = Low Risk, 1 = High Risk)
* Evaluation: Accuracy score on test data split

---

## 🚀 Future Enhancements

* 🔥 Risk probability scoring (0–100%)
* 📄 Downloadable PDF report system
* 🔐 Login authentication (Banking system simulation)
* ⚡ Advanced models (XGBoost, LightGBM)
* ☁️ Cloud deployment (Streamlit Cloud / AWS / Azure)
* 📊 Power BI-style advanced dashboard

---

## 👨‍💻 Author

**Vijay Krishnan P.M**

---

## ⭐ Project Impact

This project demonstrates:

* Real-world ML pipeline design
* End-to-end data science workflow
* UI + ML integration (production-style app)
* Financial domain understanding
* Portfolio-ready AI system

---

## ⭐ If You Like This Project

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork it
* 🔗 Share with others

---

## 📌 License

This project is for educational and portfolio purposes.

```

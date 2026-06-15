import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import plotly.express as px

# ----------------------------
# PAGE CONFIG (PRO DASHBOARD LOOK)
# ----------------------------
st.set_page_config(page_title="Financial Risk Dashboard", layout="wide")

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.title("AI Risk Dashboard")
st.sidebar.write("Upload dataset and analyze loan risk")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ----------------------------
# MAIN TITLE
# ----------------------------
st.title("💰 AI Financial Risk Analyzer Dashboard")

# ----------------------------
# RUN ONLY IF FILE UPLOADED
# ----------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Column mapping
    column_map = {
        "person_age": "Age",
        "age": "Age",
        "person_income": "Income",
        "income": "Income",
        "loan_amnt": "Loan_Amount",
        "loan_amount": "Loan_Amount",
        "person_emp_length": "Years_Employed",
        "emp_length": "Years_Employed",
        "cb_person_cred_hist_length": "Credit_Score",
        "credit_history": "Credit_Score"
    }

    df = df.rename(columns=column_map)

    required = ["Age", "Income", "Loan_Amount", "Years_Employed", "Credit_Score"]

    missing = [c for c in required if c not in df.columns]

    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()

    X = df[required]
    y = df["loan_status"]

    X = X.fillna(X.mean())

    # ----------------------------
    # TRAIN MODEL
    # ----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # ----------------------------
    # DASHBOARD METRICS
    # ----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Dataset Rows", len(df))
    col2.metric("Model Accuracy", f"{accuracy:.2f}")
    col3.metric("Features Used", len(required))

    # ----------------------------
    # CHART 1: LOAN STATUS DISTRIBUTION
    # ----------------------------
    st.subheader("Loan Status Distribution")

    fig1 = px.pie(df, names="loan_status", title="Risk Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    # ----------------------------
    # CHART 2: INCOME VS LOAN AMOUNT
    # ----------------------------
    st.subheader("Income vs Loan Amount")

    fig2 = px.scatter(
        df,
        x="Income",
        y="Loan_Amount",
        color="loan_status",
        title="Income vs Loan Amount Risk View"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ----------------------------
    # PREDICTION SECTION
    # ----------------------------
    st.subheader("🔮 Live Risk Prediction")

    colA, colB, colC = st.columns(3)

    age = colA.number_input("Age", 18, 100, 25)
    income = colB.number_input("Income", 1000, 1000000, 50000)
    loan_amount = colC.number_input("Loan Amount", 100, 1000000, 10000)

    colD, colE = st.columns(2)

    years_employed = colD.number_input("Years Employed", 0, 50, 2)
    credit_score = colE.number_input("Credit History Length", 0, 30, 5)

    if st.button("Predict Risk"):

        input_data = np.array([[age, income, loan_amount, years_employed, credit_score]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠ High Risk Loan")
        else:
            st.success("✅ Low Risk Loan")

else:
    st.info("👈 Upload a CSV file from the sidebar to start analysis")
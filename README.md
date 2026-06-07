# 💰 Financial Expense Anomaly Detection for Corporate Auditing

## Overview

The Financial Expense Anomaly Detection for Corporate Auditing System is a Machine Learning-based solution designed to identify unusual expense transactions and support auditors in prioritizing high-risk financial activities. The system analyzes corporate expense records, detects anomalies, calculates risk scores, and generates audit insights through an interactive dashboard.

Traditional auditing processes often require manual review of thousands of transactions, making anomaly detection time-consuming and prone to oversight. This project automates the identification of suspicious spending patterns, helping organizations improve financial monitoring, reduce audit effort, and strengthen compliance controls.

---

## Purpose of the Project

The primary purpose of this project is to assist finance teams and auditors in:

* Detecting abnormal expense transactions automatically.
* Identifying potentially fraudulent or high-risk expenses.
* Prioritizing audit investigations based on risk levels.
* Understanding spending behavior across departments.
* Monitoring vendor-related financial risks.
* Supporting data-driven decision-making in corporate auditing.

---

## Key Features

### 🔍 Anomaly Detection

* Uses the Isolation Forest Machine Learning algorithm.
* Detects unusual expense transactions automatically.
* Identifies suspicious spending behavior.

### 📊 Risk Assessment

* Generates Risk Scores (0–100).
* Classifies transactions into risk categories.
* Assigns audit priorities for investigation.

### 📈 Interactive Analytics Dashboard

* Department-wise Expense Analysis
* Monthly Expense Trend Analysis
* Risk Distribution Visualization
* Vendor Risk Analysis
* Employee Risk Ranking
* Baseline Spending Analysis

### 📋 Audit Support

* Suspicious Transaction Identification
* Audit Priority Ranking
* Transaction-Level Risk Explanations
* Audit Summary Reports

### ⚙️ User Features

* Department-wise Filtering
* Interactive Visualizations
* CSV Dataset Support
* Real-Time Dashboard Insights

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* Joblib
* MySQL
* GitHub

---

## Dataset Attributes

The system analyzes expense transaction records containing:

* Expense ID
* Employee ID
* Department
* Expense Type
* Vendor
* Amount
* Date

---

## Machine Learning Model

The project uses the **Isolation Forest Algorithm**, an unsupervised anomaly detection technique that isolates unusual observations from normal data patterns.

The model performs:

* Anomaly Detection
* Risk Score Generation
* Suspicious Transaction Identification
* Audit Prioritization

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Expected Outputs

The system provides:

* Suspicious Transaction Detection
* Risk Classification
* Audit Prioritization
* Departmental Spending Analysis
* Vendor Risk Assessment
* Employee Risk Ranking
* Interactive Dashboards
* Audit Reports

---

## Future Enhancements

* Real-Time Expense Monitoring
* Advanced Fraud Detection Models
* Automated Alert System
* Cloud Database Integration
* Predictive Financial Risk Analysis

---

## Author

**Utakriti Sharma**
B.Tech – Computer Science and Business Systems (CSBS)

Academic Project – Financial Expense Anomaly Detection for Corporate Auditing

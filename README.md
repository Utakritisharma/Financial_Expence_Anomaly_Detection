# Financial Expense Anomaly Detection for Corporate Auditing

## Project Overview

Financial Expense Anomaly Detection for Corporate Auditing is a machine learning-based system designed to identify unusual expense transactions and assist auditors in prioritizing financial investigations. The system analyzes corporate expense data, detects anomalies using the Isolation Forest algorithm, generates risk scores, classifies audit priorities, and presents results through an interactive dashboard.

## Objectives

* Detect unusual expense patterns within corporate financial data.
* Prioritize suspicious transactions for auditing.
* Generate risk scores for expense transactions.
* Perform statistical baseline analysis across departments.
* Provide actionable audit insights through visualization and reporting.

## Features

* Anomaly Detection using Isolation Forest
* Risk Score Generation
* Audit Priority Classification
* Department Spending Analysis
* Vendor Risk Analysis
* Employee Risk Ranking
* Statistical Baselining
* Interactive Streamlit Dashboard
* Downloadable Audit Reports

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit

## Dataset Features

The dataset contains:

* Expense ID
* Employee ID
* Department
* Expense Type
* Vendor
* Amount
* Date

## Machine Learning Model

The project uses the Isolation Forest algorithm for anomaly detection. The model identifies unusual expense transactions and assigns risk scores based on their deviation from normal spending patterns.

## Dashboard Modules

* KPI Overview
* Department Analysis
* Risk Distribution
* Vendor Analysis
* Employee Risk Ranking
* Baseline Analysis
* Audit Summary

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Output

The system provides:

* Suspicious Transaction Detection
* Risk Classification
* Audit Prioritization
* Departmental Baseline Analysis
* Downloadable Audit Reports

## Future Enhancements

* Real-Time Expense Monitoring
* Advanced Fraud Detection Models
* Automated Alert System
* Cloud Deployment
* Interactive Audit Recommendation Engine

## Author

Utakriti Sharma

B.Tech Computer Science and Business Systems (CSBS)

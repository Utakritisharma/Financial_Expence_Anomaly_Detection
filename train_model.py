import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("data/expenses.csv")

# Train anomaly detection model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

# Detect anomalies
data["Anomaly"] = model.fit_predict(data[["Amount"]])

# Convert results
data["Anomaly"] = data["Anomaly"].map({
    1: "Normal",
    -1: "Suspicious"
})

# Risk Classification
def risk_level(amount):
    if amount >= 100000:
        return "High Risk"
    elif amount >= 50000:
        return "Medium Risk"
    else:
        return "Low Risk"

data["Risk_Level"] = data["Amount"].apply(risk_level)

print("\nFinancial Expense Audit Report\n")

print(data[
    [
        "Expense_ID",
        "Department",
        "Amount",
        "Anomaly",
        "Risk_Level"
    ]
])
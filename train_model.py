import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Load dataset

data = pd.read_csv("data/expenses.csv")

# Features

X = data[["Amount"]]

# Train-Test Split

X_train, X_test = train_test_split(
X,
test_size=0.2,
random_state=42
)

# Train anomaly detection model

model = IsolationForest(
contamination=0.2,
random_state=42
)

model.fit(X_train)

# Predictions

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Save model

joblib.dump(
model,
"anomaly_model.pkl"
)

print("Model saved successfully.")

# Detect anomalies on full dataset

data["Anomaly"] = model.predict(X)

# Convert results

data["Anomaly"] = data["Anomaly"].map(
{
1: "Normal",
-1: "Suspicious"
}
)

# Risk Classification

def risk_level(amount):

    if amount >= 100000:
        return "High Risk"

    elif amount >= 50000:
        return "Medium Risk"

    else:
        return "Low Risk"


data["Risk_Level"] = data["Amount"].apply(
    risk_level
)

print("\nFinancial Expense Audit Report\n")

print(
    data[
        [
            "Expense_ID",
            "Department",
            "Amount",
            "Anomaly",
            "Risk_Level"
        ]
    ]
)

import mysql.connector
import pandas as pd

# Connect MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="financial_audit_db"
)

cursor = connection.cursor()

# Read CSV
data = pd.read_csv("data/expenses.csv")

# Insert Data
for _, row in data.iterrows():
    cursor.execute("""
        INSERT INTO expenses
        (Expense_ID, Employee_ID, Department, Expense_Type, Amount, Vendor, Date)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["Expense_ID"],
        row["Employee_ID"],
        row["Department"],
        row["Expense_Type"],
        int(row["Amount"]),
        row["Vendor"],
        row["Date"]
    ))

connection.commit()

print(f"{len(data)} Records Imported Successfully!")

connection.close()
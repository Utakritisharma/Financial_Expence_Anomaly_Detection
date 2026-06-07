import pandas as pd
import random

departments = ["Finance", "HR", "IT", "Sales"]
expense_types = [
    "Travel",
    "Food",
    "Hotel",
    "Software",
    "Office Supplies",
    "Training",
    "Consulting",
    "Marketing",
    "Equipment"
]

data = []

for i in range(1, 501):
    amount = random.randint(500, 50000)

    if random.random() < 0.05:
        amount = random.randint(80000, 200000)

    data.append([
        f"EXP{i:03}",
        f"E{i:03}",
        random.choice(departments),
        random.choice(expense_types),
        amount,
        f"Vendor_{random.randint(1,20)}",
        f"2025-01-{random.randint(1,28):02}"
    ])

df = pd.DataFrame(data, columns=[
    "Expense_ID",
    "Employee_ID",
    "Department",
    "Expense_Type",
    "Amount",
    "Vendor",
    "Date"
])

df.to_csv("data/expenses.csv", index=False)

print("500 records generated successfully!")

import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

st.set_page_config(
    page_title="AI Financial Expense Audit System",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color:#F8FAFC;
}

div[data-testid="stMetric"]{
    background:white;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #2563EB;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center'>
💰 Financial Expense Anomaly Detection for Corporate Auditing
</h1>

<h4 style='text-align:center;color:gray'>
AI Powered Audit Prioritization System
</h4>
""", unsafe_allow_html=True)

# Load data
uploaded_file = st.sidebar.file_uploader(
    "Upload Expense Dataset",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data/expenses.csv")
required_columns = [
    "Expense_ID",
    "Employee_ID",
    "Department",
    "Expense_Type",
    "Amount",
    "Vendor",
    "Date"
]

missing = [
    col for col in required_columns
    if col not in data.columns
]

if missing:
    st.error(
        f"Missing columns: {', '.join(missing)}"
    )
    st.stop()
data["Date"] = pd.to_datetime(data["Date"])

# Sidebar filter
st.sidebar.header("Dashboard Filters")
st.sidebar.markdown("""
### Model Information

Algorithm: Isolation Forest

Type: Unsupervised Learning

Purpose:
Detect unusual expense patterns for audit prioritization.
""")
departments = data["Department"].unique()

selected_departments = st.sidebar.multiselect(
    "Select Department",
    departments,
    default=departments
)

data = data[data["Department"].isin(selected_departments)]
if data.empty:

    st.markdown("""
    # 📊 Financial Expense Audit Dashboard

    ### No Department Selected

    Please select one or more departments from the sidebar to view analytics.

    Available Departments:
    - HR
    - Finance
    - Sales
    - IT
    """)

    st.stop()

# Encode categorical columns
dept_encoder = LabelEncoder()
expense_encoder = LabelEncoder()
vendor_encoder = LabelEncoder()

data["Department_Code"] = dept_encoder.fit_transform(data["Department"])
data["Expense_Code"] = expense_encoder.fit_transform(data["Expense_Type"])
data["Vendor_Code"] = vendor_encoder.fit_transform(data["Vendor"])

# Features
features = data[
    [
        "Amount",
        "Department_Code",
        "Expense_Code",
        "Vendor_Code"
    ]
]

# Train model
model = IsolationForest(
    contamination=0.10,
    random_state=42
)

data["Prediction"] = model.fit_predict(features)

scores = model.decision_function(features)

risk_scores = (1 - scores)

risk_scores = (
    100
    * (risk_scores - risk_scores.min())
    / (risk_scores.max() - risk_scores.min())
)

data["Risk_Score"] = risk_scores.round(0)

data["Anomaly"] = data["Prediction"].map(
    {
        1: "Normal",
        -1: "Suspicious"
    }
)

def classify_risk(score):

    if score >= 75:
        return "🔴 High Risk"

    elif score >= 50:
        return "🟠 Medium Risk"

    else:
        return "🟢 Low Risk"

data["Risk_Level"] = data["Risk_Score"].apply(classify_risk)

def audit_priority(score):
    if score >= 90:
        return "Critical"
    elif score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

data["Audit_Priority"] = data["Risk_Score"].apply(audit_priority)

def explain_anomaly(row):

    avg_amount = data["Amount"].mean()

    if row["Amount"] > avg_amount * 2:
        return "Expense significantly above average"

    elif row["Amount"] > avg_amount * 1.5:
        return "Expense moderately above average"

    else:
        return "Unusual spending pattern detected"

data["Reason"] = data.apply(
    explain_anomaly,
    axis=1
)

# KPI Section
total_expenses = len(data)
total_amount = data["Amount"].sum()
suspicious_count = len(data[data["Anomaly"] == "Suspicious"])
high_risk_count = len(
    data[data["Risk_Level"] == "🔴 High Risk"]
)
critical_count = len(
    data[data["Audit_Priority"] == "Critical"]
)

avg_risk = data["Risk_Score"].mean()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
"📄 Total Expenses",
total_expenses
)

c2.metric(
"💰 Total Amount",
f"₹{total_amount:,.0f}"
)

c3.metric(
"⚠ Suspicious",
suspicious_count
)

c4.metric(
"🔴 High Risk",
high_risk_count
)

c5.metric(
"🔥 Critical",
critical_count
)


st.success(f"""
🔍 Key Findings

• {suspicious_count} suspicious transactions detected

• {high_risk_count} high-risk expenses require audit

• {critical_count} critical cases need immediate review

• Average Risk Score: {avg_risk:.2f}

• Highest Risk Score: {data['Risk_Score'].max()}
""")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Dashboard",
        "Risk Analysis",
        "Vendor Analysis",
        "Audit Report",
        "Baseline Analysis"
    ]
)

with tab1:

    st.subheader("Department Spending")

    dept_spending = (
        data.groupby("Department")["Amount"]
        .sum()
        .reset_index()
    )
    fig1 = px.bar(
    dept_spending,
    x="Department",
    y="Amount",
    text_auto=".2s",
    title="💰 Department Wise Spending"
)

fig1.update_traces(
    textposition="outside"
)

fig1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_size=14,
    title_x=0.3,
    height=500
)

st.plotly_chart(
    fig1,
    use_container_width=True
)
st.subheader("📈 Monthly Expense Trend")

data["Date"] = pd.to_datetime(data["Date"])

monthly = (
    data.groupby(
        data["Date"].dt.strftime("%Y-%m")
    )["Amount"]
    .sum()
    .reset_index()
)

fig_month = px.line(
    monthly,
    x="Date",
    y="Amount",
    markers=True,
    title="Monthly Expense Trend"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

with tab2:

    st.subheader("Risk Distribution")

    risk_dist = (
        data["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    risk_dist.columns = ["Risk_Level", "Count"]

    fig2 = px.pie(
        risk_dist,
        names="Risk_Level",
        values="Count",
        hole=0.55,
        title="⚠ Risk Distribution"
    )

    fig2.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig2.update_layout(
        height=500,
        title_x=0.3
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("Top 5 Suspicious Transactions")

    top5 = data.nlargest(
        5,
        "Risk_Score"
    )

    st.dataframe(
        top5[
            [
                "Expense_ID",
                "Amount",
                "Vendor",
                "Risk_Score"
            ]
        ]
    )
with tab3:

    st.subheader("Vendor Risk Analysis")

    vendor_risk = (
        data[data["Anomaly"] == "Suspicious"]
        .groupby("Vendor")
        .size()
        .reset_index(name="Suspicious_Count")
    )

    if not vendor_risk.empty:

        fig3 = px.bar(
    vendor_risk,
    x="Vendor",
    y="Suspicious_Count",
    text_auto=True,
    title="🚨 Suspicious Transactions by Vendor"
)

fig3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    height=500
)

st.plotly_chart(
    fig3,
    use_container_width=True
)
top_vendor = (
    vendor_risk.sort_values(
        by="Suspicious_Count",
        ascending=False
    )
    .iloc[0]
)

st.warning(
    f"🚨 Highest Risk Vendor: {top_vendor['Vendor']} "
    f"({top_vendor['Suspicious_Count']} suspicious transactions)"
)

with tab4:

    st.subheader("Employee Risk Ranking")

    employee_risk = (
        data.groupby("Employee_ID")["Risk_Score"]
        .mean()
        .reset_index()
        .sort_values(
            by="Risk_Score",
            ascending=False
        )
    )

    st.dataframe(employee_risk.head(20))

    st.subheader("High Risk Transactions")

    st.dataframe(
    data.sort_values(
        by="Risk_Score",
        ascending=False
    )[
        [
            "Expense_ID",
            "Employee_ID",
            "Department",
            "Amount",
            "Risk_Score",
            "Risk_Level",
            "Audit_Priority",
            "Reason"
        ]
    ]
)

with tab5:

    st.subheader("Department Baseline Spending")

    baseline = (
        data.groupby("Department")["Amount"]
        .mean()
        .reset_index()
    )

    baseline.columns = [
        "Department",
        "Average Expense"
    ]

    st.dataframe(baseline)

    fig4 = px.bar(
        baseline,
        x="Department",
        y="Average Expense",
        text_auto=".2s",
        title="📊 Department Baseline Spending"
    )

    fig4.update_traces(
        textposition="outside"
    )

    fig4.update_layout(
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.subheader("🏆 Department Audit Priority Ranking")

    department_risk = (
        data.groupby("Department")["Risk_Score"]
        .mean()
        .reset_index()
        .sort_values(
            by="Risk_Score",
            ascending=False
        )
    )

    st.dataframe(department_risk)
    top_dept = department_risk.iloc[0]

st.error(
    f"🏆 Highest Audit Priority Department: "
    f"{top_dept['Department']}"
)

st.info(
    f"""
Audit Summary

Total Expenses Reviewed: {total_expenses}

Suspicious Transactions Found: {suspicious_count}

High Risk Cases: {high_risk_count}
"""
)
st.markdown("---")

st.caption(
    "Developed using Streamlit, Scikit-Learn and Plotly | Financial Audit Analytics Dashboard"
)

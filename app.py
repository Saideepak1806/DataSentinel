import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from modules.validation import check_missing, check_duplicates
from modules.impact import revenue_loss_due_to_missing
from modules.scoring import calculate_quality_score
from modules.alerts import generate_alerts
from modules.ingestion import inject_issues

st.set_page_config(layout="wide")

# HEADER
st.markdown("## 📊 DataSentinel")
st.caption("Real-time Data Quality Insights for Business Analytics")

st.markdown("---")

# FILE UPLOAD
st.subheader("📂 Upload Dataset")
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

# TOGGLE
inject = st.checkbox("Simulate Data Issues (for testing)", value=True)

if uploaded_file is not None:

    # ENCODING FIX
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    if inject:
        df = inject_issues(df)

    # CALCULATIONS
    missing = check_missing(df).sum()
    duplicates = check_duplicates(df)
    impact = revenue_loss_due_to_missing(df)
    score = calculate_quality_score(missing, duplicates)
    alerts = generate_alerts(missing, duplicates, impact)

    # EXEC SUMMARY
    st.markdown("### 🔎 Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Quality Score", f"{round(score,2)}/100")
    col2.metric("Missing Values", missing)
    col3.metric("Duplicates", duplicates)
    col4.metric("Revenue Impact", f"₹{round(impact,2)}")

    st.markdown("---")

    # 🔥 TOP ISSUES TABLE (NEW)
    st.markdown("### 📋 Top Data Quality Issues")

    issues_data = []

    if impact > 0:
        issues_data.append(["Revenue Impact", "HIGH", f"₹{round(impact,2)} impact due to missing values"])

    if missing > 0:
        issues_data.append(["Missing Values", "MEDIUM", f"{missing} missing values detected"])

    if duplicates > 0:
        issues_data.append(["Duplicate Records", "LOW", f"{duplicates} duplicate rows found"])

    if issues_data:
        issues_df = pd.DataFrame(issues_data, columns=["Issue", "Severity", "Description"])
        st.dataframe(issues_df, use_container_width=True)
    else:
        st.success("No major data quality issues detected")

    st.markdown("---")

    # 🔥 BUSINESS EXPLANATION PANEL (NEW)
    st.markdown("### 🧠 Business Impact Explanation")

    if missing > 0:
        st.warning(f"Missing values can lead to incorrect reporting and unreliable analytics outputs.")

    if duplicates > 0:
        st.warning(f"Duplicate records may inflate KPIs such as customer count and revenue.")

    if impact > 0:
        st.error(f"Estimated revenue impact is ₹{round(impact,2)}, which can affect business decisions significantly.")

    if missing == 0 and duplicates == 0:
        st.success("Data quality is good. Business decisions can be made with confidence.")

    st.markdown("---")

    # ALERTS
    st.markdown("### 🚨 Critical Issues (Prioritized)")

    if alerts:
        for level, msg in alerts:
            if level == "HIGH":
                st.error(f"🔴 {msg}")
            elif level == "MEDIUM":
                st.warning(f"🟠 {msg}")
            else:
                st.info(f"🔵 {msg}")
    else:
        st.success("✅ No critical issues detected")

    st.markdown("---")

    # GRAPH — Missing Values
    st.markdown("### 📉 Missing Values by Column")

    missing_by_col = df.isnull().sum()
    missing_by_col = missing_by_col[missing_by_col > 0]

    if not missing_by_col.empty:
        fig, ax = plt.subplots(figsize=(6, 3))
        missing_by_col.plot(kind='bar', ax=ax)
        st.pyplot(fig)
    else:
        st.success("No missing values across columns")

    st.markdown("---")

    # GRAPH — Duplicates
    st.markdown("### 📊 Duplicate Records Overview")

    dup_data = pd.DataFrame({
        "Type": ["Unique", "Duplicate"],
        "Count": [len(df) - duplicates, duplicates]
    })

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.bar(dup_data["Type"], dup_data["Count"])
    st.pyplot(fig2)

    st.markdown("---")

    # LOCATION
    st.markdown("### 🌍 Location Insights")

    possible_location_cols = [
        col for col in df.columns 
        if "city" in col.lower() 
        or "location" in col.lower() 
        or "state" in col.lower()
    ]

    if possible_location_cols:
        loc_col = possible_location_cols[0]
        location_counts = df[loc_col].value_counts().head(10)
        st.bar_chart(location_counts)
    else:
        st.info("No location-based column detected")

    st.markdown("---")

    # SCORE
    st.markdown("### 🎯 Data Quality Score Indicator")

    st.progress(score / 100)

    if score > 80:
        st.success("Good Data Quality")
    elif score > 50:
        st.warning("Moderate Data Quality")
    else:
        st.error("Poor Data Quality")

    st.markdown("---")

    # DATA PREVIEW
    st.markdown("### 📄 Sample Data")
    st.dataframe(df.head(), use_container_width=True)

else:
    st.info("Please upload a CSV file to begin.")
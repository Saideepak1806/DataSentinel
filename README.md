# 📊 DataSentinel — Intelligent Data Quality Monitoring System

## 🔍 Overview

DataSentinel is a business-focused data quality monitoring system built using Python and Streamlit.  
It detects, analyzes, and prioritizes data quality issues while also explaining their impact on business decisions.

Unlike traditional data cleaning tools, DataSentinel focuses on **decision-making**, not just detection.

---

## 🚨 Problem Statement

In real-world business environments, poor data quality leads to:

- Incorrect reports and dashboards  
- Misleading KPIs  
- Financial losses  
- Poor decision-making  

Most systems detect issues but fail to explain their **business impact**.

---

## 💡 Solution

DataSentinel provides:

- Automated detection of data quality issues  
- Severity-based prioritization of problems  
- Business impact estimation (e.g., revenue loss)  
- Interactive dashboard for quick decision-making  

---

## ⚙️ Features

- 📂 Upload any CSV dataset  
- 🔎 Detect missing values and duplicate records  
- 🚨 Prioritize issues based on severity (High / Medium / Low)  
- 💰 Estimate business impact (revenue loss due to bad data)  
- 📊 Visualize data quality metrics using graphs  
- 🌍 Location-based insights (if location data is present)  
- 🎯 Data Quality Score (0–100)  
- 📋 Top Issues Table with structured insights  

---

## 🧠 Key Innovation

This project goes beyond basic data cleaning by:

- Linking data issues to **business impact**  
- Prioritizing issues instead of listing everything  
- Providing **actionable insights** for stakeholders  

---

## 🛠 Tech Stack

- Python  
- Pandas, NumPy  
- Streamlit  
- Matplotlib  

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/Saideepak1806/DataSentinel.git
cd DataSentinel

pip install -r requirements.txt
streamlit run app.py

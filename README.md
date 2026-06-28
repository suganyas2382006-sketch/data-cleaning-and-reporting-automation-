# 🧹 Data Cleaning & Reporting Automation

## Project Overview

The Data Cleaning & Reporting Automation project automates data preprocessing and reporting workflows using Python, Streamlit, Pandas, and Plotly. The system automatically detects and handles missing values, removes duplicate records, cleans inconsistent data, and generates interactive reports with visual summaries.

The project improves reporting efficiency and reduces manual effort in data preparation.

---

## Objectives

- Automate data cleaning processes
- Handle missing and inconsistent data
- Remove duplicate records
- Generate automated reports and visual summaries
- Improve reporting efficiency

---

## Features

### Data Import
- Upload CSV files
- Upload Excel files (.xlsx)

### Data Cleaning Automation
- Detect missing values
- Replace missing numerical values with mean values
- Replace missing text values with "Unknown"
- Remove duplicate records
- Handle inconsistent data automatically

### KPI Metrics
- Total Rows
- Missing Values Removed
- Duplicate Records Removed
- Number of Columns

### Automated Reporting
- Missing Values Summary Chart
- Column Data Type Distribution
- Cleaned Dataset Preview
- Download Cleaned Dataset option

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

---

## Project Structure

```text
Data-Cleaning-Reporting-Automation/
│
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── dirty_data.csv
```

---

## Dataset Description

The dataset contains employee-related information with intentionally introduced issues such as:

- Missing values
- Duplicate records
- Inconsistent entries

Dataset columns:

| Column | Description |
|----------|-------------|
| Employee_ID | Unique employee identifier |
| Name | Employee name |
| Department | Department name |
| Salary | Employee salary |
| Experience | Years of experience |
| City | Employee city |
| Performance | Performance rating |

---

## Installation

Install required libraries:

```bash
pip install streamlit pandas plotly openpyxl
```

---

## Run the Project

```bash
python3 -m streamlit run app.py
```

---

## Dashboard Output

The dashboard provides:

- Raw dataset preview
- Cleaned dataset preview
- KPI cards
- Missing values report
- Data type distribution chart
- Download cleaned dataset button

---

## Business Benefits

- Reduces manual data cleaning effort
- Improves data quality
- Increases reporting speed
- Supports better decision-making
- Enhances workflow efficiency

---

## Expected Outcome

This project helps understand:

- Data preprocessing techniques
- Automation workflows
- Data quality improvement
- Reporting efficiency
- Interactive dashboard development

---

## Author

Submitted By: Suganya S
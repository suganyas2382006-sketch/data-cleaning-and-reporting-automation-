import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Cleaning & Reporting Automation",
    layout="wide"
)

st.title("🧹 Data Cleaning & Reporting Automation")

# File upload
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Raw Dataset")
    st.dataframe(df.head())

    # Store original metrics
    original_rows = len(df)
    original_missing = df.isnull().sum().sum()

    # ------------------------
    # Data Cleaning
    # ------------------------

    # Remove duplicates
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing text values
    text_cols = df.select_dtypes(include=['object']).columns

    for col in text_cols:
        df[col] = df[col].fillna("Unknown")

    cleaned_missing = df.isnull().sum().sum()

    st.subheader("Cleaned Dataset")
    st.dataframe(df.head())

    # ------------------------
    # KPI Cards
    # ------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        len(df)
    )

    c2.metric(
        "Missing Values Removed",
        original_missing - cleaned_missing
    )

    c3.metric(
        "Duplicates Removed",
        duplicate_count
    )

    c4.metric(
        "Columns",
        len(df.columns)
    )

    st.markdown("---")

    # ------------------------
    # Missing Values Chart
    # ------------------------

    missing_chart = pd.DataFrame(
        df.isnull().sum(),
        columns=["Missing"]
    )

    fig1 = px.bar(
        missing_chart,
        y="Missing",
        title="Missing Values Summary"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ------------------------
    # Data Type Distribution
    # ------------------------

    datatype = pd.DataFrame(
        df.dtypes.astype(str).value_counts()
    ).reset_index()

    datatype.columns = ["Type", "Count"]

    fig2 = px.pie(
        datatype,
        names="Type",
        values="Count",
        title="Column Data Types"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # Download cleaned data
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

else:
    st.info("Upload a dataset to start")
import streamlit as st
from data_loader import load_data
from analysis_engine import data_profile, generate_basic_insights
from visualization import (
    create_histogram,
    create_bar_chart,
    create_line_chart,
    create_scatter_plot,
    create_correlation_heatmap
)
from ai_agent import basic_query
from report_generator import create_report

st.set_page_config(page_title="AI Data Analyst System", layout="wide")

st.title("AI Data Analyst System")
st.write("Upload your dataset and explore insights.")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    profile = data_profile(df)

    st.subheader("Data Profile")

    st.write("Rows:", profile["rows"])
    st.write("Columns:", profile["columns"])
    st.write("Column Names:", profile["column_names"])
    st.write("Missing Values:", profile["missing_values"])
    st.write("Data Types:", profile["data_types"])

    st.subheader("AI Insights")

    insights = generate_basic_insights(df)

    for insight in insights:
        st.write("-", insight)

    st.subheader("Visualization")

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Histogram", "Bar Chart", "Line Chart", "Scatter Plot", "Correlation Heatmap"]
    )

    if chart_type in ["Histogram", "Bar Chart", "Line Chart"]:
        column = st.selectbox("Select column", df.columns)

        if chart_type == "Histogram":
            fig = create_histogram(df, column)

        elif chart_type == "Bar Chart":
            fig = create_bar_chart(df, column)

        elif chart_type == "Line Chart":
            fig = create_line_chart(df, column)

        st.plotly_chart(fig)

    elif chart_type == "Scatter Plot":

        col1 = st.selectbox("X Axis", df.columns)
        col2 = st.selectbox("Y Axis", df.columns)

        fig = create_scatter_plot(df, col1, col2)

        st.plotly_chart(fig)

    elif chart_type == "Correlation Heatmap":

        fig = create_correlation_heatmap(df)

        st.plotly_chart(fig)

    st.subheader("Ask AI Analyst")

    user_query = st.text_input("Ask a question about your data")

    if user_query:
        result = basic_query(df, user_query)

        st.write("Result:")
        st.write(result)

    st.subheader("Download Report")

    if st.button("Generate PDF Report"):

        report_file = create_report(insights)

        with open(report_file, "rb") as f:

            st.download_button(
                label="Download Report",
                data=f,
                file_name="analysis_report.pdf",
                mime="application/pdf"
            )
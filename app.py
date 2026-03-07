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
from ai_agent import run_llm_query
from report_generator import create_report

st.set_page_config(page_title="AI Data Analyst System", layout="wide")

st.title("AI Data Analyst System")
st.write("Upload your dataset and explore insights using AI.")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.success("Dataset Loaded Successfully")

    # Dataset preview
    st.markdown("### Dataset Preview")
    st.dataframe(df.head())

    # Data profile
    profile = data_profile(df)

    st.markdown("### Data Profile")

    st.write("Rows:", profile["rows"])
    st.write("Columns:", profile["columns"])
    st.write("Column Names:", profile["column_names"])
    st.write("Missing Values:", profile["missing_values"])
    st.write("Data Types:", profile["data_types"])

    # AI insights
    st.markdown("### AI Insights")

    insights = generate_basic_insights(df)

    for insight in insights:
        st.write("-", insight)

    # Visualization
    st.markdown("### Visualization")

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

    # AI Query Section
    st.markdown("### Ask AI Analyst")

    user_query = st.text_input("Ask a question about your data")

    if user_query:

        ai_response = run_llm_query(df, user_query)

        if "Explanation:" in ai_response:
            result, explanation = ai_response.split("Explanation:", 1)
        else:
            result = ai_response
            explanation = "No explanation generated."

        st.markdown("### Analysis Result")
        st.write(result)

        st.markdown("### AI Explanation")
        st.info(explanation)

    # PDF Report
    st.markdown("### Download Report")

    if st.button("Generate PDF Report"):

        report_file = create_report(insights)

        with open(report_file, "rb") as f:

            st.download_button(
                label="Download Report",
                data=f,
                file_name="analysis_report.pdf",
                mime="application/pdf"
            )
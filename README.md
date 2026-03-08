# LLM-Powered AI Data Analyst System

An AI-powered data analysis application that allows users to upload datasets, ask questions in natural language, automatically generate insights, create visualizations, and download analysis reports.

The system integrates **Large Language Models (LLMs)** to convert user questions into Python data analysis code, execute the analysis, and return results with clear business explanations.

---

## Features

• Upload CSV or Excel datasets  
• Automatic data profiling (rows, columns, missing values, data types)  
• AI-generated dataset insights  
• Interactive visualizations (Histogram, Bar Chart, Line Chart, Scatter Plot, Correlation Heatmap)  
• Natural language data queries powered by LLMs  
• Automatic Python (Pandas) code generation for analysis  
• AI-generated business explanations for results  
• Safe query handling (blocks machine learning model training requests)  
• Downloadable PDF analysis reports  

---

## Live Application

You can try the deployed app here:

[![Launch App](https://img.shields.io/badge/Streamlit-Live%20Demo-red?logo=streamlit)](https://ai-data-analyst-system-tylybdsucektppblzeh4ft.streamlit.app/)

---

## Tech Stack

Python  
Streamlit  
Pandas  
Plotly  
ReportLab  
LangChain  
OpenAI API  

---

## How the System Works

User uploads dataset  
↓  
User asks question in natural language  
↓  
LLM converts question → pandas analysis code  
↓  
Python executes analysis  
↓  
Result generated  
↓  
LLM explains the result in business language  
↓  
User receives insights, visualizations, and report  

---

## How to Run

### 1. Clone the repository

git clone https://github.com/Navjotkaur-22/AI-Data-Analyst-System

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add OpenAI API Key

Create a `.env` file in the project root:

OPENAI_API_KEY=your_openai_api_key

### 4. Run the application

streamlit run app.py

---

## Example Workflow

1. Upload a dataset  
2. View dataset profile and summary statistics  
3. Generate interactive visualizations  
4. Ask questions about the dataset in natural language  
5. Receive AI-generated insights and explanations  
6. Download a PDF analysis report  

---

## Example Queries

Which region has the highest sales?  
Show total sales by product category  
What is the correlation between numeric features?  
Which customer segment generates the most revenue?  

---

## Use Cases

• Business analytics  
• Sales performance analysis  
• Customer behavior insights  
• Marketing data exploration  
• Financial data analysis  

---

## Author

Navjot Kaur  
Data Scientist | ML & Data Automation Specialist  
Email:- nkaur4047@gmail.com  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/navjot-kaur-b61aab299/)

[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-green?logo=upwork)](https://www.upwork.com/freelancers/~01b30aa09d478b524c)

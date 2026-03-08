import os
import re
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def run_llm_query(df, query):

    # ---- Block ML training queries ----
    blocked_keywords = [
        "train model",
        "random forest",
        "xgboost",
        "svm",
        "logistic regression",
        "fit model",
        "predict",
        "machine learning",
        "neural network",
        "classification model"
    ]

    for word in blocked_keywords:
        if word in query.lower():
            return "This AI analyst focuses on data analysis and insights, not machine learning model training."

    # ---- Initialize LLM ----
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        temperature=0,
        model="gpt-4o-mini"
    )

    # ---- Prompt for pandas code generation ----
    prompt = f"""
You are a professional Python data analyst.

A pandas dataframe named df is already loaded.

Columns available:
{list(df.columns)}

User question:
{query}

Write Python pandas code to answer the question.

Rules:
- Use dataframe name df
- Store final result in variable named result
- Only generate pandas code
- Do not generate explanations
- Do not train ML models
"""

    response = llm.invoke(prompt)

    code = response.content.strip()

    # Remove markdown formatting if present
    code = re.sub(r"```python", "", code)
    code = re.sub(r"```", "", code).strip()

    local_vars = {"df": df}

    # ---- Execute generated code ----
    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", "No result returned.")
    except Exception as e:
        return f"Execution error: {str(e)}"

    # ---- Generate explanation ----
    explanation_prompt = f"""
Explain this data analysis result in simple business language.

User question:
{query}

Result:
{result}
"""

    explanation = llm.invoke(explanation_prompt)

    return f"{result}\n\nExplanation:\n{explanation.content}"
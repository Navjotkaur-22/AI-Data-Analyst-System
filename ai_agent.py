import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def run_llm_query(df, query):

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )

    prompt = f"""
You are a Python data analyst.

A pandas dataframe named df is already loaded.

Columns available:
{list(df.columns)}

User question:
{query}

Write pandas code to answer the question.

Rules:
- Use dataframe name df
- Store final output in variable result
- Return ONLY Python code
"""

    response = llm.invoke(prompt)

    code = response.content.strip()

    code = re.sub(r"```python", "", code)
    code = re.sub(r"```", "", code).strip()

    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", "No result produced.")
    except Exception as e:
        return f"Execution error: {str(e)}"

    explanation_prompt = f"""
Explain this data analysis result in simple business language.

User question:
{query}

Result:
{result}
"""

    explanation = llm.invoke(explanation_prompt)

    return f"{result}\n\nExplanation:\n{explanation.content}"
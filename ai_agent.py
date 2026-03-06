import pandas as pd

def basic_query(df, query):

    query = query.lower()

    if "columns" in query:
        return df.columns.tolist()

    elif "shape" in query or "size" in query:
        return df.shape

    elif "missing" in query:
        return df.isnull().sum()

    elif "summary" in query or "describe" in query:
        return df.describe()

    else:
        return "Query not understood yet."
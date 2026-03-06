import pandas as pd

def data_profile(df):

    profile = {}

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]
    profile["column_names"] = list(df.columns)
    profile["missing_values"] = df.isnull().sum().to_dict()
    profile["data_types"] = df.dtypes.astype(str).to_dict()

    return profile


def generate_basic_insights(df):

    insights = []

    insights.append(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

    missing = df.isnull().sum().sum()

    if missing > 0:
        insights.append(f"There are {missing} missing values in the dataset.")
    else:
        insights.append("No missing values detected.")

    numeric_cols = df.select_dtypes(include=['number']).columns

    insights.append(f"There are {len(numeric_cols)} numeric columns available for analysis.")

    return insights
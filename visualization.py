import plotly.express as px

def create_histogram(df, column):
    fig = px.histogram(df, x=column)
    return fig

def create_bar_chart(df, column):
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "count"]

    fig = px.bar(value_counts, x=column, y="count")
    return fig
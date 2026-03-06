import plotly.express as px
import plotly.figure_factory as ff

def create_histogram(df, column):
    fig = px.histogram(df, x=column)
    return fig


def create_bar_chart(df, column):
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "count"]

    fig = px.bar(value_counts, x=column, y="count")
    return fig


def create_line_chart(df, column):
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "count"]

    fig = px.line(value_counts, x=column, y="count")
    return fig


def create_scatter_plot(df, col1, col2):
    fig = px.scatter(df, x=col1, y=col2)
    return fig


def create_correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=["number"])

    corr = numeric_df.corr()

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.round(2).values,
        showscale=True
    )

    return fig
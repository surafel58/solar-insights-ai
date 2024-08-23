import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display  # Import the display function from IPython

def load_dataset(file_path):
    return pd.read_csv(file_path)

def display_head(df, n=5):
    print(f"First {n} rows of the dataset:")
    display(df.head(n))

def check_missing_values(df):
    print("\nMissing Values in Each Column:")
    missing_values = df.isnull().sum()
    display(missing_values)
    return missing_values

def drop_column(df, column_name):
    df.drop(columns=[column_name], inplace=True)

def replace_negative_values(df, columns):
    for column in columns:
        df[column] = df[column].apply(lambda x: max(x, 0))

def plot_boxplot(df, columns, title):
    plt.figure(figsize=(10, 5))
    df.boxplot(column=columns)
    plt.title(title)
    plt.show()

def cap_outliers(df, columns, lower_percentile, upper_percentile):
    lower_cap = df[columns].quantile(lower_percentile)
    upper_cap = df[columns].quantile(upper_percentile)
    for column in columns:
        df[column] = df[column].clip(lower_cap[column], upper_cap[column])

def display_summary_statistics(df):
    print("\nSummary Statistics after Data Quality Check:")
    display(df.describe())
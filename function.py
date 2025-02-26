import pandas as pd

df = pd.read_csv('data.csv')

# Use an immutable variable for the default argument
def better_add_column(values, df=):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
        If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    # Update the function to create a default DataFrame
    if df is None:
        df = pd.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
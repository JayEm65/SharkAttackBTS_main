"""
# initial_setup.py

This module contains functions for the initial setup of the DataFrame such as:
- Loading data from a specified URL
- Providing an initial preview of the DataFrame
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime

def load_data(url):
    """
    Load data from a specified URL into a DataFrame.

    Parameters:
    url (str): The URL to the data file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_excel(url)

def initial_preview(df):
    """
    Provide an initial preview of the DataFrame including head, info, describe, and columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.

    Returns:
    None: Prints the preview of the DataFrame.
    """
    print("head:")
    print(df.head())
    print("\ninfo:")
    df.info()
    print("\ndescribe:")
    print(df.describe())
    print("\ncolumns:")
    print(df.columns.tolist())
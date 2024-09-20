"""
# column_cleaning.py

This module contains functions for cleaning specific columns within the DataFrame such as:
- Cleaning the 'fatal' column
- Cleaning the 'sex' column
- Cleaning the 'type' column
- Cleaning the 'time' column
- Cleaning the 'age' column
"""

import pandas as pd
import re

def clean_fatal_column(df):
    """
    Clean the 'fatal' column by stripping whitespace, converting to lowercase, 
    mapping values to 'n' and 'y', and filling NaNs with the mode value.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'fatal' column.

    Returns:
    pd.DataFrame: DataFrame with cleaned 'fatal' column.
    """
    value_map = {'n': 'n', 'y': 'y'}
    df['fatal'] = df['fatal'].str.strip().str.lower().map(value_map)
    fatal_mode = df['fatal'].mode()[0]
    df['fatal'] = df['fatal'].fillna(fatal_mode)
    return df

def clean_sex_column(df):
    """
    Clean the 'sex' column by stripping whitespace, converting to lowercase, replacing invalid entries, 
    and filling NaNs with 'unknown'.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'sex' column.

    Returns:
    pd.DataFrame: DataFrame with cleaned 'sex' column.
    """
    df['sex'] = df['sex'].str.strip().str.lower()
    invalid_entries = ['lli', 'm x 2', 'n', '.']
    for entry in invalid_entries:
        df['sex'] = df['sex'].replace(entry, 'unknown')
    df['sex'] = df['sex'].fillna('unknown')
    return df

def clean_type_column(df):
    """
    Clean the 'type' column by removing invalid entries and filling NaNs with 'unknown'.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'type' column.

    Returns:
    pd.DataFrame: DataFrame with cleaned 'type' column.
    """
    df = df[df['type'] != 'invalid']
    df['type'] = df['type'].fillna('unknown')
    return df

def validate_time_format(time_str):
    """
    Validate the 'time' format ensuring it matches the "hhmm" pattern.

    Parameters:
    time_str (str): Time string to validate.

    Returns:
    str or None: Validated time string or None if invalid.
    """
    pattern = r'^\d{2}h\d{2}$'
    if re.match(pattern, time_str):
        return time_str
    else:
        return None

def clean_time_column(df):
    """
    Clean the 'time' column by validating its format, converting valid times to numeric,
    and filling NaNs with the mean value.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'time' column.

    Returns:
    pd.DataFrame: DataFrame with cleaned 'time' column.
    """
    df['time'] = df['time'].astype(str)
    df['time'] = df['time'].apply(lambda x: x.replace('h', '') if validate_time_format(x) else None)
    df['time'] = pd.to_numeric(df['time'], errors='coerce')
    mean_time = df['time'].mean()
    df['time'] = df['time'].fillna(round(mean_time))
    df['time'] = df['time'].astype(int)
    return df

def clean_age_column(df):
    """
    Clean the 'age' column by converting to numeric, filling NaNs with the mean value, 
    and rounding to the nearest integer.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'age' column.

    Returns:
    pd.DataFrame: DataFrame with cleaned 'age' column.
    """
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    age_mean = df['age'].mean()
    df['age'] = df['age'].fillna(age_mean)
    df['age'] = df['age'].round(0)
    return df
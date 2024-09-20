"""
# data_cleaning.py

This module contains functions for initial cleaning and preparation of the DataFrame such as:
- Dropping unused columns and duplicates
- Filtering rows by year
- Removing undesired types
- Renaming columns
"""

import pandas as pd

def drop_unused_columns(df):
    """
    Drop unused columns and remove duplicates in the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.

    Returns:
    pd.DataFrame: DataFrame with selected columns dropped and duplicates removed.
    """
    columns_to_drop = ["Source", "Location", "Injury", "Name", "pdf",
                       "href formula", "href", "Case Number",
                       "Case Number.1", "original order",
                       "Unnamed: 21", "Unnamed: 22", "Species "]
    return df.drop(columns=columns_to_drop).drop_duplicates().reset_index(drop=True)

def filter_by_year(df):
    """
    Filter rows with Year greater than 1800.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.

    Returns:
    pd.DataFrame: Filtered DataFrame with rows having Year > 1800.
    """
    return df[df["Year"] > 1800]

def remove_undesired_types(df):
    """
    Remove rows with undesired types.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.

    Returns:
    pd.DataFrame: DataFrame with specified undesired types removed.
    """
    undesired_types = ["Questionable", "Boat", "Provoked", "Provoked ", "?",
                       "Unverified", "Under investigation", "Unconfirmed"]
    return df[~df["Type"].isin(undesired_types)]

def rename_columns(df):
    """
    Rename and reformat columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.

    Returns:
    pd.DataFrame: DataFrame with cleaned column names.
    """
    df.columns = [col.strip().replace(" ", "_").replace(".", "").lower() for col in df.columns]
    df.rename(columns={'unnamed:_11': 'fatal'}, inplace=True)
    return df

def initial_cleaning(df):
    """
    Perform initial cleaning tasks including dropping unused columns, filtering by year,
    removing undesired types, and renaming columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the raw data.

    Returns:
    pd.DataFrame: DataFrame after initial cleaning.
    """
    df = drop_unused_columns(df)
    df = filter_by_year(df)
    df = remove_undesired_types(df)
    df = rename_columns(df)
    return df
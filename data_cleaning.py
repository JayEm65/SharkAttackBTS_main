# data_cleaning.py

import pandas as pd

def drop_unused_columns(df):
    columns_to_drop = ["Source", "Location", "Injury", "Name", "pdf",
                       "href formula", "href", "Case Number",
                       "Case Number.1", "original order",
                       "Unnamed: 21", "Unnamed: 22", "Species "]
    return df.drop(columns=columns_to_drop).drop_duplicates().reset_index(drop=True)

def filter_by_year(df):
    return df[df["Year"] > 1800]

def remove_undesired_types(df):
    undesired_types = ["Questionable", "Boat", "Provoked", "Provoked ", "?",
                       "Unverified", "Under investigation", "Unconfirmed"]
    return df[~df["Type"].isin(undesired_types)]

def rename_columns(df):
    df.columns = [col.strip().replace(" ", "_").replace(".", "").lower() for col in df.columns]
    df.rename(columns={'unnamed:_11': 'fatal'}, inplace=True)
    return df

def initial_cleaning(df):
    df = drop_unused_columns(df)
    df = filter_by_year(df)
    df = remove_undesired_types(df)
    df = rename_columns(df)
    return df
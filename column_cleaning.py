# column_cleaning.py

import pandas as pd
import re

def clean_fatal_column(df):
    value_map = {'n': 'n', 'y': 'y'}
    df['fatal'] = df['fatal'].str.strip().str.lower().map(value_map)
    fatal_mode = df['fatal'].mode()[0]
    df['fatal'] = df['fatal'].fillna(fatal_mode)
    return df

def clean_sex_column(df):
    df['sex'] = df['sex'].str.strip().str.lower()
    invalid_entries = ['lli', 'm x 2', 'n', '.']
    for entry in invalid_entries:
        df['sex'] = df['sex'].replace(entry, 'unknown')
    df['sex'] = df['sex'].fillna('unknown')
    return df

def clean_type_column(df):
    df = df[df['type'] != 'invalid']
    df['type'] = df['type'].fillna('unknown')
    return df

def validate_time_format(time_str):
    pattern = r'^\d{2}h\d{2}$'
    if re.match(pattern, time_str):
        return time_str
    else:
        return None

def clean_time_column(df):
    df['time'] = df['time'].astype(str)
    df['time'] = df['time'].apply(lambda x: x.replace('h', '') if validate_time_format(x) else None)
    df['time'] = pd.to_numeric(df['time'], errors='coerce')
    mean_time = df['time'].mean()
    df['time'] = df['time'].fillna(round(mean_time))
    df['time'] = df['time'].astype(int)
    return df

def clean_age_column(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    age_mean = df['age'].mean()
    df['age'] = df['age'].fillna(age_mean)
    df['age'] = df['age'].round(0)
    return df
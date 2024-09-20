"""
# feature_engineering.py

This module contains functions for feature engineering such as:
- Reformatting dates
- Adding seasonality information
- Handling NaNs in specific columns
"""

import pandas as pd
import re
from datetime import datetime

def reformat_date_adjusted(date_str):
    date_str = str(date_str).strip()
    if not date_str or date_str.lower() == 'nan':
        return "invalid-date"
    
    date_str = re.sub(r'^Reported\s+', '', date_str, flags=re.IGNORECASE)
    date_str = re.sub(r'\s*-\s*|\s+', ' ', date_str)
    
    try:
        if re.search(r'\d{2}\s\w+\s\d{4}', date_str):
            for fmt in ("%d %b %Y", "%d %B %Y"):
                try:
                    parsed_date = datetime.strptime(date_str, fmt)
                    return parsed_date.strftime("%m-%Y")
                except ValueError:
                    pass
        elif re.search(r'\w+\s\d{4}', date_str):
            for fmt in ("%b %Y", "%B %Y"):
                try:
                    parsed_date = datetime.strptime(date_str, fmt)
                    return parsed_date.strftime("%m-%Y")
                except ValueError:
                    pass
        elif re.match(r'\d{4}$', date_str):
            return datetime.strptime(date_str, "%Y").strftime("%Y") + "-00"
    except Exception as e:
        print(f"Error processing date '{date_str}': {e}")
    
    return "Unknown"

def apply_date_reformatting(df):
    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].apply(reformat_date_adjusted)
    return df

def get_seasonality(formatted_date):
    try:
        month = int(formatted_date.split('-')[0])
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"
        else:
            return "Unknown"
    except:
        return "Unknown"

def apply_seasonality(df):
    df['seasonality'] = df['date'].apply(get_seasonality)
    return df

def handle_activity_location_na(df):
    # Handle 'activity' column NaNs
    df.loc[df['activity'].isna(), 'activity'] = 'unknown'
    
    # Handle 'state' column NaNs
    df.loc[df['state'].isna(), 'state'] = 'Unknown'
    
    # Create 'location' column by joining 'country' and 'state'
    df['location'] = df['country'].astype(str) + ', ' + df['state'].astype(str)
    
    return df
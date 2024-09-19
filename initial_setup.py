# initial_setup.py

import pandas as pd
import numpy as np
import re
from datetime import datetime

def load_data(url):
    return pd.read_excel(url)

def initial_preview(df):
    print("head:")
    print(df.head())
    print("\ninfo:")
    df.info()
    print("\ndescribe:")
    print(df.describe())
    print("\ncolumns:")
    print(df.columns.tolist())
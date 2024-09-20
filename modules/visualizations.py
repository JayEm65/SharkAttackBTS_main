"""
# visualizations.py

This module contains functions for creating visualizations such as:
- Plotting a seasonality pie chart
- Plotting a bar chart for type distribution
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_seasonality_pie_chart(season_counts):
    """
    Plot a pie chart displaying the seasonality percentage of shark attacks.

    Parameters:
    season_counts (pd.Series): Series containing the counts of shark attacks for each season.

    Returns:
    None: Displays the pie chart.
    """
    plt.figure(figsize=(8, 8))
    season_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm", len(season_counts)))
    plt.title('Seasonality Percentage')
    plt.ylabel('')
    plt.show()

def plot_type_distribution_bar(df_copy):
    """
    Plot a bar chart displaying the distribution of different types of shark attacks.

    Parameters:
    df_copy (pd.DataFrame): DataFrame containing the cleaned data.

    Returns:
    None: Displays the bar chart.
    """
    plt.figure(figsize=(12, 6))
    sns.countplot(x='type', data=df_copy, 
                  order=df_copy['type'].value_counts().index, 
                  hue='type', palette='pastel', 
                  dodge=False, legend=False)
    plt.title('Type Distribution of Shark Attacks (Bar Plot)')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
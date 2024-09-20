# visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_seasonality_pie_chart(season_counts):
    plt.figure(figsize=(8, 8))
    season_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm", len(season_counts)))
    plt.title('Seasonality Percentage')
    plt.ylabel('')
    plt.show()

def plot_type_distribution_bar(df_copy):
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
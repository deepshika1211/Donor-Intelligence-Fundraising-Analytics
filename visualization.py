"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
This module creates professional visualizations for donor
analytics and fundraising insights.
---------------------------------------------------------------
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
from logger import logger


# Global Plot Style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["figure.dpi"] = 120


def save_plot(filename):
    """
    Save plot into output/charts folder.
    """
    os.makedirs("output/charts", exist_ok=True)

    plt.tight_layout()
    plt.savefig(f"output/charts/{filename}.png")
    plt.show()
    
def donation_distribution(df):
    """
    Histogram showing the distribution of donation amounts.
    """

    plt.figure()

    sns.histplot(
        data=df,
        x="Gift Amount",
        bins=30,
        kde=True,
        color="royalblue"
    )

    plt.title("Distribution of Donation Amounts")
    plt.xlabel("Gift Amount")
    plt.ylabel("Frequency")

    save_plot("donation_distribution")
    
def top_colleges(df):
    """
    Bar chart of top 10 colleges by donation amount.
    """

    data = (
        df.groupby("College")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure()

    sns.barplot(
        x=data.values,
        y=data.index,
        hue=data.index,
        legend=False,
        palette="viridis"
    )

    plt.title("Top 10 Colleges by Total Donations")
    plt.xlabel("Total Donation Amount")
    plt.ylabel("College")

    save_plot("top_colleges") 
    
def monthly_trend(df):
    """
    Monthly donation trend.
    """

    monthly = (
        df.groupby(["Year", "Month"])["Gift Amount"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(14, 6))

    sns.lineplot(
        data=monthly,
        x=range(len(monthly)),
        y="Gift Amount",
        marker="o"
    )

    plt.title("Monthly Donation Trend")
    plt.xlabel("Month Index")
    plt.ylabel("Donation Amount")

    save_plot("monthly_trend") 

def top_states(df):
    """
    Top 10 states by total donation amount.
    """

    data = (
        df.groupby("State")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure()

    sns.barplot(
        x=data.values,
        y=data.index,
        hue=data.index,
        legend=False,
        palette="rocket"
    )

    plt.title("Top 10 States by Total Donations")
    plt.xlabel("Total Donation Amount")
    plt.ylabel("State")

    save_plot("top_states")

def top_cities(df):
    """
    Top 10 cities by total donation amount.
    """

    data = (
        df.groupby("City")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure()

    sns.barplot(
        x=data.values,
        y=data.index,
        hue=data.index,
        legend=False,
        palette="crest"
    )

    plt.title("Top 10 Cities by Total Donations")
    plt.xlabel("Total Donation Amount")
    plt.ylabel("City")

    save_plot("top_cities")

def quarterly_trend(df):
    """
    Quarterly donation trend.
    """

    data = (
        df.groupby("Quarter")["Gift Amount"]
        .sum()
        .reset_index()
    )

    plt.figure()

    sns.lineplot(
        data=data,
        x="Quarter",
        y="Gift Amount",
        marker="o"
    )

    plt.title("Quarterly Donation Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Total Donation Amount")

    save_plot("quarterly_trend") 

def donation_category(df):
    """
    Distribution of donation categories.
    """

    plt.figure(figsize=(8,8))

    data = df["Donation Category"].value_counts()

    plt.pie(
        data.values,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=140
    )

    plt.title("Donation Category Distribution")

    save_plot("donation_category") 
    
def donation_boxplot(df):
    """
    Detect outliers in donation amounts.
    """

    plt.figure()

    sns.boxplot(
        x=df["Gift Amount"]
    )

    plt.title("Donation Amount Outlier Detection")

    save_plot("donation_boxplot") 

def correlation_heatmap(df):
    """
    Correlation heatmap for numerical variables.
    """

    numeric = df.select_dtypes(include="number")

    plt.figure(figsize=(10,8))

    sns.heatmap(
        numeric.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    save_plot("correlation_heatmap") 
    
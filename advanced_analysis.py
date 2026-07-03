"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Advanced analytics module for fundraising insights.
---------------------------------------------------------------
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from logger import logger

sns.set_theme(style="whitegrid")


def save_plot(filename):
    """
    Save plots to output/charts.
    """
    os.makedirs("output/charts", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"output/charts/{filename}.png")
    plt.show()

def pareto_analysis(df):
    """
    Determine whether a small percentage of donors
    contribute most of the donations.
    """

    donor_totals = (
        df.groupby("Prospect ID")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    donor_totals["Cumulative Donation"] = donor_totals["Gift Amount"].cumsum()

    total = donor_totals["Gift Amount"].sum()

    donor_totals["Cumulative %"] = (
        donor_totals["Cumulative Donation"] / total
    ) * 100

    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.bar(
        donor_totals.index,
        donor_totals["Gift Amount"],
        color="steelblue"
    )

    ax1.set_ylabel("Donation Amount")

    ax2 = ax1.twinx()

    ax2.plot(
        donor_totals.index,
        donor_totals["Cumulative %"],
        color="red",
        linewidth=2
    )

    ax2.set_ylabel("Cumulative %")

    plt.title("Pareto Analysis of Donor Contributions")

    save_plot("pareto_analysis")

def cumulative_donation_trend(df):
    """
    Running total of donations over time.
    """

    trend = (
        df.groupby("Gift Date")["Gift Amount"]
        .sum()
        .sort_index()
        .cumsum()
    )

    plt.figure(figsize=(12,6))

    plt.plot(
        trend.index,
        trend.values,
        linewidth=3
    )

    plt.title("Cumulative Donation Trend")
    plt.xlabel("Date")
    plt.ylabel("Running Total Donation")

    save_plot("cumulative_trend")
    
def major_analysis(df):
    """
    Top majors by donation amount.
    """

    major = (
        df.groupby("Major")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=major.values,
        y=major.index,
        hue=major.index,
        legend=False,
        palette="viridis"
    )

    plt.title("Top 10 Majors by Donation Amount")
    plt.xlabel("Donation Amount")
    plt.ylabel("Major")

    save_plot("major_analysis")

def allocation_analysis(df):
    """
    Analyze donations by gift allocation.
    """

    allocation = (
        df.groupby("Gift Allocation")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=allocation.values,
        y=allocation.index,
        hue=allocation.index,
        legend=False,
        palette="mako"
    )

    plt.title("Gift Allocation Analysis")
    plt.xlabel("Donation Amount")
    plt.ylabel("Gift Allocation")

    save_plot("allocation_analysis")
    
def allocation_treemap(df):
    """
    Treemap of Gift Allocation and Allocation Subcategory.
    """

    fig = px.treemap(
        df,
        path=["Gift Allocation", "Allocation Subcategory"],
        values="Gift Amount",
        color="Gift Amount",
        color_continuous_scale="Blues",
        title="Gift Allocation Treemap"
    )

    fig.write_html("output/charts/allocation_treemap.html")
    fig.show()
    
def donation_sunburst(df):
    """
    Sunburst chart showing donation hierarchy.
    """

    fig = px.sunburst(
        df,
        path=[
            "College",
            "Gift Allocation",
            "Allocation Subcategory"
        ],
        values="Gift Amount",
        color="Gift Amount",
        color_continuous_scale="Viridis",
        title="Donation Hierarchy"
    )

    fig.write_html("output/charts/donation_sunburst.html")
    fig.show()
    
def yearly_growth(df):
    """
    Analyze yearly donation growth.
    """

    yearly = (
        df.groupby("Year")["Gift Amount"]
        .sum()
        .reset_index()
    )

    yearly["Growth %"] = (
        yearly["Gift Amount"]
        .pct_change() * 100
    )

    print("\nYear-over-Year Growth")
    print("-" * 60)
    print(yearly)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=yearly,
        x="Year",
        y="Gift Amount",
        palette="viridis"
    )

    plt.title("Yearly Donation Amount")
    plt.xlabel("Year")
    plt.ylabel("Total Donation Amount")

    save_plot("yearly_growth")
    
def allocation_subcategory_analysis(df):
    """
    Top allocation subcategories by donation amount.
    """

    allocation = (
        df.groupby("Allocation Subcategory")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=allocation.values,
        y=allocation.index,
        hue=allocation.index,
        legend=False,
        palette="rocket"
    )

    plt.title("Top Allocation Subcategories")
    plt.xlabel("Donation Amount")
    plt.ylabel("Allocation Subcategory")

    save_plot("allocation_subcategory")
    
def executive_dashboard(df):
    """
    Print executive-level fundraising KPIs.
    """

    print("\n")
    print("=" * 70)
    print("        DONOR INTELLIGENCE EXECUTIVE DASHBOARD")
    print("=" * 70)

    print(f"Total Donations      : ${df['Gift Amount'].sum():,.2f}")
    print(f"Average Donation     : ${df['Gift Amount'].mean():,.2f}")
    print(f"Highest Donation     : ${df['Gift Amount'].max():,.2f}")
    print(f"Total Donors         : {df['Prospect ID'].nunique()}")
    print(f"Total Colleges       : {df['College'].nunique()}")
    print(f"Total States         : {df['State'].nunique()}")

    top_state = (
        df.groupby("State")["Gift Amount"]
        .sum()
        .idxmax()
    )

    top_college = (
        df.groupby("College")["Gift Amount"]
        .sum()
        .idxmax()
    )

    top_major = (
        df.groupby("Major")["Gift Amount"]
        .sum()
        .idxmax()
    )

    top_allocation = (
        df.groupby("Gift Allocation")["Gift Amount"]
        .sum()
        .idxmax()
    )

    print(f"Top State            : {top_state}")
    print(f"Top College          : {top_college}")
    print(f"Top Major            : {top_major}")
    print(f"Top Allocation       : {top_allocation}")

    print("=" * 70)
    
    logger.info("Advanced analytics completed.")
    
    


   
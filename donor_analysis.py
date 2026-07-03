"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
This module performs donor analysis and generates
business insights.
---------------------------------------------------------------
"""

import os
import pandas as pd


def save_report(df, filename):
    """
    Save a DataFrame as a CSV report.
    """
    os.makedirs("output/reports", exist_ok=True)
    path = f"output/reports/{filename}.csv"
    df.to_csv(path, index=False)
    print(f"Report saved: {path}")

def top_donors(df):
    """
    Find the top 20 donors based on total donation amount.
    """

    donors = (
        df.groupby("Prospect ID")
        .agg(
            Total_Donation=("Gift Amount", "sum"),
            Number_of_Gifts=("Gift Amount", "count"),
            Average_Donation=("Gift Amount", "mean")
        )
        .sort_values("Total_Donation", ascending=False)
        .head(20)
        .reset_index()
    )

    print("\nTop 20 Donors")
    print("-" * 60)
    print(donors)

    save_report(donors, "top_20_donors")

    return donors

def college_performance(df):
    """
    Analyze donation performance by college.
    """

    colleges = (
        df.groupby("College")
        .agg(
            Total_Donation=("Gift Amount", "sum"),
            Average_Donation=("Gift Amount", "mean"),
            Number_of_Gifts=("Gift Amount", "count")
        )
        .sort_values("Total_Donation", ascending=False)
        .reset_index()
    )

    print("\nCollege Performance")
    print("-" * 60)
    print(colleges.head(10))

    save_report(colleges, "college_performance")

    return colleges

def state_performance(df):
    """
    Analyze donation performance by state.
    """

    states = (
        df.groupby("State")
        .agg(
            Total_Donation=("Gift Amount", "sum"),
            Average_Donation=("Gift Amount", "mean"),
            Number_of_Gifts=("Gift Amount", "count")
        )
        .sort_values("Total_Donation", ascending=False)
        .reset_index()
    )

    print("\nState Performance")
    print("-" * 60)
    print(states.head(10))

    save_report(states, "state_performance")

    return states

def city_performance(df):
    """
    Analyze donation performance by city.
    """

    cities = (
        df.groupby("City")
        .agg(
            Total_Donation=("Gift Amount", "sum"),
            Average_Donation=("Gift Amount", "mean"),
            Number_of_Gifts=("Gift Amount", "count")
        )
        .sort_values("Total_Donation", ascending=False)
        .reset_index()
    )

    print("\nCity Performance")
    print("-" * 60)
    print(cities.head(10))

    save_report(cities, "city_performance")

    return cities

def largest_donations(df):
    """
    Display the 20 largest individual donations.
    """

    largest = (
        df.sort_values("Gift Amount", ascending=False)
        .head(20)
    )

    print("\nLargest Individual Donations")
    print("-" * 60)
    print(largest[["Prospect ID", "Gift Amount", "Gift Date", "College"]])

    save_report(largest, "largest_donations")

    return largest

def business_insights(df):
    """
    Print key business insights.
    """

    print("\n" + "=" * 60)
    print("BUSINESS INSIGHTS")
    print("=" * 60)

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

    avg_donation = df["Gift Amount"].mean()

    print(f"Top Donating State   : {top_state}")
    print(f"Top Performing College : {top_college}")
    print(f"Average Donation     : ${avg_donation:,.2f}")

    repeat = (
        df.groupby("Prospect ID")
        .size()
        .gt(1)
        .sum()
    )

    print(f"Repeat Donors        : {repeat}")
    

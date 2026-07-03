"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Business Intelligence Module
---------------------------------------------------------------
"""

import os
import pandas as pd
from logger import logger

def executive_kpis(df):

    print("\n")
    print("=" * 70)
    print("EXECUTIVE KPIs")
    print("=" * 70)

    total = df["Gift Amount"].sum()

    avg = df["Gift Amount"].mean()

    median = df["Gift Amount"].median()

    donors = df["Prospect ID"].nunique()

    colleges = df["College"].nunique()

    states = df["State"].nunique()

    print(f"Total Donations     : ${total:,.2f}")
    print(f"Average Donation    : ${avg:,.2f}")
    print(f"Median Donation     : ${median:,.2f}")
    print(f"Unique Donors       : {donors}")
    print(f"Colleges            : {colleges}")
    print(f"States              : {states}")
    
def top_performers(df):

    print("\n")
    print("=" * 70)
    print("TOP PERFORMERS")
    print("=" * 70)

    state = (
        df.groupby("State")["Gift Amount"]
        .sum()
        .idxmax()
    )

    college = (
        df.groupby("College")["Gift Amount"]
        .sum()
        .idxmax()
    )

    major = (
        df.groupby("Major")["Gift Amount"]
        .sum()
        .idxmax()
    )

    allocation = (
        df.groupby("Gift Allocation")["Gift Amount"]
        .sum()
        .idxmax()
    )

    print(f"Top State       : {state}")
    print(f"Top College     : {college}")
    print(f"Top Major       : {major}")
    print(f"Top Allocation  : {allocation}")
    
def repeat_donor_analysis(df):

    donor_counts = df.groupby("Prospect ID").size()

    repeat = (donor_counts > 1).sum()

    one_time = (donor_counts == 1).sum()

    rate = repeat / donor_counts.shape[0] * 100

    print("\n")
    print("=" * 70)
    print("DONOR RETENTION")
    print("=" * 70)

    print(f"Repeat Donors : {repeat}")
    print(f"One-time Donors : {one_time}")
    print(f"Retention Rate : {rate:.2f}%") 
    
def recommendations(df):

    print("\n")
    print("=" * 70)
    print("STRATEGIC RECOMMENDATIONS")
    print("=" * 70)

    print("• Focus fundraising campaigns in the highest-performing states.")
    print("• Strengthen alumni engagement for top-performing colleges.")
    print("• Encourage recurring donations from one-time donors.")
    print("• Promote underfunded allocation categories.")
    print("• Launch campaigns before historically strong donation periods.")
    
def save_summary(df):

    os.makedirs("output/reports", exist_ok=True)

    report_path = "output/reports/business_summary.txt"

    with open(report_path, "w") as file:

        file.write("DONOR INTELLIGENCE BUSINESS REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Total Donations : ${df['Gift Amount'].sum():,.2f}\n")
        file.write(f"Average Donation : ${df['Gift Amount'].mean():,.2f}\n")
        file.write(f"Unique Donors : {df['Prospect ID'].nunique()}\n")
        file.write(f"Top State : {df.groupby('State')['Gift Amount'].sum().idxmax()}\n")
        file.write(f"Top College : {df.groupby('College')['Gift Amount'].sum().idxmax()}\n")

    print(f"\nBusiness report saved to: {report_path}")
    
logger.info("Business Intelligence module completed.")
"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
This module loads, cleans, preprocesses, and enriches the
donation dataset for further analysis.
---------------------------------------------------------------
"""

import os
import pandas as pd
import numpy as np
from logger import logger


# ============================================================
# Load Dataset
# ============================================================

def load_dataset(file_path):
    """
    Load the donation dataset.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    DataFrame
    """

    try:
        df = pd.read_csv(file_path)

        print("=" * 60)
        logger.info("Dataset Loaded Successfully")
        print("=" * 60)

        return df

    except FileNotFoundError:
        print("Error: Dataset not found.")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# ============================================================
# Dataset Information
# ============================================================

def dataset_info(df):

    print("\nDataset Information")
    print("-" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names\n")
    print(df.columns.tolist())


# ============================================================
# Missing Values
# ============================================================

def check_missing_values(df):

    print("\nMissing Values")
    print("-" * 60)

    missing = df.isnull().sum()

    print(missing)

    return missing


# ============================================================
# Clean Dataset
# ============================================================

def clean_dataset(df):

    print("\nCleaning Dataset...")
    print("-" * 60)

    duplicates = df.duplicated().sum()

    print(f"Duplicate Rows Found : {duplicates}")

    df = df.drop_duplicates()

    # Convert Gift Date into datetime
    df["Gift Date"] = pd.to_datetime(
        df["Gift Date"],
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["Gift Date"])

    # Remove negative donation amounts
    df = df[df["Gift Amount"] > 0]

    return df


# ============================================================
# Feature Engineering
# ============================================================

def feature_engineering(df):

    print("\nCreating New Features...")
    print("-" * 60)

    df["Year"] = df["Gift Date"].dt.year

    df["Month"] = df["Gift Date"].dt.month_name()

    df["Quarter"] = df["Gift Date"].dt.quarter

    df["Weekday"] = df["Gift Date"].dt.day_name()

    df["Weekend"] = np.where(
        df["Weekday"].isin(["Saturday", "Sunday"]),
        "Yes",
        "No"
    )

    bins = [0, 100, 500, 1000, 5000, float("inf")]

    labels = [
        "Small",
        "Medium",
        "Large",
        "Premium",
        "VIP"
    ]

    df["Donation Category"] = pd.cut(
        df["Gift Amount"],
        bins=bins,
        labels=labels
    )

    return df


# ============================================================
# Business KPIs
# ============================================================

def calculate_kpis(df):

    print("\nBusiness KPIs")
    print("=" * 60)

    print(f"Total Donation Amount : ${df['Gift Amount'].sum():,.2f}")

    print(f"Average Donation      : ${df['Gift Amount'].mean():,.2f}")

    print(f"Median Donation       : ${df['Gift Amount'].median():,.2f}")

    print(f"Highest Donation      : ${df['Gift Amount'].max():,.2f}")

    print(f"Lowest Donation       : ${df['Gift Amount'].min():,.2f}")

    print(f"Unique Donors         : {df['Prospect ID'].nunique()}")

    print(f"Unique Colleges       : {df['College'].nunique()}")

    print(f"Unique States         : {df['State'].nunique()}")

    print(f"Date Range            : {df['Gift Date'].min().date()}  ->  {df['Gift Date'].max().date()}")


# ============================================================
# Save Cleaned Dataset
# ============================================================

def save_clean_data(df):

    os.makedirs("output", exist_ok=True)

    output_path = "output/cleaned_data.csv"

    df.to_csv(output_path, index=False)

    print("\nCleaned dataset saved successfully.")

    print(output_path)
    
    logger.info("Cleaned dataset saved successfully.")
    


# ============================================================
# Complete Preprocessing Pipeline
# ============================================================

def preprocess(file_path):

    df = load_dataset(file_path)

    if df is None:
        return None

    dataset_info(df)

    check_missing_values(df)

    df = clean_dataset(df)

    df = feature_engineering(df)

    calculate_kpis(df)

    save_clean_data(df)

    logger.info("Preprocessing pipeline completed.")

    return df

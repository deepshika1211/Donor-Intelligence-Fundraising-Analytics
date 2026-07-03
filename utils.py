"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Utility functions used across the project.
---------------------------------------------------------------
"""

import os
import pandas as pd


# ============================================================
# Create Directory
# ============================================================

def create_directory(path):
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    path : str
        Folder path to create.
    """
    os.makedirs(path, exist_ok=True)


# ============================================================
# Format Currency
# ============================================================

def format_currency(amount):
    """
    Format a numeric value as currency.

    Parameters
    ----------
    amount : float

    Returns
    -------
    str
    """
    return f"${amount:,.2f}"


# ============================================================
# Print Section Heading
# ============================================================

def print_heading(title):
    """
    Print a formatted heading.

    Parameters
    ----------
    title : str
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ============================================================
# Save DataFrame
# ============================================================

def save_dataframe(df, filename):
    """
    Save a DataFrame inside the output/reports folder.

    Parameters
    ----------
    df : pandas.DataFrame
    filename : str
    """
    create_directory("output/reports")

    output_path = os.path.join("output", "reports", filename)

    df.to_csv(output_path, index=False)

    print(f"Report saved: {output_path}")

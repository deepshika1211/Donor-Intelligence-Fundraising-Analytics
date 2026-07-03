"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Project Configuration File
---------------------------------------------------------------
"""

import os

# ===============================
# Paths
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "data",
    "advancement_donations_and_giving_demo.csv"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

CHART_DIR = os.path.join(OUTPUT_DIR, "charts")

REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

LOG_DIR = os.path.join(OUTPUT_DIR, "logs")


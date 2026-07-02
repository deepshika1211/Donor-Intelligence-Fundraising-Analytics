"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepti Yerrangi

Description:
Main file to run the preprocessing pipeline.
---------------------------------------------------------------
"""

from preprocessing import preprocess


# Path to the dataset
FILE_PATH = "data/advancement_donations_and_giving_demo.csv"


def main():
    """
    Main function to run the preprocessing pipeline.
    """
    df = preprocess(FILE_PATH)

    if df is not None:
        print("\nPreprocessing Completed Successfully!")
    else:
        print("\nPreprocessing Failed.")


# Run the program
if __name__ == "__main__":
    main()
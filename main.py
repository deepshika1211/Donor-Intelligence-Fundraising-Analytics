"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Main file to execute the complete analytics pipeline.
---------------------------------------------------------------
"""

# ============================================================
# Imports
# ============================================================

from config import DATASET_PATH
from logger import logger

from preprocessing import preprocess
from report import generate_html_report
from dashboard import generate_dashboard

from visualization import (
    donation_distribution,
    top_colleges,
    monthly_trend,
    top_states,
    top_cities,
    quarterly_trend,
    donation_category,
    donation_boxplot,
    correlation_heatmap
)

from donor_analysis import (
    top_donors,
    college_performance,
    state_performance,
    city_performance,
    largest_donations,
    business_insights
)

from advanced_analysis import (
    pareto_analysis,
    cumulative_donation_trend,
    major_analysis,
    allocation_analysis,
    allocation_treemap,
    donation_sunburst,
    yearly_growth,
    allocation_subcategory_analysis,
    executive_dashboard
)

from business_intelligence import (
    executive_kpis,
    top_performers,
    repeat_donor_analysis,
    recommendations,
    save_summary
)


# ============================================================
# Main Function
# ============================================================

def main():

    print("=" * 60)
    print("DONOR INTELLIGENCE & FUNDRAISING ANALYTICS")
    print("=" * 60)

    # --------------------------------------------------------
    # Data Preprocessing
    # --------------------------------------------------------

    df = preprocess(DATASET_PATH)

    if df is None:
        print("Preprocessing Failed.")
        logger.error("Preprocessing failed.")
        return

    logger.info("Preprocessing completed.")

    # --------------------------------------------------------
    # Data Visualization
    # --------------------------------------------------------

    donation_distribution(df)
    top_colleges(df)
    monthly_trend(df)
    top_states(df)
    top_cities(df)
    quarterly_trend(df)
    donation_category(df)
    donation_boxplot(df)
    correlation_heatmap(df)

    print("\nAll Visualizations Generated Successfully!")
    logger.info("Visualization module completed.")

    # --------------------------------------------------------
    # Donor Analysis
    # --------------------------------------------------------

    top_donors(df)
    college_performance(df)
    state_performance(df)
    city_performance(df)
    largest_donations(df)
    business_insights(df)

    print("\nDonor Analysis Completed Successfully!")
    logger.info("Donor analysis completed.")

    # --------------------------------------------------------
    # Advanced Analytics
    # --------------------------------------------------------

    pareto_analysis(df)
    cumulative_donation_trend(df)
    major_analysis(df)
    allocation_analysis(df)
    allocation_treemap(df)
    donation_sunburst(df)
    yearly_growth(df)
    allocation_subcategory_analysis(df)
    executive_dashboard(df)

    print("\nAdvanced Analytics Completed Successfully!")
    logger.info("Advanced analytics completed.")

    # --------------------------------------------------------
    # Business Intelligence
    # --------------------------------------------------------

    executive_kpis(df)
    top_performers(df)
    repeat_donor_analysis(df)
    recommendations(df)
    save_summary(df)

    print("\nBusiness Intelligence Completed Successfully!")
    logger.info("Business Intelligence completed.")

    # --------------------------------------------------------
    # Generate HTML Report
    # --------------------------------------------------------

    generate_html_report(df)

    print("\nHTML Report Generated Successfully!")
    logger.info("HTML report generated successfully.")

    generate_dashboard(df)

    print("\nDashboard Generated Successfully!")
    logger.info("Dashboard generated successfully.")
    
    print("\nProject Executed Successfully!")
    logger.info("Project execution completed.")
    

# ============================================================
# Run Project
# ============================================================

if __name__ == "__main__":
    main()
   

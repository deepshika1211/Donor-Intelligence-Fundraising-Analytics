"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Generates an HTML report summarizing the project results.
---------------------------------------------------------------
"""

import os
from logger import logger


def generate_html_report(df):

    os.makedirs("output", exist_ok=True)

    report_path = "output/donor_analytics_report.html"

    total = df["Gift Amount"].sum()
    average = df["Gift Amount"].mean()
    highest = df["Gift Amount"].max()
    donors = df["Prospect ID"].nunique()
    colleges = df["College"].nunique()
    states = df["State"].nunique()

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

    html = f"""
<!DOCTYPE html>

<html>

<head>

<title>Donor Intelligence Report</title>

<style>

body {{
font-family: Arial, sans-serif;
background:#f5f5f5;
padding:40px;
}}

.container {{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0 0 10px rgba(0,0,0,.2);
}}

h1 {{
color:#0b5394;
}}

table {{
border-collapse:collapse;
width:100%;
margin-top:20px;
}}

th,td {{
border:1px solid #ddd;
padding:10px;
}}

th {{
background:#0b5394;
color:white;
}}

.section {{
margin-top:35px;
}}

</style>

</head>

<body>

<div class="container">

<h1>Donor Intelligence & Fundraising Analytics</h1>

<p>
Automatically generated using Python.
</p>

<div class="section">

<h2>Executive KPIs</h2>

<table>

<tr><th>KPI</th><th>Value</th></tr>

<tr><td>Total Donations</td><td>${total:,.2f}</td></tr>

<tr><td>Average Donation</td><td>${average:,.2f}</td></tr>

<tr><td>Highest Donation</td><td>${highest:,.2f}</td></tr>

<tr><td>Total Donors</td><td>{donors}</td></tr>

<tr><td>Total Colleges</td><td>{colleges}</td></tr>

<tr><td>Total States</td><td>{states}</td></tr>

</table>

</div>

<div class="section">

<h2>Top Performers</h2>

<table>

<tr><th>Category</th><th>Leader</th></tr>

<tr><td>State</td><td>{top_state}</td></tr>

<tr><td>College</td><td>{top_college}</td></tr>

<tr><td>Major</td><td>{top_major}</td></tr>

<tr><td>Gift Allocation</td><td>{top_allocation}</td></tr>

</table>

</div>

<div class="section">

<h2>Business Recommendations</h2>

<ul>

<li>Increase fundraising efforts in lower-performing states.</li>

<li>Develop loyalty campaigns for repeat donors.</li>

<li>Focus campaigns on top-performing colleges.</li>

<li>Encourage recurring donations through membership programs.</li>

<li>Expand marketing for underfunded allocation categories.</li>

</ul>

</div>

<div class="section">

<h2>Generated Charts</h2>

<p>
All charts are available in the
<b>output/charts</b> folder.
</p>

</div>

<div class="section">

<h2>Project Summary</h2>

<p>

This report summarizes donor trends,
fundraising performance,
college contributions,
major-wise donations,
geographical insights,
and advanced analytics generated using Python.

</p>

</div>

</div>

</body>

</html>

"""

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(html)

    logger.info("HTML report generated successfully.")
    print(report_path)
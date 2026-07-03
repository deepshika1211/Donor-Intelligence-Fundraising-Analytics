"""
---------------------------------------------------------------
Project: Donor Intelligence & Fundraising Analytics Using Python

Author: Deepshika Yerrangi

Description:
Professional Interactive Executive Dashboard
---------------------------------------------------------------
"""

import os
import plotly.express as px
import plotly.io as pio

OUTPUT_FILE = "output/donor_dashboard.html"


def generate_dashboard(df):
    """
    Generate Professional Interactive Dashboard
    """

    print("\nGenerating Professional Dashboard...")

    os.makedirs("output", exist_ok=True)

    # ==========================================================
    # Executive KPIs
    # ==========================================================

    total_donation = df["Gift Amount"].sum()

    average_donation = df["Gift Amount"].mean()

    highest_donation = df["Gift Amount"].max()

    unique_donors = df["Prospect ID"].nunique()

    total_colleges = df["College"].nunique()

    total_states = df["State"].nunique()

    # ==========================================================
    # Prepare Data
    # ==========================================================

    monthly = (
        df.groupby(["Year", "Month"])["Gift Amount"]
        .sum()
        .reset_index()
    )

    top_colleges = (
        df.groupby("College")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    top_states = (
        df.groupby("State")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    top_majors = (
        df.groupby("Major")["Gift Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    donation_category = (
        df.groupby("Donation Category")["Gift Amount"]
        .sum()
        .reset_index()
    )

    # ==========================================================
    # Charts
    # ==========================================================

    fig_monthly = px.line(
        monthly,
        x=monthly.index,
        y="Gift Amount",
        title="Monthly Donation Trend",
        markers=True,
        color_discrete_sequence=["#2563EB"]
    )

    fig_colleges = px.bar(
        top_colleges,
        x="Gift Amount",
        y="College",
        orientation="h",
        title="Top 10 Colleges",
        color="Gift Amount",
        color_continuous_scale="Greens"
    )

    fig_states = px.bar(
        top_states,
        x="Gift Amount",
        y="State",
        orientation="h",
        title="Top 10 States",
        color="Gift Amount",
        color_continuous_scale="Oranges"
    )

    fig_category = px.pie(
        donation_category,
        values="Gift Amount",
        names="Donation Category",
        hole=.45,
        title="Donation Categories",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig_major = px.bar(
        top_majors,
        x="Gift Amount",
        y="Major",
        orientation="h",
        title="Top Majors",
        color="Gift Amount",
        color_continuous_scale="Purples"
    )

    # Convert figures to HTML

    monthly_html = pio.to_html(fig_monthly,
                               include_plotlyjs="cdn",
                               full_html=False)

    college_html = pio.to_html(fig_colleges,
                               include_plotlyjs=False,
                               full_html=False)

    state_html = pio.to_html(fig_states,
                             include_plotlyjs=False,
                             full_html=False)

    category_html = pio.to_html(fig_category,
                                include_plotlyjs=False,
                                full_html=False)

    major_html = pio.to_html(fig_major,
                             include_plotlyjs=False,
                             full_html=False)

    # ==========================================================
    # Build HTML Dashboard
    # ==========================================================

    html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>Donor Intelligence Dashboard</title>

<style>

body{{
    margin:0;
    padding:0;
    background:#eef2f7;
    font-family:Arial,Helvetica,sans-serif;
}}

.header{{
    background:linear-gradient(90deg,#0F4C81,#2563EB);
    color:white;
    text-align:center;
    padding:30px;
    box-shadow:0 3px 10px rgba(0,0,0,.2);
}}

.header h1{{
    margin:0;
    font-size:36px;
}}

.header p{{
    font-size:18px;
    margin-top:10px;
}}

.container{{
    width:95%;
    margin:auto;
}}

.kpi-row{{
    display:flex;
    justify-content:space-between;
    margin-top:30px;
    gap:20px;
}}

.card{{
    flex:1;
    border-radius:15px;
    color:white;
    padding:25px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.15);
}}

.card h2{{
    margin:0;
    font-size:34px;
}}

.card p{{
    margin-top:12px;
    font-size:18px;
}}

.blue{{background:#2563EB;}}
.green{{background:#16A34A;}}
.orange{{background:#F97316;}}
.purple{{background:#7C3AED;}}
.red{{background:#DC2626;}}

.grid{{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:25px;
    margin-top:35px;
}}

.chart{{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}}

.full{{
    grid-column:1/3;
}}

.insights{{
    background:white;
    margin-top:35px;
    border-radius:15px;
    padding:25px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}}

.footer{{
    margin-top:40px;
    padding:20px;
    text-align:center;
    color:#555;
}}

</style>

</head>

<body>

<div class="header">

<h1>🎓 Donor Intelligence & Fundraising Analytics</h1>

<p>Executive Business Dashboard</p>

<p><b>Prepared by Deepti Yerrangi</b></p>

</div>

<div class="container">

<div class="kpi-row">

<div class="card blue">

<h2>💰</h2>

<h3>${total_donation:,.0f}</h3>

<p>Total Donations</p>

</div>

<div class="card green">

<h2>👥</h2>

<h3>{unique_donors}</h3>

<p>Unique Donors</p>

</div>

<div class="card orange">

<h2>🎓</h2>

<h3>{total_colleges}</h3>

<p>Colleges</p>

</div>

<div class="card purple">

<h2>🌍</h2>

<h3>{total_states}</h3>

<p>States</p>

</div>

<div class="card red">

<h2>📈</h2>

<h3>${average_donation:,.0f}</h3>

<p>Average Donation</p>

</div>

</div>

<div class="grid">

<div class="chart full">

{monthly_html}

</div>

<div class="chart">

{college_html}

</div>

<div class="chart">

{state_html}

</div>

<div class="chart">

{category_html}

</div>

<div class="chart">

{major_html}

</div>

<div class="insights">

<h2>📌 Executive Insights</h2>

<ul style="font-size:18px; line-height:2;">

<li><b>Total Donations:</b> ${total_donation:,.2f}</li>

<li><b>Average Donation:</b> ${average_donation:,.2f}</li>

<li><b>Highest Donation:</b> ${highest_donation:,.2f}</li>

<li><b>Unique Donors:</b> {unique_donors}</li>

<li><b>Colleges Participated:</b> {total_colleges}</li>

<li><b>States Covered:</b> {total_states}</li>

<li><b>Top College:</b> {top_colleges.iloc[0]["College"]}</li>

<li><b>Top State:</b> {top_states.iloc[0]["State"]}</li>

<li><b>Top Major:</b> {top_majors.iloc[0]["Major"]}</li>

</ul>

<hr>

<h3>💡 Business Recommendations</h3>

<ul style="font-size:17px; line-height:1.8;">

<li>Increase campaigns in the highest-performing states.</li>

<li>Recognize and retain high-value donors.</li>

<li>Strengthen partnerships with top-performing colleges.</li>

<li>Encourage recurring donations through membership programs.</li>

<li>Focus future fundraising around the most successful majors.</li>

</ul>

</div>

<div class="footer">

<hr>

<h3>🎓 Donor Intelligence & Fundraising Analytics</h3>

<p>
Dashboard generated automatically using
<b>Python</b> • <b>Pandas</b> • <b>Plotly</b>
</p>

<p>
Prepared by <b>Deepti Yerrangi</b>
</p>

</div>

</div>

</body>

</html>
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(html)

    print("=" * 60)
    print("Professional Dashboard Generated Successfully!")
    print("=" * 60)
    print(f"Saved to: {OUTPUT_FILE}")
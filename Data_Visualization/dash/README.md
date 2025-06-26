# Dash Apps for Flight Data Visualization

This folder contains interactive data visualization apps built with [Dash](https://dash.plotly.com/), a Python framework for building analytical web applications.

Each app uses an airline dataset to demonstrate various types of interactive charts, such as bar and line charts.

## Contents

- `dash_bar_chart_by_state.py`: Bar chart showing total flights to each U.S. destination state for a selected year.
- `dash_line_avg_delay_by_month.py`: Line chart showing average arrival delay per month in a selected year.

## How to Run

To run a Dash app locally:

```bash
pip install dash pandas plotly
python dash_bar_chart_by_state.py
```

Then open the URL printed in your terminal (usually http://127.0.0.1:8050/) in a browser.

Dataset
All apps use the public airline dataset provided by the IBM Data Analyst course on Coursera.

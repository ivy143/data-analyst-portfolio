# F1 Performance & Strategy Analytics

## Project Overview

This project analyzes Formula 1 race data to evaluate driver performance, team dominance, and race strategy effectiveness. The goal is to extract strategic insights that explain how drivers, teams, and race conditions influence final race outcomes.

## Objective

* Analyze driver and constructor performance across races.
* Evaluate how race strategies affect final race positions.
* Build analytical models to measure performance and dominance.

## Project Structure

F1_Performance_Analytics/

data/ – Raw and processed race datasets
notebooks/ – Jupyter notebooks for analysis

01_data_cleaning.ipynb – Data preprocessing and preparation
02_driver_analysis.ipynb – Driver performance evaluation
03_team_analysis.ipynb – Constructor dominance analysis
04_strategy_analysis.ipynb – Race strategy impact analysis

dashboard/ – Optional Power BI dashboard for visualization
README.md – Project documentation

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook
* Power BI (optional for dashboard)

## Analysis Modules

### Module 1 – Driver Performance Index

Driver performance is evaluated using multiple metrics:

* Total wins
* Podium finishes
* Points per race
* Consistency score
* Overtake efficiency

These metrics are combined using a **weighted scoring model** to create a custom **Driver Performance Score**.

### Module 2 – Constructor Dominance Model

This module evaluates how dominant a team is during a season using:

* Season dominance percentage
* Average points per race
* Win probability
* Team consistency index

The goal is to measure how consistently a team performs across races.

### Module 3 – Strategy Impact Analysis

This module analyzes how race strategies affect race outcomes:

* Correlation between **grid position and final position**
* Impact of **pit stop counts**
* Influence of **safety car periods**
* Circuit difficulty index

These factors help explain how strategy decisions influence race results.

## Statistical Techniques Used

* Correlation Analysis
* Basic Regression
* Probability Estimation
* Weighted Scoring Model

## Key Insights

* Drivers with higher consistency scores tend to finish in higher positions across the season.
* Teams with strong average points per race show higher season dominance.
* Starting grid position strongly influences final race results, but strategy decisions can significantly change outcomes.
* Safety car periods can alter race strategies and affect final standings.

## Conclusion

This project demonstrates how data analysis and statistical techniques can be applied to motorsport performance evaluation. By analyzing driver metrics, team dominance, and race strategies, the project provides insights into the factors that influence success in Formula 1 racing.

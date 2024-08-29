# Shopping Trends Analysis

## Overview

This project provides an interactive web application to analyze shopping trends using Streamlit. The application allows users to filter and visualize various aspects of shopping data, including customer segmentation, purchase amounts, discount applications, shipping types, and review ratings.

## Prerequisites

- Python
- Pandas
- Plotly
- Streamlit

## Project Description

### Exploratory Data Analysis (EDA)

The Exploratory Data Analysis (EDA) phase focuses on understanding the dataset by uncovering patterns, trends, and anomalies. The following analyses were performed:

1. **Customer Segmentation**: Examined how different customer segments behave in terms of purchase amounts and frequencies.
2. **Top Categories by Purchase Amount**: Identified the most popular categories based on total purchase amounts.
3. **Customer Lifetime Value (CLV)**: Analyzed the distribution of purchase amounts to understand customer lifetime value.
4. **Purchase Amount by Discount Applied**: Compared purchase amounts for customers who applied discounts versus those who did not.
5. **Average Purchase Amount by Shipping Type**: Calculated the average purchase amount for different shipping types.
6. **Distribution of Review Ratings**: Assessed how review ratings are distributed among customers.
7. **Top Payment Methods by Purchase Amount**: Analyzed which payment methods are most commonly used based on purchase amounts.
8. **Frequency of Purchases by Shipping Type**: Examined how frequently purchases occur based on shipping types.
9. **Top Categories by Season**: Identified top-performing categories across different seasons.
10. **Average Purchase Amount by Review Rating**: Compared average purchase amounts across different review ratings.

### Streamlit Application

The Streamlit application allows users to interactively explore the dataset through various filters and visualizations. Features of the app include:

- **Gender Filter**: Change the analysis based on selected gender (Male, Female, or Overall).
- **Category Filter**: View data specific to selected product categories.
- **Age Filter**: Analyze data based on customer age groups.
- **Shipping Type Filter**: Examine purchase data based on different shipping methods.
- **Discount Applied Filter**: Compare data for customers who applied discounts versus those who did not.
- **Season Filter**: Analyze trends across different seasons.
- **Review Rating Filter**: Examine data based on review ratings.
- **Payment Method Filter**: Analyze data based on payment methods used.

Users can select various filters from the sidebar and click the "Show Analysis" button to update visualizations and view insights.

## Files

- **`app.py`**: The main Streamlit application script. This file contains the code for the Streamlit app, including the user interface and visualizations. It handles data filtering, analysis, and the display of interactive charts based on user input.

- **`shopping_trends_updated.csv`**: The dataset used for analysis. This CSV file contains the shopping trends data that the application analyzes and visualizes. It includes information on customer demographics, purchase amounts, categories, and other relevant attributes.

- **`requirements.txt`**: Lists the required Python packages for the project. This file includes all dependencies needed to run the application. It ensures that all necessary libraries are installed for the application to function correctly.


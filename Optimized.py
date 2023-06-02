import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Set Plotly template to white background
import plotly.io as pio
pio.templates.default = "plotly_white"

# Load data
data = pd.read_csv('retail_price.csv')

# Streamlit app
st.title('Retail Price Analysis App')

# Visualization Options
st.sidebar.header('Visualization Options')
chart_options = {
    'Histogram': 'Distribution of Total Price',
    'Box Plot': 'Box Plot of Unit Price',
    'Scatter Plot': 'Quantity vs Total Price with Trendline',
    'Bar Chart': 'Average Total Price by Product Category',
    'Correlation Heatmap': 'Correlation Heatmap of Numerical Features',
    'Bar Chart - Price Difference': 'Average Competitor Price Difference by Product Category'
}
selected_chart = st.sidebar.selectbox('Select a visualization:', list(chart_options.keys()))
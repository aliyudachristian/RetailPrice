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

# Sidebar
st.sidebar.header('Visualization Options')
chart_options = ['Histogram', 'Box Plot', 'Scatter Plot', 'Bar Chart', 'Correlation Heatmap', 'Bar Chart - Price Difference']
selected_chart = st.sidebar.selectbox('Select a visualization:', chart_options)

if selected_chart == 'Histogram':
    st.header('Distribution of Total Price')
    fig = px.histogram(data, x='total_price', nbins=20)
    st.plotly_chart(fig)

elif selected_chart == 'Box Plot':
    st.header('Box Plot of Unit Price')
    fig = px.box(data, y='unit_price')
    st.plotly_chart(fig)

elif selected_chart == 'Scatter Plot':
    st.header('Quantity vs Total Price with Trendline')
    fig = px.scatter(data, x='qty', y='total_price', trendline='ols')
    st.plotly_chart(fig)

elif selected_chart == 'Bar Chart':
    st.header('Average Total Price by Product Category')
    avg_price_by_category = data.groupby('product_category_name')['total_price'].mean().reset_index()
    fig = px.bar(avg_price_by_category, x='product_category_name', y='total_price')
    st.plotly_chart(fig)

elif selected_chart == 'Correlation Heatmap':
    st.header('Correlation Heatmap of Numerical Features')
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = data[numeric_columns].corr()

    fig = go.Figure(go.Heatmap(x=correlation_matrix.columns, y=correlation_matrix.columns, z=correlation_matrix.values))
    st.plotly_chart(fig)

elif selected_chart == 'Bar Chart - Price Difference':
    st.header('Average Competitor Price Difference by Product Category')
    data['comp_price_diff'] = data['unit_price'] - data['comp_1']

    avg_price_diff_by_category = data.groupby('product_category_name')['comp_price_diff'].mean().reset_index()
    fig = px.bar(avg_price_diff_by_category, x='product_category_name', y='comp_price_diff')
    st.plotly_chart(fig)
# Import libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load your sales dataset
df = pd.read_csv('sales_data.csv')  

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)  # suppress_callback_exceptions to avoid callback warnings
server = app.server

# Create the charts

# 1. Bar Chart - Yearly Sales Comparison
bar_fig = px.bar(df, x='Year', y='Sales', color='Region', barmode='group',
                 title="Yearly Sales Comparison",
                 color_discrete_sequence=px.colors.sequential.Blues)

# 2. Line Chart - Monthly Sales Trend
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
monthly_sales = df.groupby('Month').sum().reindex(months)
fig_line = px.line(
    monthly_sales,
    x=monthly_sales.index,
    y='Sales',
    title='Monthly Sales Trend',
    markers=True,
    line_shape='spline'
)

# 3. Pie Chart - Product Category Distribution
pie_fig = px.pie(df, names='Product', values='Sales',
                 title="Product Category Distribution",
                 color_discrete_sequence=px.colors.sequential.Blues)

# 4. Scatter Plot - Sales vs Profit Relationship
scatter_fig = px.scatter(df, x='Sales', y='Profit', color='Region', size='Sales',
                         title="Sales vs Profit Relationship",
                         color_discrete_sequence=px.colors.sequential.Blues)

# 5. Heatmap - Correlation Matrix
corr = df[['Sales', 'Profit']].corr()
heatmap_fig = px.imshow(corr, text_auto=True, color_continuous_scale='Blues',
                        title="Sales Correlation Matrix")

# App Layout
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'background-color': '#f9f9f9', 'padding': '20px'}, children=[
    
    # Header
    html.H1("Company Growth Analysis", style={'text-align': 'center', 'color': '#1f77b4', 'font-size': '40px'}),
    
    html.Br(),
    
    # Bar Chart Section
    html.H2("Yearly Sales Comparison", style={'color': '#1f77b4'}),
    html.P("This bar chart shows how our sales figures have grown over the years across different regions. It provides a clear comparison year-over-year."),
    dcc.Graph(figure=bar_fig),
    
    html.Br(),
    
    # Line Chart Section
    html.H2("2. Monthly Sales Trend", style={'color': '#003366'}),
    html.P("This line chart highlights how sales fluctuated over the year, giving insights into seasonality and business cycles."),
    dcc.Graph(figure=fig_line),
    
    html.Br(),
    
    # Pie Chart Section
    html.H2("Product Category Distribution", style={'color': '#1f77b4'}),
    html.P("This pie chart visualizes the contribution of each product category to the total sales, giving insight into our top-performing products."),
    dcc.Graph(figure=pie_fig),
    
    html.Br(),
    
    # Scatter Plot Section
    html.H2("Sales vs Profit Relationship", style={'color': '#1f77b4'}),
    html.P("This scatter plot explores the relationship between sales and profit for different regions, highlighting areas of strength and opportunity."),
    dcc.Graph(figure=scatter_fig),
    
    html.Br(),
    
    # Heatmap Section
    html.H2("Sales Correlation Matrix", style={'color': '#1f77b4'}),
    html.P("The heatmap illustrates the correlation between sales and profit, helping us understand the strength and direction of these relationships."),
    dcc.Graph(figure=heatmap_fig),
    
    html.Br(),
])



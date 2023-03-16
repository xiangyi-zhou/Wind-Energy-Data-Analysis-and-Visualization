import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Define the connection string
user = 'postgres'
password = 'postgresql2023'
host = 'localhost'
port = '5432'
database = 'wind_energy_database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# Create a connection to the database
engine = create_engine(connection_string)


country_map = {
    'CZ': 'Czechia',
    'DK': 'Denmark',
    'FR': 'France',
    'DE': 'Germany',
    'PL': 'Poland',
    'SE': 'Sweden',
    'CH': 'Switzerland',
    'UK': 'United Kingdom'
}

# Define the SQL query to retrieve the data
query = '''
SELECT commissioning_date, electrical_capacity
FROM mytable
'''

# Load the data into a pandas dataframe
df = pd.read_sql(query, engine)

# Convert commissioning_date to a datetime object
df['commissioning_date'] = pd.to_datetime(df['commissioning_date'])

# Set the index to commissioning_date
df = df.set_index('commissioning_date')

# Get the earliest and latest year in the data
earliest_year = df.index.min().year
latest_year = df.index.max().year

# Define function to create pie chart
def pie_chart_get_data():
    # Define the SQL query to retrieve the data
    query = '''
    SELECT country, SUM(electrical_capacity) as total_capacity
    FROM mytable
    GROUP BY country
    '''

    # Load the data into a pandas dataframe
    df = pd.read_sql(query, engine)

    # Map country codes to full country names
    df['country'] = df['country'].map(country_map)
    
    return df

def pie_chart_draw(dataframe):
    # Calculate the percentage of total capacity by country
    dataframe['percentage'] = 100 * dataframe['total_capacity'] / dataframe['total_capacity'].sum()
    
    # Create the pie chart
    fig = px.pie(dataframe, values='percentage', names='country', title='Percentage of Total Capacity by Country')
    fig.update_traces(marker=dict(colors=['#94DAFF', '#99D0E0', '#B1D0E0', '#64b5f6', '#93B5C6', '#A2DBFA','#A2DBFA', '#9ACEFF']))


    return fig

# Style the first chart div
chart_div_style = {
    'display': 'inline-block',
    'vertical-align': 'top',
    'width': '35%',
    'height': '500px',
    'margin': '1%',
    'border': '1px solid #C8D4E3',
    'box-shadow': '2px 2px 2px lightgrey',
    'padding': '20px',
}

chart_div1 = html.Div(children=[
    dcc.Graph(
        id='pie-chart',
        figure=pie_chart_draw(pie_chart_get_data())
    ),

], style=chart_div_style)


# Style the second chart div
chart_div2 = html.Div(children=[
    html.Label('Select a country'),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': value, 'value': key} for key, value in country_map.items()],
        value='UK'
    ),
    dcc.Graph(id='wind-energy-bar-chart')
], style=chart_div_style)

# Style the third chart div
chart_div3 = html.Div(children=[
    dcc.Graph(
        id='monthly-plot',
        figure={
            'data': [
                {'x': df.index, 'y': df['electrical_capacity'], 'type': 'line', 'name': 'Electrical Capacity'},
            ],
            'layout': {
                'title': 'Monthly Total Electrical Capacity (EU)'
            }
        }
    ),
    dcc.RangeSlider(
        id='year-slider',
        min=earliest_year,
        max=latest_year,
        step=1,
        value=[latest_year - 4, latest_year],
        marks={
            str(year): str(year) for year in range(earliest_year, latest_year+1, 5)
        }
    ),
    
], style={
    'display': 'inline-block',
    'width': '75%',
    'margin': '1%',
    'border-left': '1px solid #C8D4E3',
    'border-right': '1px solid #C8D4E3',
    'border-top': '1px solid #C8D4E3',
    'border-bottom': '1px solid #C8D4E3',
    'box-shadow': '2px 2px 2px lightgrey',
    'padding': '10px'
})


# Define the Dash app and layout
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([    
    html.H1('Wind Energy Dashboard (European Union)', 
        style={'color': 'black', 'font-family': 'Arial'}),   
    chart_div1,    
    chart_div2,    
    chart_div3
], style={'text-align': 'center'})


# Define the callback function to update the bar chart based on the selected country    
@app.callback(
    Output('wind-energy-bar-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_bar_chart(country):
    
    # Query the database for the data
    query = f"SELECT electrical_capacity, nuts_2_region FROM mytable WHERE country='{country}'"
    df = pd.read_sql_query(query, engine)
    
    # Sort the dataframe by nuts_2_region
    df = df.sort_values(by='nuts_2_region')
    # Get the order of nuts_2_region for the current country
    fig = {
            'data': [
                {'x': df['nuts_2_region'], 'y': df['electrical_capacity'], 'type': 'bar'},
            ],
            'layout': {
                'title': f'Overrall Wind Energy Capacity in {country_map[country]}',
                'yaxis': {'title': 'Installed Electrical Capacity (MW)'},
                'xaxis': {'title': 'The code of the NUTS 2 region', 'categoryorder': 'array', 'categoryarray': df['nuts_2_region']},
            }
        }
    return fig

# Define the callback function to update the monthly plot based on the selected year range
@app.callback(
    Output(component_id='monthly-plot', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')]
)
def update_figure(year_range):
    # Filter the data by year range
    filtered_df = df[(df.index.year >= year_range[0]) & (df.index.year <= year_range[1])]

    # Resample the data to mon  thly frequency
    monthly_df = filtered_df.resample('M').sum()

    # Create a new plot
    fig = {
        'data': [
            {'x': monthly_df.index, 'y': monthly_df['electrical_capacity'], 'type': 'line', 'name': 'Electrical Capacity'},
        ],
        'layout': {
            'title': f'Monthly Total Electrical Capacity {year_range[0]} - {year_range[1]}',
            'yaxis': {'title': 'Installed Electrical Capacity (MW)'}
        }
    }

    # Return the new plot
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
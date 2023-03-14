import dash
import dash_core_components as dcc
import dash_html_components as html
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
    df['country'] = df['country'].map(country_map)
    
    return df

# Define function to create pie chart
def pie_chart_draw(dataframe):
    # Calculate the percentage of total capacity by country
    dataframe['percentage'] = 100 * dataframe['total_capacity'] / dataframe['total_capacity'].sum()
    
    # Create the pie chart
    fig = px.pie(dataframe, values='percentage', names='country', title='Percentage of Total Capacity by Country')

    return fig


# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Wind Energy Installations in the EU'),

    dcc.Graph(
        id='pie-chart',
        figure=pie_chart_draw(pie_chart_get_data())
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

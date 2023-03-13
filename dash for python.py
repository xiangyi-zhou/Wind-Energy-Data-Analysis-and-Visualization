import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
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

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Wind Energy Data Analysis (European Union)'),

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
])

# Define the callback function to update the plot
@app.callback(
    Output(component_id='monthly-plot', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')]
)
def update_figure(year_range):
    # Filter the data by year range
    filtered_df = df[(df.index.year >= year_range[0]) & (df.index.year <= year_range[1])]

    # Resample the data to monthly frequency
    monthly_df = filtered_df.resample('M').sum()

    # Create a new plot
    fig = {
        'data': [
            {'x': monthly_df.index, 'y': monthly_df['electrical_capacity'], 'type': 'line', 'name': 'Electrical Capacity'},
        ],
        'layout': {
            'title': f'Monthly Total Electrical Capacity (EU) {year_range[0]} - {year_range[1]}',
            'yaxis': {'title': 'Installed Electrical Capacity (MW)'}
        }
    }

    # Return the new plot
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

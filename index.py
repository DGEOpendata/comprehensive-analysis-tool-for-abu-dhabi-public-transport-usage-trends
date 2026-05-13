python
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the dataset
file_path = 'Public_Transport_Ridership_Data.csv'
data = pd.read_csv(file_path)

# Data Preprocessing
data['datetime'] = pd.to_datetime(data['datetime'])
data['month'] = data['datetime'].dt.month
data['hour'] = data['datetime'].dt.hour

# Calculate KPIs
monthly_ridership = data.groupby('month')['ridership'].sum()
ridership_by_route = data.groupby('route')['ridership'].sum()
peak_hours = data.groupby('hour')['ridership'].sum()

# Build Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Abu Dhabi Public Transport Analysis'),
    html.Label('Monthly Ridership'),
    dcc.Graph(
        id='monthly-ridership',
        figure={
            'data': [
                {'x': monthly_ridership.index, 'y': monthly_ridership.values, 'type': 'bar', 'name': 'Monthly Ridership'}
            ],
            'layout': {
                'title': 'Monthly Ridership Trends'
            }
        }
    ),
    html.Label('Ridership by Route'),
    dcc.Graph(
        id='ridership-by-route',
        figure={
            'data': [
                {'x': ridership_by_route.index, 'y': ridership_by_route.values, 'type': 'bar', 'name': 'Ridership by Route'}
            ],
            'layout': {
                'title': 'Ridership by Route'
            }
        }
    ),
    html.Label('Peak Hours'),
    dcc.Graph(
        id='peak-hours',
        figure={
            'data': [
                {'x': peak_hours.index, 'y': peak_hours.values, 'type': 'line', 'name': 'Peak Hours'}
            ],
            'layout': {
                'title': 'Peak Travel Hours'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

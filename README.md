## Wind Energy Dashboard (European Union)

This is a dashboard that displays wind energy data for the European Union. The dashboard consists of three charts:

1. A pie chart showing the percentage of total capacity by country
2. A bar chart showing the overall wind energy capacity in a selected country
3. A line chart showing the monthly total electrical capacity for the European Union

The pie chart and the bar chart have dropdown menus for country selection. The line chart has a slider for selecting a year range.

![Screenshot](Screenshot.jpeg)

### Technologies Used

The following technologies were used to build this dashboard:

- Dash
- Plotly
- Pandas
- SQLAlchemy


### Data Source:

https://data.open-power-system-data.org/renewable_power_plants/2020-08-25

### Running the Dashboard

To run the dashboard, first clone this repository. Then, install the necessary dependencies by running the following command in your terminal:

> pip install -r requirements.txt

After installing the dependencies, run the following command to start the dashboard:

> python app.py

This will start a local server on your machine. You can view the dashboard by navigating to `http://localhost:8050` in your web browser.

### Reference
https://github.com/microsoft/ML-For-Beginners

https://github.com/microsoft/Data-Science-For-Beginners
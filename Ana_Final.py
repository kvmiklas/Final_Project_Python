"""Python_Project: Wind Rose Chart on the Minimum and Maximum Wind Speeds
Hurrican Ana of 2015."""
###Import plotly in order to install Plotly's Python package.
###Used the package manager pip inside terminal of the C:/Windows system.
###Import shapefile that contains the Hurricane data.

import shapefile
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('kvmiklas', 'k11mrmy94i')

###Reads the shapefile and accesses the required point data from the point shapefile that has the wind speeds for hurricane. 

sf = shapefile.Reader("Hurricane_ana/al012015_pts.shp")
data = sf.shapeRecords()
wind_speeds = []
for row in data:
    wind_speeds.append(row.record[11])
    
###Script that creates a Wind Rose Chart on Hurricane Ana for the Maximum and Minimum wind speeds.
trace1 = go.Area(
        r = [0, 0, 0, 0, 0, 0, 0, max(wind_speeds)],
        t = ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West','N-W'],
        name = '(Maximum Wind Speed- Tropical Storm)',
        marker = dict(
            color = 'red'
        )
)

trace2 = go.Area(
        r = [0, 0, 0, 0, 0, 0, 0, min(wind_speeds)],
        t = ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West','N-W'],
        name = '(Minimum Wind Speed- Tropical Depression)',
        marker = dict(
            color = 'blue'
        )
)
     
    
            
data = [trace1, trace2]
layout = go.Layout(
    title = 'Wind Speed for Hurricane Ana 2015',
    font = dict(
        size = 16
    ),
    radialaxis = dict(
        ticksuffix = '%'
    ),
    orientation = 270
)

fig = go.Figure(data = data, layout = layout)
plot_url = py.plot(fig, filename = 'polar-area-chart')

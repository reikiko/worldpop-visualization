import pandas as pd
import bokeh

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.layouts import widgetbox, row, gridplot
from bokeh.models import Slider, Select
from bokeh.io import curdoc, show, output_notebook

curdoc().theme = "light_minimal"

data = pd.read_csv('archive/population_total_long.csv')

#Setting source
source = ColumnDataSource(data={
    'x': data['Year'],
    'y': data['Population']})

#Making line plot
plot = figure(title = 'Population per Year', x_axis_label = 'Year', y_axis_label = 'Population',
           plot_height=700, plot_width=700, tools=[HoverTool(tooltips='@y')])

plot.c(x='x', y='y', source=source, line_width=3)

#Define Update function
def update_plot(attr, old, new):
    x = x_select.value
    y = y_select.value

    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y

    new_data = {
    'x': data[x],
    'y': data[y]}
    
    source.data = new_data

    plot.title.text = '%s per Year' % y
    
# Make a dropdown select
x_select = Select(
    options=['Year'],
    value='Year',
    title='X Axis')
x_select.on_change('value', update_plot)

y_select = Select(
    options=['Population', 'NetChange', 'Urban'],
    value='Population',
    title='Y Axis')
y_select.on_change('value', update_plot)

layout = row(widgetbox(x_select, y_select), plot)
curdoc().add_root(layout)
# Importing the necessary modules and tools
from math import pi

import pandas

from bokeh.palettes import Category20c
from bokeh.plotting import figure, output_file, show
from bokeh.transform import cumsum

# Creating the output HTML file in the current folder
output_file("pie.html")

# Reading the CSV data into a Pandas dataframe
data = pandas.read_csv("D:\\bokeh\\countries.csv")

# Referencing the two columns that contain the necessary data
country = data["Country"]
population = data["Population"]

# Configuring the pie wedge size based on the Population value
data['angle'] = data['Population'] / data['Population'].sum() * (2 * pi)

# Configuring the colors to use for each wedge
data['color'] = Category20c[len(data)]

# Creating a new plot with various optional parameters
p = figure(plot_height=400, title="Top 10 Countries by Population", toolbar_location=None,
           tools="hover", tooltips="@Country: @Population", x_range=(-0.5, 1.0))

# Configuring wedge visual properties
# wedge: https://bokeh.pydata.org/en/latest/docs/reference/models/glyphs/wedge.html
# cumsum: https://bokeh.pydata.org/en/latest/docs/reference/transform.html#bokeh.transform.cumsum
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Country', source=data)

# Setting other optional parameters
p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

# Displaying the final result
show(p)
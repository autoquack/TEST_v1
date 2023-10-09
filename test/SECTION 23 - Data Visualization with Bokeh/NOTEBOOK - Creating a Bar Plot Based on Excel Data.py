# Importing the necessary modules and tools
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral10
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap

import pandas

# Reading the Excel data into a Pandas dataframe
top10 = pandas.read_excel("D:\\bokeh\\top10.xlsx")

# Creating the output HTML file in the current folder
output_file("bar.html")

# Referencing the two columns that contain the necessary data
language = top10["Language"]
rating = top10["Ratings"]

# At the most basic level, a ColumnDataSource is simply a mapping between column names and lists of data.
# The ColumnDataSource takes a data parameter which is a dict,
# with string column names as keys and lists (or arrays) of data values as values.
# If one positional argument is passed in to the ColumnDataSource initializer, it will be taken as data.
# Once the ColumnDataSource has been created, it can be passed into the source parameter of plotting methods
# which allows you to pass a column’s name as a stand in for the data values
# Source: https://bokeh.pydata.org/en/latest/docs/user_guide/data.html#columndatasource
source = ColumnDataSource(data=dict(language=language, rating=rating))

# Creating a new plot with various optional parameters
# Ranges: https://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#setting-ranges
p = figure(x_range=language, plot_height=800, toolbar_location=None, title="Top 10 Programming Languages")

# Drawing the vertical bars and setting visual properties
# vbar: https://bokeh.pydata.org/en/latest/docs/reference/models/glyphs/vbar.html
# factor_cmap: https://bokeh.pydata.org/en/latest/docs/reference/transform.html#bokeh.transform.factor_cmap
p.vbar(x='language', top='rating', width=0.7, source=source, legend_label="Languages",
       line_color='white', fill_color=factor_cmap('language', palette=Spectral10, factors=language))

# Setting other optional parameters
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 16
p.legend.orientation = "horizontal"
p.legend.location = "top_right"

# Displaying the final result
show(p)
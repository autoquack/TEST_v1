In
recent
versions
of
Bokeh, you
might
get
a
warning
when
running
the
code in the
previous
video:

BokehDeprecationWarning: 'legend'
keyword is deprecated, use
explicit
'legend_label', 'legend_field', or 'legend_group'
keywords
instead
To
fix
this, just
replace
legend in your
code
with legend_label.

from bokeh.plotting import figure, output_file, show

x = [10, 20, 30, 40, 50, 60, 70, 90]
y = [11, 12, 14, 16, 17, 18, 19, 21]

output_file("line.html")

p = figure(title="Basic Line Plot", x_axis_label='X-Axis', y_axis_label='Y-Axis')

p.line(x, y, legend_label="Price", line_width=3)

show(p)
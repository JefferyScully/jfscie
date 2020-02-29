import json
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN


def make_plot():
    p = figure(plot_width=400, plot_height=400, sizing_mode="scale_width")
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
    return p

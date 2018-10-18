import os
from os.path import dirname, join

from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from bokeh.embed import components
from bokeh.layouts import gridplot
from bokeh.plotting import figure

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, NumberFormatter
from bokeh.io import curdoc

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

def create_bokeh_hist(data, title='', background_fill_color='#E8DDCB', bins='auto'):
    p = figure(title=title, background_fill_color=background_fill_color)
    hist, edges = np.histogram(data, density=True, bins=bins)
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
            fill_color="#036564", line_color="#033649")
    return p

# Create the main plot
def create_figure(current_feature_name, bins):
	p = create_bokeh_hist(iris_df[current_feature_name], bins=bins)

	# Set the y axis label
	p.yaxis.axis_label = 'Count'
	return p

@app.route('/')
def index():
	# Determine the selected feature
	current_feature_name = request.args.get("feature_name")
	if current_feature_name == None:
		current_feature_name = "Sepal Length"

	# Create the plot
	plot = create_figure(current_feature_name, 10)
		
	# Embed plot into HTML via Flask Render
	script, div = components(plot)
	return render_template("iris_index1.html", script=script, div=div,
		feature_names=feature_names,  current_feature_name=current_feature_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import render_template, url_for, jsonify, request
from flask_jfscie import app

import json
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
# from bokeh.sampledata.iris import flowers


# This would be the data that you recieved
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

user_data = [
    {
        'first':'jeff',
        'last':'scully',
        'handle':'me'},
    {
        'first':'lacey',
        'last':'scully',
        'handle':'her'}
]

def make_plot():
    p = figure(plot_width=400, plot_height=400, sizing_mode="scale_width")
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
    return p

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, user_data=user_data, resources=CDN.render()) # Render_template is a method that takes in the file, & (what is passed to HTML = python object)


# @app.route("/about") # This tells flask to create an about path
# def about():
#     return render_template('about.html', title='About')

# I need to add the account setting page and the Main advertizement page(possibly using hugo and template to get this off with a bang)



#background process happening without any refreshing
@app.route('/row_click', methods=['POST'])
def background_process_test():
    member = request.form['member_id']
    return jsonify({"result":"success", "data":member})

@app.route('/plot')
def plot():
    p = make_plot()
    return json.dumps(json_item(p, "myplot"))

# Sources : https://dash.plotly.com/
#           https://plotly.com/python/mapbox-density-heatmaps/

import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

## If you face error :
#  * Environment: production
#   WARNING: This is a development server. Do not use it in a production deployment.
#   Use a production WSGI server instead.

##
#source to check :
 #https://plotly.com/python/v3/create-online-dashboard-legacy/#:~:text=get_preview()-,Choose%20Plots,created%20by%20using%20its%20url.&text=Pythonplotbot%27s%20interactive%20graph%20and%20data,values%20from%200%20to%200.


 #%%%%%%%%%%%% Solution 1:
 # source: https://exerror.com/warning-this-is-a-development-server-do-not-use-it-in-a-production-deployment-use-a-production-wsgi-server-instead/
 from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

 #%%%%%%%%%%%% Solution 2:
export FLASK_APP=example
export FLASK_ENV=development
flask run

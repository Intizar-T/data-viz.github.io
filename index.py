from flask import Flask
import dash
from dash import dcc
from dash import html
from dash import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import scipy as sp
from statsmodels.formula.api import ols

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

server=Flask(__name__)
app = dash.Dash(__name__, suppress_callback_exceptions=True, server=server, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


#index_page = html.Div([
#    dcc.Link('Main', href='/'),
#    html.Br(),
#    dcc.Link('Page-2', href='/page-2'),
#])

signup_layout = html.Div([
    html.Div(['<3', html.A('Sign Up', href='/signup', id='signup')], id='menu'),
    html.Div([
        html.H3('Sign In Page'),
        dcc.Input(id='userid', type='text', placeholder='User ID'),
        html.Br(),
        dcc.Input(id='userpass', type='text', placeholder='Password'),
        html.Br(),
        html.A(html.Button('Sign in', id='signin_button'), href='/')
        ,
    ], id='account'),
], id='body')

#@app.callback(dash.dependencies.Output('body', 'children'),
#              [dash.dependencies.Input('userid', 'userpass')])
#def page_1_dropdown(value):
#    return 'You have selected "{}"'.format(value)

signin_layout = html.Div([
    html.Div(['<3', html.A('Sign In', href='/signin', id='signin')], id='menu'),
    html.Div([
        html.H3('Sign Up Page'),
        dcc.Input(id='username', type='text', placeholder='Name'),
        html.Br(),
        dcc.Input(id='useremail', type='text', placeholder='Email'),
        html.Br(),
        dcc.Input(id='userpass', type='text', placeholder='Password'),
        html.Br(),
        html.A(html.Button('Sign Up', id='signup_button'), href='/')
        ,
    ], id='account'),
], id='body')

#@app.callback(dash.dependencies.Output('page-2-content', 'children'),
#              [dash.dependencies.Input('page-2-radios', 'value')])
#def page_2_radios(value):
#    return 'You have selected "{}"'.format(value)


main_layout = html.Div([
    html.Div([
        '<3',
        html.A('My HRV', href='/', id='myhrv'),
        html.A('My Stress Level', href='/', id='mystresslevel'),
        html.A('Suggestions', href='/', id='suggestions'),
        html.A('My Account', href='/', id='myaccount')],
        style={},
        className='mainmenu'),
    html.Div(['Main Page']),
    html.Br(),
    html.A('Sign In', href='/signin'),
    html.Br(),
    html.A('Sign Up', href='/signup'),
    html.Br(),
    html.A('Chart 1', href='/chart1'),
    html.Br(),
    html.A('Chart 2', href='/chart2'),
    html.Br(),
    html.A('Chart 3', href='/chart3'),
    html.Br(),
    html.A('Chart 4', href='/chart4')
], id='main_layout')


chart1Source=pd.DataFrame({
    'GSR':[384, 425, 399, 344, 379, 443, 460, 387, 399, 398,357,393,407,439,371,403,375,245,162,168],
    'HRV':[0.929152,0.696864,0.763232,0.763232,0.962336,0.91256,0.846192,0.763232,0.74664,0.8296,
           0.779824,0.564128,0.91256,0.8296,0.564128,0.929152,0.730048,0.813008,0.431392,0.613904],
    'Temperature':[33.34,33.38,33.62,33.66,33.52,33.61,33.3,33.23,33.21,33.21,
                   33.3,33.24,33.24,33.25,33.72,33.38,33.05,32.92,32.7,32.17]
})
#GSRFormula = -0.05 * Temperature + 400 (Dummy formula)
chart1Source['GSRCalculated']=chart1Source['Temperature']*(-0.05) + 400
chart1Source['deltaGSR']=chart1Source['GSRCalculated']-chart1Source['GSR']
chart1Source['Healthy']=chart1Source.apply(lambda row : row['deltaGSR']>0, axis=1).astype(int)
chart1Source['Healthy']=np.where(chart1Source['Healthy'], 'Healthy', 'Unhealthy')
#chart1Source['Healthy'].replace('True', "Healthy")
#chart1Source['Healthy'].replace(False, "Unhealthy")
#chart1Source['healthyHRV']=chart1Source.loc[chart1Source['deltaGSR']>=0]['HRV']

figure1=px.scatter(chart1Source, x='deltaGSR', y='HRV', color='Healthy', trendline="ols", trendline_scope="overall",
                   title="GSR vs HRV")
figure1.add_vline(x=0, line_dash="dot")
figure1.add_vrect(x0=0, x1=300,
                  annotation_text="Healthy HRV", annotation_position="top left",
                  fillcolor="blue", opacity=0.1, line_width=0)
figure1.add_vrect(x0=-100, x1=0, annotation_text="Unhealthy HRV", annotation_position="top right", fillcolor="red", opacity=0.1, line_width=0)


chart2Source=pd.DataFrame({
    'Time':[1557286092300, 1557286182500, 1557286663900, 1557287476100, 1557288258200,
            1557288739500, 1557290604800, 1557291056200, 1557291116100, 1557291567400,
            1557292289300, 1557292469800, 1557292770700, 1557294124300, 1557294337700,
            1557294395900, 1557294425900, 1557294455900, 1557294485300, 1557294576500],
    'HRV':[0.929152,0.696864,0.763232,0.763232,0.962336,0.91256,0.846192,0.763232,0.74664,0.8296,
           0.779824,0.564128,0.91256,0.8296,0.564128,0.929152,0.730048,0.813008,0.431392,0.613904]
})

chart2Source['Timestamp']=pd.to_datetime(chart2Source['Time'], unit='ms')
chart2Source['Healthy']=chart2Source.apply(lambda row : row['HRV']>0.799592, axis=1).astype(int)
chart2Source['Healthy']=np.where(chart2Source['Healthy'], 'Healthy', 'Unhealthy')

#figure2=px.scatter(chart2Source, x='Timestamp', y='HRV', color='Healthy', title="time vs HRV")
figure2=go.Figure()
figure2.add_trace(go.Scatter(x=chart2Source['Timestamp'], y=chart2Source['HRV'], mode='lines+markers'))

threshold1=chart2Source['HRV'].max()
threshold2=chart2Source['HRV'].quantile(q=0.8413)
threshold3=chart2Source['HRV'].quantile(q=0.5)
threshold4=chart2Source['HRV'].quantile(q=0.1587)
threshold5=chart2Source['HRV'].min()

figure2.add_hrect(y0=threshold2, y1=1,
                  annotation_text="No Stress at all", annotation_position="top right",
                  fillcolor="blue", opacity=0.3, line_width=0)

figure2.add_hrect(y0=threshold3, y1=threshold2,
                  annotation_text="Healthy Stress", annotation_position="top right",
                  fillcolor="blue", opacity=0.1, line_width=0)

figure2.add_hrect(y0=threshold4, y1=threshold3,
                  annotation_text="Slight Stress", annotation_position="top right",
                  fillcolor="red", opacity=0.1, line_width=0)

figure2.add_hrect(y0=0.4, y1=threshold4,
                  annotation_text="Severe Stress", annotation_position="top right",
                  fillcolor="red", opacity=0.3, line_width=0)

chart3Source=pd.DataFrame({
    'Timestamp':[pd.Timestamp(2021, 11, 10, 0), pd.Timestamp(2021, 11, 10, 1), pd.Timestamp(2021, 11, 10, 2),
                 pd.Timestamp(2021, 11, 10, 3), pd.Timestamp(2021, 11, 10, 4), pd.Timestamp(2021, 11, 10, 5),
                 pd.Timestamp(2021, 11, 10, 6), pd.Timestamp(2021, 11, 10, 7), pd.Timestamp(2021, 11, 10, 8), 
                 pd.Timestamp(2021, 11, 10, 9), pd.Timestamp(2021, 11, 10, 10), pd.Timestamp(2021, 11, 10, 11)],
    'HRV':[0.962336,0.66368,1.128256,0.547536,0.929152,1.012112,1.16144,0.779824,0.613904,0.58072,0.895968,0.91256]
})

figure3=go.Figure()
figure3.add_trace(go.Scatter(x=chart3Source['Timestamp'], y=chart3Source['HRV'], mode='lines+markers'))

#Use the threshold value found in chart2
#Except max and min values
threshold31=chart3Source['HRV'].max()
threshold35=chart3Source['HRV'].min()
figure3.add_hrect(y0=threshold2, y1=threshold31,
                  annotation_text="Unhealthy HRV range", annotation_position="top right",
                  fillcolor="red", opacity=0.3, line_width=0)

figure3.add_hrect(y0=threshold4, y1=threshold2,
                  annotation_text="Healthy HRV range", annotation_position="top right",
                  fillcolor="blue", opacity=0.1, line_width=0)

figure3.add_hrect(y0=threshold35, y1=threshold4,
                  annotation_text="Unhealthy HRV range", annotation_position="top right",
                  fillcolor="red", opacity=0.3, line_width=0)


#Activity score is calculated
#STILL = 0
#ON_FOOT = 0.1
#WALKING = 0.5
#RUNNING = 0.8
#ON_BICYCLE = 0.8
#TILTING, IN_VEHICLE, UNKNOWN = not calculated
chart4Source=pd.DataFrame({
  'HRV':[0.962336,0.66368,1.128256,0.547536,0.929152,1.012112,1.16144,0.779824,0.613904,0.58072,0.895968,0.91256],
  'Activity_Score':[0.8, 0.1, 0.5, np.NaN, 0.5, 0.8, 0.8, 0, 0.1, 0.8, 0.8, 0.8]
})

figure4=px.scatter(chart4Source, x='Activity_Score', y='HRV', trendline="ols", trendline_scope="overall",
                   title="Activity Score vs HRV")
threshold41=chart4Source['HRV'].max()
threshold45=chart4Source['HRV'].min()

figure4.add_hrect(y0=threshold3, y1=1.25,
                  annotation_text="Healthy Stress Level", annotation_position="top right",
                  fillcolor="blue", opacity=0.3, line_width=0)

figure4.add_hrect(y0=0.5, y1=threshold3,
                  annotation_text="Unhealthy Stress Level", annotation_position="top right",
                  fillcolor="red", opacity=0.1, line_width=0)







chart1Layout = html.Div(children=[
    html.Div(children=['chart 1 - GSR vs HRV']),
    dcc.Graph(
        id='chart1',
        #figure={l
        #    'data': [{
        #        'x':chart1Source['deltaGSR'],
        #        'y':chart1Source['HRV']
        #    }]
        #}
        figure=figure1
    )
])
chart2Layout=html.Div(children=[
    html.Div(children=['chart 2 - time vs HRV']),
    dcc.Graph(
        id='chart2',
        figure=figure2
    )
])
chart3Layout=html.Div(children=[
    html.Div(children=['chart 3 - time vs HRV : My Stress level']),
    dcc.Graph(
        id='chart3',
        figure=figure3
    )
])
chart4Layout = html.Div(children=[
    html.Div(children='chart 4 - Physical Activity vs HRV'),
    html.Div(children=['We calculated Physical Activity Score to quantize the activity value and deal with numbers']),
    html.Br(),
    html.Div(children=['STILL = 0']),
    html.Div(children=['ON_FOOT = 0.1']),
    html.Div(children=['WALKING = 0.5']),
    html.Div(children=['RUNNING = 0.8']),
    html.Div(children=['ON_BICYCLE = 0.8']),
    html.Div(children=['TILTING, IN_VEHICLE, UNKNOWN = not calculated']),
    dcc.Graph(
        id='chart4',
        figure=figure4
    ),
    html.Div(children=['We can see that enough physical activity increases HRV.']),
    html.Div(children=['And Increasing HRV means that you are not stressed!'])
])




# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/signin':
        return signup_layout
    elif pathname == '/signup':
        return signin_layout
    elif pathname == '/':
        return main_layout
    elif pathname == '/chart1':
        return chart1Layout
    elif pathname == '/chart2':
        return chart2Layout
    elif pathname == '/chart3':
        return chart3Layout
    elif pathname == '/chart4':
        return chart4Layout
    else:
        return 'wrong pathname'
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)
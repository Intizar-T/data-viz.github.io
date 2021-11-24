import dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import dash_bootstrap_components as dbc
from process import preprocess
from flask import Flask
from dash import dcc, html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])

x = preprocess()


app.layout = html.Div(
        [
            html.Div(
                dcc.Dropdown(id='my-dropdown', options=[{'label': user, 'value': user} for user in x.users()], placeholder="UID"),
                style={"marginTop":"15px", "marginLeft": "43%", "width":"15%", "maxHeight":"20px"}
            ),
            html.Div(id="user-infos", children=[]),
            html.Br(),
            html.Div(id="gsr-hrv-time", children=[]),
            html.Br(),          
            html.Div(id="phy-activity", children=[])
        ]
)
 

def body_infos_2(value, infos):
    infos_1 = infos.copy()
    del infos_1["Gender"], infos_1["Age"]

    fig = px.bar(x=list(infos_1.keys()), y=list(infos_1.values()))
    return html.Div(
            [
                html.Div(
                    html.H3(f"{value}"),
                    className="lead d-flex justify-content-center text-center"
                ),

                html.Div(
                    html.Div(
                        html.H6("Mental Health Spectrum"),
                        className="lead d-flex justify-content-center text-center"
                    ),

                    html.Div(
                        dcc.Graph(figure=fig),
                        className=""
                    )
                )

            ]
        )


def body_infos_1(value, infos):
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.H3(f"{value}"), className="col-2 offset-5 lead d-flex justify-content-center text-center")
                ]

            ),
            dbc.Row(
                [
                    dbc.Col(html.P(f"{infos['Gender']}, {infos['Age']}"), className="col-2 offset-5 small lead d-flex justify-content-center text-center")        
                ]
            ),
            html.Br(),
    
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Openness", className="card-title d-flex justify-content-center text-center", style={"fontWeight":"500"}),
                                    html.Br(),
                                    html.H6(f"{infos['Openness']}", className="card-subtitle fw-bold d-flex justify-content-center text-center"),
                                    html.Br(),
                                    html.P("High - Inventive/ Curious", className="lead", style={"fontSize":"13px"}),
                                    html.P("Low - Consistent/ Cautious", className="lead", style={"fontSize":"13px"})
                                ],
                            ),
                            className="bg-light"
                        ),
                        className="col-md-2 offset-md-1 col-sm-12"
                    ),
                    
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Conscientiousness", className="card-title d-flex justify-content-center text-center", style={"fontWeight":"500"}),
                                    html.Br(),
                                    html.H6(f"{infos['Conscientiousness']}", className="card-subtitle fw-bold d-flex justify-content-center text-center"),
                                    html.Br(),
                                    html.P("High - Efficient/ Organized", className="lead", style={"fontSize":"13px"}),
                                    html.P("Low - Easy-going/ Careless", className="lead", style={"fontSize":"13px"})
                                ]
                            ),
                            className="bg-light"
                        ),
                        className="col-md-2 col-sm-12"
                    ),
                    
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Neuroticism", className="card-title d-flex justify-content-center text-center", style={"fontWeight":"500"}),
                                    html.Br(),
                                    html.H6(f"{infos['Neuroticism']}", className="card-subtitle fw-bold d-flex justify-content-center text-center"),
                                    html.Br(),
                                    html.P("High - Sensitive/ Nervous", className="lead", style={"fontSize":"13px"}),
                                    html.P("Low - Secure/ Confident", className="lead", style={"fontSize":"13px"})
                                ]
                            ),
                            className="bg-light"
                        ),
                        className="col-md-2 col-sm-12",
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Extraversion", className="card-title d-flex justify-content-center text-center", style={"fontWeight":"500"}),
                                    html.Br(),
                                    html.H6(f"{infos['Extraversion']}", className="card-subtitle fw-bold d-flex justify-content-center text-center"),
                                    html.Br(),
                                    html.P("High - Outgoing/ Energetic", className="lead", style={"fontSize":"13px"}),
                                    html.P("Low - Solitary/ Reserved", className="lead", style={"fontSize":"13px"})
                                ]
                            ),
                            className="bg-light"
                        ),
                        className="col-md-2 col-sm-12"
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Agreeableness", className="card-title d-flex justify-content-center text-center", style={"fontWeight":"500"}),
                                    html.Br(),
                                    html.H6(f"{infos['Agreeableness']}", className="card-subtitle fw-bold d-flex justify-content-center text-center"),
                                    html.Br(),
                                    html.P("High - Friendly/ Caring", className="lead", style={"fontSize":"13px"}),
                                    html.P("Low - Unsociable/ Detached", className="lead", style={"fontSize":"13px"})
                                ]
                            ),
                            className="bg-light"
                        ),
                        className="col-md-2 col-sm-12"
                    )
                ]
            ),
            html.Br(),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(html.P("Mental Health Spectrum"), className="col-4 offset-4 small lead d-flex justify-content-center text-center")        
                ]
            ),

            dbc.Row(
                [
                dbc.Col(
                        html.P("Very Poor", className="lead fw-normal px-0", style={"fontSize":"15px"}),
                        className="col-md-2 offset-md-1 d-flex justify-content-center text-center" 
                ),

                dbc.Col(
                        html.P("Poor", className="lead fw-normal px-0", style={"fontSize":"15px"}),
                        className="col-md-3 d-flex justify-content-center text-center" 
                ),
                dbc.Col(
                        html.P("Good", className="lead fw-normal px-0", style={"fontSize":"15px"}),
                        className="col-md-3 d-flex justify-content-center text-center" 
                ),
                dbc.Col(
                        html.P("Very Good", className="lead fw-normal", style={"fontSize":"15px"}),
                        className="col-md-2 d-flex justify-content-center text-center" 
                )
                ]
            ),

            dbc.Row(
                [
                dbc.Col(
                        html.Div(style={"backgroundColor":"#750000", "minHeight":"20px"}),
                        className="col-md-2 offset-md-1" 
                ),
                dbc.Col(
                        html.Div(style={"backgroundColor":"#B50000", "minHeight":"20px"}),
                        className="col-md-3" 
                ),
                dbc.Col(
                        html.Div(style={"backgroundColor":"#7FB2F0", "minHeight":"20px"}),
                        className="col-md-3" 
                ),
                dbc.Col(
                        html.Div(style={"backgroundColor":"#35478C", "minHeight":"20px"}),
                        className="col-md-2" 
                )
                ]
            )
        ],
        style={"marginTop": "40px"}
    )

def stress_level(df):
    labels = list(df.index.values)
    poor, very_poor = 0, 0
    for label in labels:
        if label == 'Poor':
            poor = df.loc['Poor', 'Temperature']
        elif label == 'Very Poor':
            very_poor = df.loc['Very Poor', 'Temperature']
    
    total = np.sum(df.iloc[:, 1])
    if total == 0:
        return 0
    else:
        return round(((poor +  very_poor) / total) * 100, 1)


def gsr_hrv_time(df1, df2):
    card_hrv = dbc.Card(
        dbc.CardBody(
            [
                html.H4("HRV", className="card-title display-5 fw-normal"),
                html.Br(),
                html.P("Who knew how important the interval between each of your heartbeats are?", className="card-subtitle lead fw-normal"),
                html.Br(),
                html.P(
                    "Some quick example text to build on the card title and make "
                    "up the bulk of the card's content.",
                    className="card-text",
                ),
                html.Br(),           
                dbc.CardLink("Read More", href="#", style={"textDecoration": "none", "color": "inherit"}),
            ]
        ),
        style={"width": "18rem"},
    )

    card_gsr = dbc.Card(
        dbc.CardBody(
            [
                html.H4("GSR", className="card-title display-5 fw-normal"),
                html.Br(),
                html.P("What you wear on your body can actually indicate ...", className="card-subtitle lead fw-normal"),
                html.Br(),
                html.P(
                    "GSR can be used as a stress indicator when analyzed carefully"
                    "Some quick example text to build on the card title and make "
                    "up the bulk of the card's content.",
                    className="card-text",
                ),
                html.Br(),          
                dbc.CardLink("Read More", href="#", style={"textDecoration": "none", "color": "inherit"}),
            ]
        ),
        style={"width": "18rem"},
    )
     
    progress_bar = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.P("Stress Level"), className="col-4 offset-4 small lead d-flex justify-content-center text-center")        
                ]
            ),

            dbc.Row(
                [
                    dbc.Progress(label=f"{stress_level(df2)}%", value=stress_level(df2), color="danger", style={"height": "30px", "fontWeight":"600"})
                ],
                className="mx-auto px-0", style={"width":"80%"}
            )
        ]
    )
    gsr_hrv_graph = go.Figure()
    gsr_hrv_graph.add_trace(
        go.Scatter(
            x=df1[df1['label'] == 'Very Poor']['Gsr_difference'],
            y=df1[df1['label'] == 'Very Poor']['Interval'],
            mode="markers",
            name="Very Poor",
            marker_color="#750000")
    )
    gsr_hrv_graph.add_trace(
        go.Scatter(
            x=df1[df1['label'] == 'Poor']['Gsr_difference'],
            y=df1[df1['label'] == 'Poor']['Interval'],
            mode="markers",
            name="Poor",
            marker_color="#B50000")
    )
    gsr_hrv_graph.add_trace(
        go.Scatter(
            x=df1[df1['label'] == 'Good']['Gsr_difference'],
            y=df1[df1['label'] == 'Good']['Interval'],
            mode="markers",
            name="Good",
            marker_color="#7FB2F0")
    )
    gsr_hrv_graph.add_trace(
        go.Scatter(
            x=df1[df1['label'] == 'Very Good']['Gsr_difference'],
            y=df1[df1['label'] == 'Very Good']['Interval'],
            mode="markers",
            name="Very Good",
            marker_color="#35478C")
    )

    #gsr_hrv_graph = px.scatter(df1.sort_values(by='label'), x='Gsr_difference', y='Interval', color='label', color_discrete_sequence=['#7FB2F0', '#B50000', '#35478C', '#750000'])
    gsr_hrv_graph.update_layout(showlegend=False, template='plotly_dark')
    gsr_hrv_graph.update_xaxes(title_text='', showticklabels=False)
    gsr_hrv_graph.update_yaxes(title_text='Hear Rate Variability')

    hrv_time_graph = go.Figure()
    hrv_time_graph.add_trace(
        go.Scatter(
            x=df1.index,
            y=df1['Interval'],
            mode='lines+markers',
            name='HRV',
            line_color='rgb(0,100,80)'
            )
    )
    hrv_time_graph.update_layout(
        xaxis_title='Time',
        yaxis_title='HRV',
        xaxis=
            dict(
                rangeselector=dict(
                    buttons=list([
                        dict(label="sec", step="second"),
                        dict(label="min", step="minute"),
                        dict(label="hour", step="hour"),
                        dict(label="day", step="day"),
                        dict(label="all", step="all")
                    ])
                )
            )
    )

    body_health = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            card_hrv,
                            html.Br(),
                            html.Br(),
                            card_gsr
                        ],
                        className="offset-sm-4 col-sm-8 offset-md-1 col-md-3"
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(figure=gsr_hrv_graph),
                            dcc.Graph(figure=hrv_time_graph) 
                        ],
                        className="offset-sm-2 col-sm-10 col-md-6"

                    )
                ]
            ),
        
            progress_bar
        ]
    )

    return body_health



def physical_activity_graph(df):
    card_physical = dbc.Card(
        dbc.CardBody(
            [
                html.H4("Physical Activity", className="card-title display-5 fw-normal"),
                html.Br(),
                html.P("What you wear on your body can actually indicate ...", className="card-subtitle lead fw-normal"),
                html.Br(),
                html.P(
                    "GSR can be used as a stress indicator when analyzed carefully"
                    "Some quick example text to build on the card title and make "
                    "up the bulk of the card's content.",
                    className="card-text",
                ),
                html.Br(),          
                dbc.CardLink("Read More", href="#", style={"textDecoration": "none", "color": "inherit"}),
            ]
        ),
        style={"width": "18rem"},
    )

    physical_graph = px.scatter(df, y='confidence', color="type")
    physical_graph.update_layout(template='plotly_dark')
    physical_graph.update_xaxes(title_text='')

    page_footer = html.Footer(
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P("Contact Us", className="lead")
                            ],
                            className="col-md-3"
                        ),
                        dbc.Col(
                            [
                                html.P("About", className="lead")
                            ],
                            className="col-md-5"
                        ),
                        dbc.Col(
                            [
                                html.P("Members", className="lead"),
                                html.Br(),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col(html.P("/"), className="col-md-4 mt-2"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-github"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-linkedin"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3")
                                    ]
                                ),
                                html.Br(),

                                dbc.Row([
                                    dbc.Col(html.P("/"), className="col-md-4 mt-2"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-github"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-linkedin"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3")
                                    ]
                                ),
                                html.Br(),

                                dbc.Row([
                                    dbc.Col(html.P("/", className="small"), className="col-md-4 mt-2"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-github"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3"),
                                    dbc.Col(dcc.Link(html.I(className="bi bi-linkedin"), href="/", target="_blanket", style={"fontSize": "25px", "padding": "10px", "width": "80px", "height": "80px", "borderRadius": "50%", "color": "#f2f2f2"}), className="col-md-3")
                                    ]
                                ),
                            ],
                            className="col-md-3"
                        )
                    ]
                ),

                dbc.Row(html.P("Copyright &copy; 2021 All rights reserved.", className="small copyright", style={"marginTop":"120px"}), className="text-center")
            ],
            style={"padding": "40px", "paddingBottom": "0px", "borderTop": "1px solid #eee", "marginTop":"70px"}
        ),
        className="text-center",
        style={"position":"relative", "height":"500px", "bottom":"0", "left":"0", "width":"100%", "backgroundColor": "#052E3C", "color": "#f2f2f2"}
    )

    body_physical = html.Div(
        [
            dbc.Row(
                [
                    dbc.Row([
                        html.Div(html.Button("AM", id="am", className="me-2 btn btn-secondary px-10", n_clicks=0), className="btn-group btn-group-sm mr-1", style={"margin": "100px 5px 0px 105px", "width":"15%"}),
                        html.Div(html.Button("PM", id="pm", className="me-2 btn btn-secondary px-10", n_clicks=0), className="btn-group btn-group-sm mr-1", style={"margin": "100px 5px 0px 20px", "width":"15%"})
                    ]),
                    dbc.Row(
                        dbc.Col(
                            dcc.Graph(figure=physical_graph),
                            className="offset-md-1"
                        )
                    )
                ]
            ),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="daily_phy"), className="col-sm-10 col-md-8"),
                    dbc.Col(card_physical, className="col-sm-10 col-md-4")
                ]
            ),
            page_footer
        ]
    )

    return body_physical  

@app.callback(
    Output('user-infos', 'children'),
    Input('my-dropdown', 'value')
)
def user_infos(value):
    if value is None:
        raise PreventUpdate
    else:
        infos = x.extract_user_info(value)
        return body_infos_1(value, infos)



@app.callback(
    Output('gsr-hrv-time', 'children'),
    Output('phy-activity', 'children'),
    Input('my-dropdown', 'value')
)
def insert_graphs(value):
    if value is None:
        raise PreventUpdate
    else:
        skin_gsr_hrv, phy, level = x.wrapper_function(value, cleaned=True, preprocessed=True)        
        return gsr_hrv_time(skin_gsr_hrv, level), physical_activity_graph(phy)


if __name__ == "__main__":
    app.run_server(debug=True)
import dash
import plotly.express as px
import plotly.graph_objects as go
from process import preprocess
from flask import Flask, render_template
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])

x = preprocess()
users = x.users()
#skin_gsr, gsr_hrv, phy = x.wrapper_function('P0720')

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])



nav = html.Div(
    [
        html.Ul(
            [
                html.Li(dcc.Link("<UID>", href="/", className="navbar-link lead fw-bold d-flex align-items-center py-0 px-4 ms-3 mb-1 mb-md-4", style={"textDecoration": "none", "color": "black"}), className="nav-item"),
                html.Li(dcc.Link("Health", href="/health", className="nav-link lead fw-normal d-flex align-items-center py-0 px-4 ms-3 mb-1 mb-md-4", style={"color": "black"}), className="nav-item"),     
                html.Li(dcc.Link("Stress", href="/stress", className="nav-link lead fw-normal d-flex align-items-center py-0 px-4 ms-3 mb-1 mb-md-4", style={"color": "black"}), className="nav-item"),    
                html.Li(dcc.Link("Result", href="/result", className="nav-link lead fw-normal d-flex align-items-center py-0 px-4 ms-3 mb-1 mb-md-4", style={"color": "black"}), className="nav-item")
            ],
            className="navbar-nav flex-row flex-wrap"
        ),
        html.Ul(
            [
                #html.Li(dcc.Link(html.I(className="fas fa-user-circle"), href="/profile", className="nav-link d-flex align-items-center py-0 px-4 ms-3 mb-1 mb-md-4", style={"color": "black"}), className="nav-item"),
                html.Li(dbc.Button(dcc.Link("Exit", href="/signin", className="fw-normal", style={"textDecoration": "none", "color": "black"}), outline=True, color="light", className="me-1 mb-2 btn-sm"), className="nav-item")
            ],
            className="navbar-nav flex-row flex-wrap ms-auto"
        )   
    ],
    className="nav fixed-top navbar-expand-md navbar-dark pt-4 pl-4 pe-4 pb-0 mx-auto",
    style={"backgroundColor": "#658B97", "fontWeight": "600", "fontSize": "15px"}
)



footer = html.Footer(
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
            html.P(
                "Blue - Healthy ranges", className="fw-bold", style={"color":"blue"}
            ),
            html.P(
                "Red - Unhealthy ranges", className="fw-bold", style={"color":"red"}
            ),            
            dbc.CardLink("Read More", href="#"),
        ]
    ),
    style={"width": "18rem", "marginTop": "90px"},
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
            html.P(
                "Blue - Healthy ranges", className="fw-bold", style={"color":"blue"}
            ),
            html.P(
                "Red - Unhealthy ranges", className="fw-bold", style={"color":"red"}
            ),              
            dbc.CardLink("Read More", href="#"),
        ]
    ),
    style={"width": "18rem"},
)





card_physical = html.Div(
    [
        html.H3("Physical Activity", className="fw-bold"),
        html.Div(
            [
                html.Br(),
                html.P("The ultimate solution to all our health problems!", className="lead fw-normal"),
                html.Br(),
                html.P(
                    "GSR can be used as a stress indicator when analyzed carefully"
                    "Some quick example text to build on the card title and make "
                    "up the bulk of the card's content.",
                    className="",
                ),
                html.Br(),
            ],
            className="bg-light"
        )
    ]
)




body_home = html.Div(
    [
        html.Div(id="user-infos", children=[], style={"marginTop":"90px"})
    ]
)



body_health = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        card_hrv,
                        html.Br(),
                        html.Br(),
                        card_gsr
                    ],
                    className="col offset-sm-4 col-sm-8 offset-md-1 col-md-3"
                ),
                html.Div(
                    [
                        dcc.Graph(id="hrv_gsr", className="row col-12"),
                        dcc.Graph(id="hrv_gsr", className="row col-12")
                    ],
                    className="col offset-sm-2 col-sm-10 col-md-6"
                )
            ],
            className="row"
        )
    ],
    className="conatiner-fluid"
)



body_stress = html.Div(
            [
                html.Div(
                    [
                        html.P("Current stress level", className="text-center lead fw-normal"),
                        html.Div(dbc.Progress(label="73%", value=73, color="danger", style={"height": "30px"}), className="mx-auto", style={"width":"80%"})
                    ],
                    className="row", style={"marginTop":"90px"}
                ),

                html.Div(
                    [
                        html.Div([
                            html.Div(html.Button("AM", id="am", className="me-2 btn btn-secondary px-10", n_clicks=0), className="btn-group btn-group-sm mr-1", style={"margin": "100px 5px 0px 70px", "width":"10%"}),
                            html.Div(html.Button("PM", id="pm", className="me-2 btn btn-secondary px-10", n_clicks=0), className="btn-group btn-group-sm mr-1", style={"margin": "100px 5px 0px 20px", "width":"10%"})
                        ]),
                        html.Div(dcc.Graph(id="str_phy"))
                    ],
                    className="row offset-md-1"
                ),

                html.Div(
                    [
                        html.Div(dcc.Graph(id="daily_phy"), className="col offset-sm-1 col-sm-10 col-md-6"),
                        html.Div(card_physical, className="col offset-sm-4 col-sm-8 offset-md-1 col-md-3")
                    ],
                    className="row"
                )
            ]
)



layout_page_signin = html.Div(
        [
            dcc.Store(id="selected-user", data=""),
            dcc.Input(id='input-element', placeholder="UID" , type='text', list="users_ID", style={"borderRadius":"5px"}),
            html.Span(html.I(id="button-element", n_clicks=0, className="bi bi-arrow-right-circle-fill"), className="btn mb-2"),
            html.Datalist(id="users_ID", children=[html.Option(value=user) for user in users]),
            html.Div(id="output-element", children=[]),
        ],
        style={"marginLeft": "43%", "marginTop":"18%"}
)



layout_page_profile = html.Div(
    [
        nav,
        html.H3("User infos", style={"marginTop":"100px"}),
        footer
    ]
)



layout_page_health = html.Div(
    [
        nav,
        body_health,
        footer
    ]
)



layout_page_stress = html.Div(
    [
        nav,
        body_stress,
        footer
    ]
)



layout_page_result = html.Div(
    [
        nav,
        html.H3("Results", style={"marginTop":"100px"}),
        footer  
    ]
)



app.layout = url_bar_and_content_div

app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_page_profile,
    layout_page_health,
    layout_page_stress,
    layout_page_result,
    layout_page_signin
])



@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == "/signin":
        return layout_page_signin        
    elif pathname == "/health":
        return layout_page_health
    elif pathname == "/stress":
        return layout_page_stress
    elif pathname == "/result":
        return layout_page_result     
    else:
        return layout_page_profile




@app.callback(
    [Output('selected-user', 'data'), Output('output-element', 'children')],
    Input('button-element', 'n_clicks'),
    State('input-element', 'value')
)
def on_signin(n_clicks, value):
    if value is None:
        raise PreventUpdate
    elif value in users:
        return value, dbc.Button(dcc.Link("Continue", href="/", className="fw-normal", style={"textDecoration": "none", "color": "inherit"}), outline=True, color="dark", className="d-flex align-items-center justify-content-center")
    else:
        return value, html.P("Not a proper UID", className="lead mt-1")




@app.callback(
    Output('user-infos', 'children'),
    Input('selected-user', 'data'),
    prevenet_initial_call=False
)
def get_user_infos(value):
    my_list = x.extract_user_info(value)
    if my_list == []:
        return "Hey"
    return my_list



if __name__ == "__main__":
    app.run_server(debug=True)



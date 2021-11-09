import dash
from dash import dcc
from dash import html
from dash import Input, Output

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(__name__, suppress_callback_exceptions=True)

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
    html.Div(['Main Page'])
], id='main_layout')

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
    else:
        return 'wrong pathname'
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)
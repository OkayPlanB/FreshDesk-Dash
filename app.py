from dash import Dash, html, dcc, callback, Input, Output
from ticketCall import *
import dash_bootstrap_components as dbc
import schedule
import time

global RCOpen, FRDue
RCOpen = str(getRCOpen())
FRDue = str(getFRDue())

global KodyTotal, KodyWOC, KodyOpen
KodyTotal, KodyWOC, KodyOpen = getKody()

global GabeTotal, GabeWOC, GabeOpen
GabeTotal, GabeWOC, GabeOpen = getGabe()

global JimmyTotal, JimmyWOC, JimmyOpen
JimmyTotal, JimmyWOC, JimmyOpen = getJimmy()

global PatTotal, PatWOC, PatOpen
PatTotal, PatWOC, PatOpen = getPat()

global RaulTotal, RaulWOC, RaulOpen
RaulTotal, RaulWOC, RaulOpen = getRaul()

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Open RC',
                    style={"background-color": "#f7cca8", "font-size": "20px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='RCValue',
                    style={"text-align": "center", "font-size": "60px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#e8ad7d",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="3"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'FR Due',
                    style={"background-color": "#f7a8b0", "font-size": "20px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='FRDue',
                    style={"text-align": "center", "font-size": "60px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#d97c85",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="3"),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Kody Total',
                    style={"background-color": "#e17de8", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='KodyTotal',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#ee95f5",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Kody WoC',
                    style={"background-color": "#e17de8", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='KodyWoC',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#ee95f5",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Kody Open',
                    style={"background-color": "#e17de8", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='KodyOpen',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#ee95f5",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Gabe Total',
                    style={"background-color": "#6da3de", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='GabeTotal',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#7ca9d9",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Gabe WoC',
                    style={"background-color": "#6da3de", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='GabeWoC',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#7ca9d9",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Gabe Open',
                    style={"background-color": "#6da3de", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='GabeOpen',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#7ca9d9",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        ],
        className="g-0",),
        
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Jimmy Tickets',
                    style={"background-color": "#6ce070", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='JimmyTotal',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#81e385",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Jimmy WoC',
                    style={"background-color": "#6ce070", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='JimmyWoC',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#81e385",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Jimmy Open',
                    style={"background-color": "#6ce070", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='JimmyOpen',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#81e385",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Pat Tickets',
                    style={"background-color": "#e0bf6c", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='PatTotal',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#edd087",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Pat WoC',
                    style={"background-color": "#e0bf6c", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='PatWoC',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#edd087",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    'Pat Open',
                    style={"background-color": "#e0bf6c", "font-size": "15px", "font-weight": "bold"}
                ),
                dbc.CardBody(
                    id='PatOpen',
                    style={"text-align": "center", "font-size": "40px"}
                ),
            ],
            style={"height": "150px", "border-radius": "10px", "background-color": "#edd087",
                "box-shadow": "1px 2px 7px 0px grey"},
            className="border-0")
            ],
            width="2"),
        ],
        className="g-0",)
])

print('Start App') 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

print('App Layout Loaded')
app.layout = dbc.Container([

        layout
        ,
        dcc.Interval(
            id='interval-component',
            interval=60*1000,
            n_intervals=0
        )
    ])


@callback(
    Output(component_id='RCValue', component_property='children'),
    Output(component_id='FRDue', component_property='children'),
    Output(component_id='KodyTotal', component_property='children'),
    Output(component_id='KodyWoC', component_property='children'),
    Output(component_id='KodyOpen', component_property='children'),
    Output(component_id='GabeTotal', component_property='children'),
    Output(component_id='GabeWoC', component_property='children'),
    Output(component_id='GabeOpen', component_property='children'),
    Output(component_id='JimmyTotal', component_property='children'),
    Output(component_id='JimmyWoC', component_property='children'),
    Output(component_id='JimmyOpen', component_property='children'),
    Output(component_id='PatTotal', component_property='children'),
    Output(component_id='PatWoC', component_property='children'),
    Output(component_id='PatOpen', component_property='children'),
    Input('interval-component', 'n_intervals'),
    )
    
def update_output(n):
    RCOpen = getRCOpen()
    FRDue = getFRDue()
    
    KodyTotal, KodyWoC, KodyOpen = getKody()
    
    GabeTotal, GabeWOC, GabeOpen = getGabe()
    
    JimmyTotal, JimmyWOC, JimmyOpen = getJimmy()
    
    PatTotal, PatWOC, PatOpen = getPat()
    
    RaulTotal, RaulWOC, RaulOpen = getRaul()
    
    return RCOpen, FRDue, KodyTotal, KodyWoC, KodyOpen, GabeTotal, GabeWOC, GabeOpen, JimmyTotal, JimmyWOC, JimmyOpen, PatTotal, PatWOC, PatOpen


if __name__ == '__main__':
    app.run_server(debug=False, port='80', host='192.168.150.102')
    #app.run(debug=True)
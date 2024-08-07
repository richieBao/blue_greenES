import dash_bootstrap_components as dbc

from utils.pages.carbon.carbon_callbacks import *

carbon_map=\
    html.Div([
        html.Div([
            
            html.Div(id='folium-map-container-carbon'),
            dcc.Input(id='num-carbon', type='number', debounce=True, min=2, step=1),
            ],            
            # style={'display':'grid','padding-left':'50px'}
            ),     
        ],
        # style={'border-bottom':'solid black 1px','display':'grid','grid-template-columns':'600px auto','height':'580px',
        #        'grid-auto-flow':'row'}
    )        


def layout_carbon():
    layout=dbc.Card(carbon_map, body=True, className="mt-2")                
                
    return layout


# dbc.Card("碳储存和封存", body=True, className="mt-2")

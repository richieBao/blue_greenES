import dash_bootstrap_components as dbc

from utils.pages.carbon.carbon_callbacks import *

carbon_map=\
    html.Div([
        dbc.Row([
            
            dbc.Col([
                html.Div([
                dbc.Button("绘制分析边界", id="draw_boundary"),
                dbc.Button("应用分析边界", id="save_boundary",n_clicks=0),
                dbc.Button("清除所有绘制", id="clear_all")  
                ],className="d-grid gap-2",)
                
            ],md=2),
            
            dbc.Col([
                dbc.Input(id='num-carbon', type='number', debounce=True, min=2, step=1),
                html.Div(id='folium-map-container-carbon'),
            ],md=10)
                        
            ]),  
        

        ],
        # style={'border-bottom':'solid black 1px','display':'grid','grid-template-columns':'600px auto','height':'580px',
        #        'grid-auto-flow':'row'}
    )        


def layout_carbon():
    layout=dbc.Card(carbon_map, body=True, className="mt-2")                
                
    return layout


# dbc.Card("碳储存和封存", body=True, className="mt-2")

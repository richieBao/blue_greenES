import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc,Input, Output,callback,ctx
import dash_leaflet as dl
# from dash_extensions.javascript import assign
import json
import matplotlib.colors as mcolors

from utils.args import args
# from utils.pages.carbon.carbon_callbacks import *
from utils.misc.database import SQLite2df

BLANK_LINE=html.Div(style={'height':'10px'})

def layout_carbon():
    layout=html.Div([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H5("1. 绘制或上载分析区域", className="card-title"),
                    carbon_map,                     
                    ]),
                    className="mt-2"),
            BLANK_LINE,
            dbc.Card([
                dbc.CardBody([
                        block_glc_table,
                        ]),
                    ]),
            BLANK_LINE,
            dbc.Card([
                dbc.CardBody([
                        html.H5("2. 碳库", className="card-title"),
                        ]),
                    ]),
            
                ])        
                     
        ])
                
    return layout

DB_GLC_INFO_SOURCE=args.db.bng_db 
glc_table_name='glc_categories'
glc_categories_df=SQLite2df(DB_GLC_INFO_SOURCE,glc_table_name)

def glc_categories_color():     
    glc_color_hex={str(row["lcid"]):mcolors.to_hex([int(row['color_r'])/255,int(row['color_g'])/255,int(row['color_b'])/255])[1:] for _,row in glc_categories_df.iterrows()}
    return glc_color_hex    

glc_color_hex=glc_categories_color()  
glc_color_hex_str=str(glc_color_hex).replace(" ", "")
glc_color_hex_str=glc_color_hex_str.replace("'", '"')
glc_url=args.map.glc_tile_url+"colormap=explicit&explicit_color_map="+glc_color_hex_str
# print(glc_url)
# glc_url=args.map.glc_tile_url

map_controller = html.Div(children=[
        # html.Div("Parameter"),
        # dcc.Dropdown(id="dd_param", options=[dict(value=p, label=lbl_map[p]) for p in PARAMS], value=param0),
        # html.Br(),
        # html.Div("Colorscale"),
        # dcc.Dropdown(id="dd_cmap", options=[dict(value=c, label=c) for c in cmaps], value=cmap0),
        html.Br(),
        html.Div("透明度"),
        dcc.Slider(id="opacity", min=0, max=1, value=0.5, step=0.1, marks={0: "0", 0.5: "0.5", 1: "1"}),
        html.Br(),
        # html.Div("Stretch range"),
        # dcc.RangeSlider(id="srng", min=srng0[0], max=srng0[1], value=srng0,
        #                 marks={v: "{:.1f}".format(v) for v in srng0}),
        # html.Br(),
        # html.Div("Value @ click position"),
        # html.P(children="-", id="label"),
    ], className="info")

m=dl.Map(children=[
    dl.LayersControl([dl.BaseLayer(dl.TileLayer(url=args.map.url_osm),name="openstreetmap", checked=True),
                      dl.BaseLayer(dl.TileLayer(url=args.map.url_gaode),name="高德地图", checked=False)]+
                     [dl.Overlay(dl.TileLayer(url=glc_url,id="glc",opacity=0.5),name="GLC-30m精细土地覆盖数据", checked=True)],
    #  maxZoom=20,
    id="lc",
    position="bottomleft",
    ),    
    dl.FeatureGroup([dl.EditControl(id="edit_control",position="topright")]),
    dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="hectares",
                      activeColor="#214097", completedColor="#972158"),
    dl.FullScreenControl(),
    ], 
    center=args.map.coordi_XAUAT, 
    zoom=11,
    style={'width': '100%', 'height': '50vh'}, 
    attributionControl=False,
    id="map") # , "display": "inline-block"

carbon_map=\
    html.Div([
        dbc.Row([
            
            dbc.Col([
                html.Div([
                dbc.Button("绘制分析边界", id="draw_boundary"),
                dbc.Button("应用分析边界", id="save_boundary",n_clicks=0), # ,title="仅使用第1个边界"
                html.P(children=["（仅使用绘制的第1个边界）"],className='note',id='save_boundary_info'),
                dbc.Button("清除所有绘制", id="clear_all")  
                ],className="d-grid gap-2",)
                
            ],md=2),
            
            dbc.Col([
                html.Div(children=[
                    # html.Div(id='folium-map-container-carbon'),
                    m,
                    map_controller,                    
                    ],
                    style={"display": "grid"}
                    ),                
            ],md=10)
                        
            ]),  
        
        ],
        # style={'border-bottom':'solid black 1px','display':'grid','grid-template-columns':'600px auto','height':'580px',
        #        'grid-auto-flow':'row'}
    )     

block_glc_table=\
    html.Div([
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the first section"),
                        dash.dash_table.DataTable(
                            glc_categories_df.to_dict("records"),
                            [{"name": i, "id": i} for i in glc_categories_df.columns],
                            id="glc_info_table",
                            page_size=20,
                            ),
                        # dbc.Button("Click here"),
                    ],
                    title="查看 GLC_FCS30D 精细土地覆盖数据信息",
                ),
            ],
            start_collapsed=True,
        ),
        
        ])

#------------------------------------------------------------------------------
@callback(Output("edit_control", "drawToolbar", allow_duplicate=True), Input("draw_boundary", "n_clicks"),prevent_initial_call=True)
def draw_boundary(n_clicks):
    return dict(mode="polygon", n_clicks=n_clicks)  # include n_click to ensure prop changes

# Trigger mode (edit) + action (remove all)
@callback(Output("edit_control", "editToolbar"), Input("clear_all", "n_clicks"))
def clear_all(n_clicks):
    return dict(mode="remove", action="clear all", n_clicks=n_clicks)  # include n_click to ensure prop changes

@callback(
    Output("save_boundary_info", "children"), 
    Input('save_boundary',"n_clicks"),
    Input("edit_control", "geojson"),
    prevent_initial_call=True
    )
def dump_boundary(n_clicks,data):
    if 'save_boundary'==ctx.triggered_id and data['features']:   
        # print(data)
        with open(args.workspace.draw_boundary_fn,'w') as f:
            json.dump(data,f)
        return "（已应用绘制的分析边界）"
    else:
        return "（仅使用绘制的第1个边界）"
        

@callback(Output("glc", "opacity"), [Input("opacity", "value")])
def update_opacity(opacity):
    return opacity


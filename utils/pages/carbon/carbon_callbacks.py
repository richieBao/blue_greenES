# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:29:49 2024

@author: richiebao
"""
import dash
from dash import Dash, html, dcc,Input, Output,callback,ctx
import folium

from utils.misc.map import plot_map
from utils.misc.gadgets import colorize_array
from utils.misc.glc_preprocessing import glc_loading,glc_cmap

from utils.args import args
from utils.misc.database import accdb2df

import dash_leaflet as dl
from dash_extensions.javascript import assign
import json

DB_GLC_INFO_SOURCE=args.db.bng_db
table_name='glc_categories'



# @callback(
#     Output('folium-map-container-carbon', 'children'),
#     Input('num-carbon', 'value')
# )
# def map(num):
#     print(f"~~~{num}")
#     # mask = df['Variable'] == dropdown
#     # dff = df[mask].copy()
#     m=plot_map()
    
#     city_name="西安"
#     year=2022    
#     img,img_T,centre_lat, centre_lon,bounds_fin,meta=glc_loading(city_name,year)
    
#     DB_GLC_INFO_SOURCE=args.db.bng_db #r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
#     table_name='glc_categories'
#     df=accdb2df(DB_GLC_INFO_SOURCE,table_name)
#     cmap,norm=glc_cmap(df)    
    
#     print("+++1")
#     colored_data=colorize_array(img[0],cmap=cmap)
#     print("+++2")
    
#     m.add_child(folium.raster_layers.ImageOverlay(
#         image=colored_data,
#         opacity=.7,
#         bounds = bounds_fin,
#         zindex=1,
#         interactive=True,
#         control=True,
#         ))
#     print("+++3")
#     m.location=[centre_lat, centre_lon]
    
    
#     folium.LayerControl(position="bottomleft").add_to(m)
#     print("+++4")
#     # m.save(r'C:\Users\richi\omen_richiebao\omen_github\blue_greenES_workspace\temp\mymap.html')
    
#     src_doc = m.get_root().render()  #obtain the HTML content 
#     return html.Iframe(srcDoc=src_doc, style={'width': '100%','height': '800px'})


# layout = html.Div("Home page content")
# layout = html.Div(id='folium-map-container')

# layout = html.Div([
#     html.Div(id='folium-map-container'),
#     html.P('Enter a composite number to see its prime factors'),
#     dcc.Input(id='num', type='number', debounce=True, min=2, step=1),
#     html.P(id='err', style={'color': 'red'}),
#     html.P(id='out')
# ])

# url_testing="http://localhost:5000/singleband/20002022/E105N35/{z}/{x}/{y}.png?colormap=greys&stretch_range=[10,124.86]"

# @callback(
#     Output('folium-map-container-carbon', 'children'),
#     Input('num-carbon', 'value')
# )
# def map(num):       
    
#     m=dl.Map(center=args.map.coordi_XAUAT, zoom=17, children=[
#         dl.TileLayer(url=args.map.url_gaode), 
#         dl.TileLayer(url=url_testing, maxZoom=20,),
#         dl.FeatureGroup([
#             dl.EditControl(id="edit_control",position="topright")]),
#     ], style={'width': '100%', 'height': '50vh', "display": "inline-block"}, id="map"),
    
#     # m=dl.Map(dl.TileLayer(url=args.map.url_gaode), center=args.map.coordi_XAUAT, zoom=17, style={'height': '50vh'})
    
#     return m

# # Trigger mode (draw marker).
# @callback(Output("edit_control", "drawToolbar"), Input("draw_boundary", "n_clicks"))
# def trigger_mode(n_clicks):
#     return dict(mode="polygon", n_clicks=n_clicks)  # include n_click to ensure prop changes

# # Trigger mode (edit) + action (remove all)
# @callback(Output("edit_control", "editToolbar"), Input("clear_all", "n_clicks"))
# def trigger_action(n_clicks):
#     return dict(mode="remove", action="clear all", n_clicks=n_clicks)  # include n_click to ensure prop changes

# # Copy data from the edit control to the geojson component.
# @callback(
#     # Output("geojson", "data"), 
#     Input('save_boundary',"n_clicks"),
#     Input("edit_control", "geojson"))
# def dump_boundary(n_clicks,data):
#     if 'save_boundary'==ctx.triggered_id and data['features']:   
#         print(data)
#         with open(args.workspace.draw_boundary_fn,'w') as f:
#             json.dump(data,f)
    
    # return x
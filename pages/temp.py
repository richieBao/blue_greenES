# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:35:35 2024

@author: richi
"""
import dash
from dash import Dash, html, dcc,Input, Output,callback

import folium
from folium.plugins import Draw,MeasureControl,MiniMap,MousePosition

dash.register_page(__name__,name="TEMP", path='/temp')

def plot_map():
    #ommited code
    coordinate = (34.237075,108.967996)
    m = folium.Map(location=coordinate, zoom_start=17, world_copy_jump=True, prefer_canvas=True)
    #ommited code
    
    m.add_child(MeasureControl())
    
    url1 ='http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
    # url2 = "http://webst04.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}"
    
        
    folium.TileLayer(tiles = url1, name = "高德地图", attr='amap', control = True,show=True).add_to(m)    
    MousePosition().add_to(m)
    MiniMap(toggle_display=True).add_to(m)
    folium.plugins.Geocoder(position="bottomleft").add_to(m)    
    
    Draw(
        export=True,
        # filename=save_fn,
        position="topleft",
        draw_options={
            "polyline": True,
            "rectangle": True,
            "circle": True,
            "circlemarker": True,
        },
        edit_options={"poly": {"allowIntersection": False}},
    ).add_to(m)    
    
    
    
    src_doc = m.get_root().render()  #obtain the HTML content 
    return src_doc



@callback(
    Output('folium-map-container', 'children'),
    Input('num', 'value')
)
def make_folium_map(num):
    print(f"~~~{num}")
    # mask = df['Variable'] == dropdown
    # dff = df[mask].copy()
    return html.Iframe(srcDoc=plot_map(), style={'width': '100%','height': '800px'})



# layout = html.Div("Home page content")
# layout = html.Div(id='folium-map-container')

layout = html.Div([
    html.Div(id='folium-map-container'),
    html.P('Enter a composite number to see its prime factors'),
    dcc.Input(id='num', type='number', debounce=True, min=2, step=1),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])
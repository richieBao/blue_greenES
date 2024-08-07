# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:29:49 2024

@author: richiebao
"""
import dash
from dash import Dash, html, dcc,Input, Output,callback

from utils.pages.misc.map import plot_map


@callback(
    Output('folium-map-container-carbon', 'children'),
    Input('num-carbon', 'value')
)
def make_folium_map(num):
    print(f"~~~{num}")
    # mask = df['Variable'] == dropdown
    # dff = df[mask].copy()
    return html.Iframe(srcDoc=plot_map(), style={'width': '100%','height': '800px'})

# layout = html.Div("Home page content")
# layout = html.Div(id='folium-map-container')

# layout = html.Div([
#     html.Div(id='folium-map-container'),
#     html.P('Enter a composite number to see its prime factors'),
#     dcc.Input(id='num', type='number', debounce=True, min=2, step=1),
#     html.P(id='err', style={'color': 'red'}),
#     html.P(id='out')
# ])



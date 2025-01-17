from dash import html
import dash_bootstrap_components as dbc

path_pagename_map = {
    "/calculate/carbon": "碳储存和封存",
    "/calculate/topic-2": "",
    "/calculate/topic-3": ""
}

def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(name, className="ms-2"),
                    ],
                    href=href,
                    active="exact",
                )
                for href, name in path_pagename_map.items()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )

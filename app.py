import dash

from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
suppress_callback_exceptions=True

# select the Bootstrap stylesheets and figure templates for the theme toggle here:
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
# dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = dash.Dash(
    __name__,
    use_pages=True,
    # external_stylesheets=[dbc.themes.BOOTSTRAP,url_theme2,], 
    external_stylesheets=[dbc.themes.SLATE,'/assets/custom.css',],
    suppress_callback_exceptions=True
    
)
# app.config.suppress_callback_exceptions=True

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

footer = dbc.Container(
    dbc.Row(
        [
            dbc.Col(html.A("richiebao | GitHub", href="https://github.com/richieBao"), align="right"),
        ],
    ),
    className="footer",
    fluid=True,
)

navbar = dbc.NavbarSimple(
    # dbc.Nav(
    #     [
    #         dbc.NavLink(page["name"], href=page["path"])
    #         for page in dash.page_registry.values()
    #     ],
    # ),
    children=[
        dbc.NavItem(dbc.NavLink("主页", href="/")),
        dbc.NavItem(dbc.NavLink("计算", href="/calculate/topic-1")),
        dbc.NavItem(dbc.NavLink("数据库", href="/database")),
        dbc.NavItem(dbc.NavLink("TEMP", href="/temp")),
        
    ],    
    
    brand="城市蓝绿空间规划与生态系统服务功能优化技术 —— 专项科学计算工具",
    brand_href="/",
    color="dark", #"primary","dark"
    dark=True,
    # className="mb-2",
)


app.layout = dbc.Container(
    [navbar, theme_toggle,dash.page_container,footer],
    fluid=True,
)


# Overall layout
# app.layout = html.Div([
#     navbar,  # Include the navigation bar
#     # theme_toggle,
#     dash.page_container,
#     footer,  # Include the footer
# ])


if __name__ == "__main__":
    print([(page['name'],page['path']) for page in  dash.page_registry.values()])
    app.run_server(debug=True)

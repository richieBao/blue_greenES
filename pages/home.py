from dash import html,dcc
import dash

dash.register_page(__name__, path="/")


layout = html.Div( 
    
    html.Iframe(
       src="https://boardmix.cn/app/share/CAE.CIiKvQ4gASoQV3oL583gdIVqGxboyEBfWzAGQAE/4vHZHN?elementNodeGuid=5:1483",
       width="100%",height="1000"    
        ),
    )
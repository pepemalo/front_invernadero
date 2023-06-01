from dash import Dash, dcc, html, Input, Output, dash_table, dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import date
import pandas as pd
import base64
import datetime
import io
import os



app = Dash(__name__, external_stylesheets=[
           dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

server = app.server

PLOTLY_LOGO = "https://www.redttu.edu.co/es/wp-content/uploads/2015/12/23.-ISER.png"
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "07rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#004B23", # BARRA IZQUIERDA
}
SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "margin": "100vw",
    #"padding": 0,   
    #"background-color": "#c1fba4",
    "background": "linear-gradient(to right, #C5F9D7, #c1fba4)"
}
CALEN_STYLE = {
    "margin-left": "2rem",
    "margin-right": "0rem",
}
LATERAL_STYLE = {
    "position": "relative",
    "width": "90px",
    "padding": "1px",
    "margin-right": "0px",
    "margin-left": "1px",
}


cart_style = {
    'background-color': 'white',
    'border': '2px solid gray',
    'border-radius': '10px',
    'padding': '10px',
    'width': '100%',
    'height': '150px',
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'justify-content': 'center'
}

cart_text_style = {
    'font-size': '30px',
    'font-weight': 'bold',
    'cursor': 'pointer'
}


sidebar = html.Div(
    [

    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/img/img1.png"},
        {"key": "2", "src": "/img/greenhouse-g9e7235412_640.png"},
        {"key": "3", "src": "/img/img3.png"},
        {"key": "4", "src": "/img/img4.png"},
    ],
    controls=True,
    indicators=True,
)
nav = dbc.Nav(

    [
        dbc.NavItem(dbc.NavLink("Menu", active=True,
                    className="text-white", id="btn_sidebar", href="#")),
        dbc.NavItem(dbc.NavLink("Graficas", className="text-white",
                    active=True, href="/graficas")),
        dbc.NavItem(dbc.NavLink(
            "Manual", className="text-white", href="/manual")),
        dbc.NavItem(dbc.NavLink("Modal", className="text-white",
                    id="open", n_clicks=0, href="#")),
        dbc.Modal(
            [
                dbc.ModalHeader("DESARROLLADO POR", className="modal-title font-weight-bold text-primary",
                                style={"text-align": "center", "font-size": "2rem"}),
                html.H2("Anderson Cardozo Arrieta", className="card-text"),
                html.H2(" ", className="card-text"),
                html.H2("Yordan Daniel Tarazona Gamboa",
                        className="card-text"),
                html.H2(" ", className="card-text"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Cerrar", id="close", className="ms-auto", color="outline-success", n_clicks=0
                    )
                ),
            ], id="modal",
            is_open=False,
        ),
    ],
    style=LATERAL_STYLE,
)
nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Menu", active=True,
                    className="text-white", id="btn_sidebar", href="#")),
        dbc.NavItem(dbc.NavLink("Graficas", className="text-white",
                    active=True, href="/graficas")),
        dbc.NavItem(dbc.NavLink(
            "Manual", className="text-white", href="/manual")),
        dbc.NavItem(dbc.NavLink("Modal", className="text-white",
                    id="open", n_clicks=0, href="#")),
        dbc.Modal(
            [
                dbc.ModalHeader("DESARROLLADO POR", className="modal-title font-weight-bold text-primary",
                                style={"text-align": "center", "font-size": "2rem"}),
                html.H2("Anderson Cardozo Arrieta", className="card-text"),
                html.H2(" ", className="card-text"),
                html.H2("Yordan Daniel Tarazona Gamboa",
                        className="card-text"),
                html.H2(" ", className="card-text"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Cerrar", id="close", className="ms-auto", color="outline-success", n_clicks=0
                    )
                ),
            ], id="modal",
            is_open=False,
        ),
    ],
    style=LATERAL_STYLE,
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="80px")),
                        dbc.Col(dbc.NavbarBrand("Invernadero", className="text-black",
                                                style={"font-size": "24px", "font-weight": "bold", "color": "white"}))
                    ],
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Collapse(
                nav,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
    ),
    color="#008000",  # BARRA SUPERIOR LATERAL
    dark=False,
    className="fixed-top",
    style={"height": "80px"},
)
"""
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            html.A([
                html.Div('Your cart', style=cart_text_style),
                html.Div('Total items: 10'),
                html.Div('Total price: $100')
            ], id='cart-link', href='/robot.py')
        ], width=3, style={'background-color': 'White ', 'color': 'White ', 'height': '20vh', 'width': '40vh', 'padding': '6px', 'border': '8px solid black'}),
        dbc.Col([
            html.Div('Main content goes here')
        ], width=9)
    ], style={'margin': '0px', 'height': '20vh'}),
],
)
"""
plantilla = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div(children=[
    dcc.Store(id='side_click'),
    dcc.Location(id="url"),
    navbar,
    sidebar,
    # app.layout,
    plantilla,
])


@app.callback(Output('url', 'pathname'), [Input('cart-link', 'n_clicks')], [State('url', 'pathname')])
def go_to_robot(n_clicks, pathname):
    if n_clicks is not None:
        return '/robot.py'
    return pathname


@app.callback(
    [Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),],
    [Input("btn_sidebar", "n_clicks")],
    [State("side_click", "data"),]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'
    return sidebar_style, content_style, cur_nclick


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output('bargraph', 'figure'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('selec_grafi', 'value'),
    Input('selec_opc', 'value')
)
def update_graph(start, end, grafi, opci):
    df = ''
    if start and end:
        start = date.fromisoformat(start)
        start = start.strftime('%Y-%m-%d')
        end = date.fromisoformat(end)
        end = end.strftime('%Y-%m-%d')

        if opci == "API":
            print("Conxion por medio de API")
            dt = pd.read_json(
                "https://rest-server-invernadero.onrender.com/api/v1/filterDatos/"+start+"&"+end+"")
            df = pd.DataFrame(dt)
            print("Graficara los archivos ::", df)
        else:
            print("Conxion LOCAL")
            dt = pd.read_csv('../datosTrue01.csv')
            df = pd.DataFrame(dt)
            rango = (df.FECHA >= start) & (df.FECHA <= end)
            df1 = df.loc[rango]
            pd.to_datetime(df1.FECHA, format="%Y/%m/%d")
            aux = None
            fch = []
            for i in df1.FECHA:
                if i != aux:
                    aux = i
                    fch.append(i)
            datos = []
            aux = []
            df2 = df1
            for i in df2:
                if i != 'FECHA':
                    for j in range(0, len(fch)):
                        print("Dentro del for recorriendo j:: ", j)
                        rango = (df.FECHA == fch[j])
                        df1 = df.loc[rango]
                        aux.append(df1[i].mean())
                    datos.append(aux)
                    aux = []
            dtTrue = {'FECHA': fch,
                      'T1': datos[0], 'T2': datos[1], 'T3': datos[2], 'T4': datos[3],
                      'H1': datos[4], 'H2': datos[5], 'H3': datos[6], 'H4': datos[7],
                      'MO1': datos[8], 'MO2': datos[9], 'MO3': datos[10], 'MO4': datos[11],
                      'LUX1': datos[12], 'LUX2': datos[13], 'LUX3': datos[14], 'LUX4': datos[15], }
            df = pd.DataFrame(dtTrue)
            print(df)
            pd.to_datetime(df.FECHA, format="%Y/%m/%d")

    if start and end and grafi == 'Barra':
        my_bar = px.bar(df, x='FECHA', y=['T1', 'H1', 'MO1', 'LUX1'])
        my_bar.update_layout(xaxis_visible=True)
        return my_bar
    if start and end and grafi == 'Linea':
        my_line = px.line(df, x='FECHA', y=['T1', 'H1', 'MO1', 'LUX1'])
        my_line.update_layout(xaxis_visible=True)
        return my_line
    if start and end and grafi == 'Area':
        my_area = px.area(df, x='FECHA', y=['T1', 'H1', 'MO1', 'LUX1'])
        my_area.update_layout(xaxis_visible=True)
        return my_area
    else:
        return dash.no_update



@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    img1 = "https://www.gacetaregional.com/sitegr/wp-content/uploads/2019/09/iser-de-pamplona.png"
    img2 = "https://cdn.pixabay.com/photo/2020/04/06/11/22/seedling-5009286_960_720.jpg"
    img3 = "https://cdn.pixabay.com/photo/2016/10/30/05/49/agriculture-1782437_960_720.jpg"
    img4 = "https://cdn.pixabay.com/photo/2020/04/06/11/22/seedling-5009289_960_720.jpg"
    img5 = "https://cdn.pixabay.com/photo/2017/04/23/07/00/garden-2253111_960_720.jpg"
    if pathname == "/graficas":

        return [
            html.Div([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Seleccione',
                        html.A('El Archivo')
                    ]),
                    style={
                        'width': '200px',
                        'height': '50px',
                        'lineHeight': '40px',
                        'borderStyle': 'groove',
                        'borderRadius': '10px',
                        'textAlign': 'center',
                        'background-color': '#7FFFD4',
                        "position": 'relative',
                        "top": '50px',
                        "left": '20px',
                    },
                    # Allow multiple files to be uploaded
                    multiple=False,
                ),
                html.Div(id='output-data-upload'),
            ]),
            html.Div([
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date_placeholder_text='Select a date',
                    end_date_placeholder_text='Select a date',
                    style={
                        "position": 'relative',
                        "top": '-0px',
                        "right": '-250px',
                    }
                ),
                html.Div([
                    dbc.Container(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(html.P("Forma de la Grafica"),),
                                    dbc.Col(html.P("Modo Graficas"),),
                                ],
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(dcc.Dropdown(['Linea', 'Area', 'Barra'], 'Barra',
                                                         id='selec_grafi', style={
                                            "width": "120px",
                                            "top": '-15px',
                                            "left": '25px',
                                            },
                                    ),),
                                    dbc.Col(dcc.Dropdown(['LOCAL', 'API'], 'API',
                                                         id='selec_opc', style={
                                            "width": "120px",
                                            "top": '-15px',
                                            "left": '25px',
                                            },
                                    )),
                                ],
                            ),
                        ],),
                ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='bargraph',
                                  style={
                                      "width": '10',
                                      'position': 'relative',
                                  },
                                  figure={})
                    ],
                    ),
                ],
                    justify="center",
                ),
            ]),
        ]

    elif pathname == "/manual":
        print("OPCION MANUAL.")
        file_path = os.path.abspath("MANUAL DE USUARIO V2.pdf")
        print("Busco el Archivo en la siguiente ruta.", file_path)
        with open(file_path, 'rb') as f:
            pdf_bytes = f.read()
            # print(" pdf convertido a bytes :",pdf_bytes)
            pdf_b64 = base64.b64encode(pdf_bytes).decode('utf-8')
            pdf_url = f"data:application/pdf;base64,{pdf_b64}"
            # print(" pdf  ruta f :",pdf_url)
            pdf_viewer = html.Iframe(src=pdf_url, width='80%', height='700')
            print("Ya convirtio el Archivo .")
        return [
            html.Br(),
            dbc.CardBody(
                [
                    html.H4("Intrucciones"),
                    # Aquí agregamos el componente html.Div que contiene el pdf_viewer
                    html.Div(children=[pdf_viewer])
                ], style={"textAlign": "center"},
            )
        ]
    elif pathname == "/":
        return [
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": img1, "img_style": {
                                "max-height": "500px"}},
                            {"key": "2", "src": img2, "img_style": {
                                "max-height": "500px"}},
                            {"key": "3", "src": img3, "img_style": {
                                "max-height": "500px"}},
                            {"key": "4", "src": img4, "img_style": {
                                "max-height": "500px"}},
                            {"key": "5", "src": img5, "img_style": {
                                "max-height": "500px"}},
                        ],
                        controls=True,
                        indicators=True,
                        interval=1500,
                        ride="carousel",
                        className="carousel-fade",
                    )
                ], width=8)
            ], justify="center"),
        ]

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == ('__main__'):
    app.run_server(debug=False)

# standard library
import os

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go

# pydata stack
import pandas as pd
#from sqlalchemy import create_engine

#Read CSV
import csv
import flask
from random import randint



# set params
#conn = create_engine(os.environ['DB_URI'])


###########################
# Data Manipulation / Model
###########################


import os

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import plotly.graph_objs as go

# pydata stack
import pandas as pd
#from sqlalchemy import create_engine

#Read CSV
import csv
import flask
from random import randint


def readCSV():
    data=pd.read_csv('Calculo_de_BEP.csv', header=None)
    #with open('Calculo_de_BEP.csv', newline='') as csvfile:
    #    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #    for row in data:
    #        print(', '.join(row))
    return data

df2 = readCSV()
#print(df2)


#########################
# Dashboard Layout / View
#########################

ALLOWED_TYPES = ("number")

#Other Types
#    "text", "number", "password", "email", "search",
#    "tel", "url", "range", "hidden",)

#app = dash.Dash()

# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))



external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']
#cssURL = "https://rawgit.com/richard-muir/uk-car-accidents/master/road-safety.css"
# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
external_stylesheets = ['https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css']
external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], server=server)
theme =  {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'foreground': '#FFA500',
    'background2': '#C0C0C0',
    'none': '#FFFFFF'
}

#app = dash.Dash(__name__,  server=server)

# Include the external CSS

#app.css.append_css({
#    "external_url": cssURL
#})


import base64


image_filename = 'TedCas.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')
#test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')



#app.layout = html.Div([
#    html.Div([
#    html.Img(src='data:image/png;base64,{}'.format(encoded_image), style={'height':'10%', 'width':'10%'})
#    ]),
#    html.H2("Calculo ROI ARCH para su negocio"),

app.layout = html.Div(style={'backgroundColor': colors['none']}, id='dark-theme-container', children=[
    html.Div([
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image), className='three columns', style={'height':'10%', 'width':'10%'})#, style={'width': '16%', 'display': 'inline-block'})
            ],   style={'textAlign': 'center','backgroundColor': colors['foreground']},),    
        html.Div([
            html.H2("Cálculo PRI ARCH para su negocio", className='three columns')#, style={'width': '16%', 'display': 'inline-block'})   
           ],   style={'textAlign': 'center'}),
            ],
        style={'width': '100%', 'display': 'inline-block'}),
   


   
    #We create a container of 25% of the width of the page
    html.Div([
        #We add three containers inside (three dropdowns). Each one is 100% of width in order to fit one below the other (if they were for example 50%, they would be shown one beside the other)
        html.Div([
                #html.Div('Acción', className='three columns', style={'width': '50%', 'display': 'inline-block'}),
                #6 columns
                #First Column: title
                html.Div(df2.iloc[1,0], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad1",
                    type="number",
                    placeholder=40#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}
     
                    ),
                                
                #Third Column: title
                html.Div(df2.iloc[1,1], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste1",
                    type="number",
                    placeholder=30#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[1,2], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionFija",
                    type="number",
                    placeholder=8000#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}
                    
                    ),
            ],
            style={'width': '100%', 'display': 'inline-block'}),
            html.Div([

                   #First Column: title
                html.Div(df2.iloc[2,0], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad2",
                    type="number",
                    placeholder=300#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}

                   ),
                                
                #Third Column: title
                html.Div(df2.iloc[2,1], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste2",
                    type="number",
                    placeholder=0.005#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[2,2], className='three columns', style={'width': '10%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionMensual",
                    type="number",
                    placeholder=300#"input type {}".format("number")
                    ), style={'width': '22%', 'display': 'inline-block'}
                    
                    ),






                #html.Div(df2.iloc[1,1], className='three columns', style={'width': '50%', 'display': 'inline-block'}),

                #html.Div(dcc.Dropdown(
                #    id="Points1",
                #    options=[{
                #        'label': i,
                #        'value': i
                #    } for i in number_points_predict],
                #    value=number_points_predict[0]), style={'width': '50%', 'display': 'inline-block'}),
            ],
            style={'width': '100%', 'display': 'inline-block'}),
            #html.Div([
            
                
            #    html.Div(df2.iloc[2,0], className='three columns', style={'width': '50%', 'display': 'inline-block'}),
                                   
            #    html.Div(dcc.Dropdown(
            #        id="Prediction1",
            #        options=[{
            #            'label': i,
            #            'value': i
            #        } for i in number_points_future],
            #        value=number_points_future[0]), style={'width': '50%', 'display': 'inline-block'}),

            #],
            #style={'width': '100%', 'display': 'inline-block'}),
                       
         ], style={'width': '100%','display': 'inline-block' ,'backgroundColor': colors['background2']}),
                    

    html.Div(style={'backgroundColor': colors['background2']}, id='graph-container', 
             children=[dcc.Graph(id='ROIPrediction', config = {'displaylogo': False})])
])




#############################################
# Interaction Between Components / Controller
#############################################

############################################
#PREDICT VALUE MACHINE LEARNING FUNCTIONS
############################################
import numpy as np 




#############################################

#########################################################
#LOAD STOCK VALUE
#########################################################
@app.callback(
    dash.dependencies.Output('ROIPrediction', 'figure'),
    [dash.dependencies.Input('Cantidad1', 'value'),
     dash.dependencies.Input('Coste1', 'value'),
     dash.dependencies.Input('Cantidad2', 'value'),
     dash.dependencies.Input('Coste2', 'value'),
     dash.dependencies.Input('InversionFija', 'value'),
     dash.dependencies.Input('InversionMensual', 'value'),
     #dash.dependencies.Input('Prediction1', 'value'),

     ]
    )
#Each input of the function is one of the inputs above
def update_graph(Cantidad1, Coste1, Cantidad2, Coste2, InversionFija, InversionMensual):
    #coste=[]
    
    mes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    nummeses=len(mes)
    coste = np.arange(nummeses)
    inversion = np.arange(nummeses)
    PRI_vector= np.arange(nummeses)
    Beneficio = np.arange(nummeses)

    #Ciclo de un año
    #Protección frente a Nulls
    #region Proteccion
    if Cantidad1==None:
        Ca1=1
    else:
        Ca1=Cantidad1
    if Cantidad2==None:
        Ca2=1
    else:
        Ca2=Cantidad2
    if Coste1==None:
        Co1=1
    else:
        Co1=Coste1
    if Coste2==None:
        Co2=1
    else:
        Co2=Coste2
    if Cantidad1==None:
        C1=1
    else:
        C1=Cantidad1
    if InversionFija==None:
        IF=1
    else:
        IF=InversionFija
    if InversionMensual==None:
        IM=1
    else:
        IM=InversionMensual
    #endregion
    PRI=0
    #Fin de la protección   
    for i in mes:
        #Calculamos coste acumulativo por mes (cada mes el coste es el del anterior más el actual)
        #print(Ca1, Co1, Ca2, Co2, IF, IM)
        coste[i-1]=Ca1*Co1*i+Ca2*Co2*i
        inversion[i-1]=IF+i*IM
        if coste[i-1]>inversion[i-1]:
            PRI_vector[i-1]=inversion[i-1]
            Beneficio[i-1]=coste[i-1]
        else:
            PRI_vector[i-1]=coste[i-1]
            Beneficio[i-1]=inversion[i-1]
        #Beneficio[i-1]=coste[i-1]-PRI_vector[i-1]
        #print ("Coste =" + str(coste[i-1]) + "Inversion = " + str(inversion[i-1]))
    

    xval=mes
    yval=np.array([coste,inversion,Beneficio])
    print(Beneficio)
    title=["Gasto actual","Inversión ARCH", "Beneficio (Area verde)"]
    fillcolor=[None,None,'tonexty']
    mode_line=['lines','lines', 'none']
    #fillcolor=[None,'tonexty']


    figure={
            'data': [
            go.Scatter(
                x=xval ,
                y = yval[row].tolist(),
                mode=mode_line[row],#'lines', #markers
                opacity=0.7,
                marker={
                    'size': 10,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=title[row],
                fill=fillcolor[row]
                #template="plotly_dark"
            )for row in range(len(yval))
            ],
            'layout': go.Layout(
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                xaxis = {'title': 'Mes'},
                yaxis = {'title': 'Coste'},
                plot_bgcolor = colors['background2'],
                paper_bgcolor = colors['background2']
                )
            
        }
        

    return figure




if __name__ == '__main__':
    app.run_server(debug=True)



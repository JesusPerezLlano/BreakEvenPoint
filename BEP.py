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
app = dash.Dash(__name__, server=server)

import base64


image_filename = 'TedCas.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')
#test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')



app.layout = html.Div([
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image), style={'height':'10%', 'width':'10%'})
    ]),
    html.H2("Calculo ROI ARCH para su negocio"),
   
    #We create a container of 25% of the width of the page
    html.Div([
        #We add three containers inside (three dropdowns). Each one is 100% of width in order to fit one below the other (if they were for example 50%, they would be shown one beside the other)
        html.Div([
                #html.Div('Acción', className='three columns', style={'width': '50%', 'display': 'inline-block'}),
                #6 columns
                #First Column: title
                html.Div(df2.iloc[1,0], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad1",
                    type="number",
                    placeholder=40#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
     
                    ),
                                
                #Third Column: title
                html.Div(df2.iloc[1,1], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste1",
                    type="number",
                    placeholder=30#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[1,2], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionFija",
                    type="number",
                    placeholder=8000#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                    
                    ),
            ],
            style={'width': '100%', 'display': 'inline-block'}),
            html.Div([

                   #First Column: title
                html.Div(df2.iloc[2,0], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad2",
                    type="number",
                    placeholder=300#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}

                   ),
                                
                #Third Column: title
                html.Div(df2.iloc[2,1], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste2",
                    type="number",
                    placeholder=0.005#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[2,2], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionMensual",
                    type="number",
                    placeholder=300#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                    
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
                       
         ], style={'width': '75%','display': 'inline-block'}),
                    


    dcc.Graph(id='ROIPrediction'),
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
    coste = np.arange(12)
    inversion = np.arange(12)
    mes=[1,2,3,4,5,6,7,8,9,10,11,12]
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
    #Fin de la protección   
    for i in mes:
        #Calculamos coste acumulativo por mes (cada mes el coste es el del anterior más el actual)
        #print(Ca1, Co1, Ca2, Co2, IF, IM)
        coste[i-1]=Ca1*Co1*i+Ca2*Co2*i
        inversion[i-1]=IF+i*IM
        #print ("Coste =" + str(coste[i-1]) + "Inversion = " + str(inversion[i-1]))
    
    
    xval=mes
    yval=np.array([coste,inversion])
    title=["ahorro","inversion"]
   


    figure={
            'data': [
            go.Scatter(
                x=xval ,
                #y=plot_frame[Accion],
                #y=y,
                y = yval[row].tolist(),
                #text="azul",
                mode='lines', #markers
                opacity=0.7,
                marker={
                    'size': 10,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=title[row]
            )for row in range(len(yval))
            ],
            'layout': go.Layout(
                #xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                #yaxis={'title': 'Customer Order Status for {}'.format(Accion)},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                xaxis = {'title': 'Mes'},
                yaxis = {'title': 'Coste'}
                #hovermode='closest'
                )
        
        }

    return figure




if __name__ == '__main__':
    app.run_server(debug=True)




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
app = dash.Dash(__name__, server=server)


app.layout = html.Div([
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image), style={'height':'10%', 'width':'10%'})
    ]),
    html.H2("Calculo ROI ARCH para su negocio"),
   
    #We create a container of 25% of the width of the page
    html.Div([
        #We add three containers inside (three dropdowns). Each one is 100% of width in order to fit one below the other (if they were for example 50%, they would be shown one beside the other)
        html.Div([
                #html.Div('Acción', className='three columns', style={'width': '50%', 'display': 'inline-block'}),
                #6 columns
                #First Column: title
                html.Div(df2.iloc[1,0], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad1",
                    type="number",
                    placeholder=20#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
     
                    ),
                                
                #Third Column: title
                html.Div(df2.iloc[1,1], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste1",
                    type="number",
                    placeholder=30#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[1,2], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionFija",
                    type="number",
                    placeholder=8000#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                    
                    ),
            ],
            style={'width': '100%', 'display': 'inline-block'}),
            html.Div([

                   #First Column: title
                html.Div(df2.iloc[2,0], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                #Second column: data
                html.Div(
                    
                    dcc.Input(
                    id="Cantidad2",
                    type="number",
                    placeholder=500#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}

                   ),
                                
                #Third Column: title
                html.Div(df2.iloc[2,1], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Fourth column: data
                html.Div(
                    dcc.Input(
                    id="Coste2",
                    type="number",
                    placeholder=0.005#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                                       
                    ),
                
                #Fifth Column: title
                html.Div(df2.iloc[2,2], className='three columns', style={'width': '16%', 'display': 'inline-block'}),
                
                #Sixth column: data
                html.Div(
                    
                    dcc.Input(
                    id="InversionMensual",
                    type="number",
                    placeholder=300#"input type {}".format("number")
                    ), style={'width': '16%', 'display': 'inline-block'}
                    
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
                       
         ], style={'width': '75%','display': 'inline-block'}),
                    


    dcc.Graph(id='ROIPrediction'),
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
    coste = np.arange(12)
    inversion = np.arange(12)
    mes=[1,2,3,4,5,6,7,8,9,10,11,12]
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
    #Fin de la protección   
    for i in mes:
        #Calculamos coste acumulativo por mes (cada mes el coste es el del anterior más el actual)
        #print(Ca1, Co1, Ca2, Co2, IF, IM)
        coste[i-1]=Ca1*Co1*i+Ca2*Co2*i
        inversion[i-1]=IF+i*IM
        #print ("Coste =" + str(coste[i-1]) + "Inversion = " + str(inversion[i-1]))
    
    
    xval=mes
    yval=np.array([coste,inversion])
    title=["ahorro","inversion"]
   


    figure={
            'data': [
            go.Scatter(
                x=xval ,
                #y=plot_frame[Accion],
                #y=y,
                y = yval[row].tolist(),
                #text="azul",
                mode='lines', #markers
                opacity=0.7,
                marker={
                    'size': 10,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=title[row]
            )for row in range(len(yval))
            ],
            'layout': go.Layout(
                #xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                #yaxis={'title': 'Customer Order Status for {}'.format(Accion)},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                xaxis = {'title': 'Mes'},
                yaxis = {'title': 'Coste'}
                #hovermode='closest'
                )
        
        }

    return figure




if __name__ == '__main__':
    app.run_server(debug=True)




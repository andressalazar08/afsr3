import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import dash_table
import plotly.graph_objects as go

app=dash.Dash(__name__)
import pandas as pd

titulo=html.H1("Modelo de Jerarquía Analítica AHP",style={'text-align':'center','font-family':'Arial Black','color':'blue'})
subtitulo=html.H2("Cuatro Criterios / Tres Alternativas",style={'text-align':'center','font-family':'Arial Black'})
nombre=html.H3('Pablo Steven Torres Cortes',style={'font-family':'Arial'}) 
universidad=html.H3('Universidad Santiago de Cali',style={'font-family':'Arial'})


#Uso de Callbacks
A=dcc.Input(id='criterio1',value=1,type='number')
B=dcc.Input(id='criterio2',value=1,type='number')
C=dcc.Input(id='criterio3',value=1,type='number')
D=dcc.Input(id='criterio4',value=1,type='number')
E=dcc.Input(id='criterio5',value=1,type='number')
F=dcc.Input(id='criterio6',value=1,type='number')
#----------------------------------------------------------------------------
G=dcc.Input(id='c1alternativa1',value=1,type='number')
H=dcc.Input(id='c1alternativa2',value=1,type='number')
I=dcc.Input(id='c1alternativa3',value=1,type='number')
#----------------------------------------------------------------------------
J=dcc.Input(id='c2alternativa1',value=1,type='number')
K=dcc.Input(id='c2alternativa2',value=1,type='number')
L=dcc.Input(id='c2alternativa3',value=1,type='number')
#----------------------------------------------------------------------------
M=dcc.Input(id='c3alternativa1',value=1,type='number')
N=dcc.Input(id='c3alternativa2',value=1,type='number')
O=dcc.Input(id='c3alternativa3',value=1,type='number')
#----------------------------------------------------------------------------
P=dcc.Input(id='c4alternativa1',value=1,type='number')
Q=dcc.Input(id='c4alternativa2',value=1,type='number')
R=dcc.Input(id='c4alternativa3',value=1,type='number')
#----------------------------------------------------------------------------
resultado1=html.H3(id='micriterio1',children='')
texto1=html.H3(id='micriterio2',children='')
resultadotabla1=html.Div(id='tabla1criterio',children=dash_table.DataTable())
resultadotabla2=html.Div(id='tabla2criterio',children=dash_table.DataTable())
#-----------------------------------------------------------------------------
resultado2=html.H3(id='c1mialternativa1',children='')
texto2=html.H3(id='c1mialternativa2',children='')
resulc1alter1=html.Div(id='alternc1resul1',children=dash_table.DataTable())
resulc1alter2=html.Div(id='alternc1resul2',children=dash_table.DataTable())
#-----------------------------------------------------------------------------
resultado3=html.H3(id='c2mialternativa1',children='')
texto3=html.H3(id='c2mialternativa2',children='')
resulc2alter1=html.Div(id='alternc2resul1',children=dash_table.DataTable())
resulc2alter2=html.Div(id='alternc2resul2',children=dash_table.DataTable())
#-----------------------------------------------------------------------------
resultado4=html.H3(id='c3mialternativa1',children='')
texto4=html.H3(id='c3mialternativa2',children='')
resulc3alter1=html.Div(id='alternc3resul1',children=dash_table.DataTable())
resulc3alter2=html.Div(id='alternc3resul2',children=dash_table.DataTable())
#-----------------------------------------------------------------------------
resultado5=html.H3(id='c4mialternativa1',children='')
texto5=html.H3(id='c4mialternativa2',children='')
resulc4alter1=html.Div(id='alternc4resul1',children=dash_table.DataTable())
resulc4alter2=html.Div(id='alternc4resul2',children=dash_table.DataTable())
#-----------------------------------------------------------------------------
resulc8alter80=html.H3(id='tablitafinal0',children='')
resulc8alter81=html.H3(id='tablitafinal1',children='',style={'color':'red'})
resulc8alter82=html.H3(id='tablitafinal2',children='')

@app.callback(
[Output(component_id='micriterio1',component_property='children'),
 Output(component_id='micriterio2',component_property='children'),
 Output(component_id='tabla1criterio',component_property='children'),
 Output(component_id='tabla2criterio',component_property='children'),
 Output(component_id='c1mialternativa1',component_property='children'),
 Output(component_id='c1mialternativa2',component_property='children'),
 Output(component_id='alternc1resul1',component_property='children'),
 Output(component_id='alternc1resul2',component_property='children'),
 Output(component_id='c2mialternativa1',component_property='children'),
 Output(component_id='c2mialternativa2',component_property='children'),
 Output(component_id='alternc2resul1',component_property='children'),
 Output(component_id='alternc2resul2',component_property='children'),
 Output(component_id='c3mialternativa1',component_property='children'),
 Output(component_id='c3mialternativa2',component_property='children'),
 Output(component_id='alternc3resul1',component_property='children'),
 Output(component_id='alternc3resul2',component_property='children'),
 Output(component_id='c4mialternativa1',component_property='children'),
 Output(component_id='c4mialternativa2',component_property='children'),
 Output(component_id='alternc4resul1',component_property='children'),
 Output(component_id='alternc4resul2',component_property='children'),
 Output(component_id='tablitafinal0',component_property='children'),
 Output(component_id='tablitafinal1',component_property='children'),
 Output(component_id='tablitafinal2',component_property='children'),

],

[
Input(component_id='criterio1',component_property='value'),
Input(component_id='criterio2',component_property='value'),
Input(component_id='criterio3',component_property='value'),
Input(component_id='criterio4',component_property='value'),
Input(component_id='criterio5',component_property='value'),
Input(component_id='criterio6',component_property='value'),
Input(component_id='c1alternativa1',component_property='value'),
Input(component_id='c1alternativa2',component_property='value'),
Input(component_id='c1alternativa3',component_property='value'),
Input(component_id='c2alternativa1',component_property='value'),
Input(component_id='c2alternativa2',component_property='value'),
Input(component_id='c2alternativa3',component_property='value'),
Input(component_id='c3alternativa1',component_property='value'),
Input(component_id='c3alternativa2',component_property='value'),
Input(component_id='c3alternativa3',component_property='value'),
Input(component_id='c4alternativa1',component_property='value'),
Input(component_id='c4alternativa2',component_property='value'),
Input(component_id='c4alternativa3',component_property='value'),


]  
)

def miFuncion(dato1,dato2,dato3,dato4,dato5,dato6,c1dato1,c1dato2,c1dato3,c2dato1,c2dato2,c2dato3,c3dato1,c3dato2,c3dato3,c4dato1,c4dato2,c4dato3):
    #Matriz comparacion criterios por pares
    diag=1
    C1_C2=dato1
    C1_C3=dato2
    C1_C4=dato3
    C2_C3=dato4
    C2_C4=dato5
    C3_C4=dato6
    C1_C2_Inv=1/C1_C2
    C1_C3_Inv=1/C1_C3
    C1_C4_Inv=1/C1_C4
    C2_C3_Inv=1/C2_C3
    C2_C4_Inv=1/C2_C4
    C3_C4_Inv=1/C3_C4
    
    matriz_inicial={
    "C1":{"C1":diag,"C2":C1_C2,"C3":C1_C3,"C4":C1_C4},
    "C2":{"C1":C1_C2_Inv,"C2":diag,"C3":C2_C3,"C4":C2_C4},
    "C3":{"C1":C1_C3_Inv,"C2":C2_C3_Inv,"C3":diag,"C4":C3_C4},
    "C4":{"C1":C1_C4_Inv,"C2":C2_C4_Inv,"C3":C3_C4_Inv,"C4":diag},
    }
    
    #Primer Paso del AHP
    AHPSteven_paso1=pd.DataFrame(matriz_inicial)
    AHPSteven_paso1=AHPSteven_paso1.T
    AHPSteven_paso1_a=AHPSteven_paso1.sum()
    
    #Paso1a
    AHPSteven_paso1_a=pd.DataFrame(AHPSteven_paso1_a)
    AHPSteven_paso1_a=AHPSteven_paso1_a.T
    AHPSteven_paso1_b=AHPSteven_paso1.div(AHPSteven_paso1_a.iloc[0])
    AHPSteven_paso1_c=AHPSteven_paso1_b.mean(axis=1)
    AHPSteven_paso1_c=pd.DataFrame(AHPSteven_paso1_c)
    AHPSteven_paso1_c=AHPSteven_paso1_c.T
    
    #Calculo del lambda max
    lambda_max=(AHPSteven_paso1_a*AHPSteven_paso1_c)
    lambda_max=lambda_max.sum(axis=1)
    
    CC=((lambda_max-4)/3)/0.900
    respuesta1=html.H3(CC)
    
    tablacriterio1df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_paso1.columns)],
        data=AHPSteven_paso1.to_dict('records'),    
    )
    
    tablacriterio2df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_paso1_c.columns)],
        data=AHPSteven_paso1_c.to_dict('records'),    
    )
    
    #Matriz comparacion alternativas por pares
    diag=1
    A1_A2=c1dato1
    A1_A3=c1dato2
    A2_A3=c1dato3
    A1_A2_Inv=1/A1_A2
    A1_A3_Inv=1/A1_A3
    A2_A3_Inv=1/A2_A3
    
    matriz_secundaria1={
    'A1':{'A1':diag,'A2':A1_A2,'A3':A1_A3},
    'A2':{'A1':A1_A2_Inv,'A2':diag,'A3':A2_A3},
    'A3':{'A1':A1_A3_Inv,'A2':A2_A3_Inv,'A3':diag},
    }
    
    #Primer Paso del AHP
    AHPSteven_c1paso2=pd.DataFrame(matriz_secundaria1)
    AHPSteven_c1paso2=AHPSteven_c1paso2.T
    AHPSteven_c1paso2_a=AHPSteven_c1paso2.sum()
    
    #Paso2a
    AHPSteven_c1paso2_a=pd.DataFrame(AHPSteven_c1paso2_a)
    AHPSteven_c1paso2_a=AHPSteven_c1paso2_a.T
    AHPSteven_c1paso2_b=AHPSteven_c1paso2.div(AHPSteven_c1paso2_a.iloc[0])
    AHPSteven_c1paso2_c=AHPSteven_c1paso2_b.mean(axis=1)
    AHPSteven_c1paso2_c=pd.DataFrame(AHPSteven_c1paso2_c)
    AHPSteven_c1paso2_c=AHPSteven_c1paso2_c.T
    
    #Calculo del lambda max
    lambda_max=(AHPSteven_c1paso2_a*AHPSteven_c1paso2_c)
    lambda_max=lambda_max.sum(axis=1)
    
    CC2=((lambda_max-3)/2)/0.58
    respuesta2=html.H3(CC2)
    
    tablac1alternativa1df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c1paso2.columns)],
        data=AHPSteven_c1paso2.to_dict('records'),    
    )
    
    tablac1alternativa2df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c1paso2_c.columns)],
        data=AHPSteven_c1paso2_c.to_dict('records'),    
    )
    
    #Matriz comparacion alternativas por pares
    diag=1
    A1_A2=c2dato1
    A1_A3=c2dato2
    A2_A3=c2dato3
    A1_A2_Inv=1/A1_A2
    A1_A3_Inv=1/A1_A3
    A2_A3_Inv=1/A2_A3
    
    matriz_secundaria2={
    'A1':{'A1':diag,'A2':A1_A2,'A3':A1_A3},
    'A2':{'A1':A1_A2_Inv,'A2':diag,'A3':A2_A3},
    'A3':{'A1':A1_A3_Inv,'A2':A2_A3_Inv,'A3':diag},
    }
    
    #Primer Paso del AHP
    AHPSteven_c2paso2=pd.DataFrame(matriz_secundaria2)
    AHPSteven_c2paso2=AHPSteven_c2paso2.T
    AHPSteven_c2paso2_a=AHPSteven_c2paso2.sum()
    
    #Paso2a
    AHPSteven_c2paso2_a=pd.DataFrame(AHPSteven_c2paso2_a)
    AHPSteven_c2paso2_a=AHPSteven_c2paso2_a.T
    AHPSteven_c2paso2_b=AHPSteven_c2paso2.div(AHPSteven_c2paso2_a.iloc[0])
    AHPSteven_c2paso2_c=AHPSteven_c2paso2_b.mean(axis=1)
    AHPSteven_c2paso2_c=pd.DataFrame(AHPSteven_c2paso2_c)
    AHPSteven_c2paso2_c=AHPSteven_c2paso2_c.T
    
    #Calculo del lambda max
    lambda_max=(AHPSteven_c2paso2_a*AHPSteven_c2paso2_c)
    lambda_max=lambda_max.sum(axis=1)
    
    CC3=((lambda_max-3)/2)/0.58
    respuesta3=html.H3(CC3)
    
    tablac2alternativa1df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c2paso2.columns)],
        data=AHPSteven_c2paso2.to_dict('records'),    
    )
    
    tablac2alternativa2df=dash_table.DataTable(
       columns=[{'name':i,'id':i} for i in (AHPSteven_c2paso2_c.columns)],
        data=AHPSteven_c2paso2_c.to_dict('records'),    
    )
    
    #Matriz comparacion alternativas por pares
    diag=1
    A1_A2=c3dato1
    A1_A3=c3dato2
    A2_A3=c3dato3
    A1_A2_Inv=1/A1_A2
    A1_A3_Inv=1/A1_A3
    A2_A3_Inv=1/A2_A3
    
    matriz_secundaria3={
    'A1':{'A1':diag,'A2':A1_A2,'A3':A1_A3},
    'A2':{'A1':A1_A2_Inv,'A2':diag,'A3':A2_A3},
    'A3':{'A1':A1_A3_Inv,'A2':A2_A3_Inv,'A3':diag},
    }
    
    #Primer Paso del AHP
    AHPSteven_c3paso2=pd.DataFrame(matriz_secundaria3)
    AHPSteven_c3paso2=AHPSteven_c3paso2.T
    AHPSteven_c3paso2_a=AHPSteven_c3paso2.sum()
    
    #Paso2a
    AHPSteven_c3paso2_a=pd.DataFrame(AHPSteven_c3paso2_a)
    AHPSteven_c3paso2_a=AHPSteven_c3paso2_a.T
    AHPSteven_c3paso2_b=AHPSteven_c3paso2.div(AHPSteven_c3paso2_a.iloc[0])
    AHPSteven_c3paso2_c=AHPSteven_c3paso2_b.mean(axis=1)
    AHPSteven_c3paso2_c=pd.DataFrame(AHPSteven_c3paso2_c)
    AHPSteven_c3paso2_c=AHPSteven_c3paso2_c.T
    
    #Calculo del lambda max
    lambda_max=(AHPSteven_c3paso2_a*AHPSteven_c3paso2_c)
    lambda_max=lambda_max.sum(axis=1)
    
    CC4=((lambda_max-3)/2)/0.58
    respuesta4=html.H3(CC4)
    
    
    tablac3alternativa1df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c3paso2.columns)],
        data=AHPSteven_c3paso2.to_dict('records'),    
    )
    
    tablac3alternativa2df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c3paso2_c.columns)],
        data=AHPSteven_c3paso2_c.to_dict('records'),    
    )
    
    #Matriz comparacion alternativas por pares
    diag=1
    A1_A2=c4dato1
    A1_A3=c4dato2
    A2_A3=c4dato3
    A1_A2_Inv=1/A1_A2
    A1_A3_Inv=1/A1_A3
    A2_A3_Inv=1/A2_A3
    
    matriz_secundaria4={
    'A1':{'A1':diag,'A2':A1_A2,'A3':A1_A3},
    'A2':{'A1':A1_A2_Inv,'A2':diag,'A3':A2_A3},
    'A3':{'A1':A1_A3_Inv,'A2':A2_A3_Inv,'A3':diag},
    }
    
    #Primer Paso del AHP
    AHPSteven_c4paso2=pd.DataFrame(matriz_secundaria4)
    AHPSteven_c4paso2=AHPSteven_c4paso2.T
    AHPSteven_c4paso2_a=AHPSteven_c4paso2.sum()
    
    #Paso2a
    AHPSteven_c4paso2_a=pd.DataFrame(AHPSteven_c4paso2_a)
    AHPSteven_c4paso2_a=AHPSteven_c4paso2_a.T
    AHPSteven_c4paso2_b=AHPSteven_c4paso2.div(AHPSteven_c4paso2_a.iloc[0])
    AHPSteven_c4paso2_c=AHPSteven_c4paso2_b.mean(axis=1)
    AHPSteven_c4paso2_c=pd.DataFrame(AHPSteven_c4paso2_c)
    AHPSteven_c4paso2_c=AHPSteven_c4paso2_c.T
    
    #Calculo del lambda max
    lambda_max=(AHPSteven_c4paso2_a*AHPSteven_c4paso2_c)
    lambda_max=lambda_max.sum(axis=1)
    
    CC5=((lambda_max-3)/2)/0.58
    respuesta5=html.H3(CC5)
    
    
    tablac4alternativa1df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c4paso2.columns)],
        data=AHPSteven_c4paso2.to_dict('records'),    
    )
    
    tablac4alternativa2df=dash_table.DataTable(
        columns=[{'name':i,'id':i} for i in (AHPSteven_c4paso2_c.columns)],
        data=AHPSteven_c4paso2_c.to_dict('records'),    
    )
    
    #VP Final
    final=pd.concat([AHPSteven_c1paso2_c.T,AHPSteven_c2paso2_c.T,AHPSteven_c3paso2_c.T,AHPSteven_c4paso2_c.T], axis=1)
    
    vp=final.dot(AHPSteven_paso1_c.T.to_numpy())
    vp=vp.values.tolist()
    
    
    
    
    tcblitafinal0=vp[0]
    tcblitafinal1=vp[1]
    tcblitafinal2=vp[2]
    
   
    
    
    return respuesta1,CC,tablacriterio1df,tablacriterio2df,respuesta2,CC2,tablac1alternativa1df,tablac1alternativa2df,respuesta3,CC3,tablac2alternativa1df,tablac2alternativa2df,respuesta4,CC4,tablac3alternativa1df,tablac3alternativa2df,respuesta5,CC5,tablac4alternativa1df,tablac4alternativa2df,tcblitafinal0,tcblitafinal1,tcblitafinal2










app.layout=html.Div([titulo,subtitulo,nombre,universidad,A,B,C,D,E,F,resultadotabla1,resultadotabla2,resultado1,texto1,G,H,I,resulc1alter1,resulc1alter2,resultado2,texto2,J,K,L,resulc2alter1,resulc2alter2,resultado3,texto3,M,N,O,resulc3alter1,resulc3alter2,resultado4,texto4,P,Q,R,resulc4alter1,resulc4alter2,resultado5,texto5,resulc8alter80,resulc8alter81,resulc8alter82 ])



if __name__=="__main__":
    app.run_server(debug=True)

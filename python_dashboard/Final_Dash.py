# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
# from components import Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import plotly.graph_objs as go
import plotly
import callbacks
import numpy as np
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

toxicity = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
fig = go.Figure(data=[
        go.Bar(name='Score', x=toxicity, y=[0,0,0,0,0,0], marker={
            'color': [0,0,0,0,0,0],
            'colorscale': 'Portland'},
        )],
        layout = {'title':'Score of Toxic Level for Your Comment:',
        'xaxis': {'categoryorder': 'array','categoryarray': [x for _, x in sorted(zip([0,0,0,0,0,0], toxicity))],
        'title' : 'Toxicity Category'},
        'yaxis':{'title' : 'Score (0-1)'}
    })


app = dash.Dash(__name__)
colors = {
    'background': '#FFFFFF',
    'text': '#D35400'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Toxic Comment Detection and Classification Demo',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Input(id='comments', type = 'text', placeholder = "Please Enter Your Comment Here :)", value = "", style={
        'width': '90%', 
        'height': 70,
        'textAlign': 'center',
        'margin-left': 50,
        'margin-right': 50,
        'font-size': '18px',

        }),
    html.Div(id='output', style={
        'textAlign': 'center',
        'color': '#AED6F1'

    }),
    dcc.Graph(id = 'score_bar', figure=fig),

])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('comments', 'value')])
def update_graph(comment):
    # print(start_date)
    # comment = 'i hate you'
    comment_list=[]
    comment_list.append(comment)

    # transform the training, validation data using count vectorizer object
    
    xtrain_count =  count_vect.transform(comment_list)

    toxic = lr_toxic_model.predict_proba(xtrain_count)
    severe_toxic = lr_severe_toxic_model.predict_proba(xtrain_count)
    obscene = lr_obscene_model.predict_proba(xtrain_count)
    threat = lr_threat_model.predict_proba(xtrain_count)
    insult = lr_insult_model.predict_proba(xtrain_count)
    identity_hate = lr_identity_hate_model.predict_proba(xtrain_count)
    probability_list = [toxic[:,1].item(), severe_toxic[:,1].item(), obscene[:,1].item(), threat[:,1].item(), insult[:,1].item(), identity_hate[:,1].item()]
    
    toxicity = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    prob_sum = 0
    prob_count_above = 0
    for prob in probability_list:
        prob_sum = prob_sum+prob
        if prob>0.6:
            prob_count_above = prob_count_above + 1
    if comment == '':
        return ""
    elif prob_sum>2 or prob_count_above>1:
        return "Sorry, your comment has been blocked."
    else:
        return "Your comment has been successfully published. Thank you."


@app.callback(
    dash.dependencies.Output('output', 'style'),
    [dash.dependencies.Input('comments', 'value')])
def update_graph(comment):
    # print(start_date)
    # comment = 'i hate you'
    comment_list=[]
    comment_list.append(comment)

    # transform the training, validation data using count vectorizer object
    
    xtrain_count =  count_vect.transform(comment_list)

    toxic = lr_toxic_model.predict_proba(xtrain_count)
    severe_toxic = lr_severe_toxic_model.predict_proba(xtrain_count)
    obscene = lr_obscene_model.predict_proba(xtrain_count)
    threat = lr_threat_model.predict_proba(xtrain_count)
    insult = lr_insult_model.predict_proba(xtrain_count)
    identity_hate = lr_identity_hate_model.predict_proba(xtrain_count)
    probability_list = [toxic[:,1].item(), severe_toxic[:,1].item(), obscene[:,1].item(), threat[:,1].item(), insult[:,1].item(), identity_hate[:,1].item()]
    
    toxicity = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    prob_sum = 0
    prob_count_above = 0
    for prob in probability_list:
        prob_sum = prob_sum+prob
        if prob>0.8:
            prob_count_above = prob_count_above + 1
    if comment == '':
        return {'textAlign': 'center', 'color': '#196F3D'}
    elif prob_sum>2 or prob_count_above>1:
        return {'textAlign': 'center', 'color': '#943126'}
    else:
        return {'textAlign': 'center', 'color': '#196F3D'}


@app.callback(
    dash.dependencies.Output('score_bar', 'figure'),
    [dash.dependencies.Input('comments', 'value')])
def update_graph(comment):
    
    # comment = 'i hate you'
    comment_list=[]
    comment_list.append(comment)

    # transform the training, validation data using count vectorizer object
    
    xtrain_count =  count_vect.transform(comment_list)
    toxic = lr_toxic_model.predict_proba(xtrain_count)
    severe_toxic = lr_severe_toxic_model.predict_proba(xtrain_count)
    obscene = lr_obscene_model.predict_proba(xtrain_count)
    threat = lr_threat_model.predict_proba(xtrain_count)
    insult = lr_insult_model.predict_proba(xtrain_count)
    identity_hate = lr_identity_hate_model.predict_proba(xtrain_count)
    probability_list = [toxic[:,1].item(), severe_toxic[:,1].item(), obscene[:,1].item(), threat[:,1].item(), insult[:,1].item(), identity_hate[:,1].item()]
    toxicity = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    color_list = []

    for num in probability_list:
        if num>0.8:
            color_list.append('#E74C3C')
        elif num>0.6:
            color_list.append('#F39C12')
        elif num>0.4:
            color_list.append('#F1C40F')
        elif num>0.2:
            color_list.append('#3498DB')
        else:
            color_list.append('#21618C')


    if comment !="":
        fig = go.Figure(data=[
            go.Bar(name='Score', x=toxicity, y=probability_list, 
                # marker={
                # 'color': probability_list,
                # # 'colorscale': [[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'],[1.0, 'rbg(217,30,30)']]
                # 'colorscale': 'Portland',
                # },
                marker_color = color_list,
            )],
            layout = {'title':'Score of Toxic Level for Your Comment:',
            'xaxis': {'categoryorder': 'array','categoryarray': [x for _, x in sorted(zip(probability_list, toxicity))],
            'title' : 'Toxicity Category'},
            'yaxis':{'title' : 'Score (0-1)', 'range': [0,1]}
        })
    else:
        fig = go.Figure(data=[
            go.Bar(name='Score', x=toxicity, y=[0,0,0,0,0,0], marker={
                'color': [0,0,0,0,0,0],
                # 'colorscale': [[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'],[1.0, 'rbg(217,30,30)']]
                'colorscale': 'Portland',
                },
            )],
            layout = {'title':'Score of Toxic Level for Your Comment:',
            'xaxis': {'categoryorder': 'array','categoryarray': [x for _, x in sorted(zip([0,0,0,0,0,0], toxicity))],
            'title' : 'Toxicity Category'},
            'yaxis':{'title' : 'Score (0-1)',  'range': [0,1]}
        })

    return fig

if __name__ == '__main__':
    model1 = open("logreg_toxic_model.pkl", "rb")
    lr_toxic_model = joblib.load(model1)
    model2 = open("logreg_severe_toxic_model.pkl", "rb")
    lr_severe_toxic_model = joblib.load(model2)
    model3 = open("logreg_obscene_model.pkl", "rb")
    lr_obscene_model = joblib.load(model3)
    model4 = open("logreg_threat_model.pkl", "rb")
    lr_threat_model = joblib.load(model4)
    model5 = open("logreg_insult_model.pkl", "rb")
    lr_insult_model = joblib.load(model5)
    model6 = open("logreg_identity_hate_model.pkl", "rb")
    lr_identity_hate_model = joblib.load(model6)


    vectorizer = open("count_vect.pickel", "rb")
    count_vect = joblib.load(vectorizer)
    app.run_server(debug=True)
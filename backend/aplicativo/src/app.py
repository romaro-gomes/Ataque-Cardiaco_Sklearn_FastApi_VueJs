from fastapi import FastAPI,Form, HTTPException,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from caracteristicas import cardioCaracterísticas

import pandas as pd
import pickle

app= FastAPI()

templates=Jinja2Templates(directory='../template')

modelo=pickle.load(open('../../ml/modelo/artefato/modelo.pkl','rb'))

def extrair_valores(dados):
    return [getattr(dados,campo) for campo in dados.__annotations__.keys()]

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request':request})

@app.post('/resultado')
async def predict(request: Request,
                idade:int =Form(...),
                sexo:str =Form(...),
                dor_peitoral:str =Form(...),
                pressao_em_repouso:int =Form(...),
                colesterol:int =Form(...),
                glicemia_posprandial:str =Form(...),
                eletrocardiograma_em_repouso:str =Form(...),
                frequencia_cardiaca_maxima: int=Form(...),
                angina_em_exercicio: int=Form(...),
                depressao_ST: float =Form(...),
                inclinacao_ST:int=Form()
                  ):
    
    dados= cardioCaracterísticas(
        idade=idade,
        sexo=sexo,
        dor_peitoral=dor_peitoral,
        pressao_em_repouso=pressao_em_repouso,
        colesterol=colesterol,
        glicemia_posprandial=glicemia_posprandial,
        eletrocardiograma_em_repouso=eletrocardiograma_em_repouso,
        frequencia_cardiaca_maxima=frequencia_cardiaca_maxima,
        angina_em_exercicio=angina_em_exercicio,
        depressao_ST=depressao_ST,
        inclinacao_ST=inclinacao_ST
    )

    dados_df = pd.DataFrame([extrair_valores(dados)], columns=dados.__annotations__.keys())
    prediction = modelo.predict(dados_df)
    proba=modelo.predict_proba(dados_df)
    probability=f"{proba.tolist()[0][1]:.2f}% {proba.tolist()[0][0]:.2f}%"
    if prediction[0] == 0:
        pred='Negativo'
    else:
        pred='Positivo'
    return templates.TemplateResponse("resultado.html", {"request": request, "prediction": pred, "probability":probability} )
                                      
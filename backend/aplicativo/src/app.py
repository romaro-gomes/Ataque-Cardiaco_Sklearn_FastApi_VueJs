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
                  )
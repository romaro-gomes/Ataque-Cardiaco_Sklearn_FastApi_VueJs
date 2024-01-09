from pydantic import BaseModel
class ataqueCardiaco(BaseModel):
    idade: int
    sexo: str
    dor_peitoral: str
    pressao_em_repouso: int
    colesterol: int
    glicemia_posprandial: str
    eletrocardiograma_em_repouso: str
    frequencia_cardiaca_maxima: int
    angina_em_exercicio: int
    depressao_ST: float
    inclinacao_ST: int
    
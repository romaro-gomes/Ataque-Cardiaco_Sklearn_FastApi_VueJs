# Aplicação Web Para Auxílio de Tomadas de Decisão - Ataque Cardíaco ou Infarto.

## Introdução

**Este é um modelo de portfólio. Não deve ser usado na prática clínica, nem no autodiagnóstico ou automedicação.** 

Ataque Cardíaco ou Infarto é um quadro clínico em que células do coração do paciente encontram-se mortas. Geralmente, a falência das células é provocada pela diminuição ou ausência no fornecimento de oxigênio, levando as células à necrose, posterior liberação de cálcio na corrente sanguínea, provocando as dores no peito devido às contrações musculares.

Nos casos de emergência, o tratamento do infarto varia dependendo do resultado do exame físico, entretanto, é primordial o uso do eletrocardiograma EEG para avaliar as características dos batimentos.

O risco de infarto é fortemente associado à história clínica posterior, fatores genéticos e estilo de vida dos pacientes. Sendo importante ao médico e toda a equipe de saúde multidisciplinar orientar o paciente nos cuidados que ele deve seguir e o que fazer caso ele consiga notar o início de um ataque cardíaco.

O objetivo desta aplicação web, construída a partir de um modelo de aprendizado de máquina treinado com base em dados públicos, é ajudar profissionais da saúde a decidir o risco de uma paciente ter ou não um ataque cardíaco e o nível de esforço dedicado no acompanhamento do mesmo.

Ressalto: **Esta aplicação é apenas para portfólio e não tem pretensão e nem deve ser utilizada na prática clínica, no autodiagnóstico ou automedicação.**

Referências: 

- [https://www.scielo.br/j/abc/a/QvqxLFycJhLvNGFzPhsbZPF/?lang=pt](https://www.scielo.br/j/abc/a/QvqxLFycJhLvNGFzPhsbZPF/?lang=pt)

- [https://bvsms.saude.gov.br/ataque-cardiaco-infarto/](https://bvsms.saude.gov.br/ataque-cardiaco-infarto/)

- [https://www.pfizer.com.br/noticias/ultimas-noticias/como-reconhecer-um-infarto-cardiaco](https://www.pfizer.com.br/noticias/ultimas-noticias/como-reconhecer-um-infarto-cardiaco)

- [https://www.msdmanuals.com/pt-br/casa/fatos-r%C3%A1pidos-dist%C3%BArbios-do-cora%C3%A7%C3%A3o-e-dos-vasos-sangu%C3%ADneos/doen%C3%A7a-arterial-coronariana/ataque-card%C3%ADaco](https://www.msdmanuals.com/pt-br/casa/fatos-r%C3%A1pidos-dist%C3%BArbios-do-cora%C3%A7%C3%A3o-e-dos-vasos-sangu%C3%ADneos/doen%C3%A7a-arterial-coronariana/ataque-card%C3%ADaco)

## Metodologia

- [Análise Exploratória dos Dados](backend/ml/eda)
- [Treinamento do Modelo](backend/ml/modelo\notebook/treinamento)

## Uso

### Máquina Local

#### Instalar bibliotecas Python

```bash
pip install -r backend\requirements.txt


## Metodologia

- [Análise Exploratória dos Dados](backend\ml\eda)
- [Treianemnto  do Modelo](backend\ml\modelo\notebook\treinamento)

## Uso

### Máquina Local

#### Instalar bibliotecas Python

pip install backend\requirements.txt

#### Instalar VueJs
npm install vue

##### Rodar o servidor

**cd backend\aplicativo\src** uvicorn app:app

##### Rodar o fronteend

**cd frontend\app** npm run dev

```

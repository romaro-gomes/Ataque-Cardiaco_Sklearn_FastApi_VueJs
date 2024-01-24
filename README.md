# Aplicação Web Para Auxilio de Tomadas de Decisão - Ataque Cardíaco ou Infarto.

## Introdução

**Este é um modelo de portifólio. Não deve ser usado na prática clínica, nem no autodiagnpostico ou automedicação** 

Ataque Cardíaco ou Infarto é um quadro clínico em que células do coração do coração do pacientes encontram-se mortas. Geralmente a falência das células é provoada pelo diminuição ou ausência no fornecimento de ocigênio, levando as célula a necrose, postrior liberação de cálcio na corrente sanguínea, provocando as dores peitoral devido as contrações musculares.

Nos casos de emergências, o tratamento do infarto varia depdendendo do resultado do exame físico, entretanto é primordial o uso so eletrocardiagrama EEG para se avaliar as características dos batimentos.

O risco infarto é fortemente associado hidtória cl´nica posterior, fatores genéticos e estilo de vida dos pacientes. Sendo importante ao médico e todo a equipe de saúde multiciplinar orientar ao pacientes nos cuidados que ele deve ser seguir e o que fazer  caso ele consiga notar po ínício de uma ataqtue cardíco.

O objetvo desta aplicação web, construída apartir de um modelo de aprendiao de máquina treiado apartir de dados públicos, é ajudar profissioniais da saúde decidir o risco de uma paciente ter ou não um ataque cardíaco e o npivel de esforço dedicado no acompahemento do mesmo.

Ressalto: **Esta aplicação é apenas para portifólio e não tem possuí pretensão e nem deve ser utilizado na prática clínica, no autodiagnósticos ou automedicação**

Referências: 

- https://www.scielo.br/j/abc/a/QvqxLFycJhLvNGFzPhsbZPF/?lang=pt

- https://bvsms.saude.gov.br/ataque-cardiaco-infarto/

- https://www.pfizer.com.br/noticias/ultimas-noticias/como-reconhecer-um-infarto-cardiaco

- https://www.msdmanuals.com/pt-br/casa/fatos-r%C3%A1pidos-dist%C3%BArbios-do-cora%C3%A7%C3%A3o-e-dos-vasos-sangu%C3%ADneos/doen%C3%A7a-arterial-coronariana/ataque-card%C3%ADaco


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



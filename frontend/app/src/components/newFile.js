/* __placeholder__ */
export default (await import('vue')).defineComponent({
data() {
return {
idade: null,
sexo: null,
dor_peitoral: null,
pressao_em_repouso: null,
colesterol: null,
glicemia_posprandial: null,
eletrocardiograma_em_repouso: null,
frequencia_cardiaca_maxima: null,
angina_em_exercicio: null,
depressao_ST: null,
inclinacao_ST: null,
};
},

methods: {
addIdade() {
{
this.idade += 1;
}
},

diminuirIdade() {
if (this.idade <= 0) {
this.idade === 0;
} else {
this.idade -= 1;
}
},

revelarResultado() {
return this.resultado !== null;
},
},

async enviarCaracteristicas(e) {
e.preventDefault();

const dados = {
idade: this.idade,
sexo: this.sexo,
dor_peitoral: this.dor_peitoral,
pressao_em_repouso: this.pressao_em_repouso,
colesterol: this.colesterol,
glicemia_posprandial: this.glicemia_posprandial,
eletrocardiograma_em_repouso: this.eletrocardiograma_em_repouso,
frequencia_cardiaca_maxima: this.frequencia_cardiaca_maxima,
angina_em_exercicio: this.angina_em_exercicio,
depressao_ST: parseFloat(this.depressao_ST),
inclinacao_ST: this.inclinacao_ST,

resultado: null,
positivo: null,
negativo: null,
};

const dadosJson = JSON.stringify(dados);

console.log(dadosJson);

const req = await fetch('http://localhost:8000/resultado-json',
{
method: "POST",
headers: { 'Content-Type': "application/json" },
body: dadosJson
});

console.log(req);

const res = await req.json();

const resultado = res.resultado;

const probabilidade = res.probability;

const probabilidades = probabilidade.split(' ');

const positivo = probabilidades[0];
const negativo = probabilidades[1];

console.log(resultado, positivo, negativo);

this.resultado = resultado;
this.positivo = positivo;
this.negativo = negativo;




}
});

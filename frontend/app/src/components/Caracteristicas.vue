<template>
    <form method="POST" @submit="enviarCaracteristicas">
        <div class="caracteristicas">
            <div class="linha-centralizada">
                <div>
                    <label for="">Idade: </label>
                    <input v-model='idade' type="number">
                    <div id="alerta" v-show="mostrarAlertaIdade">
                        <p>
                            A idade deve ser no minimo 18 anos
                        </p>
                        <button @click="fecharIdade">Fechar</button>
                    </div>
                </div>

                <div>
                    <label for="">Sexo: </label>
                    <input v-model='sexo' type="radio" value="0">
                    <label for="">Masculino</label>
                    <input v-model='sexo' type="radio" value="1">
                    <label for="">Feminino</label>
                </div>
            </div>

            <div class="linha">
                <div>
                    <label for="">Frequencia Cardiaca Máxima: </label>
                    <input v-model='frequencia_cardiaca_maxima' type="number">
                </div>

                <div>
                    <label for="">Colesterol: </label>
                    <input v-model='colesterol' type="number">
                </div>

                <div>
                    <label for="">Pressao em Repouso: </label>
                    <input v-model='pressao_em_repouso' type="number">
                </div>

                <div>
                    <label for="">Depressão ST (Entre -2.5 e 6.5): </label>

                    <input v-model='depressao_ST' type="number">
                    <div id="alerta" v-show="mostrarAlertaDepressaoST">
                        <p>
                            O valor está fora da faixa esperada
                        </p>
                        <button @click="fecharDepressao">Fechar</button>
                    </div>
                </div>
            </div>

            <div class="linha">

                <div>
                    <label for="">Glicemia Pos-Pandrial: </label>
                    <input v-model='glicemia_posprandial' type="radio" value="0">
                    <label for="">0</label>
                    <input v-model='glicemia_posprandial' type="radio" value="1">
                    <label for="">1</label>
                </div>

                <div>
                    <label for="">Eletrocardiograma em Reposuo: </label>
                    <input v-model='eletrocardiograma_em_repouso' type="radio" value="0">
                    <label for="">0</label>
                    <input v-model='eletrocardiograma_em_repouso' type="radio" value="1">
                    <label for="">1</label>
                    <input v-model='eletrocardiograma_em_repouso' type="radio" value="2">
                    <label for="">2</label>
                </div>

                
                <div>
                    <label for="">Inclinação ST: </label>
                    <input v-model="inclinacao_ST" type="radio" value=0>
                    <label for="">0</label>
                    <input v-model="inclinacao_ST" type="radio" value=1>
                    <label for="">1</label>
                    <input v-model="inclinacao_ST" type="radio" value=2>
                    <label for="">2</label>
                    <input v-model="inclinacao_ST" type="radio" value=3>
                    <label for="">3</label>
                </div>

            </div>

            <div class="linha-centralizada">
                
                <div>
                    <label for="">Angina em Exercício: </label>
                    <input v-model='angina_em_exercicio' type="radio" value="0">
                    <label for="">0</label>
                    <input v-model='angina_em_exercicio' type="radio" value="1">
                    <label for="">1</label>
                </div>


                <div>
                    <label for="">Tipo de Dor Peitoral: </label>
                    <input v-model="dor_peitoral" type="radio" value=1>
                    <label for="">1</label>
                    <input v-model="dor_peitoral" type="radio" value=2>
                    <label for="">2</label>
                    <input v-model="dor_peitoral" type="radio" value=3>
                    <label for="">3</label>
                    <input v-model="dor_peitoral" type="radio" value=4>
                    <label for="">4</label>
                </div>

                

            </div>

            <div class="linha-centralizada">
                <input class="botao" type="submit" value="Enviar Dados do Paciente">
            </div>

            <div style="display:flex; text-align:center; flex-direction:column;" v-show="resultado !== null">
                <div style='margin: 0px;'>
                    <p
                        style='color:white; background-color: black; display: inline-block; font-size: 30px; padding: 20px;text-decoration: solid;'>
                        Resultado: {{ resultado }}</p>
                </div>
                <div style='margin: 0px; font-size: 20px;'>
                    <p>Positivo: {{ positivo }}</p>
                    <p>Negativo: {{ negativo }}</p>
                </div>
            </div>
        </div>
    </form>

    <div class="linha-centralizada">
        <button class="botao" @click="limparFormulario">Limpar Formulário</button>
    </div>
</template>

<script>
export default {
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

            resultado: null,
            positivo: null,
            negativo: null,

            mostrarAlertaDepressaoST: false,
            mostrarAlertaIdade: false,       
        }
    },

    methods: {
        validarDepressao() {
            if (this.depressao_ST < -2.5 || this.depressao_ST > 6.5) {
                this.mostrarAlertaDepressaoST = true;
            } else {
                this.mostrarAlertaDepressaoST = false;
            }
        },

        validarIdade() {
            if (this.idade < 18) {
                this.mostrarAlertaIdade = true;
            } else {
                this.mostrarAlertaIdade = false;
            }
        },

        fecharIdade(){

            this.mostrarAlertaIdade=false;

        },

        fecharDepressao(){
            this.mostrarAlertaDepressaoST=false;
        },

        async enviarCaracteristicas(e) {
            e.preventDefault();

            this.validarIdade();
            this.validarDepressao();

            if(this.mostrarAlertaDepressaoST){
                return;
            }

            if(this.mostrarAlertaIdade){
                return;
            }


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

            }

            const dadosJson = JSON.stringify(dados)

            console.log(dadosJson)

            const req = await fetch('http://localhost:8000/resultado-json',
                {
                    method: "POST",
                    headers: { 'Content-Type': "application/json" },
                    body: dadosJson
                });

            console.log(req)

            const res = await req.json()

            const resultado = res.resultado

            const probabilidade = res.probability

            const probabilidades = probabilidade.split(' ')

            const positivo = probabilidades[0]
            const negativo = probabilidades[1]

            console.log(resultado, positivo, negativo)

            this.resultado = resultado
            this.positivo = positivo
            this.negativo = negativo




        },

        limparFormulario() {
            this.idade = null;
            this.sexo = null;
            this.dor_peitoral = null;
            this.pressao_em_repouso = null;
            this.colesterol = null;
            this.glicemia_posprandial = null;
            this.eletrocardiograma_em_repouso = null;
            this.frequencia_cardiaca_maxima = null;
            this.angina_em_exercicio = null;
            this.depressao_ST = null;
            this.inclinacao_ST = null;

            this.mostrarAlertaDepressaoST = false;
            this.mostrarAlertaIdade = false;
        },

}
}
</script>

<style>
.caracteristicas {
    color: black;
    font-weight: bold;
    text-align: left;
    padding: 100px;
}

.caracteristicas div {
    margin-bottom: 40px;
}

.caracteristicas span:hover {
    color: red;
    background-color: blue;
    font-style: italic;
}

#alerta {
    color: red;
    background-color: black;
    padding: 10px;
    margin: 2px;
    display: inline-block;
}

.linha {
    display: flex;
    flex-wrap: wrap;
    margin: 20px;
}

.linha>div {
    flex: 1;
    margin: 0 8px;
    box-sizing: border-box;
}

.linha-centralizada{
    display: flex;
    justify-content: center;
    align-items: center;
    gap:50px
}

.botao{
    width: 250px;
    height: 50px;
    padding: 10px;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 15px;
    background-color: black;
    color: aliceblue;
    font-weight: bold;
}
</style>
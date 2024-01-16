<template>
    <form  method="POST" @submit="enviarCaracteristicas">
        <div class="caracteristicas">
            <div>
                <label for="">Idade: </label>
                <input v-model='idade' type="number">
                <button @click="addIdade">+Idade</button>
                <button @click="diminuirIdade">-Idade</button>
                <p>
                    <span>{{ idade }}</span>
                </p>
            </div>

            <div>
                <label for="">Colesterol: </label>
                <input v-model='colesterol' type="number">
                <p>
                    <span>{{ colesterol }}</span>
                </p>
            </div>

            <div>
                <label for="">Pressao em Repouso: </label>
                <input v-model='pressao_em_repouso' type="number">
                <p >
                    <span>{{ pressao_em_repouso }}</span>
                </p>
            </div>

            <div>
                <label for="">Frequencia Cardiaca Máxima: </label>
                <input v-model='frequencia_cardiaca_maxima' type="number">
                <p>
                    <span>{{ frequencia_cardiaca_maxima }}</span>
                </p>
            </div>

            <div>
                <label for="">Depressão ST: </label>
                <input v-model='depressao_ST' type="number">
                <p>
                    <span>{{ depressao_ST }}</span>
                </p>
            </div>

            <div>
                <label for="">Sexo: </label>
                <input v-model='sexo' type="radio"  value="0">
                <label for="">Masculino</label>
                <input v-model='sexo' type="radio"  value="1">
                <label for="">Femino</label>
            </div>

            <div>
                <label for="">Glicemia Pos-Pandrial: </label>
                <input v-model='glicemia_posprandial' type="radio"  value="0">
                <label for="">0</label>
                <input v-model='glicemia_posprandial' type="radio"  value="1">
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
                <label for="">Angina em Exercício: </label>
                <input v-model="angina_em_exercicio" type="number"/>
                <p><span>{{ angina_em_exercicio }}</span></p>
            </div>

            <div>
                <label for="">Inclinação ST: </label>
                <input v-model="inclinacao_ST" type="number"/>
                <p><span>{{ inclinacao_ST }}</span></p>
            </div>

            <div>
                <label for="">Tipo de Dor Peitoral: </label>
                <select v-model="dor_peitoral">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
                <p><span>{{ dor_peitoral }}</span></p>
            </div>

            <div>
                <input type="submit" value="Enviar Dados do Paciente">
            </div>

            <div v-show="resultado !== null">
                <p>Resultado: {{ resultado }}</p>
                <p>Positivo: {{  positivo }}</p>
                <p>Negativo: {{  negativo }}</p>
            </div>
        
        </div>
    </form>
   
</template>

<script>
export default{
    data(){
        return{
            idade:null,
            sexo:null,
            dor_peitoral:null,           
            pressao_em_repouso:null,
            colesterol:null,            
            glicemia_posprandial:null,
            eletrocardiograma_em_repouso:null,
            frequencia_cardiaca_maxima:null,            
            angina_em_exercicio:null,
            depressao_ST:null,    
            inclinacao_ST:null,

            resultado: null,
            positivo: null,
            negativo: null,   
            
                 

        }
    },

    methods: {
        addIdade(){{
            this.idade += 1
        }},

        diminuirIdade(){
            if (this.idade <= 0){
                this.idade === 0
            } else {
            this.idade -= 1
            }},


        async enviarCaracteristicas(e){
            e.preventDefault();

            const dados={
                idade:this.idade,
                sexo:this.sexo,
                dor_peitoral:this.dor_peitoral,
                pressao_em_repouso:this.pressao_em_repouso,
                colesterol:this.colesterol,                     
                glicemia_posprandial:this.glicemia_posprandial,
                eletrocardiograma_em_repouso:this.eletrocardiograma_em_repouso,
                frequencia_cardiaca_maxima:this.frequencia_cardiaca_maxima,
                angina_em_exercicio:this.angina_em_exercicio,
                depressao_ST: parseFloat(this.depressao_ST),
                inclinacao_ST: this.inclinacao_ST,       

            }

            const dadosJson= JSON.stringify(dados)

            console.log(dadosJson)

            const req= await fetch('http://localhost:8000/resultado-json',
            {
                method: "POST",
                headers: {'Content-Type': "application/json"},
                body: dadosJson
            });

            console.log(req)

            const res = await req.json()

            const resultado= res.resultado

            const probabilidade= res.probability

            const probabilidades=  probabilidade.split(' ')

            const positivo = probabilidades[0]
            const negativo =  probabilidades[1]

            console.log( resultado, positivo, negativo)

            this.resultado = resultado
            this.positivo = positivo
            this.negativo = negativo


    

        }
    }

}
</script>

<style>
.caracteristicas{
    color:black ;
    font-weight: bold;
    text-align: left;   
}

.caracteristicas div {
    margin-bottom: 40px;
}

.caracteristicas span:hover{
    color:red;
    background-color: blue;
    font-style: italic;
}



</style>
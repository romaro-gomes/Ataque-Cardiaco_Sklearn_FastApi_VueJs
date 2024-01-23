<template>
    <header style="display: flex;  align-items: center;">
        <div>
        <img :src="fonte_da_foto" :alt="alternativo" srcset="">
        </div>
        <div style="align-content: center; margin: auto;">
        <p style="color: aliceblue; font-size:30px"> Modelo de Predição há Ataques Cardiacos</p>
        </div>
        <div>
        <img :src="fonte_da_foto" :alt="alternativo" srcset="">
        </div>
    </header>
</template>

<script>
export default{
    data(){
        return{
            ativo: false,
            nome: 'Pedro',
            fonte_da_foto: "../../src/assets/heart_boy.jpg",
            alternativo:'Carro',
        }
        
    }
    
}
</script>

<style>
.texto{
    color:blue;
    text-align: center;
}

img{
    width: 200px;
    height: 100px;
}
header{
    background-color: black;
}
</style>
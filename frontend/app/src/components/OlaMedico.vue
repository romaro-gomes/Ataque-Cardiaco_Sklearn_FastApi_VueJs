<template>
    <header>
        <img :src="fonte_da_foto" :alt="alternativo" srcset=""> 
    </header>
    
    <main>
    <p class="texto">Olá médico {{ nome }}</p>
    <p v-if="ativo"> Presente</p>
    <p class='texto' v-else>Ausente</p>
    </main>
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
<template>
<!-- in vue 2. x you need wrap these buttons in a div-->
    <button class="carrusel-control left" @click="$emit('Prev')">Prev</button>
    <button class="carrusel-control right" @click="$emit('next')">Next</button>
</template>


<style scoped>
.carrusel-control{
    background-color: black;
    border: none;
    display: inline-block;
    position: absolute;
    height: 50px;
    width: 70px;@click="$emit('Prev')">Prev</button>
    top: calc(50% - 25px);
    color: #f3f3f3;
    cursor: pointer;
}
.left{
    left: 0;
}
.right{
    right: 0;
}
</style>
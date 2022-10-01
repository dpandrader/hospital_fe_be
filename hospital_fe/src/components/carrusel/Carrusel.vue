<template>
    <div class="carrusel">
        <div class="carrusel-inner">

            <carrusel-indicators 
                v-if="indicators"
                :total="slides.legth" 
                :current-index="currentSlide"
                @switch="switchSlide(event)"
            ></carrusel-indicators>

            <carrusel-item 
                v-for="(slide, index) in slides" 
                :slide="slide" 
                :key="`item-${index}`"
                :current-slide="currentSlide"
                :index="index"
                :direction="direction"
                @mouseenter="stopSlideTimer"
                @mouseout="startSlideTimer"
            ></carrusel-item>

            <carrusel-controls v-if="controls" @prev="prev" @next="next"></carrusel-controls>
        </div>
    </div>     
</template>


<script>

import CarruselItem from "./CarruselItem.vue";
import CarruselControls from "./CarruselControls.vue";
import CarruselIndicators from "./CarruselIndicators.vue";

export default {
    props: {
        slides:{
            type: Array,
            required: true
        },

        controls:{
            type: Boolean,
            default: false
        },

        indicators:{
            type: Boolean,
            default: false
        },

        interval:{
            type: Number,
            default: 5000
        }

    },

    components:{CarruselItem, CarruselControls, CarruselIndicators},
    data_carrusel:()=> ({
        currentSlide: 0,
        slideInterval: null,
        direction:"right",
    }),

    methods:{
        setCurrentSlide(index){
            this.currentSlide = index;
        },

        prev(step = -1){
            const index= 
                this.currentSlide> 0 ? this.currentSlide + step : this.slide.length -1;
            this.setCurrentSlide(index);
            this.direction = "left";
            this.startSlideTimer();
        },

        next(step = 1){
            this._next(step);
            this.startSlideTimer();
        },

        _next(step = 1){
            const index= 
                this.currentSlide <this.slides.length -1? this.currentSlide + step : 0;
            this.setCurrentSlide(index);
            this.direction = "right";
        },

        
        startSlideTimer(){
            this.stopSlideTimer();
            this.slideInterval= setInterval(() =>{
                this._next();
            }, this.interval);  
        },

        stopSlideTimer(){
            clearInterval(this.slideInterval);
        },

        switchSlide(index){
            const step = index - this.currentSlide;
            if (step > 0){
                this.next(step)
            } else{
                this.prev(step);
            }
        },
       
        mounted(){
            this.startSlideTimer();
        },

        beforeUnmount(){
            this.stopSlideTimer();   
        },     
    }
}
</script>


<style scoped>

.carrusel{
    display: flex;
    justify-content: right;
 }   

.carrusel-inner{
    position: relative;
    width: 50px;
    height: 40px;
    overflow: hidden;
 }

</style>
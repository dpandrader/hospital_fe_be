<template>
  <carrusel :slides="slides" :interval="3000" controls indicators></carrusel>
  
  <div id="app" class="app">

      <div class="header">
      
      <h1>Hospital Atenea</h1><img src="./assets/logo_atena.jpg" alt="" class="logo1">
    
      <nav>
        <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
        <button v-if="is_auth" v-on:click="loadAccount"> Cuenta </button>
        <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>       
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>Hospital Atenea 2022</h2>
    </div>

  </div>
</template>


<script>

import Carrusel from "./components/carrusel/Carrusel.vue";
export default {
  name: 'App',
  
  data: function(){
    return{
      is_auth: false
    }
  },
  
  data_carrusel:()=> ({
    slides:[
      "./components/carrusel/medicamentos.jpeg",
      "./assets/medicamentos.jpeg",
      "./assets/medicamentos1.jpeg",

    ],

  }),

  components: {
    Carrusel
  },

  methods:{
    verifyAuth: function() {
          this.is_auth = localStorage.getItem("isAuth") || false;
          
          if (this.is_auth == false)
            this.$router.push({ name: "logIn" });
          else
            this.$router.push({ name: "home" });
        },

    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },

    loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

    loadHome: function() {
      this.$router.push({ name: "home" });
    },

    loadsignUpMedico: function() {
      this.$router.push({ name: "signUpMedico" });
    },

    loadsignUpEnfermero: function() {
      this.$router.push({ name: "signUpEnfermero" });
    },

    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },

    
    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },

    completedSignUp: function(data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },

  },

  created: function(){
    this.verifyAuth()
  }

}

</script>


<style>

  body{
    margin: 0 0 0 0;
  }
  
  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 75px;

    background-color: #1371ab ;
    color:#E5E7E9 ;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }

  .header nav{
    height: 100%;
    width: 30%;

    display: flex;
    justify-content: space-around;
    align-items: center;

    font-size: 20px;
  }

  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;

    background: #FDFEFE;
  }

  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 75px;
    background-color: #1371ab;
    color: #E5E7E9;
  }

  .footer h2{
    width: 100%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  .logo1{
    width: 50px;
  }
</style>


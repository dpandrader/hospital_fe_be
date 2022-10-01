<template>
    
    <div class="logIn_user">
        

        <div class="imagen">
            <img src="../assets/atenea.jpg" alt="">
            
        </div>

        <div class="container_logIn_user">
            <h2>Iniciar Sesión</h2>

            <form v-on:submit.prevent="processLogInUser" >
                <input type="text" v-model="user.username" placeholder="Usuario">
                <br>
                <input type="password" v-model="user.password" placeholder="Contraseña">
                <br>
                <button type="submit">Ingresar</button>
                <br>
                <h5> Si usted no tiene cuenta registrese como :</h5>
                <button @click="goToPaciente()"> Paciente</button>
                <button @click="goToMedico()"> Medico</button>
                <button @click="goToEnfermero()"> Enfermero</button>
               
            </form>
        </div>
    
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "LogIn",

    data: function(){
        return {
            user: {
                username:"",
                password:""
            }
        }
    },

    methods: {
        processLogInUser: function(){
            axios.post(
                "https://hospitalapp01.herokuapp.com/login/",
                    this.user,
                    {headers: {}}
                    )
                    .then((result) => {
                        let dataLogIn = {
                            username: this.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                        }

                        this.$emit('completedLogIn', dataLogIn)
                    })
                    .catch((error) => {

                        if (error.response.status == "401")
                            alert("ERROR 401: Credenciales Incorrectas.");
                    });
        },
        goToMedico(){
        this.$router.push('signUpMedico'); 
        },
        goToEnfermero(){
        this.$router.push('signUpEnfermero'); 
        },
        goToPaciente(){
        this.$router.push('signUp'); 
        }
    }
}
</script>

<style>
    .logIn_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;

        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: row;
        flex-wrap: wrap;
        align-content: center;
    }

    .container_logIn_user {
        border: 3px solid #1371ab;
        border-radius: 40px;
        width: 20%;
        height: 85%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }


    .logIn_user h2{
        color: #1371ab;
    }

    .logIn_user form{
        width: 70%;

    }

    .logIn_user input{
        height: 30px;
        width: 80%;

        box-sizing: border-box;
        /* padding: 10px 20px; */
        margin: 5px 0;
        border: 1px solid #1371ab;
        border-radius: 10px;
    }

    .logIn_user button{
        width: 80%;
        height: 30px;

        color: #E5E7E9;
        background: #1371ab;
        border: 1px solid #E5E7E9;

        border-radius: 10px;
        padding: 5px 5px;
        margin: 3px 0;
    }

    .logIn_user button:hover{
        color: #E5E7E9;
        background: #84b3d3;
        border: 1px solid #1371ab;
    }
    
</style>

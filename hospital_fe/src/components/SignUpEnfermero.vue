<template>

    <div class="signUp_enfermero">
        <div class="logo">
            <img src="../assets/atenea.jpg" alt="logo">
        </div>
        
        <div class="container_signUp_enfermero">
            <br>
            <br>
            <br>
            <h2>Registro  de Enfermero</h2>
            
            <form v-on:submit.prevent="processSignUp" >

                <input type="text" v-model="user.username" placeholder="Usuario">
                <br>
                
                <input type="password" v-model="user.password" placeholder="Contraseña">
                <br>

                <input type="text" v-model="user.nombres" placeholder="Nombres">
                <br>

                <input type="text" v-model="user.apellido" placeholder="Apellidos">
                <br>

                <input type="text" v-model="user.identificacion" placeholder="Identificación">
                <br>
                
                <input type="text" v-model="user.fecha_nacimiento" placeholder="Fecha Nacimineto">
                <br>
                
                <input type="text" v-model="user.direccion" placeholder="Direccion">
                <br>

                <input type="text" v-model="user.ciudad" placeholder="Ciudad">
                <br>

                <input type="text" v-model="user.numero_telefonico" placeholder="Número Telefónico">
                <br>

                <input type="email" v-model="user.email" placeholder="Email">
                <br>
                
                <button type="submit">Registrarse</button>
            </form>
        </div>
    
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "SignUpEnfermero",
    data: function(){
        return {
            user: {
                username: "",
                password: "",
                nombres: "",
                apellidos: "",
                identificacion: "",
                fecha_nacimiento: "",
                direccion: "",
                ciudad: "",
                numero_telefonico: "",
                email: "",
                especialidad: "",
                }
                
            }
        },
    

    methods: {
        processSignUp: function(){
            axios.post(
                "https://hospitalapp01.herokuapp.com/user/",
                this.user,
                {headers: {}}

            ).then((result) => {
                    let dataSignUp = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }

                    this.$emit('completedSignUp', dataSignUp)

                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });
        }
    }
}


</script>

<style>

    .signUp_enfermero{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_signUp_enfermero {
        border: 3px solid #1371ab;
        border-radius: 40px;
        width: 25%;
        height: 95%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .signUp_enfermero h2{
        color: #1371ab;
    }

    .signUp_enfermero form{
    width: 70%;
    }

    .signUp_enfermero input{
        height: 28px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        
        border: 1px solid #1371ab;
        border-radius: 10px;
    }

    .signUp_enfermero button{
        width: 100%;
        height: 40px;
        
        color: #E5E7E9;
        background: #1371ab;
        border: 1px solid #E5E7E9;
        
        border-radius: 10px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_enfermero button:hover{
        color: #E5E7E9;
        background: #84b3d3;
        border: 1px solid #1371ab;
        border-radius: 10px;
    }

    .logo{
        
        
        
    }

    .logo img{
        width: 300px;
        margin-right: 300px;       
        border-radius: 18px;
    }
    
</style>
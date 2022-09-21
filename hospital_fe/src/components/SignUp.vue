<template>

    <div class="signUp_user">
        <div class="logo">
            <img src="../assets/atena_2.png" alt="logo">
        </div>
        
        <div class="container_signUp_user">
            <h2>Area de Registro</h2>
            
            <form v-on:submit.prevent="processSignUp" >
                <input type="text" v-model="user.username" placeholder="Nombre Usuario">
                <br>
                <input type="password" v-model="user.password" placeholder="contraseña">
                <br>

                <input type="text" v-model="user.name" placeholder="Nombres">
                <br>

                <input type="text" v-model="user.lastname" placeholder="Apellidos">
                <br>

                <input type="text" v-model="user.birth_date" placeholder="Fecha Nacimineto">
                <br>

                <input type="text" v-model="user.address" placeholder="Direccion">
                <br>

                <input type="text" v-model="user.city" placeholder="Ciudad">
                <br>

                <input type="text" v-model="user.telephone_number" placeholder="Numero Telefonico">
                <br>

                <input type="email" v-model="user.email" placeholder="Email">
                <br>

                <input type="number" v-model="user.account.balance" placeholder="Initial Balance">
                <br>

                <button type="submit">Registrarse</button>
            </form>
        </div>
    
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "SignUp",
    data: function(){
        return {
            user: {
                username: "",
                password: "",
                name: "",
                lastname: "",
                birth_date: "",
                address: "",
                city: "",
                telephone_number: "",
                email: "",
                account: {
                    lastChangeDate: (new Date()).toJSON().toString(),
                    balance: 0,
                    isActive: true
                }
            }
        }
    },

    methods: {
        processSignUp: function(){
            axios.post(
                "https://hospitalapp01.herokuapp.com/user/",
                this.user,
                {headers: {}}
            )
                .then((result) => {
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

    .signUp_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_signUp_user {
        border: 3px solid #1371ab;
        border-radius: 40px;
        width: 25%;
        height: 90%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .signUp_user h2{
        color: #1371ab;
    }

    .signUp_user form{
    width: 70%;
    }

    .signUp_user input{
        height: 28px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        
        border: 1px solid #1371ab;
        border-radius: 10px;
    }

    .signUp_user button{
        width: 100%;
        height: 40px;
        
        color: #E5E7E9;
        background: #1371ab;
        border: 1px solid #E5E7E9;
        
        border-radius: 10px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_user button:hover{
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
import { defineStore } from "pinia";

export const useAuthStore = defineStore("Auth", {
    state: () => {
        return {
            isAuthenticated: false,
            userId: '',
            authenticationToken: '',
            csrfToken: '',
            loginErrors: {},
            registerErrors: {}
        }
    },
    getters: {

    },
    actions: {
        async getCsrfToken(){
            const csrf_token = await fetch("http://localhost:5000/login", {
                        "method": "GET",
                        "headers": {
                            "Content-Type": "application/json"
                        }
                        })
                        .then(response => response.json())
                        .then(data => data.response.csrf_token)
                        .catch(err => {
                        console.error(err);
                        });
            this.csrfToken = csrf_token;
            console.log(csrf_token);
        },
        async register(username, email, password){
            this.registerErrors = {};
            await this.getCsrfToken();
            const data = {
                username:username,
                email: email,
                password: password,
                csrf_token: this.csrfToken
            };
            await fetch("http://localhost:5000/register?include_auth_token", {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(data => {
                    if(parseInt(data.meta.code) >= 400){
                        this.registerErrors = data.response.errors;
                        throw Error("Unable to register");
                    }
                    return data;
                })
                .then(data => {
                    this.csrfToken = data.response.csrf_token;
                    this.authenticationToken = data.response.user.authentication_token;
                    this.userId = data.response.user.id;
                    this.isAuthenticated = true;

                    const authData = {}
                    authData.csrfToken = this.csrfToken;
                    authData.authenticationToken = this.authenticationToken;
                    authData.userId = this.userId;
                    sessionStorage.flashCardAppAuth = JSON.stringify(authData);
                })
                .catch(err => {
                console.error(err);
                });

        },
        async login(email, password){
            this.loginErrors = {};
            await this.getCsrfToken();
            const data = {
                email: email,
                password: password,
                csrf_token: this.csrfToken
            };
            console.log(JSON.stringify(data));
            await fetch("http://localhost:5000/login?include_auth_token", {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(data => {
                    if(parseInt(data.meta.code) >= 400){
                        this.loginErrors = data.response.errors;
                        throw Error("Unable to login");
                    }
                    return data;
                })
                .then(data => {
                    this.csrfToken = data.response.csrf_token;
                    this.authenticationToken = data.response.user.authentication_token;
                    this.userId = data.response.user.id;
                    this.isAuthenticated = true;

                    const authData = {}
                    authData.csrfToken = this.csrfToken;
                    authData.authenticationToken = this.authenticationToken;
                    authData.userId = this.userId;
                    sessionStorage.flashCardAppAuth = JSON.stringify(authData);
                })
                .catch(err => {
                console.error(err);
                });
        },
        logout() {
            fetch("http://localhost:5000/logout", {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                }
                })
                .then(response => {
                console.log(response);
                })
                .catch(err => {
                console.error(err);
                });
            this.isAuthenticated = false;
            sessionStorage.clear();
            this.userId = '';
            this.authenticationToken = '';
            this.csrfToken = '';
            this.loginErrors = {};
        },
        authFromSessionStorage() {
            console.log("authFromSessionStorage")
            if(sessionStorage.flashCardAppAuth){
                console.log("sessionStorage present");
                const authData = JSON.parse(sessionStorage.flashCardAppAuth);
                this.csrfToken = authData.csrfToken;
                this.authenticationToken = authData.authenticationToken;
                this.userId = authData.userId;
                this.isAuthenticated = true;
                return true;
            }
            return false;
        }
    }
})